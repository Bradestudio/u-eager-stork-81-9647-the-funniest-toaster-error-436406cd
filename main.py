#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one deadpan error message — a kitchen toaster blaming its owner —
to /output/entry.txt (1-120 UTF-8 characters, not whitespace only).
"""

import os

ENTRY = "ERROR: I toasted it perfectly. You abandoned it for 20 minutes. This is on you."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert text.strip(), "entry must not be whitespace only"
    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except (PermissionError, OSError):
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    print(text)


if __name__ == "__main__":
    main()
