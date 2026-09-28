#!/usr/bin/env bash
# Overwrite LittleTiles ja_JP in the GTNH 2.8.4 Prism instance.
#
# Source is the repo load file (ParaTranz mirror + 手元ドラフト).
# 2.8.4 uses TX-Loader 1.8.5, so the game-visible copy is forceload.
# littletiles-1.5.14-GTNH.jar ships no assets/littletiles/lang/ja_JP.lang, so
# the pack copy wins outright. load/ is the 2.9 layout of the pack and is not
# written: the official 2.8.4 zip has no load copy of this folder.
#
# The mirror has 61 keys but the 2.8.4 jar only looks up 32 of them; the rest
# (Chisel shapes and place modes, the collision tool) belong to newer versions
# and are harmless extra entries here.
#
# Usage:
#   ./sync-verified-lt.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-lt.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc
REL_LANG="config/txloader/load/LittleTiles[littletiles]/lang/ja_JP.lang"
SOURCE_LANG="$REPO_ROOT/ja_JP/$REL_LANG"
FORCE_DST="$INSTANCE_MC/config/txloader/forceload/LittleTiles[littletiles]/lang/ja_JP.lang"

if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing LittleTiles lang: $(short_path "$SOURCE_LANG")" >&2
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
echo "Source:   $(short_path "$SOURCE_LANG")"
for mark in 下書き 自訳 提出済み; do
  n="$(grep -c "^[^#].*=\[$mark\]" "$SOURCE_LANG" || true)"
  [[ "$n" -gt 0 ]] && echo "Marks:    [$mark] $n 件"
done

mkdir -p "$(dirname "$FORCE_DST")"
cp -a "$SOURCE_LANG" "$FORCE_DST"
echo "Wrote forceload (game-visible on 2.8.4)"
echo "  $(short_path "$FORCE_DST")"

echo "Synced LittleTiles ja_JP."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
