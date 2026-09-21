#!/usr/bin/env python3
"""Merge BetterQuesting name/desc entries into an existing lang file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ENTRY_RE = re.compile(r"^(betterquesting\.quest\.[^.]+\.(?:name|desc))=(.*)$")


def read_entries(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ENTRY_RE.match(line)
        if match:
            entries[match.group(1)] = match.group(2)
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--overlay", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    updates = read_entries(args.overlay)
    if not updates:
        raise SystemExit("Overlay contains no BetterQuesting entries")

    output: list[str] = []
    replaced: set[str] = set()
    for line in args.base.read_text(encoding="utf-8").splitlines():
        match = ENTRY_RE.match(line)
        if match and match.group(1) in updates:
            key = match.group(1)
            output.append(f"{key}={updates[key]}")
            replaced.add(key)
        else:
            output.append(line)

    missing = [key for key in updates if key not in replaced]
    if missing:
        output.extend(["", "# Release-scoped test overlay entries"])
        output.extend(f"{key}={updates[key]}" for key in missing)

    args.output.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(
        f"Merged {len(updates)} entries "
        f"({len(replaced)} replaced, {len(missing)} appended)"
    )


if __name__ == "__main__":
    main()
