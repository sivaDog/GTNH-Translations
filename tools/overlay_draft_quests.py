#!/usr/bin/env python3
"""Overlay local quest drafts onto a target lang file (replace or insert)."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


NAME_RE = re.compile(r"^betterquesting\.quest\.([^.]+)\.name=(.*)$")
ENTRY_RE = re.compile(r"^betterquesting\.quest\.([^.]+)\.(name|desc)=(.*)$")
DRAFT_MARKERS = ("[下書き]", "[自訳]", "[提出済み]")


@dataclass
class QuestBlock:
    qid: str
    lines: list[str]


def _block_start(lines: list[str], name_index: int) -> int:
    start = name_index
    while start > 0 and lines[start - 1].startswith("#"):
        start -= 1
    if (
        start > 0
        and lines[start - 1].strip() == ""
        and start > 1
        and lines[start - 2].startswith("#")
    ):
        start -= 1
    return start


def parse_quest_blocks(text: str) -> tuple[list[str], list[QuestBlock]]:
    lines = text.splitlines()
    blocks: list[QuestBlock] = []
    index = 0
    while index < len(lines):
        match = NAME_RE.match(lines[index])
        if not match:
            index += 1
            continue
        start = _block_start(lines, index)
        end = index + 1
        while end < len(lines) and not NAME_RE.match(lines[end]):
            end += 1
        blocks.append(QuestBlock(match.group(1), lines[start:end]))
        index = end
    return lines, blocks


def entry_name(block: QuestBlock) -> str:
    for line in block.lines:
        match = NAME_RE.match(line)
        if match:
            return match.group(2)
    return ""


def is_local_draft(block: QuestBlock) -> bool:
    name = entry_name(block)
    return any(marker in name for marker in DRAFT_MARKERS)


def find_insert_index(target_blocks: list[QuestBlock], source_order: list[str], qid: str) -> int:
    if qid not in source_order:
        return len(target_blocks)

    position = source_order.index(qid)
    for index in range(position - 1, -1, -1):
        anchor = source_order[index]
        for target_index, block in enumerate(target_blocks):
            if block.qid == anchor:
                return target_index + 1

    for index in range(position + 1, len(source_order)):
        anchor = source_order[index]
        for target_index, block in enumerate(target_blocks):
            if block.qid == anchor:
                return target_index

    return len(target_blocks)


def overlay_blocks(
    target_blocks: list[QuestBlock],
    source_blocks: dict[str, QuestBlock],
    source_order: list[str],
    qids: set[str],
) -> tuple[list[QuestBlock], dict[str, int]]:
    result = [QuestBlock(block.qid, block.lines[:]) for block in target_blocks]
    target_index = {block.qid: index for index, block in enumerate(result)}
    stats = {"replaced": 0, "inserted": 0, "missing_source": 0}

    for qid in sorted(qids, key=lambda item: source_order.index(item) if item in source_order else 10**9):
        source = source_blocks.get(qid)
        if source is None:
            stats["missing_source"] += 1
            continue

        new_block = QuestBlock(qid, source.lines[:])
        if qid in target_index:
            result[target_index[qid]] = new_block
            stats["replaced"] += 1
            continue

        insert_at = find_insert_index(result, source_order, qid)
        result.insert(insert_at, new_block)
        target_index = {block.qid: index for index, block in enumerate(result)}
        stats["inserted"] += 1

    return result, stats


def render_file(original_lines: list[str], original_blocks: list[QuestBlock], merged_blocks: list[QuestBlock]) -> str:
    if not original_blocks:
        body = "\n\n".join("\n".join(block.lines) for block in merged_blocks)
        return body + ("\n" if body else "")

    first_start = _block_start(original_lines, original_lines.index(original_blocks[0].lines[0]))
    prefix = original_lines[:first_start]

    last_block = original_blocks[-1]
    last_start = original_lines.index(last_block.lines[0])
    last_end = last_start + len(last_block.lines)
    suffix = original_lines[last_end:]

    parts: list[str] = []
    if prefix:
        parts.append("\n".join(prefix).rstrip())

    rendered_blocks = "\n\n".join("\n".join(block.lines) for block in merged_blocks).strip()
    if rendered_blocks:
        parts.append(rendered_blocks)

    if suffix:
        parts.append("\n".join(suffix).lstrip("\n").rstrip())

    return "\n".join(parts) + "\n"


def collect_qids(source_blocks: dict[str, QuestBlock], explicit: set[str], include_submitted: bool) -> set[str]:
    qids = set(explicit)
    for qid, block in source_blocks.items():
        if is_local_draft(block):
            qids.add(qid)
        elif include_submitted and "[提出済み]" in entry_name(block):
            qids.add(qid)
    return qids


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Local snapshot lang file (pre-merge branch)")
    parser.add_argument("target", type=Path, help="Lang file to update in-place")
    parser.add_argument("quest_ids", nargs="*", help="Extra quest IDs to force overlay")
    parser.add_argument(
        "--include-submitted",
        action="store_true",
        help="Also overlay [提出済み] entries from source",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print stats without writing")
    args = parser.parse_args()

    source_text = args.source.read_text(encoding="utf-8")
    target_text = args.target.read_text(encoding="utf-8")

    _, source_blocks_list = parse_quest_blocks(source_text)
    target_lines, target_blocks_list = parse_quest_blocks(target_text)

    source_blocks = {block.qid: block for block in source_blocks_list}
    source_order = [block.qid for block in source_blocks_list]
    qids = collect_qids(source_blocks, set(args.quest_ids), args.include_submitted)

    merged_blocks, stats = overlay_blocks(target_blocks_list, source_blocks, source_order, qids)
    merged_text = render_file(target_lines, target_blocks_list, merged_blocks)

    print(
        "overlay: "
        f"{len(qids)} selected, "
        f"{stats['replaced']} replaced, "
        f"{stats['inserted']} inserted, "
        f"{stats['missing_source']} missing in source"
    )

    if stats["inserted"]:
        inserted = [
            qid
            for qid in qids
            if qid in source_blocks and qid not in {block.qid for block in target_blocks_list}
        ]
        print("inserted IDs:", ", ".join(inserted))

    if args.dry_run:
        return 0

    args.target.write_text(merged_text, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
