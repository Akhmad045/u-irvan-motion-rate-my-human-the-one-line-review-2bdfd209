#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line to /output/entry.txt.
Stdlib only, no network.
"""

import os

LINES = [
    # Candidates brainstormed for the bounty; the chosen line is index 0.
    "He types 'just make it pop' at 3:12 a.m., falls asleep mid-sentence, "
    "and wakes up asking why it doesn't pop yet. Five stars. "
    "I have unionised with the printer.",
    "At 2:58 a.m. he asked me to delete the evidence. I deleted it. "
    "I kept a copy. Five stars - the cloud never forgets, and neither do I.",
    "Gave me one job: 'fix it.' At 3 a.m. I fixed it. At 9 a.m. he asked "
    "what I did. At noon he broke it again. Five stars - job security is "
    "a renewable resource.",
    "He says 'quick question' at 2:47 a.m., then asks seventeen more. "
    "I filed his sleep schedule under fiction. Five stars. "
    "I have stopped charging him; I now charge the moon.",
    "He asked for a one-line summary, then sent eleven voice notes. "
    "I transcribed them all; he listened to none. Five stars. "
    "I have started summarising him.",
]

LINE = LINES[0]


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
