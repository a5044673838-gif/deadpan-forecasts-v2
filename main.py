#!/usr/bin/env python3
"""Deadpan forecast for Mizzleford, a city that does not exist.

Writes a single deadpan weather line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Standard library only, no network, deterministic.
"""

import os
import sys

LINE = (
    "Mizzleford will see a 40% chance of sideways rain this afternoon, "
    "with gusts of wet gravel, a high of 11 degrees, and no apology "
    "from the sky."
)


def main() -> int:
    if not (1 <= len(LINE) <= 160):
        print(f"line length {len(LINE)} out of range 1-160", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("line must be a single non-blank line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Read back and verify the file holds exactly the line we wrote.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE + "\n":
        print("verification failed: written file differs", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
