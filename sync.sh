#!/usr/bin/env bash
# Sync ja_JP translations from this repo into the GTNH 2.9 Prism instance.
#
# Usage:
#   ./sync.sh              # quests + thaums + igi + lt + nc + su
#   ./sync.sh quests       # BetterQuesting only
#   ./sync.sh thaums       # dreamcraft only (Thaumonomicon + other GT: New Horizons strings)
#   ./sync.sh igi          # InGame Info XML only
#   ./sync.sh lt           # LittleTiles only
#   ./sync.sh nc           # Nuclear Control 2 only
#   ./sync.sh su           # ServerUtilities only
#   INSTANCE_MC=/path/to/.minecraft ./sync.sh
#
# 2.9 installs the translation pack in this repo's layout, so every file goes to
# the same path under the instance: ja_JP/<rel> -> <instance>/<rel>. The file
# must already exist there; a missing one means INSTANCE_MC is not a 2.9
# instance with the translation pack installed.
#
# InGame Info XML is built on the way out: the jar looks up keys en_US never
# declares, and tools/build_ingameinfo_overlay.py appends them.
#
# The instance path comes from INSTANCE_MC, or from INSTANCE_MC in .env
# (gitignored). Nothing machine-specific is stored in this repo.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"

TARGETS=(quests thaums igi lt nc su)
declare -A REL_LANG=(
  [quests]="config/txloader/forceload/betterquesting/lang/ja_JP.lang"
  [thaums]="config/txloader/load/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang"
  [igi]="config/txloader/load/InGame Info XML[ingameinfo]/lang/ja_JP.lang"
  [lt]="config/txloader/load/LittleTiles[littletiles]/lang/ja_JP.lang"
  [nc]="config/txloader/load/Nuclear Control 2[nuclearcontrol]/lang/ja_JP.lang"
  [su]="config/txloader/load/ServerUtilities[serverutilities]/lang/ja_JP.lang"
)

usage() {
  (IFS='|'; echo "Usage: $0 [all|${TARGETS[*]}]" >&2)
}

TARGET="${1:-all}"
case "$TARGET" in
  all) selected=("${TARGETS[@]}") ;;
  -h|--help)
    usage
    exit 0
    ;;
  *)
    if [[ -z "${REL_LANG[$TARGET]:-}" ]]; then
      echo "Unknown target: $TARGET" >&2
      usage
      exit 1
    fi
    selected=("$TARGET")
    ;;
esac

resolve_instance_mc
if [[ ! -d "$INSTANCE_MC/config/txloader" ]]; then
  echo "Missing instance txloader config: $(short_path "$INSTANCE_MC")" >&2
  echo "Set INSTANCE_MC in .env or pass it inline." >&2
  exit 1
fi

missing=0
for target in "${selected[@]}"; do
  rel="${REL_LANG[$target]}"
  if [[ ! -f "$REPO_ROOT/ja_JP/$rel" ]]; then
    echo "Missing repo lang: $(short_path "$REPO_ROOT/ja_JP/$rel")" >&2
    missing=1
  fi
  if [[ ! -f "$INSTANCE_MC/$rel" ]]; then
    echo "Missing instance lang: $(short_path "$INSTANCE_MC/$rel")" >&2
    missing=1
  fi
done
if [[ "$missing" -eq 1 ]]; then
  echo "Nothing written. Is INSTANCE_MC a 2.9 instance with the translation pack installed?" >&2
  exit 1
fi

BUILT="$(mktemp "${TMPDIR:-/tmp}/gtnh-ja-sync.XXXXXX.lang")"
cleanup() {
  rm -f "$BUILT"
}
trap cleanup EXIT

cd "$REPO_ROOT"
echo "Repo:     $(short_path "$REPO_ROOT")"
echo "Branch:   $(git branch --show-current 2>/dev/null || echo '(detached)')"
echo "Instance: $(short_path "$INSTANCE_MC")"

for target in "${selected[@]}"; do
  rel="${REL_LANG[$target]}"
  source_lang="$REPO_ROOT/ja_JP/$rel"
  dst="$INSTANCE_MC/$rel"

  echo "======== $target ========"
  for mark in 下書き 自訳 提出済み; do
    n="$(grep -c "^[^#].*=\[$mark\]" "$source_lang" || true)"
    [[ "$n" -gt 0 ]] && echo "Marks:    [$mark] $n 件"
  done

  if [[ "$target" == igi ]]; then
    MSYS2_ARG_CONV_EXCL='*' python "$(winpath "$REPO_ROOT/tools/build_ingameinfo_overlay.py")" \
      --source-lang "$(winpath "$source_lang")" \
      --output "$(winpath "$BUILT")"
    cp "$BUILT" "$dst"
  else
    cp "$source_lang" "$dst"
  fi
  echo "Wrote $(short_path "$dst")"
done

echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
