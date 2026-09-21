#!/usr/bin/env bash
# Overwrite dreamcraft Thaumonomicon ja_JP in the GTNH 2.8.4 Prism instance.
#
# Source is the repo load file (ParaTranz / 手元ドラフトの正本).
# 2.8.4 uses TX-Loader 1.8.5, so the game-visible copy is forceload.
# The leftover load copy from the 2026-07-18 ja_JP overlay is also
# overwritten when present, so the two instance files do not drift.
#
# Usage:
#   ./sync-verified-thaums.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-thaums.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
INSTANCE_MC="${INSTANCE_MC:-$HOME/AppData/Roaming/PrismLauncher/instances/GT_New_Horizons_2.8.4_Java_17-25/.minecraft}"
REL_LANG="config/txloader/load/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"
SOURCE_LANG="$REPO_ROOT/ja_JP/$REL_LANG"
FORCE_DST="$INSTANCE_MC/config/txloader/forceload/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"
LOAD_DST="$INSTANCE_MC/config/txloader/load/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"

if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing dreamcraft lang: $SOURCE_LANG" >&2
  exit 1
fi
if [[ ! -d "$INSTANCE_MC" ]]; then
  echo "Missing instance .minecraft: $INSTANCE_MC" >&2
  echo "Set INSTANCE_MC to your Prism instance path." >&2
  exit 1
fi

cd "$REPO_ROOT"
echo "Repo:     $REPO_ROOT"
echo "Branch:   $(git branch --show-current 2>/dev/null || echo '(detached)')"
echo "Instance: $INSTANCE_MC"
echo "Source:   $SOURCE_LANG"

mkdir -p "$(dirname "$FORCE_DST")"
cp -a "$SOURCE_LANG" "$FORCE_DST"
echo "Wrote forceload (game-visible on 2.8.4)"
echo "  $FORCE_DST"

if [[ -f "$LOAD_DST" ]]; then
  cp -a "$SOURCE_LANG" "$LOAD_DST"
  echo "Wrote load (leftover overlay; not used while forceload exists)"
  echo "  $LOAD_DST"
fi

echo "Synced dreamcraft Thaumonomicon ja_JP."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
