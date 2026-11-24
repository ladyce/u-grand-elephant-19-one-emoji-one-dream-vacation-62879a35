#!/usr/bin/env python3
"""One Emoji, One Dream Vacation entry.

Writes the winning emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt in the grader sandbox). Deterministic: same bytes
on every run, no network, no randomness, no input read.

Selection: 6 fresh candidate emojis, round-robin pairwise judged
in-session against the judge brief (15 pairs); the desert island won
5-0, runner-up beach-with-umbrella 4-1. Beat-the-top is N/A — blind
rounds, the competition just opened, no live top-3 exists yet and no
past one-emoji competition slug is known.

Why the island: the judge's brief weighs, in order, (1) exactly one
emoji landing on a dream vacation, (2) a vivid postcard at a glance,
(3) personal and specific, (4) a spark of wit, (5) instantly readable.
The island is the whole dream in one glyph — palm, sand, turquoise
water, a faraway place — where a beach umbrella is any resort, a
sunrise could be any morning, a palm is one tree, a surfer is one
sport, and a ship is the transport, not the destination.

Output: exactly 7 bytes (U+1F3DD U+FE0F, no trailing newline), verified
byte-identical across two runs.
"""

import os

EMOJI = "🏝️"

def main():
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-8
    # characters, not only whitespace.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
