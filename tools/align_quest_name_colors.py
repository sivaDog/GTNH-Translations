#!/usr/bin/env python3
"""Align BetterQuesting quest-name § color/style prefixes to latest DefaultQuests.

Compares master questbook JSON titles with ja_JP.lang `.name=` values, then:
  1) rewrites leading § codes (after optional [下書き]/[自訳]/[提出済み])
  2) optionally exports a ParaTranz JSON for bulk import / API push

Examples:
  # dry-run summary
  python tools/align_quest_name_colors.py \\
    --modpack ../GT-New-Horizons-Modpack

  # apply to lang + export ParaTranz patch
  python tools/align_quest_name_colors.py \\
    --modpack ../GT-New-Horizons-Modpack \\
    --apply \\
    --export notes/_paratranz-quest-name-color-fixes.json

  # push translations via ParaTranz API (needs PARATRANZ_TOKEN)
  python tools/align_quest_name_colors.py \\
    --modpack ../GT-New-Horizons-Modpack \\
    --apply \\
    --push \\
    --project-id 8922
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

FNAME = re.compile(r"^(?P<title>.+)-(?P<id>[A-Za-z0-9_-]{22})==\.json$")
LABEL_RE = re.compile(r"^\[(下書き|自訳|提出済み)\]")
NAME_RE = re.compile(r"^betterquesting\.quest\.(?P<id>[^.]+)\.name=(?P<value>.*)$")
LEAD_RE = re.compile(r"^((?:§.)*)")


def leading_codes(text: str) -> str:
    return LEAD_RE.match(text or "").group(1)


def split_label(value: str) -> tuple[str, str]:
    match = LABEL_RE.match(value or "")
    if not match:
        return "", value or ""
    return match.group(0), value[match.end() :]


def align_value(ja_value: str, master_name: str) -> str | None:
    """Return updated JA value, or None if no change needed / not applicable."""
    master_lead = leading_codes(master_name)
    if not master_lead:
        return None
    label, rest = split_label(ja_value)
    ja_lead = leading_codes(rest)
    if ja_lead == master_lead:
        return None
    body = rest[len(ja_lead) :]
    return f"{label}{master_lead}{body}"


def index_master_names(modpack_quests: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for path in modpack_quests.rglob("*.json"):
        match = FNAME.match(path.name)
        if not match:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        props = data.get("properties:10", {}).get("betterquesting:10", {})
        name = props.get("name:8")
        if isinstance(name, str):
            out[match.group("id")] = name
    return out


def collect_fixes(lang_lines: list[str], master_names: dict[str, str]) -> list[dict]:
    fixes: list[dict] = []
    for line_no, line in enumerate(lang_lines, start=1):
        match = NAME_RE.match(line)
        if not match:
            continue
        qid = match.group("id")
        old = match.group("value")
        master = master_names.get(qid)
        if master is None:
            continue
        new = align_value(old, master)
        if new is None:
            continue
        fixes.append(
            {
                "id": qid,
                "line": line_no,
                "old": old,
                "new": new,
                "master": master,
                "old_codes": leading_codes(split_label(old)[1]),
                "new_codes": leading_codes(split_label(new)[1]),
                "lang_key": f"lang|betterquesting.quest.{qid}.name",
            }
        )
    return fixes


def apply_fixes(lang_lines: list[str], fixes: list[dict]) -> list[str]:
    by_line = {item["line"]: item for item in fixes}
    out: list[str] = []
    for line_no, line in enumerate(lang_lines, start=1):
        fix = by_line.get(line_no)
        if not fix:
            out.append(line)
            continue
        match = NAME_RE.match(line)
        assert match is not None
        out.append(f"betterquesting.quest.{fix['id']}.name={fix['new']}")
    return out


def export_paratranz_json(fixes: list[dict], master_names: dict[str, str]) -> list[dict]:
    """ParaTranz-friendly rows (key / original / translation)."""
    rows = []
    for fix in fixes:
        rows.append(
            {
                "key": fix["lang_key"],
                "original": master_names[fix["id"]],
                "translation": fix["new"],
            }
        )
    return rows


def push_paratranz(fixes: list[dict], project_id: int, token: str, file_suffix: str) -> None:
    try:
        import httpx
    except ImportError as exc:
        raise SystemExit("httpx is required for --push (pip/poetry install httpx)") from exc

    headers = {"Authorization": token}
    base = "https://paratranz.cn/api"

    with httpx.Client(base_url=base, headers=headers, timeout=60.0) as client:
        files_res = client.get(f"/projects/{project_id}/files")
        files_res.raise_for_status()
        files = files_res.json()
        file_id = None
        for item in files:
            name = item.get("name") or ""
            if name.endswith(file_suffix):
                file_id = item["id"]
                break
        if file_id is None:
            raise SystemExit(f"ParaTranz file ending with {file_suffix!r} not found")

        wanted = {fix["lang_key"]: fix for fix in fixes}
        page = 1
        updated = 0
        missing: list[str] = []
        matched: dict[str, dict] = {}
        while True:
            res = client.get(
                f"/projects/{project_id}/strings",
                params={"file": file_id, "page": page, "pageSize": 800},
            )
            res.raise_for_status()
            payload = res.json()
            for row in payload.get("results") or []:
                key = row.get("key")
                if key in wanted:
                    matched[key] = row
            page_count = payload.get("pageCount") or payload.get("page_count") or 1
            if page >= page_count:
                break
            page += 1

        for key, fix in wanted.items():
            row = matched.get(key)
            if row is None:
                missing.append(key)
                continue
            string_id = row["id"]
            body = {
                "id": string_id,
                "key": key,
                "original": row.get("original") or fix["master"],
                "translation": fix["new"],
                "stage": 1,
            }
            put = client.put(f"/projects/{project_id}/strings/{string_id}", json=body)
            put.raise_for_status()
            updated += 1

        print(f"ParaTranz push: updated={updated}, missing_on_paratranz={len(missing)}")
        if missing:
            print("missing keys (first 20):")
            for key in missing[:20]:
                print(" ", key)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--modpack",
        type=Path,
        required=True,
        help="Path to GT-New-Horizons-Modpack (latest DefaultQuests)",
    )
    parser.add_argument(
        "--lang",
        type=Path,
        default=Path("ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang"),
        help="Target ja_JP.lang path",
    )
    parser.add_argument("--apply", action="store_true", help="Write aligned names into --lang")
    parser.add_argument("--export", type=Path, help="Write ParaTranz JSON patch to this path")
    parser.add_argument("--push", action="store_true", help="Upload changed translations via ParaTranz API")
    parser.add_argument("--project-id", type=int, default=8922, help="ParaTranz project id (ja_JP=8922)")
    parser.add_argument(
        "--paratranz-file-suffix",
        default="config/txloader/forceload/betterquesting/lang/ja_JP.lang.json",
        help="ParaTranz file name suffix to locate quest lang file",
    )
    parser.add_argument("--limit", type=int, default=0, help="Only process first N fixes (debug)")
    args = parser.parse_args()

    quests_root = args.modpack / "config/betterquesting/DefaultQuests/Quests"
    if not quests_root.is_dir():
        raise SystemExit(f"DefaultQuests not found: {quests_root}")
    if not args.lang.is_file():
        raise SystemExit(f"lang not found: {args.lang}")

    master_names = index_master_names(quests_root)
    raw = args.lang.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    lines = raw.decode("utf-8").splitlines()
    fixes = collect_fixes(lines, master_names)
    if args.limit > 0:
        fixes = fixes[: args.limit]

    transitions = Counter((f["old_codes"], f["new_codes"]) for f in fixes)
    print(f"master colored titles indexed: {sum(1 for n in master_names.values() if leading_codes(n))}")
    print(f"fixes needed: {len(fixes)}")
    print("top transitions:")
    for (old_c, new_c), count in transitions.most_common(15):
        print(f"  {count:4d}  {old_c or '(none)'!r} -> {new_c!r}")

    if args.export:
        rows = export_paratranz_json(fixes, master_names)
        args.export.parent.mkdir(parents=True, exist_ok=True)
        args.export.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"exported {len(rows)} rows -> {args.export}")

    if args.apply:
        new_lines = apply_fixes(lines, fixes)
        args.lang.write_text(newline.join(new_lines) + newline, encoding="utf-8", newline="")
        print(f"applied {len(fixes)} name fixes -> {args.lang}")

    if args.push:
        token = os.environ.get("PARATRANZ_TOKEN")
        if not token:
            raise SystemExit("PARATRANZ_TOKEN env var is required for --push")
        if not fixes:
            print("nothing to push")
        else:
            push_paratranz(fixes, args.project_id, token, args.paratranz_file_suffix)

    if not args.apply and not args.export and not args.push:
        print("dry-run only (pass --apply / --export / --push)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
