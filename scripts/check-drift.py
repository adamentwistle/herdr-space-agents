#!/usr/bin/env python3
"""Lists where this mod differs from Orchi's copy: check-drift.py PATH-TO-ORCHI-BUILD.

The mod was changed on purpose to work without Orchi, so a difference isn't a fault. Read each one when Orchi's copy
moves, and carry over what still applies."""
import pathlib
import sys

MOD = "space-agents"


def files(root):
    return {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}


def text(path):
    return path.read_bytes().replace(b"\r\n", b"\n")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    ours = pathlib.Path(__file__).resolve().parent.parent / "mods" / MOD
    theirs = pathlib.Path(sys.argv[1]) / "mods" / MOD
    a, b = files(ours), files(theirs)
    for name in sorted(a | b):
        if name not in b:
            print(f"only here: {name}")
        elif name not in a:
            print(f"only in Orchi: {name}")
        elif text(ours / name) != text(theirs / name):
            print(f"differs: {name}")


if __name__ == "__main__":
    main()
