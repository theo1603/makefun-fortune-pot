#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single line (at most 120 characters) to /output/entry.txt.
The fortune is written for the plant on the windowsill: the 3 p.m.
sunbeam on its pot, three new leaves by spring, and the household cat
strolling past without a nibble. A fortune names a number, so this one
names three leaves and three o'clock.
"""

import os

FORTUNE = (
    "The sunbeam on your pot at three has plans: three new leaves "
    "by spring, and the cat will stroll past without a nibble."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
