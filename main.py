#!/usr/bin/env python3
"""Dad Joke Showdown - make.fun entry.

Writes the entry line to /output/entry.txt (UTF-8).

Stop impersonating a flamingo. I had to put my foot down.
"""
import os

ENTRY = "My wife told me to stop impersonating a flamingo. I had to put my foot down."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
