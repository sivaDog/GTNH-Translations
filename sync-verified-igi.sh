#!/usr/bin/env bash
# Overwrite InGame Info XML ja_JP in the GTNH 2.8.4 Prism instance.
#
# Source is the repo load file (ParaTranz / 手元ドラフトの正本).
# 2.8.4 uses TX-Loader 1.8.5, so the game-visible copy is forceload.
# InGameInfoXML-2.8.30.jar ships no assets/ingameinfo/lang/ja_JP.lang, so the
# pack copy wins outright; the leftover load copy is overwritten too so the
# two instance files do not drift.
#
# Covers the config GUI and /igi taglist only. The HUD itself is
# config/InGameInfoXML/InGameInfo_ja_JP.xml and is not synced here.
#
# The repo lang is the ParaTranz mirror and stays 1:1 with en_US (274 keys).
# The keys the 2.8.30 jar looks up but en_US never declares are appended on the
# way out by tools/build_ingameinfo_2_8_4_overlay.py, not stored in the mirror.
#
# Usage:
#   ./sync-verified-igi.sh
#   INSTANCE_MC=/path/to/.minecraft ./sync-verified-igi.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
. "$REPO_ROOT/tools/sync-common.sh"
resolve_instance_mc
REL_LANG="config/txloader/load/InGame Info XML[ingameinfo]/lang/ja_JP.lang"
SOURCE_LANG="$REPO_ROOT/ja_JP/$REL_LANG"
FORCE_DST="$INSTANCE_MC/config/txloader/forceload/InGame Info XML[ingameinfo]/lang/ja_JP.lang"
LOAD_DST="$INSTANCE_MC/config/txloader/load/InGame Info XML[ingameinfo]/lang/ja_JP.lang"
BUILT="$(mktemp "${TMPDIR:-/tmp}/gtnh-ja-ingameinfo.XXXXXX.lang")"

cleanup() {
  rm -f "$BUILT"
}
trap cleanup EXIT

if [[ ! -f "$SOURCE_LANG" ]]; then
  echo "Missing ingameinfo lang: $(short_path "$SOURCE_LANG")" >&2
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

# MSYS mangles POSIX paths passed to a Windows python, and the '[' in the
# bracket folder name defeats its auto-conversion, so convert explicitly.
winpath() {
  if command -v cygpath >/dev/null 2>&1; then cygpath -w "$1"; else printf '%s' "$1"; fi
}
MSYS2_ARG_CONV_EXCL='*' python "$(winpath "$REPO_ROOT/tools/build_ingameinfo_2_8_4_overlay.py")"   --source-lang "$(winpath "$SOURCE_LANG")"   --output "$(winpath "$BUILT")"

mkdir -p "$(dirname "$FORCE_DST")"
cp -a "$BUILT" "$FORCE_DST"
echo "Wrote forceload (game-visible on 2.8.4)"
echo "  $(short_path "$FORCE_DST")"

if [[ -f "$LOAD_DST" ]]; then
  cp -a "$BUILT" "$LOAD_DST"
  echo "Wrote load (leftover overlay; not used while forceload exists)"
  echo "  $(short_path "$LOAD_DST")"
fi

echo "Synced InGame Info XML ja_JP."
echo "Done. Restart Minecraft (or switch language EN->JA) to apply."
