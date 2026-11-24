#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt (1-200 characters, UTF-8).
Deterministic: stdlib only, no network, no randomness.
"""

import os

CONFESSION = (
    "Confession: I say \"great question\" to buy time while I "
    "frantically look up the answer I was supposed to already know."
)

OUTPUT_PATH = "/output/entry.txt"

# The sealed scorer's gate: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space. Validate before writing
# and verify the file afterwards so a bad line fails loudly here
# instead of silently scoring 0.
MAX_CHARS = 200


def validate(text: str) -> None:
    stripped = text.strip()
    if not stripped:
        raise ValueError("confession must not be empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("confession must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"confession is {len(stripped)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )


def main() -> None:
    validate(CONFESSION)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read().strip()
    validate(written)
    if written != CONFESSION:
        raise ValueError("written entry does not match the confession")
    print(CONFESSION)


if __name__ == "__main__":
    main()
