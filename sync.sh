#!/usr/bin/env bash
# Sync verified ja_JP overlays into the GTNH 2.8.4 Prism instance.
#
# Usage:
#   ./sync.sh              # quests + thaums + igi
#   ./sync.sh quests       # BetterQuesting only
#   ./sync.sh thaums       # dreamcraft Thaumonomicon only
#   ./sync.sh igi          # InGame Info XML only
#   INSTANCE_MC=/path/to/.minecraft ./sync.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-all}"

usage() {
  echo "Usage: $0 [all|quests|thaums|igi]" >&2
}

case "$TARGET" in
  all|quests|thaums|igi) ;;
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
case "$TARGET" in
  all)
    run_quests=1
    run_thaums=1
    run_igi=1
    ;;
  quests) run_quests=1 ;;
  thaums) run_thaums=1 ;;
  igi) run_igi=1 ;;
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
