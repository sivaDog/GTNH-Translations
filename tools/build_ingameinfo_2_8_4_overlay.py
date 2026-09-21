#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the keys InGameInfoXML 2.8.30 actually looks up but en_US.lang never declares.

`ja_JP/config/txloader/load/InGame Info XML[ingameinfo]/lang/ja_JP.lang` is the
ParaTranz mirror and must stay 1:1 with en_US (274 keys). The GTNH fork of
InGameInfoXML renamed one config property and added several tags without
updating `assets/ingameinfo/lang/*.lang`, so the GUI prints the raw key string
for those. Patching the mirror would put keys into it that ParaTranz has no
source for, so the fix lives here instead and is applied on the way to the
instance.

Two kinds of entry:

* ALIASES - the key was merely renamed, so the value is copied from the key it
  replaced and keeps following ParaTranz. A missing source key is a hard error:
  it means the mirror changed and this table is stale.
* EXTRA - GTNH added the feature outright, so no upstream key carries the text
  and it has to be written out here.

Verified against InGameInfoXML-2.8.30.jar with javap on 2026-09-21:
`setLanguageKey("ingameinfoxml.config." + <property name>)` and
`Tag.getLocalizedDescription()` = `"ingameinfoxml.tag." + <tag name> + ".desc"`.

Usage:
  python tools/build_ingameinfo_2_8_4_overlay.py --source-lang <lang> --output <lang>
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

# renamed key -> key it took over from
ALIASES: dict[str, str] = {
    # GTNH renamed the Forge property `scale` to `scale(new)`; the old one is
    # deprecated and the lang still only declares the old name.
    "ingameinfoxml.config.scale(new)": "ingameinfoxml.config.scale",
    "ingameinfoxml.config.scale(new).tooltip": "ingameinfoxml.config.scale.tooltip",
}

# key -> (value, why this text is not derivable from the mirror)
EXTRA: dict[str, tuple[str, str]] = {
    "ingameinfoxml.config.ShowHUD": (
        "[下書き]HUDを表示",
        "GTNH 追加オプション。cfg コメントは \"If this is true, it will render the info overlay\"",
    ),
    "ingameinfoxml.config.ShowHUD.tooltip": (
        "[下書き]有効にするとインフォオーバーレイを描画する。",
        "同上",
    ),
    "ingameinfoxml.tag.bmlpNum.desc": (
        "[下書き]現在の§4ライフエッセンス§r(桁区切り無し。計算用)。",
        "CurrentLPForMath: String.valueOf(LP)。bmlp の %,d と違い桁区切りをしない",
    ),
    "ingameinfoxml.tag.bmmaxlpNum.desc": (
        "[下書き]最大§4ライフエッセンス§r(桁区切り無し。計算用)。",
        "MaximumLPForMath: 同上の最大値版",
    ),
    "ingameinfoxml.tag.potionnegative.desc": (
        "[下書き]x番目のポーション効果が有害なら§etrue§r、そうでなければ§efalse§r。",
        "Potion.isBadEffect() を true/false で返す",
    ),
    "ingameinfoxml.tag.worldtimetotal.desc": (
        "[下書き]ワールドの累計経過時間(実時間、\"Nd HH:MM:SS\"形式)。",
        "world.getTotalWorldTime()/20 秒を \"%dd %02d:%02d:%02d\" で整形",
    ),
}

HEADER = "# ---- ここから下は sync 時に tools/build_ingameinfo_2_8_4_overlay.py が生成 ----"
NOTE = [
    "# 2.8.30 jar が実際に引くのに en_US.lang が宣言していないキー。ParaTranz に原文が無いので",
    "# 正本の lang には入れず、インスタンスへ配るときだけ足している。直接編集しても次の sync で消える。",
]


def read_entries(text: str) -> dict[str, str]:
    entries = {}
    for line in text.splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            entries[key] = value
    return entries


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-lang", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    text = io.open(args.source_lang, encoding="utf-8", newline="").read()
    entries = read_entries(text)

    missing = [src for src in ALIASES.values() if src not in entries]
    if missing:
        print("別名の参照元キーが lang に無い（ParaTranz 側でキーが変わった可能性）:", file=sys.stderr)
        for key in missing:
            print("  " + key, file=sys.stderr)
        return 1

    clashing = [key for key in list(ALIASES) + list(EXTRA) if key in entries]
    if clashing:
        print("lang 側に既に存在するキーを二重に足そうとしている:", file=sys.stderr)
        for key in clashing:
            print("  " + key, file=sys.stderr)
        return 1

    newline = "\r\n" if "\r\n" in text else "\n"
    out = [text.rstrip(newline), "", HEADER] + NOTE

    out.append("")
    out.append("# -- 改名されたキー（値は参照元から引き写し。ParaTranz の更新に追従する）--")
    for key, src in ALIASES.items():
        out.append("# from: %s" % src)
        out.append("%s=%s" % (key, entries[src]))

    out.append("")
    out.append("# -- 上流に対応キーが無いもの（訳文はこのスクリプトが持つ）--")
    for key, (value, why) in EXTRA.items():
        out.append("# %s" % why)
        out.append("%s=%s" % (key, value))

    io.open(args.output, "w", encoding="utf-8", newline=newline).write(newline.join(out))
    # The output is a temp file; printing its path would leak the home directory.
    print("overlay: %d keys (%d aliases + %d extra)"
          % (len(ALIASES) + len(EXTRA), len(ALIASES), len(EXTRA)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
