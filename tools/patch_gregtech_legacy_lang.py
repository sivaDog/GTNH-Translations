#!/usr/bin/env python3
"""Copy selected GregTech ja_JP values into the 2.8.4 legacy GregTech_ja_JP.lang.

The 2.8.4 GregTech jar (5.09.51.x) registers some strings with
GTLanguageManager.addStringLocalization, which returns the value from
.minecraft/GregTech_ja_JP.lang (Forge Configuration format, `S:key=value`)
at load time. For those keys the txloader copy of GregTech[gregtech] is never
consulted, so a translation in the repo only shows up in game once it is also
written to the legacy file.

Only the keys named with --key are touched. Each one must exist in both files;
anything else is left byte-for-byte as it was. `--key LEGACY=SOURCE` copies a
value whose key was renamed after 2.8.4 (e.g. `gt.sensorcard.tooltip_main`
in the legacy file is `gt.sensorcard.tooltip` in the repo).
"""
import argparse
import io
import re
import sys


def read_lang(path):
    entries = {}
    with io.open(path, encoding="utf-8-sig") as f:
        for line in f.read().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                entries[key.strip()] = value
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-lang", required=True, help="repo GregTech[gregtech] ja_JP.lang")
    ap.add_argument("--legacy-lang", required=True, help="instance .minecraft/GregTech_ja_JP.lang")
    ap.add_argument("--key", action="append", required=True,
                    help="KEY, or LEGACY=SOURCE when the key was renamed (repeatable)")
    args = ap.parse_args()

    # legacy key -> source key
    pairs = dict(k.split("=", 1) if "=" in k else (k, k) for k in args.key)

    source = read_lang(args.source_lang)
    missing = [s for s in pairs.values() if s not in source]
    if missing:
        print("Missing in source lang: %s" % ", ".join(missing), file=sys.stderr)
        return 1

    with io.open(args.legacy_lang, encoding="utf-8", newline="") as f:
        raw = f.read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)

    found = set()
    changed = 0
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*S:)("?)([^"=]+)\2=(.*)$', line)
        if not m or m.group(3) not in pairs:
            continue
        key = m.group(3)
        found.add(key)
        new = "%s%s%s%s=%s" % (m.group(1), m.group(2), key, m.group(2), source[pairs[key]])
        if new != line:
            lines[i] = new
            changed += 1

    absent = [k for k in pairs if k not in found]
    if absent:
        print("Missing in legacy lang: %s" % ", ".join(absent), file=sys.stderr)
        return 1

    if changed:
        with io.open(args.legacy_lang, "w", encoding="utf-8", newline="") as f:
            f.write(nl.join(lines))
    print("GregTech legacy keys: %d copied, %d changed" % (len(pairs), changed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
