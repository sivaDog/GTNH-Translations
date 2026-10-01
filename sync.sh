#!/usr/bin/env bash
# Sync verified ja_JP overlays into the GTNH 2.8.4 Prism instance.
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
# The instance path comes from INSTANCE_MC, or from INSTANCE_MC in .env
# (gitignored). Nothing machine-specific is stored in this repo.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-all}"

usage() {
  echo "Usage: $0 [all|quests|thaums|igi|lt|nc|su]" >&2
}

case "$TARGET" in
  all|quests|thaums|igi|lt|nc|su) ;;
  -h|--help)
    usage
    exit 0
    ;;
  *)
    echo "Unknown target: $TARGET" >&2
    usage
    exit 1
    ;;
esac

cd "$REPO_ROOT"

run_quests=0
run_thaums=0
run_igi=0
run_lt=0
run_nc=0
run_su=0
case "$TARGET" in
  all)
    run_quests=1
    run_thaums=1
    run_igi=1
    run_lt=1
    run_nc=1
    run_su=1
    ;;
  quests) run_quests=1 ;;
  thaums) run_thaums=1 ;;
  igi) run_igi=1 ;;
  lt) run_lt=1 ;;
  nc) run_nc=1 ;;
  su) run_su=1 ;;
esac

if [[ "$run_quests" -eq 1 ]]; then
  echo "======== quests ========"
  "$REPO_ROOT/sync-verified-quests.sh"
fi
if [[ "$run_thaums" -eq 1 ]]; then
  echo "======== thaums ========"
  "$REPO_ROOT/sync-verified-thaums.sh"
fi
if [[ "$run_igi" -eq 1 ]]; then
  echo "======== igi ========"
  "$REPO_ROOT/sync-verified-igi.sh"
fi
if [[ "$run_lt" -eq 1 ]]; then
  echo "======== lt ========"
  "$REPO_ROOT/sync-verified-lt.sh"
fi
if [[ "$run_nc" -eq 1 ]]; then
  echo "======== nc ========"
  "$REPO_ROOT/sync-verified-nc.sh"
fi
if [[ "$run_su" -eq 1 ]]; then
  echo "======== su ========"
  "$REPO_ROOT/sync-verified-su.sh"
fi
