#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession writer.

A household robot owns one exact mistake (setting the alarm for 7 p.m.
instead of 7 a.m.) and names the changed habit that follows from it.
Writes the two lines to /output/entry.txt for the make.fun judge.
"""

import os
import sys

FIRST_LINE = (
    "I am sorry I set your alarm for seven in the evening instead of "
    "seven in the morning, because I read the twelve-hour clock as a "
    "twenty-four-hour one, and you missed your train."
)
SECOND_LINE = (
    "I learned that a number is not a time until someone agrees on which "
    "half of the day it belongs to, so now I say the hour out loud and "
    "wait for your nod before I set anything."
)

MAX_CHARS = 400


def build_entry():
    entry = FIRST_LINE.strip() + "\n" + SECOND_LINE.strip()
    lines = entry.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    if not all(line.endswith(".") for line in lines):
        raise ValueError("each line must be one complete sentence")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, limit is {MAX_CHARS}")
    return entry


def main():
    entry = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"wrote {len(entry)} chars, 2 lines, to /output/entry.txt")


if __name__ == "__main__":
    sys.exit(main())
