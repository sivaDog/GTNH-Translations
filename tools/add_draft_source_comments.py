#!/usr/bin/env python3
"""Add English source comments above draft BetterQuesting translations."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DRAFT_NAME_RE = re.compile(
    r"^betterquesting\.quest\.(?P<id>[^.]+)\.name=\[下書き\]"
)
SOURCE_COMMENT_RE = re.compile(r"^# EN (?:name|desc):")


def load_sources(paths: list[Path]) -> dict[str, tuple[str, str]]:
    sources: dict[str, tuple[str, str]] = {}
    for path in paths:
        rows = json.loads(path.read_text(encoding="utf-8"))
        for row in rows:
            quest_id = row.get("latest_id") or row.get("id")
            name = row.get("name_en")
            desc = row.get("desc_en")
            if quest_id and name is not None and desc is not None:
                clean = lambda value: re.sub(r"\r?\n", "%n", value).rstrip()
                sources[quest_id] = (clean(name), clean(desc))
    return sources


def clean_draft_blocks(lines: list[str]) -> list[str]:
    """Remove previously generated comments, including multiline spillover."""
    cleaned: list[str] = []
    index = 0
    while index < len(lines):
        if not lines[index].startswith("# Quest:"):
            if not SOURCE_COMMENT_RE.match(lines[index]):
                cleaned.append(lines[index])
            index += 1
            continue
        end = index + 1
        while end < len(lines) and not lines[end].startswith("# Quest:"):
            end += 1
        block = lines[index:end]
        draft_index = next(
            (offset for offset, line in enumerate(block) if DRAFT_NAME_RE.match(line)),
            None,
        )
        if draft_index is None:
            cleaned.extend(line for line in block if not SOURCE_COMMENT_RE.match(line))
        else:
            cleaned.append(block[0])
            cleaned.extend(block[draft_index:])
        index = end
    return cleaned


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path, action="append")
    args = parser.parse_args()

    sources = load_sources(args.source)
    raw = args.lang.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    lines = clean_draft_blocks(raw.decode("utf-8").splitlines())
    output: list[str] = []
    added = 0
    missing: list[str] = []

    for line in lines:
        if SOURCE_COMMENT_RE.match(line):
            continue
        match = DRAFT_NAME_RE.match(line)
        if match:
            quest_id = match["id"]
            source = sources.get(quest_id)
            if source is None:
                missing.append(quest_id)
            else:
                output.extend(
                    [f"# EN name: {source[0]}", f"# EN desc: {source[1]}"]
                )
                added += 1
        output.append(line)

    if missing:
        raise SystemExit("Missing English source for drafts: " + ", ".join(missing))
    args.lang.write_text(newline.join(output) + newline, encoding="utf-8", newline="")
    print(f"Added English source comments to {added} drafts")


if __name__ == "__main__":
    main()
