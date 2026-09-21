#!/usr/bin/env python3
"""Build a release-ID BetterQuesting overlay from a quest scope mapping."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ENTRY_RE = re.compile(
    r"^betterquesting\.quest\.(?P<id>[^.]+)\.(?P<field>name|desc)=(?P<value>.*)$"
)


def read_lang(path: Path) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ENTRY_RE.match(line)
        if match:
            entries.setdefault(match["id"], {})[match["field"]] = match["value"]
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", required=True, type=Path)
    parser.add_argument("--source-lang", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    scope = json.loads(args.scope.read_text(encoding="utf-8"))
    source = read_lang(args.source_lang)
    output = [
        "# Generated test overlay; do not commit as a release translation.",
        f"# Latest modpack commit: {scope['latest_modpack_commit']}",
        f"# Test release: {scope['release_ref']} ({scope['release_modpack_commit']})",
        "",
    ]
    missing = []
    for quest in scope["included"]:
        latest_id = quest["latest_id"]
        release_id = quest["release_id"]
        entry = source.get(latest_id, {})
        if "name" not in entry or "desc" not in entry:
            missing.append(latest_id)
            continue
        output.extend(
            [
                f"# Quest: {quest['slug']}",
                f"betterquesting.quest.{release_id}.name={entry['name']}",
                f"betterquesting.quest.{release_id}.desc={entry['desc']}",
                "",
            ]
        )
    if missing:
        raise SystemExit(f"Missing source lang entries for: {', '.join(missing)}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(output), encoding="utf-8")


if __name__ == "__main__":
    main()
