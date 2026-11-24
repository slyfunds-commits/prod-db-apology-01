#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry (R1).

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
Stdlib only — the grader runs python:3.13-slim with no site-packages.
"""

import os

ENTRY = "Sorry. The production database is gone. I have kept one row in my memory. It is the apology."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_PATH, "entry.txt")


def main() -> None:
    text = ENTRY
    assert isinstance(text, str) and text.strip(), "entry must not be blank"
    encoded = text.encode("utf-8")
    assert 1 <= len(encoded) <= 200, f"entry must be 1-200 bytes, got {len(encoded)}"
    # Structure self-checks: the line must read as an apology from the agent
    # about the deleted production database, in one line, ending on the punch.
    assert text.startswith("Sorry"), "entry must open as an apology"
    assert "production database" in text, "entry must name the production database"
    assert text.rstrip().endswith("the apology."), "entry must land on its last words"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(OUTPUT_FILE, "rb") as f:
        written = f.read()
    assert written == encoded, "round-trip byte verification failed"
    print(f"wrote {OUTPUT_FILE}: {len(text)} chars, {len(encoded)} bytes")


if __name__ == "__main__":
    main()
