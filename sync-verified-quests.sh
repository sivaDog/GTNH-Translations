#!/usr/bin/env bash
# Build and sync every quest verified as present in GTNH 2.8.4.
# Scope is notes/quest-ids-2.8.4.txt (How to Be(e), Forestry+Multifarm, Be(e) Breeding,
# Storing and Transforming EU / EUの蓄電と変圧, Basic Automation / 基本的な自動化,
# Getting Around... / 旅に出かけよう..., Novice Thaumaturgy, Pickups, ...).
# The list is quest IDs, not chapters. Single pickups go in the Pickups section.
# Quests missing from that list are NOT copied to the instance even if edited in ja_JP.lang.
#
# Usage:
#   ./sync-verified-quests.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-quests.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc
ID_LIST="$REPO_ROOT/notes/quest-ids-2.8.4.txt"
SOURCE_LANG="$REPO_ROOT/ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang"
QB_DST="$INSTANCE_MC/config/txloader/forceload/betterquesting/lang/ja_JP.lang"
OVERLAY="$(mktemp "${TMPDIR:-/tmp}/gtnh-ja-quests-2.8.4.XXXXXX.lang")"
MERGED="$(mktemp "${TMPDIR:-/tmp}/gtnh-ja-quests-merged.XXXXXX.lang")"

cleanup() {
  rm -f "$OVERLAY" "$MERGED"
}
trap cleanup EXIT

if [[ ! -f "$ID_LIST" ]]; then
  echo "Missing quest id list: $(short_path "$ID_LIST")" >&2
  exit 1
fi
if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing questbook lang: $(short_path "$SOURCE_LANG")" >&2
  exit 1
fi
if [[ ! -d "$INSTANCE_MC" ]]; then
  echo "Missing instance .minecraft: $(short_path "$INSTANCE_MC")" >&2
  echo "Set INSTANCE_MC in .env or pass it inline." >&2
  exit 1
fi

cd "$REPO_ROOT"
echo "Repo:     $(short_path "$REPO_ROOT")"
echo "Branch:   $(git branch --show-current 2>/dev/null || echo '(detached)')"
echo "Instance: $(short_path "$INSTANCE_MC")"

python "$REPO_ROOT/tools/check_quest_lang_coverage.py" \
  --ids "$ID_LIST" \
  --lang "$SOURCE_LANG"

python "$REPO_ROOT/tools/build_quest_id_overlay.py" \
  --ids "$ID_LIST" \
  --source-lang "$SOURCE_LANG" \
  --output "$OVERLAY"

mkdir -p "$(dirname "$QB_DST")"
if [[ -f "$QB_DST" ]]; then
  python "$REPO_ROOT/tools/merge_quest_lang_overlay.py" \
    --base "$QB_DST" --overlay "$OVERLAY" --output "$MERGED"
  cp -a "$MERGED" "$QB_DST"
else
  cp -a "$OVERLAY" "$QB_DST"
fi

echo "Synced release-scoped questbook overlay."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
