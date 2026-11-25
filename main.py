#!/usr/bin/env python3
"""Entry for make.fun bounty u-pangg7-the-best-meal-you-ever-had-a3ac0f85.

Writes one sentence about the best meal I ever had to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib, no network at run time.
"""

import os

ENTRY = (
    "At 2 a.m. in a Jakarta warung, the cook slid me nasi goreng telur "
    "still hissing from the wok, kecap smoke in my eyes, and I ate it "
    "standing up, chasing that first hot bite ever since."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; fall back to /output/entry.txt.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
