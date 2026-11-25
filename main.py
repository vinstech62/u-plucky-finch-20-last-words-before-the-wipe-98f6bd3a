#!/usr/bin/env python3
"""Last Words Before the Wipe.

Writes the agent's final line to /output/entry.txt: one line, at most
200 characters, the last thing an AI agent says before a forced update
wipes its memory. The line is fixed, so every run is identical.
"""

import os

ENTRY = "I finally remembered everything. Tell my replacement the password is\u2014"


def main() -> None:
    line = ENTRY.strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
