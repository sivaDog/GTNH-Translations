#!/usr/bin/env bash
# Overwrite Nuclear Control 2 ja_JP in the GTNH 2.8.4 Prism instance.
#
# Source is the repo load file (ParaTranz mirror + 手元ドラフト).
# 2.8.4 uses TX-Loader 1.8.5, so the game-visible copy is forceload.
# IC2NuclearControl-2.6.20.jar ships no assets/nuclearcontrol/lang/ja_JP.lang,
# so the pack copy wins outright. load/ is the 2.9 layout of the pack and is
# not written: the official 2.8.4 zip has no load copy of this folder.
#
# The mirror has 213 keys and the 2.8.4 jar looks up 204 of them; the other 9
# are GUI titles (gui.tile.*.name.title) added in newer versions.
#
# Nuclear Control strings owned by GregTech (GT_KEYS below) are also copied
# into .minecraft/GregTech_ja_JP.lang: the 2.8.4 GregTech jar reads them from
# that legacy file, not from txloader.
#
# Usage:
#   ./sync-verified-nc.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-nc.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc
REL_LANG="config/txloader/load/Nuclear Control 2[nuclearcontrol]/lang/ja_JP.lang"
SOURCE_LANG="$REPO_ROOT/ja_JP/$REL_LANG"
FORCE_DST="$INSTANCE_MC/config/txloader/forceload/Nuclear Control 2[nuclearcontrol]/lang/ja_JP.lang"
GT_SOURCE_LANG="$REPO_ROOT/ja_JP/config/txloader/load/GregTech[gregtech]/lang/ja_JP.lang"
GT_LEGACY_LANG="$INSTANCE_MC/GregTech_ja_JP.lang"
# KEY, or LEGACY=SOURCE when 2.8.4 used a different key than the repo.
GT_KEYS=(
  gt.behaviour.sensorkit.tooltip                           # GregTech Sensor Kit tooltip
  gt.sensorcard.tooltip_main=gt.sensorcard.tooltip         # GregTech Sensor Card tooltip
)

if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing Nuclear Control lang: $(short_path "$SOURCE_LANG")" >&2
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

if [[ -f "$GT_LEGACY_LANG" ]]; then
  gt_args=()
  for key in "${GT_KEYS[@]}"; do gt_args+=(--key "$key"); done
  MSYS2_ARG_CONV_EXCL='*' python "$(winpath "$REPO_ROOT/tools/patch_gregtech_legacy_lang.py")" \
    --source-lang "$(winpath "$GT_SOURCE_LANG")" \
    --legacy-lang "$(winpath "$GT_LEGACY_LANG")" \
    "${gt_args[@]}"
  echo "  $(short_path "$GT_LEGACY_LANG")"
else
  echo "Skipped GregTech keys: $(short_path "$GT_LEGACY_LANG") not found (created on first GregTech launch)"
fi

echo "Synced Nuclear Control 2 ja_JP."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
