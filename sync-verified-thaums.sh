#!/usr/bin/env bash
# Overwrite dreamcraft (Thaumonomicon and the rest of the GT: New Horizons
# strings) ja_JP in the GTNH 2.8.4 Prism instance.
#
# Source is the repo load file (ParaTranz / 手元ドラフトの正本).
# 2.8.4 uses TX-Loader 1.8.5, so the game-visible copy is forceload. load/ is
# the 2.9 layout of the pack and is not written: the official 2.8.4 zip has no
# load copy of this folder.
#
# The mirror follows the 2.9 CoreMod, so it is fitted to 2.8.4 on the way out by
# tools/build_dreamcraft_2_8_4_overlay.py: keys 2.9 dropped are filled back in,
# and values whose format specifiers the 2.8.4 code cannot feed are reverted.
# Both fall back to the official 2.8.4 ja_JP, read from RELEASE_284_MC (env or
# .env; default ../releases/2.8.4/.minecraft next to this repo), else English.
#
# Usage:
#   ./sync-verified-thaums.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-thaums.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc
REL_LANG="config/txloader/load/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"
SOURCE_LANG="$REPO_ROOT/ja_JP/$REL_LANG"
FORCE_DST="$INSTANCE_MC/config/txloader/forceload/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"
PACK_EN="$INSTANCE_MC/config/txloader/load/dreamcraft/lang/en_US.lang"

if [[ -z "${RELEASE_284_MC:-}" && -f "$REPO_ROOT/.env" ]]; then
  RELEASE_284_MC="$(sed -n 's/^RELEASE_284_MC=//p' "$REPO_ROOT/.env" \
    | head -n 1 | tr -d '\r' | sed 's/^"\(.*\)"$/\1/')"
fi
RELEASE_284_MC="${RELEASE_284_MC:-$REPO_ROOT/../releases/2.8.4/.minecraft}"
RELEASE_JA="$RELEASE_284_MC/config/txloader/forceload/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"

BUILT="$(mktemp "${TMPDIR:-/tmp}/gtnh-ja-dreamcraft.XXXXXX.lang")"
cleanup() {
  rm -f "$BUILT"
}
trap cleanup EXIT

if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing dreamcraft lang: $(short_path "$SOURCE_LANG")" >&2
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
if [[ -f "$RELEASE_JA" ]]; then
  echo "Release:  official 2.8.4 ja_JP found"
else
  echo "Release:  official 2.8.4 ja_JP not found; fallbacks will be English"
fi

MSYS2_ARG_CONV_EXCL='*' python "$(winpath "$REPO_ROOT/tools/build_dreamcraft_2_8_4_overlay.py")" \
  --source-lang "$(winpath "$SOURCE_LANG")" \
  --mods-dir "$(winpath "$INSTANCE_MC/mods")" \
  --pack-en "$(winpath "$PACK_EN")" \
  --release-ja "$(winpath "$RELEASE_JA")" \
  --output "$(winpath "$BUILT")"

mkdir -p "$(dirname "$FORCE_DST")"
cp -a "$BUILT" "$FORCE_DST"
echo "Wrote forceload (game-visible on 2.8.4)"
echo "  $(short_path "$FORCE_DST")"

echo "Synced dreamcraft ja_JP."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
