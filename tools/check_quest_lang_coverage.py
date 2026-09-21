#!/usr/bin/env python3
"""Report quest IDs listed for sync that are missing from ja_JP.lang."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ENTRY_RE = re.compile(r"^betterquesting\.quest\.([^.]+)\.(name|desc)=(.*)$")


def load_ids(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def load_entries(path: Path) -> dict[str, set[str]]:
    entries: dict[str, set[str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ENTRY_RE.match(line)
        if match:
            entries.setdefault(match.group(1), set()).add(match.group(2))
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ids", required=True, type=Path)
    parser.add_argument("--lang", required=True, type=Path)
    args = parser.parse_args()

    ids = load_ids(args.ids)
    entries = load_entries(args.lang)
    incomplete = [qid for qid in ids if entries.get(qid) != {"name", "desc"}]

    if incomplete:
        print("Missing name/desc for:", ", ".join(incomplete), file=sys.stderr)
        print(
            "Hint: after upstream merge run "
            "./tools/restore_drafts_after_merge.sh",
            file=sys.stderr,
        )
        return 1

    print(f"All {len(ids)} listed quests are present in {args.lang.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
