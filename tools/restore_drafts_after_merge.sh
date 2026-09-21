#!/usr/bin/env bash
# Restore local [下書き] quest entries after merging origin/master.
#
# Usage (from repo root, on work branch right after merge commit):
#   ./tools/restore_drafts_after_merge.sh
#   ./tools/restore_drafts_after_merge.sh path/to/local-snapshot.lang
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$REPO_ROOT/ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang"
SOURCE="${1:-}"

if [[ -z "$SOURCE" ]]; then
  if git -C "$REPO_ROOT" rev-parse --verify HEAD^1 >/dev/null 2>&1; then
    SOURCE="$(mktemp "${TMPDIR:-/tmp}/gtnh-local-pre-merge.XXXXXX.lang")"
    git -C "$REPO_ROOT" show "HEAD^1:ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang" >"$SOURCE"
    cleanup() { rm -f "$SOURCE"; }
    trap cleanup EXIT
    echo "Using pre-merge snapshot from HEAD^1"
  else
    echo "Pass a local snapshot lang file: $0 path/to/local.lang" >&2
    exit 1
  fi
fi

python "$REPO_ROOT/tools/overlay_draft_quests.py" "$SOURCE" "$TARGET"
echo "Done. Run ./sync-verified-quests.sh and restart Minecraft to verify."
