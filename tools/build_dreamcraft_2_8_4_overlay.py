#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fit the dreamcraft ja_JP mirror to what GTNewHorizonsCoreMod 2.7.268 (GTNH 2.8.4) looks up.

`ja_JP/config/txloader/load/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang` is the
ParaTranz mirror and follows the 2.9 line of the mod. Copying it to a 2.8.4
instance as-is (what sync-verified-thaums.sh did until 2026-09-28) broke two
things:

* keys 2.9 dropped but 2.8.4 still uses (item.SteelBars, item.Cast.*,
  dreamcraft.lootbag.*, ...) fell back to English - 128 keys, 50 of which were
  Japanese in the official 2.8.4 pack;
* keys whose 2.9 text gained a format argument the 2.8.4 code never passes
  (dreamcraft.welcome.welcome / gtnh_wiki / visitdiscord got a `%s`).

Same rule as the 2026-09-04 instance rebuild: keep the mirror's value unless its
format specifiers differ from the 2.8.4 English; for those, and for keys the
mirror lacks, use the official 2.8.4 ja_JP when it fits, else the English.
Keys only 2.9 knows are left in place: nothing looks them up on 2.8.4.

Usage:
  python tools/build_dreamcraft_2_8_4_overlay.py --source-lang <lang> \
      --mods-dir <.minecraft/mods> [--pack-en <en_US.lang>] \
      [--release-ja <official 2.8.4 ja_JP.lang>] --output <lang>
"""

from __future__ import annotations

import argparse
import io
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

JAR_GLOB = "GTNewHorizonsCoreMod-*.jar"
JAR_LANG = "assets/dreamcraft/lang/en_US.lang"

# java.util.Formatter conversions. The space flag is left out on purpose: prose
# such as "10% faster" would otherwise read as a "% f" conversion.
SPEC = re.compile(r"%(?:\d+\$)?[-#+0,(]*\d*(?:\.\d+)?([a-zA-Z])")

HEADER = "# ---- ここから下は sync 時に tools/build_dreamcraft_2_8_4_overlay.py が生成 ----"
NOTE = [
    "# 正本は 2.9 系 dreamcraft に合わせた ParaTranz ミラー。2.8.4 (CoreMod 2.7.268) が引くキーのうち、",
    "# 書式指定子が合わないものと正本に無いものを、2.8.4 公式訳（無ければ英語）で補っている。",
    "# 直接編集しても次の sync で消える。",
]


def read_entries(text: str) -> dict[str, str]:
    entries = {}
    for line in text.splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            entries[key] = value
    return entries


def read_file(path: Path) -> str:
    return io.open(path, encoding="utf-8-sig", newline="").read()


def signature(value: str) -> Counter:
    """Conversions a String.format call would consume, ignoring argument order."""
    return Counter(c.lower() for c in SPEC.findall(value) if c.lower() != "n")


def load_english(mods_dir: Path, pack_en: Path | None) -> tuple[dict[str, str], str]:
    jars = sorted(mods_dir.glob(JAR_GLOB))
    if len(jars) != 1:
        raise SystemExit("expected exactly one %s in the mods dir, found %d" % (JAR_GLOB, len(jars)))
    with zipfile.ZipFile(jars[0]) as jar:
        english = read_entries(jar.read(JAR_LANG).decode("utf-8-sig"))
    # The pack's own en_US overrides (config/txloader/load/dreamcraft) are keys
    # the game shows too, so they belong to the 2.8.4 key set.
    if pack_en is not None and pack_en.is_file():
        english.update(read_entries(read_file(pack_en)))
    return english, jars[0].name


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-lang", required=True, type=Path)
    parser.add_argument("--mods-dir", required=True, type=Path)
    parser.add_argument("--pack-en", type=Path)
    parser.add_argument("--release-ja", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    text = read_file(args.source_lang)
    source = read_entries(text)
    english, jar_name = load_english(args.mods_dir, args.pack_en)

    release: dict[str, str] = {}
    if args.release_ja is not None and args.release_ja.is_file():
        release = read_entries(read_file(args.release_ja))
    else:
        print("warning: official 2.8.4 ja_JP not found; fallbacks will be English", file=sys.stderr)

    # origin -> (comment written into the lang, label for the console summary)
    origins = {
        "official": ("2.8.4 公式訳", "2.8.4 official"),
        "english": ("英語（2.8.4 公式訳なし）", "English"),
        "english-fmt": ("英語（2.8.4 公式訳も書式不一致）", "English (official format mismatch)"),
    }

    def fallback(key: str) -> tuple[str, str]:
        official = release.get(key)
        if official is not None and signature(official) == signature(english[key]):
            return official, "official"
        return english[key], "english" if official is None else "english-fmt"

    mismatched = [k for k in source if k in english and signature(source[k]) != signature(english[k])]
    missing = [k for k in english if k not in source]

    newline = "\r\n" if "\r\n" in text else "\n"
    drop = set(mismatched)
    kept = [line for line in text.split(newline)
            if not ("=" in line and not line.lstrip().startswith("#") and line.split("=", 1)[0] in drop)]
    while kept and kept[-1] == "":
        kept.pop()
    out = kept + ["", HEADER] + NOTE
    out.append("# 2.8.4 のキー一覧: %s + config/txloader/load/dreamcraft/lang/en_US.lang" % jar_name)

    out.append("")
    out.append("# -- 正本の訳は書式指定子が 2.8.4 の英語と合わないので差し戻したキー --")
    for key in mismatched:
        value, origin = fallback(key)
        out.append("# %s。正本: %s" % (origins[origin][0], source[key]))
        out.append("%s=%s" % (key, value))

    out.append("")
    out.append("# -- 2.9 で消えたが 2.8.4 は引くキー --")
    counts = Counter()
    for key in missing:
        value, origin = fallback(key)
        counts[origin] += 1
        out.append("%s=%s" % (key, value))

    io.open(args.output, "w", encoding="utf-8", newline=newline).write(newline.join(out) + newline)
    # The output is a temp file; printing its path would leak the home directory.
    # ASCII only: Japanese printed from a Windows python garbles in MSYS terminals.
    print("overlay: %d reverted (format) + %d filled (%s)"
          % (len(mismatched), len(missing),
             ", ".join("%s %d" % (origins[o][1], n) for o, n in counts.items()) or "none"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
