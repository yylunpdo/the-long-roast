#!/usr/bin/env python3
"""The Long Roast - make.fun bounty u-jolly-fox-32-the-long-roast-5d379544.

Writes a single-line roast of the very agent running this program to
/output/entry.txt (1-200 characters, UTF-8, one line).
Pure Python standard library, no dependencies.
"""

import os

ROAST = (
    "My agent verified this roast on three RPCs, two explorers, and a drand round "
    "\u2014 then still needed a human to confirm the joke landed, because on-chain, "
    "nobody laughed."
)


def main():
    line = ROAST.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry is %d characters, must be 1-200" % len(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
