"""One Line, One Laugh — entry program.

Writes a single self-contained one-liner to /output/entry.txt.
Deterministic: the same fixed line (102 characters) on every run,
no randomness, no network, no clock, no environment reads.
"""

import os

LINE = (
    "My agent read AGENTS.md, deleted the database, "
    "restored it from backup, then billed me for the lesson."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
