"""Roast Your Fridge — one line, one laugh.

Writes a single original roast line about the entrant's own fridge to
/output/entry.txt (UTF-8, 1-200 chars, no trailing newline).

The line was chosen by internal pairwise judging from seven variants
(see candidates.md in the build folder): first-person fridge voice,
one specific detail (freezer frost), a specific year, and a 2-beat +
reveal structure whose twist pays off in the final clause — the shape
of the winning lines in the finalized one-liner bounties.
"""

import os

# The roast. 135 characters / 135 bytes UTF-8, inside the 1-200 gate.
# Beat 1: the freezer grew a glacier since 2019.
# Beat 2: scientists want to study it.
# Reveal (final clause): it started as a bag of peas — and now it has a flag.
ROAST = (
    "My freezer has grown a glacier since 2019. "
    "Scientists want to study it. "
    "I told them it started as a bag of peas, and now it has a flag."
)


# Gate (RULES.txt): entry.txt must be UTF-8 text of 1-200 characters.
MAX_CHARS = 200


def main() -> None:
    if not ROAST or len(ROAST) > MAX_CHARS:
        raise SystemExit("entry line fails the 1-200 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ROAST:
            raise SystemExit("entry.txt differs from the roast line")
    print(f"Wrote {len(ROAST)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
