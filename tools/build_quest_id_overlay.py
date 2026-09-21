#!/usr/bin/env python3
"""Build a BetterQuesting overlay from a release-verified quest ID list."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ENTRY_RE = re.compile(
    r"^betterquesting\.quest\.(?P<id>[^.]+)\.(?P<field>name|desc)=(?P<value>.*)$"
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ids", required=True, type=Path)
    parser.add_argument("--source-lang", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    ids = [
        line.strip()
        for line in args.ids.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate quest IDs in list")

    wanted = set(ids)
    entries: dict[str, dict[str, str]] = {}
    for line in args.source_lang.read_text(encoding="utf-8").splitlines():
        match = ENTRY_RE.match(line)
        if match and match["id"] in wanted:
            entries.setdefault(match["id"], {})[match["field"]] = match["value"]

    incomplete = [
        quest_id
        for quest_id in ids
        if set(entries.get(quest_id, {})) != {"name", "desc"}
    ]
    if incomplete:
        raise SystemExit("Missing name/desc for: " + ", ".join(incomplete))

    output = [
        "# Generated from the release-verified quest ID list.",
        f"# Source ID list: {args.ids.name}",
        "",
    ]
    for quest_id in ids:
        output.extend(
            [
                f"betterquesting.quest.{quest_id}.name={entries[quest_id]['name']}",
                f"betterquesting.quest.{quest_id}.desc={entries[quest_id]['desc']}",
                "",
            ]
        )
    args.output.write_text("\n".join(output), encoding="utf-8")
    print(f"Built overlay for {len(ids)} verified quests")


if __name__ == "__main__":
    main()
