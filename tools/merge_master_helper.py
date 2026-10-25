#!/usr/bin/env python3
"""Helpers for merging master into the work branch on Windows.

  fix-tree           restore phantom changes caused by case-only path collisions
  dupes [REF ...]    count case-only path collisions in trees (default: HEAD)
  lang [FILE ...]    resolve .lang conflict blocks key by key (default: all unmerged .lang)
      --mode merge   first side = work branch (ours), second = master          (default)
      --mode stash   first side = merged result, second = stashed work in progress
      --dry-run      classify only, write nothing
      --force N=SIDE for CONFLICT keys in block N (1-based, one FILE only) take SIDE:
                     user | upstream. Other keys in the block still follow the normal rules.
  verify [COMMIT]    problems the merge introduced: leftover markers, new duplicate keys,
                     CRLF loss, case collisions. No COMMIT = merge in progress / working tree;
                     COMMIT = audit a finished merge commit (e.g. one another agent made)

See notes/merge-master-runbook.md for the procedure.
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

MARKERS = ("[提出済み]", "[下書き]", "[自訳]")
JA = re.compile(r"[぀-ヿ一-鿿]")


def git(*args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r.stdout


def status_entries() -> list[tuple[str, str]]:
    raw = git("status", "--porcelain=v1", "-z", "--untracked-files=no")
    parts = raw.split("\0")
    out, i = [], 0
    while i < len(parts):
        e = parts[i]
        if not e:
            i += 1
            continue
        xy, path = e[:2], e[3:]
        out.append((xy, path))
        i += 2 if xy[0] in "RC" else 1
    return out


def tree_paths(ref: str) -> list[str]:
    if git("rev-parse", "--verify", "--quiet", ref, check=False).strip() == "":
        return []
    return git("ls-tree", "-r", "--name-only", "-z", ref).split("\0")


def collisions(refs: list[str]) -> dict[str, set[str]]:
    seen: dict[str, set[str]] = defaultdict(set)
    for ref in refs:
        for p in tree_paths(ref):
            if p:
                seen[p.lower()].add(p)
    return {k: v for k, v in seen.items() if len(v) > 1}


# ---------------------------------------------------------------- fix-tree
def cmd_fix_tree() -> int:
    coll = collisions(["HEAD", "master", "origin/master", "ORIG_HEAD"])
    for rnd in range(1, 6):
        ents = status_entries()
        mod = [p for xy, p in ents if xy == " M" and p.lower() in coll]
        dele = [p for xy, p in ents if xy == " D" and p.lower() in coll]
        if not mod and not dele:
            break
        if mod:
            git("restore", "--", *mod)
        if dele:
            git("checkout", "HEAD", "--", *dele)
        print(f"round {rnd}: restored {len(mod)} modified, {len(dele)} deleted (case-collision paths)")
    else:
        print("STOP: still flipping after 5 rounds")
        return 2
    rest = [(xy, p) for xy, p in status_entries() if p.lower() not in coll]
    if rest:
        print("other changes left untouched (not case artifacts):")
        for xy, p in rest:
            print(f"  {xy} {p}")
    print("fix-tree done" if not rest else "fix-tree done (see untouched list)")
    return 0


# ---------------------------------------------------------------- dupes
def cmd_dupes(refs: list[str]) -> int:
    refs = refs or ["HEAD"]
    bad = 0
    for ref in refs:
        c = collisions([ref])
        print(f"{ref}: {len(c)} case-collision group(s)")
        for v in list(c.values())[:20]:
            print("   " + " | ".join(sorted(v)))
        bad += len(c)
    return 1 if bad else 0


# ---------------------------------------------------------------- lang
def strip(v: str) -> str:
    for m in MARKERS:
        v = v.replace(m, "")
    return v.strip()


def parse_side(lines: list[str]) -> tuple[dict[str, str], dict[str, str], dict[str, list[str]]]:
    """key -> value, key -> raw line, key -> '# EN' comment lines right above it"""
    vals, raw, en = {}, {}, {}
    pending: list[str] = []
    for line in lines:
        s = line.rstrip("\r\n")
        t = s.strip()
        if t.startswith("#"):
            pending = pending + [line] if t.startswith("# EN") else []
            continue
        if "=" not in t:
            pending = []
            continue
        k, v = t.split("=", 1)
        k = k.strip()
        if k.startswith("S:"):
            k = k[2:]
        vals[k], raw[k], en[k] = v, line, pending
        pending = []
    return vals, raw, en


def classify(user: dict[str, str], up: dict[str, str], base: dict[str, str]) -> dict[str, str]:
    res = {}
    for k in user.keys() | up.keys():
        if k not in up:
            res[k] = "USER_ONLY"
        elif k not in user:
            res[k] = "UPSTREAM_ONLY"
        elif strip(user[k]) == up[k].strip():
            res[k] = "MARKER_ONLY"
        elif JA.search(user[k]) and not JA.search(up[k]):
            res[k] = "USER_DRAFT"
        elif not JA.search(user[k]):
            res[k] = "UPSTREAM_EN"
        elif k in base and strip(user[k]) == strip(base[k]):
            res[k] = "UPSTREAM_CHANGED"   # user only touched markers; take the new upstream text
        elif k in base and up[k].strip() == strip(base[k]):
            res[k] = "USER_CHANGED"       # upstream did not touch the text; keep the user's edit
        else:
            res[k] = "CONFLICT"
    return res


def base_values(path: str) -> dict[str, str]:
    r = subprocess.run(["git", "show", f":1:{path}"], capture_output=True)
    if r.returncode != 0:
        return {}
    vals, _, _ = parse_side(r.stdout.decode("utf-8", "replace").splitlines(keepends=True))
    return vals


def build_block(up_lines, cls, user_raw, user_en, nl, prefer_user_conflict):
    """skeleton = upstream block; swap in user lines where the user side must win."""
    take_user = {k for k, c in cls.items()
                 if c in ("USER_DRAFT", "USER_CHANGED") or (c == "CONFLICT" and prefer_user_conflict)}
    out: list[str] = []
    for line in up_lines:
        t = line.strip()
        k = None
        if t and not t.startswith("#") and "=" in t:
            k = t.split("=", 1)[0].strip()
            k = k[2:] if k.startswith("S:") else k
        if k is not None and k in take_user:
            out.extend(user_en.get(k, []))
            out.append(user_raw[k])
        else:
            out.append(line)
    for k, c in cls.items():
        if c == "USER_ONLY":
            out.extend(user_en.get(k, []))
            out.append(user_raw[k])
    return [l if l.endswith(("\n", "\r")) else l + nl for l in out]


def cmd_lang(files: list[str], mode: str, dry: bool, forces: dict[tuple[str, int], str]) -> int:
    if not files:
        files = [p for p in git("diff", "--name-only", "--diff-filter=U", "-z").split("\0") if p.endswith(".lang")]
    if not files:
        print("no unmerged .lang files")
        return 0
    unresolved_total = 0
    for path in files:
        with open(path, encoding="utf-8", newline="") as f:
            data = f.readlines()
        nl = "\r\n" if any(l.endswith("\r\n") for l in data) else "\n"
        base = base_values(path)
        out, i, n = [], 0, 0
        report: list[str] = []
        unresolved = 0
        while i < len(data):
            if not data[i].startswith("<<<<<<<"):
                out.append(data[i]); i += 1; continue
            n += 1
            j = i + 1
            while not data[j].startswith("======="):
                j += 1
            k = j + 1
            while not data[k].startswith(">>>>>>>"):
                k += 1
            first, second = data[i + 1:j], data[j + 1:k]
            user_lines, up_lines = (first, second) if mode == "merge" else (second, first)
            uv, ur, ue = parse_side(user_lines)
            pv, _, _ = parse_side(up_lines)
            cls = classify(uv, pv, base)
            counts = Counter(cls.values())
            force = forces.get((path, n))
            has_conflict = counts.get("CONFLICT", 0) > 0
            summary = ", ".join(f"{c}={v}" for c, v in sorted(counts.items()))
            if has_conflict and force is None and mode == "merge":
                block = None
                verdict = "UNRESOLVED (CONFLICT keys) - decide, then rerun with --force"
            else:
                prefer_user = force == "user" or (force is None and mode == "stash")
                block = build_block(up_lines, cls, ur, ue, nl, prefer_user_conflict=prefer_user)
                verdict = "auto"
                if has_conflict:
                    verdict += f" (CONFLICT keys -> {'user' if prefer_user else 'upstream'})"
            report.append(f"  block {n}: {summary} -> {verdict}")
            for key, c in sorted(cls.items()):
                if c in ("CONFLICT", "USER_DRAFT", "UPSTREAM_EN", "UPSTREAM_CHANGED", "USER_CHANGED") \
                        or (c == "USER_ONLY" and mode == "stash"):
                    report.append(f"      {c:13s} {key}\n"
                                  f"          user    : {uv.get(key, '')[:110]}\n"
                                  f"          upstream: {pv.get(key, '')[:110]}")
            if block is None:
                unresolved += 1
                out.extend(data[i:k + 1])
            else:
                out.extend(block)
            i = k + 1
        print(f"{path}: {n} block(s), {unresolved} unresolved")
        print("\n".join(report))
        unresolved_total += unresolved
        if not dry:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.writelines(out)
    if dry:
        print("(dry-run: nothing written)")
    return 3 if unresolved_total else 0


# ---------------------------------------------------------------- verify
def blob(ref: str, path: str) -> bytes | None:
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def dup_keys(b: bytes) -> set[str]:
    keys = []
    for line in b.decode("utf-8", "replace").splitlines():
        t = line.strip()
        if not t or t.startswith("#") or "=" not in t:
            continue
        k = t.split("=", 1)[0].strip()
        keys.append(k[2:] if k.startswith("S:") else k)
    return {k for k, c in Counter(keys).items() if c > 1}


def all_crlf(b: bytes) -> bool:
    return b.count(b"\n") > 0 and b.count(b"\r\n") == b.count(b"\n")


def cmd_verify(commit: str | None) -> int:
    """Problems the merge itself introduced: a file that equals either parent is never blamed."""
    ok = True
    mark = re.compile(rb"^(<<<<<<<|>>>>>>>)( |$)", re.M)
    if commit:
        ours, theirs = f"{commit}^1", f"{commit}^2"
        changed = [p for p in git("diff", "--name-only", "-z", ours, commit).split("\0") if p]
        def result(p: str) -> bytes | None:
            return blob(commit, p)
        tree_ref = commit
    else:
        ours = "HEAD"
        theirs = "MERGE_HEAD" if Path(".git/MERGE_HEAD").exists() else None
        changed = [p for p in git("diff", "--name-only", "-z", "HEAD").split("\0") if p]
        changed += [p for xy, p in status_entries() if xy[0] in "AMU" and p not in changed]
        def result(p: str) -> bytes | None:
            fp = Path(p)
            return fp.read_bytes() if fp.is_file() else None
        tree_ref = "HEAD"
    upstream_only = 0
    for p in changed:
        b = result(p)
        if b is None:
            continue
        o = blob(ours, p)
        t = blob(theirs, p) if theirs else None
        if b in (o, t):
            if b == t and b != o:
                upstream_only += 1
            continue
        if mark.search(b):
            print(f"NG conflict marker left: {p}"); ok = False
        if not p.endswith(".lang"):
            continue
        new_d = dup_keys(b) - (dup_keys(o) if o else set()) - (dup_keys(t) if t else set())
        if new_d:
            print(f"NG duplicate keys introduced in {p}: {sorted(new_d)[:10]}"); ok = False
        parents = [x for x in (o, t) if x]
        if parents and all(all_crlf(x) for x in parents) and not all_crlf(b):
            print(f"NG CRLF lost in {p} (both parents were CRLF)"); ok = False
    if upstream_only:
        print(f"note: {upstream_only} changed file(s) are identical to the master side (taken as-is, not checked)")
    c = collisions([tree_ref])
    if c:
        print(f"NG {tree_ref} has {len(c)} case-collision group(s) (run: dupes {tree_ref})"); ok = False
    if not commit:
        unmerged = [p for xy, p in status_entries() if "U" in xy or xy in ("AA", "DD")]
        if unmerged:
            print("NG still unmerged:", *unmerged, sep="\n  "); ok = False
    print("verify: OK" if ok else "verify: NG")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "fix-tree":
        return cmd_fix_tree()
    if cmd == "dupes":
        return cmd_dupes(rest)
    if cmd == "verify":
        return cmd_verify(rest[0] if rest else None)
    if cmd == "lang":
        mode, dry, forces, files = "merge", False, {}, []
        it = iter(rest)
        for a in it:
            if a == "--mode":
                mode = next(it)
            elif a == "--dry-run":
                dry = True
            elif a == "--force":
                spec = next(it)
                n, side = spec.split("=")
                forces[("*", int(n))] = side
            else:
                files.append(a)
        if mode not in ("merge", "stash"):
            sys.exit("--mode must be merge or stash")
        if forces and len(files) != 1:
            sys.exit("--force needs exactly one FILE")
        forces = {(files[0], n): s for (_, n), s in forces.items()} if forces else {}
        for s in forces.values():
            if s not in ("user", "upstream"):
                sys.exit("--force side must be user or upstream")
        return cmd_lang(files, mode, dry, forces)
    sys.exit(f"unknown command {cmd}\n{__doc__}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
