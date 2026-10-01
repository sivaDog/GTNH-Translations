#!/usr/bin/env bash
# Overwrite ServerUtilities ja_JP in the GTNH 2.8.4 Prism instance.
#
# Source is the repo load file (ParaTranz mirror + 手元ドラフト).
# 2.8.4 uses TX-Loader 1.8.5, so the game-visible copy is forceload.
# ServerUtilities-2.2.2.jar ships its own assets/serverutilities/lang/ja_JP.lang,
# but a bracket domain that exists only in forceload is declared last and wins
# over it. load/ is the 2.9 layout of the pack and is not written: a load/ copy
# would lose to the jar again (the official 2.8.4 zip has none).
#
# The mirror has 734 keys; 70 of them are only looked up by newer versions and
# are harmless extra entries on 2.8.4.
#
# Usage:
#   ./sync-verified-su.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-su.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc
REL_LANG="config/txloader/load/ServerUtilities[serverutilities]/lang/ja_JP.lang"
SOURCE_LANG="$REPO_ROOT/ja_JP/$REL_LANG"
FORCE_DST="$INSTANCE_MC/config/txloader/forceload/ServerUtilities[serverutilities]/lang/ja_JP.lang"
LOAD_DST="$INSTANCE_MC/config/txloader/load/ServerUtilities[serverutilities]"

if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing ServerUtilities lang: $(short_path "$SOURCE_LANG")" >&2
  exit 1
fi
if [[ ! -d "$INSTANCE_MC" ]]; then
  echo "Missing instance .minecraft: $(short_path "$INSTANCE_MC")" >&2
  echo "Set INSTANCE_MC in .env or pass it inline." >&2
  exit 1
fi
if [[ -e "$LOAD_DST" ]]; then
  echo "Warning: $(short_path "$LOAD_DST") exists; the jar's ja_JP may win over forceload." >&2
fi

cd "$REPO_ROOT"
echo "Repo:     $(short_path "$REPO_ROOT")"
echo "Branch:   $(git branch --show-current 2>/dev/null || echo '(detached)')"
echo "Instance: $(short_path "$INSTANCE_MC")"
echo "Source:   $(short_path "$SOURCE_LANG")"
for mark in 下書き 自訳 提出済み; do
  n="$(grep -c "^[^#].*=\[$mark\]" "$SOURCE_LANG" || true)"
  [[ "$n" -gt 0 ]] && echo "Marks:    [$mark] $n 件"
done

mkdir -p "$(dirname "$FORCE_DST")"
cp -a "$SOURCE_LANG" "$FORCE_DST"
echo "Wrote forceload (game-visible on 2.8.4)"
echo "  $(short_path "$FORCE_DST")"

echo "Synced ServerUtilities ja_JP."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
