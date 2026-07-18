#!/usr/bin/env bash
# Sync ja_JP overlay from this repo into the GTNH Prism instance.
#
# Usage:
#   ./sync-to-instance.sh              # sync current checkout's ja_JP/
#   ./sync-to-instance.sh --pull       # git pull current branch, then sync
#   ./sync-to-instance.sh --questbook  # questbook lang only (faster for draft checks)
#   ./sync-to-instance.sh --dry-run    # show what would be copied
#
# Override instance path if needed:
#   INSTANCE_MC=/path/to/.minecraft ./sync-to-instance.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
INSTANCE_MC="${INSTANCE_MC:-$HOME/AppData/Roaming/PrismLauncher/instances/GT_New_Horizons_2.8.4_Java_17-25/.minecraft}"
SRC="$REPO_ROOT/ja_JP"

DO_PULL=0
QUESTBOOK_ONLY=0
DRY_RUN=0

for arg in "$@"; do
  case "$arg" in
    --pull) DO_PULL=1 ;;
    --questbook|-q) QUESTBOOK_ONLY=1 ;;
    --dry-run) DRY_RUN=1 ;;
    -h|--help)
      sed -n '2,14p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 1
      ;;
  esac
done

if [[ ! -d "$SRC" ]]; then
  echo "Missing ja_JP folder: $SRC" >&2
  exit 1
fi
if [[ ! -d "$INSTANCE_MC" ]]; then
  echo "Missing instance .minecraft: $INSTANCE_MC" >&2
  echo "Set INSTANCE_MC to your Prism instance path." >&2
  exit 1
fi

cd "$REPO_ROOT"
BRANCH="$(git branch --show-current 2>/dev/null || echo '(detached)')"
echo "Repo:     $REPO_ROOT"
echo "Branch:   $BRANCH"
echo "Instance: $INSTANCE_MC"

if [[ "$DO_PULL" -eq 1 ]]; then
  echo "Pulling current branch..."
  git pull --ff-only
fi

QB_SRC="$SRC/config/txloader/forceload/betterquesting/lang/ja_JP.lang"
QB_DST="$INSTANCE_MC/config/txloader/forceload/betterquesting/lang/ja_JP.lang"

copy_path() {
  local from="$1" to="$2"
  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "DRY would copy: $from -> $to"
    return
  fi
  mkdir -p "$(dirname "$to")"
  cp -a "$from" "$to"
}

if [[ "$QUESTBOOK_ONLY" -eq 1 ]]; then
  if [[ ! -f "$QB_SRC" ]]; then
    echo "Missing questbook lang: $QB_SRC" >&2
    exit 1
  fi
  copy_path "$QB_SRC" "$QB_DST"
  echo "Synced questbook ja_JP.lang only."
else
  if [[ -f "$SRC/GregTech_ja_JP.lang" ]]; then
    copy_path "$SRC/GregTech_ja_JP.lang" "$INSTANCE_MC/GregTech_ja_JP.lang"
  fi
  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "DRY would copy: $SRC/config/. -> $INSTANCE_MC/config/"
  else
    cp -a "$SRC/config/." "$INSTANCE_MC/config/"
  fi
  echo "Synced full ja_JP overlay."
fi

if [[ "$DRY_RUN" -eq 0 ]]; then
  echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
fi
