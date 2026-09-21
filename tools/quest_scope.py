#!/usr/bin/env python3
"""Compare a quest line between two GTNH Modpack git refs."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


QUEST_FILE_RE = re.compile(r"^(?P<slug>.+)-(?P<id>[A-Za-z0-9_-]{22})==\.json$")
LANG_ENTRY_RE = re.compile(
    r"^betterquesting\.quest\.(?P<id>[^.]+)\.(?P<field>name|desc)=(?P<value>.*)$"
)
TEMPLATE_PATH = "config/txloader/load/betterquesting/lang/template.lang"


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    ).stdout


def find_questline(repo: Path, ref: str, needle: str) -> str:
    root = "config/betterquesting/DefaultQuests/QuestLines"
    names = git(repo, "ls-tree", "-d", "--name-only", f"{ref}:{root}").splitlines()
    paths = [f"{root}/{name}" for name in names]
    matches = [path for path in paths if needle.casefold() in Path(path).name.casefold()]
    if len(matches) != 1:
        raise SystemExit(f"Expected one quest line matching {needle!r} at {ref}: {matches}")
    return matches[0]


def read_quests(repo: Path, ref: str, questline: str) -> list[dict[str, str]]:
    paths = git(repo, "ls-tree", "-r", "--name-only", ref, "--", questline).splitlines()
    quests = []
    for path in paths:
        match = QUEST_FILE_RE.match(Path(path).name)
        if match:
            quests.append({"id": match["id"], "slug": match["slug"], "path": path})
    return quests


def read_template(repo: Path, ref: str) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{ref}:{TEMPLATE_PATH}"],
        check=False,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    for line in result.stdout.splitlines():
        match = LANG_ENTRY_RE.match(line)
        if match:
            entries.setdefault(match["id"], {})[match["field"]] = match["value"]
    return entries


def normalized_name(value: str) -> str:
    value = re.sub(r"§.", "", value)
    return re.sub(r"\W+", "", value, flags=re.UNICODE).casefold()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--modpack-repo", required=True, type=Path)
    parser.add_argument("--release-ref", default="2.8.4")
    parser.add_argument("--latest-ref", default="origin/master")
    parser.add_argument("--questline", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    release_line = find_questline(args.modpack_repo, args.release_ref, args.questline)
    latest_line = find_questline(args.modpack_repo, args.latest_ref, args.questline)
    release_quests = read_quests(args.modpack_repo, args.release_ref, release_line)
    latest_quests = read_quests(args.modpack_repo, args.latest_ref, latest_line)
    release_text = read_template(args.modpack_repo, args.release_ref)
    latest_text = read_template(args.modpack_repo, args.latest_ref)

    release_by_slug = {quest["slug"]: quest for quest in release_quests}
    release_by_id = {quest["id"]: quest for quest in release_quests}
    release_by_name: dict[str, list[dict[str, str]]] = {}
    for quest in release_quests:
        name = release_text.get(quest["id"], {}).get("name", "")
        release_by_name.setdefault(normalized_name(name), []).append(quest)

    included = []
    latest_only = []
    matched_release_paths: set[str] = set()
    for latest in latest_quests:
        release = release_by_id.get(latest["id"])
        match_kind = "same-id"
        if release is None:
            release = release_by_slug.get(latest["slug"])
            match_kind = "same-slug"
        if release is not None and release["path"] in matched_release_paths:
            release = None
        latest_entry = latest_text.get(latest["id"], {})
        if release is None:
            candidates = release_by_name.get(normalized_name(latest_entry.get("name", "")), [])
            if len(candidates) == 1:
                release = candidates[0]
                match_kind = "same-english-name"
        if release is None:
            latest_only.append({**latest, "name_en": latest_entry.get("name", "")})
            continue

        release_entry = release_text.get(release["id"], {})
        matched_release_paths.add(release["path"])
        included.append(
            {
                "latest_id": latest["id"],
                "release_id": release["id"],
                "slug": latest["slug"],
                "match": match_kind,
                "same_id": latest["id"] == release["id"],
                "name_en": latest_entry.get("name", ""),
                "release_name_en": release_entry.get("name", ""),
                "source_changed": (
                    latest_entry != release_entry if latest_entry and release_entry else None
                ),
                "latest_path": latest["path"],
                "release_path": release["path"],
            }
        )

    release_only = [
        {**quest, "name_en": release_text.get(quest["id"], {}).get("name", "")}
        for quest in release_quests
        if quest["path"] not in matched_release_paths
    ]
    payload = {
        "latest_modpack_commit": git(args.modpack_repo, "rev-parse", args.latest_ref).strip(),
        "latest_ref": args.latest_ref,
        "release_modpack_commit": git(args.modpack_repo, "rev-parse", args.release_ref).strip(),
        "release_ref": args.release_ref,
        "questline": args.questline,
        "counts": {
            "latest": len(latest_quests),
            "release": len(release_quests),
            "included": len(included),
            "latest_only": len(latest_only),
            "release_only": len(release_only),
        },
        "included": included,
        "latest_only": latest_only,
        "release_only": release_only,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
