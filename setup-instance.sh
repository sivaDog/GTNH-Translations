#!/usr/bin/env bash
# One-shot setup for a fresh GTNH 2.8.4 Prism instance's ja_JP translations.
#
# 2.8.4 ships TX-Loader 1.8.5, where config/txloader/load/ is injected too early
# to override mod jars, while the current ParaTranz packs are built for
# TX-Loader 1.8.7+ and put everything in load/. Run this once after installing
# the modpack and the translation pack; it is idempotent, so re-running after a
# pack reinstall is safe (and necessary -- a reinstall undoes the fixes).
#
# Usage:
#   ./setup-instance.sh --dry-run     # show what would change
#   ./setup-instance.sh               # apply
#   INSTANCE_MC=/path/to/.minecraft ./setup-instance.sh
#
# Afterwards run ./sync.sh to push the verified quest / Thaumonomicon overlays.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc

if [[ ! -d "$INSTANCE_MC/mods" ]]; then
  echo "Missing instance .minecraft (no mods/): $(short_path "$INSTANCE_MC")" >&2
  echo "Set INSTANCE_MC in .env or pass it inline." >&2
  exit 1
fi

cd "$REPO_ROOT"
echo "Repo:     $(short_path "$REPO_ROOT")"
echo "Branch:   $(git branch --show-current 2>/dev/null || echo '(detached)')"
echo "Instance: $(short_path "$INSTANCE_MC")"
echo

python "$REPO_ROOT/tools/setup_instance_2_8_4.py" \
  --instance "$INSTANCE_MC" \
  --repo "$REPO_ROOT" \
  "$@"

echo
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
echo "Next: ./sync.sh   (verified quest + Thaumonomicon overlays)"
