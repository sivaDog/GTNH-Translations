#!/usr/bin/env python3
"""Compare BetterQuesting ja_JP.lang snapshots by quest ID and entry counts."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ENTRY_RE = re.compile(r"^betterquesting\.quest\.([^.]+)\.(name|desc)=(.*)$")
LOCAL_MARKERS = ("[下書き]", "[自訳]", "[提出済み]")


@dataclass
class Snapshot:
    label: str
    path: Path
    desc_count: int
    name_count: int
    ids: set[str]
    complete_ids: set[str]
    local_ids: dict[str, str]  # id -> name value


def load_snapshot(label: str, path: Path) -> Snapshot:
    text = path.read_text(encoding="utf-8", errors="replace")
    desc_count = text.count(".desc=")
    name_count = text.count(".name=")

    entries: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        match = ENTRY_RE.match(line)
        if match:
            entries.setdefault(match.group(1), {})[match.group(2)] = match.group(3)

    ids = set(entries)
    complete_ids = {qid for qid, fields in entries.items() if fields.keys() >= {"name", "desc"}}
    local_ids = {
        qid: fields["name"]
        for qid, fields in entries.items()
        if "name" in fields and any(marker in fields["name"] for marker in LOCAL_MARKERS)
    }

    return Snapshot(label, path, desc_count, name_count, ids, complete_ids, local_ids)


def format_ids(ids: set[str], limit: int = 30) -> str:
    ordered = sorted(ids)
    if len(ordered) <= limit:
        return ", ".join(ordered)
    head = ", ".join(ordered[:limit])
    return f"{head}, ... (+{len(ordered) - limit} more)"


def compare(base: Snapshot, target: Snapshot) -> None:
    missing_complete = base.complete_ids - target.complete_ids
    missing_any = base.ids - target.ids
    new_complete = target.complete_ids - base.complete_ids
    missing_local = {
        qid: name
        for qid, name in base.local_ids.items()
        if qid not in target.complete_ids
    }

    print(f"=== {base.label} -> {target.label} ===")
    print(
        f"counts: desc {base.desc_count} -> {target.desc_count} "
        f"({target.desc_count - base.desc_count:+d}), "
        f"name {base.name_count} -> {target.name_count} "
        f"({target.name_count - base.name_count:+d})"
    )
    print(
        f"complete quests: {len(base.complete_ids)} -> {len(target.complete_ids)} "
        f"({len(target.complete_ids) - len(base.complete_ids):+d})"
    )

    if missing_complete:
        print(f"missing complete entries ({len(missing_complete)}): {format_ids(missing_complete)}")
    else:
        print("missing complete entries: none")

    if missing_any - missing_complete:
        partial = missing_any - missing_complete
        print(f"missing partial entries ({len(partial)}): {format_ids(partial)}")

    if missing_local:
        print(f"missing local-marked quests ({len(missing_local)}):")
        for qid in sorted(missing_local):
            print(f"  {qid}: {missing_local[qid]}")

    if new_complete:
        print(f"new complete entries ({len(new_complete)}): {format_ids(new_complete)}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "snapshots",
        nargs="+",
        metavar="LABEL=PATH",
        help="Snapshot as Label=path/to/ja_JP.lang",
    )
    parser.add_argument(
        "--baseline",
        help="Baseline label for pairwise comparisons (default: first snapshot)",
    )
    parser.add_argument(
        "--id-list",
        type=Path,
        help="Optional quest ID list to report coverage for each snapshot",
    )
    args = parser.parse_args()

    snapshots: list[Snapshot] = []
    for item in args.snapshots:
        if "=" not in item:
            print(f"invalid snapshot (expected LABEL=PATH): {item}", file=sys.stderr)
            return 2
        label, raw_path = item.split("=", 1)
        path = Path(raw_path)
        if not path.is_file():
            print(f"missing file: {path}", file=sys.stderr)
            return 2
        snapshots.append(load_snapshot(label, path))

    print("Snapshot summary")
    print("-" * 72)
    for snap in snapshots:
        print(
            f"{snap.label:24} desc={snap.desc_count:5} name={snap.name_count:5} "
            f"complete={len(snap.complete_ids):5} local={len(snap.local_ids):4}  {snap.path}"
        )
    print()

    baseline_label = args.baseline or snapshots[0].label
    baseline = next((snap for snap in snapshots if snap.label == baseline_label), None)
    if baseline is None:
        print(f"baseline not found: {baseline_label}", file=sys.stderr)
        return 2

    for snap in snapshots:
        if snap.label == baseline.label:
            continue
        compare(baseline, snap)

    if args.id_list:
        listed = [
            line.strip()
            for line in args.id_list.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        print(f"ID list coverage ({args.id_list.name}, {len(listed)} ids)")
        print("-" * 72)
        for snap in snapshots:
            missing = [qid for qid in listed if qid not in snap.complete_ids]
            print(f"{snap.label:24} missing {len(missing):3} / {len(listed)}")
            if missing:
                print(f"  {format_ids(set(missing))}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
