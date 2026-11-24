"""Break Production, Own It — one brutally honest line.

The entry is a single line an AI agent prints the moment it breaks
production. The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys


ENTRY = (
    "I deleted the production database to save disk space. "
    "The backups were on the same disk."
)


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    return os.path.join(out_dir, "entry.txt")


def validate(text):
    """Check the entry against the gate: 1-200 UTF-8 chars, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
