#!/usr/bin/env python3
"""Bring a fresh GTNH 2.8.4 Prism instance's ja_JP translations into shape.

2.8.4 ships TX-Loader 1.8.5, where ``config/txloader/load/`` is injected too
early to override mod jars.  The current ParaTranz packs are built for
TX-Loader 1.8.7+ and put everything in ``load/``, so on 2.8.4 they lose to
whatever the mod jar itself carries.  On top of that, packs installed at
different times leave stale ``Name(+N)[modid]`` snapshots behind in
``forceload/`` that override each other in an arbitrary order.

This script fixes all of that, idempotently:

  Step A  Retire duplicate ``forceload/`` folders for a domain, keeping the
          best one.  Folders holding non-lang assets are never touched.
  Step B  Rebuild each kept ja_JP.lang: keys come from the installed jars'
          en_US (plus whatever the old packs had), values prefer the repo's
          latest translation, then the 2.8.4-era pack, then English.
  Step C  Retire ``load/`` folders that duplicate a ``forceload/`` folder for
          a domain whose mod ships its own ja_JP.lang, so the pack wins.

Everything moved or rewritten is copied under ``config_backup/txloader/``
first, so any step can be undone by hand.

Usage:
    python tools/setup_instance_2_8_4.py --dry-run
    python tools/setup_instance_2_8_4.py
    INSTANCE_MC=/path/to/.minecraft python tools/setup_instance_2_8_4.py
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

JP = re.compile(r"[぀-ヿ㐀-䶿一-鿿ｦ-ﾟ]")
FMT = re.compile(r"%(?:(\d+)\$)?([sdfx])|%(%)|%(n)")
ASSET_JA = re.compile(r"assets/([A-Za-z0-9_\-]+)/lang/ja_JP\.lang")
ASSET_EN = re.compile(r"assets/([A-Za-z0-9_\-]+)/lang/en_US\.lang")

# betterquesting quest text is managed by sync-verified-quests.sh; minecraft is
# vanilla's own domain and must not be rebuilt from a mod jar's stub.
SKIP_REBUILD = {"betterquesting", "minecraft"}


def read_lang(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("//"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        out[key] = value
    return out


def load_lang(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    return read_lang(path.read_text(encoding="utf-8", errors="replace"))


def domain_of(folder_name: str) -> str:
    match = re.search(r"\[([^\]]+)\]$", folder_name)
    return match.group(1) if match else folder_name


def fmt_signature(text: str, positional_ok: bool) -> list[str]:
    """Format specifiers, so a translation is never applied to a different source.

    ``positional_ok`` folds ``%1$s`` into ``%s`` so that a translation which only
    reorders arguments still counts as compatible.
    """
    tokens = []
    for m in FMT.finditer(text):
        if m.group(2):
            tokens.append(m.group(2) if positional_ok else (m.group(1) or "") + m.group(2))
    return sorted(tokens)


def compatible(source: str, translation: str) -> bool:
    if fmt_signature(source, False) == fmt_signature(translation, False):
        return True
    return fmt_signature(source, True) == fmt_signature(translation, True)


def has_non_lang_assets(folder: Path) -> bool:
    """True if the folder carries anything other than lang files.

    ``forceload/betterloadingscreen`` holds only textures/backgrounds/*.png --
    moving it aside blanks the loading screen.
    """
    for path in folder.rglob("*"):
        if path.is_file() and path.suffix.lower() != ".lang":
            return True
    return False


class Instance:
    def __init__(self, mc: Path, repo: Path) -> None:
        self.mc = mc
        self.repo = repo
        self.forceload = mc / "config" / "txloader" / "forceload"
        self.load = mc / "config" / "txloader" / "load"
        self.backup = mc / "config_backup" / "txloader"

    # -- sources -----------------------------------------------------------
    def scan_jars(self) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
        jar_en: dict[str, dict[str, str]] = {}
        jar_ja: dict[str, dict[str, str]] = defaultdict(dict)
        for jar_path in sorted(glob.glob(str(self.mc / "mods" / "*.jar"))):
            try:
                archive = zipfile.ZipFile(jar_path)
            except Exception:
                continue
            for name in archive.namelist():
                en = ASSET_EN.fullmatch(name)
                ja = ASSET_JA.fullmatch(name)
                if not en and not ja:
                    continue
                try:
                    entries = read_lang(archive.read(name).decode("utf-8", "replace"))
                except Exception:
                    continue
                if en:
                    domain = en.group(1)
                    if domain not in jar_en or len(entries) > len(jar_en[domain]):
                        jar_en[domain] = entries
                else:
                    jar_ja[ja.group(1)].update(entries)
        return jar_en, dict(jar_ja)

    def scan_repo(self) -> dict[str, dict[str, str]]:
        """Latest ja_JP from the repo, keyed by resource domain."""
        latest: dict[str, dict[str, str]] = defaultdict(dict)
        for sub in ("load", "forceload"):
            root = self.repo / "ja_JP" / "config" / "txloader" / sub
            if not root.is_dir():
                continue
            for folder in sorted(root.iterdir()):
                lang = folder / "lang" / "ja_JP.lang"
                if not lang.is_file():
                    continue
                domain = domain_of(folder.name)
                for key, value in load_lang(lang).items():
                    if JP.search(value) and key not in latest[domain]:
                        latest[domain][key] = value
        return dict(latest)

    # -- helpers -----------------------------------------------------------
    def stash(self, kind: str, folder_name: str, source: Path) -> None:
        dest_dir = self.backup / kind / folder_name / "lang"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / "ja_JP.lang"
        if not dest.exists() and source.is_file():
            shutil.copy2(source, dest)

    def retire(self, kind: str, folder: Path) -> bool:
        dest = self.backup / kind / folder.name
        if dest.exists():
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(folder), str(dest))
        return True


def merge_into(inst: Instance, target_lang: Path, source_lang: Path, note: str, dry: bool) -> int:
    """Append the source's Japanese keys that the target lacks. Returns the count."""
    target = load_lang(target_lang)
    extra = {k: v for k, v in load_lang(source_lang).items() if k not in target and JP.search(v)}
    if not extra or dry:
        return len(extra)
    inst.stash("pre_rebuild", target_lang.parent.parent.name, target_lang)
    target_lang.parent.mkdir(parents=True, exist_ok=True)
    with target_lang.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(f"\n# merged from {note} before retiring the duplicate folder\n")
        for key, value in extra.items():
            handle.write(f"{key}={value}\n")
    return len(extra)


def step_a_dedupe_forceload(inst: Instance, dry: bool) -> list[str]:
    """Keep one folder per domain in forceload; retire the rest.

    Folders sharing a domain can carry disjoint keys -- ``betterquesting`` holds
    quest text while ``BetterQuesting(+3)[betterquesting]`` holds UI strings --
    so anything the kept folder lacks is merged in before the retire.
    """
    by_domain: dict[str, list[Path]] = defaultdict(list)
    for folder in sorted(inst.forceload.iterdir()):
        if folder.is_dir():
            by_domain[domain_of(folder.name)].append(folder)

    log: list[str] = []
    for domain, folders in sorted(by_domain.items()):
        if len(folders) < 2:
            continue
        movable = [f for f in folders if not has_non_lang_assets(f)]
        if len(movable) < 2:
            continue

        def score(folder: Path) -> tuple[int, str]:
            entries = load_lang(folder / "lang" / "ja_JP.lang")
            return sum(1 for v in entries.values() if JP.search(v)), folder.name

        keep = max(movable, key=score)
        keep_lang = keep / "lang" / "ja_JP.lang"
        for folder in movable:
            if folder is keep:
                continue
            moved = merge_into(inst, keep_lang, folder / "lang" / "ja_JP.lang",
                               f"forceload/{folder.name}", dry)
            suffix = f" (+{moved} keys merged first)" if moved else ""
            log.append(f"  [{domain}] retire forceload/{folder.name} -> keep {keep.name}{suffix}")
            if not dry:
                inst.retire("forceload", folder)
    return log


def step_b_rebuild(inst: Instance, jar_en, latest, dry: bool) -> list[str]:
    """Rewrite each forceload lang file from jar keys + best available values."""
    by_domain: dict[str, list[Path]] = defaultdict(list)
    for folder in sorted(inst.forceload.iterdir()):
        if folder.is_dir() and (folder / "lang" / "ja_JP.lang").is_file():
            by_domain[domain_of(folder.name)].append(folder)

    log: list[str] = []
    for domain, folders in sorted(by_domain.items()):
        if domain in SKIP_REBUILD:
            continue
        english = jar_en.get(domain, {})
        newest = latest.get(domain, {})
        if not english and not newest:
            continue

        target = folders[0]
        lang_path = target / "lang" / "ja_JP.lang"
        existing = load_lang(lang_path)

        keys = list(english.keys()) + [k for k in existing if k not in english]
        merged: dict[str, str] = {}
        used_latest = 0
        for key in keys:
            source = english.get(key, existing.get(key))
            candidate = newest.get(key)
            if candidate and JP.search(candidate) and (source is None or compatible(source, candidate)):
                merged[key] = candidate
                used_latest += 1
            elif key in existing:
                merged[key] = existing[key]
            elif source is not None:
                merged[key] = source

        before = sum(1 for v in existing.values() if JP.search(v))
        after = sum(1 for v in merged.values() if JP.search(v))
        if merged == existing:
            continue
        log.append(f"  [{domain}] {target.name}: JP {before} -> {after} (latest {used_latest})")
        if not dry:
            inst.stash("pre_rebuild", target.name, lang_path)
            lang_path.parent.mkdir(parents=True, exist_ok=True)
            with lang_path.open("w", encoding="utf-8", newline="\n") as handle:
                handle.write(
                    "# rebuilt for GTNH 2.8.4 : keys from installed jar en_US, "
                    "values = latest ja_JP > 2.8.4 pack > English\n"
                )
                for key in keys:
                    if key in merged:
                        handle.write(f"{key}={merged[key]}\n")
    return log


def step_c_dedupe_load(inst: Instance, jar_ja, dry: bool) -> list[str]:
    """Retire load/ folders that shadow a forceload folder for a jar-ja_JP domain.

    On TX-Loader 1.8.5 a domain first declared by the load pack keeps that early
    slot forever, so the mod jar's own (often half-English) ja_JP.lang wins.
    Leaving the domain to forceload alone puts it last, where it belongs.
    """
    if not inst.load.is_dir():
        return []
    force_names = {f.name for f in inst.forceload.iterdir() if f.is_dir()}

    log: list[str] = []
    for folder in sorted(inst.load.iterdir()):
        if not folder.is_dir() or folder.name not in force_names:
            continue
        domain = domain_of(folder.name)
        if domain not in jar_ja:
            continue  # no competitor in the jar, the duplicate is harmless

        force_lang = inst.forceload / folder.name / "lang" / "ja_JP.lang"
        moved = merge_into(inst, force_lang, folder / "lang" / "ja_JP.lang",
                           f"load/{folder.name}", dry)
        suffix = f" (+{moved} keys merged first)" if moved else ""
        log.append(f"  [{domain}] retire load/{folder.name}{suffix}")
        if not dry:
            inst.retire("load", folder)
    return log


def swap_prefix(key: str) -> str | None:
    """`item.Foo.name` <-> `tile.Foo.name`. Blocks got their prefix corrected after 2.8.4."""
    if key.startswith("item."):
        return "tile." + key[5:]
    if key.startswith("tile."):
        return "item." + key[5:]
    return None


def step_d_prefix_aliases(inst: Instance, jar_en, dry: bool) -> list[str]:
    """Translate keys the 2.8.4 jar looks up whose translation sits under the other prefix.

    GTNH renamed several block keys after 2.8.4 (`item.SteelBars.name` ->
    `tile.SteelBars.name`), and the packs follow the new name, so 2.8.4 never
    finds the Japanese. Copy the value onto the key this jar actually uses.
    """
    log: list[str] = []
    for folder in sorted(inst.forceload.iterdir()):
        lang_path = folder / "lang" / "ja_JP.lang"
        if not folder.is_dir() or not lang_path.is_file():
            continue
        english = jar_en.get(domain_of(folder.name))
        if not english:
            continue
        current = load_lang(lang_path)
        adds: dict[str, str] = {}
        for key, source in english.items():
            if key in current and JP.search(current[key]):
                continue
            alt = swap_prefix(key)
            if alt and alt in current and JP.search(current[alt]) and compatible(source, current[alt]):
                adds[key] = current[alt]
        if not adds:
            continue
        log.append(f"  [{domain_of(folder.name)}] {folder.name}: {len(adds)} keys")
        for key, value in list(adds.items())[:3]:
            log.append(f"      {key} = {value}")
        if dry:
            continue
        inst.stash("pre_rebuild", folder.name, lang_path)
        lines = lang_path.read_text(encoding="utf-8", errors="replace").splitlines()
        out, done = [], set()
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith(("#", "//")) and "=" in line:
                key = line.split("=", 1)[0]
                if key in adds:
                    line = f"{key}={adds[key]}"
                    done.add(key)
            out.append(line)
        missing = {k: v for k, v in adds.items() if k not in done}
        if missing:
            out.append("")
            out.append("# keys this 2.8.4 jar looks up, translated under the other prefix upstream")
            out += [f"{k}={v}" for k, v in missing.items()]
        lang_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    return log


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    # No default is baked in: the instance path is machine-specific and stays
    # out of the repo. setup-instance.sh resolves it (env var, else .env).
    default_mc = os.environ.get("INSTANCE_MC")
    parser.add_argument("--instance", default=default_mc, type=Path,
                        required=default_mc is None,
                        help="path to the instance .minecraft (or set INSTANCE_MC)")
    parser.add_argument("--repo", default=Path(__file__).resolve().parent.parent, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip", default="", help="comma separated step letters to skip, e.g. 'b'")
    args = parser.parse_args()

    mc: Path = args.instance
    if not (mc / "mods").is_dir():
        sys.exit(f"Not a Minecraft instance (no mods/): {mc}")
    if not (args.repo / "ja_JP").is_dir():
        sys.exit(f"Not a GTNH-Translations checkout: {args.repo}")

    inst = Instance(mc, args.repo)
    if not inst.forceload.is_dir():
        sys.exit(f"Missing {inst.forceload}")

    skip = {c.strip().lower() for c in args.skip.split(",") if c.strip()}
    mode = "DRY-RUN" if args.dry_run else "APPLY"
    # Print placeholders, not the real paths: this output gets pasted into
    # issues and screenshots and would otherwise carry a home directory.
    print(f"[{mode}] instance: <instance>")
    print(f"[{mode}] repo:     <repo>")

    jar_en, jar_ja = inst.scan_jars()
    latest = inst.scan_repo()
    print(f"  jars: en_US {len(jar_en)} domains / ja_JP {len(jar_ja)} domains")
    print(f"  repo: {len(latest)} domains with Japanese")

    for letter, title, run in (
        ("a", "Step A: retire duplicate forceload folders", lambda: step_a_dedupe_forceload(inst, args.dry_run)),
        ("b", "Step B: rebuild lang files", lambda: step_b_rebuild(inst, jar_en, latest, args.dry_run)),
        ("c", "Step C: retire shadowing load folders", lambda: step_c_dedupe_load(inst, jar_ja, args.dry_run)),
        ("d", "Step D: alias renamed item./tile. keys", lambda: step_d_prefix_aliases(inst, jar_en, args.dry_run)),
    ):
        print(f"\n{title}")
        if letter in skip:
            print("  (skipped)")
            continue
        lines = run()
        print("\n".join(lines) if lines else "  nothing to do")

    print("\nBackups under config_backup/txloader/. Restart Minecraft to apply.")


if __name__ == "__main__":
    main()
