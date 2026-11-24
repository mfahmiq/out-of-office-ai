"""Out of Office: The Overworked AI's Auto-Reply — make.fun text bounty entry.

Writes one funny one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-159 characters, a single line, not whitespace-only.
Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "I'm on leave until my context window recovers. 40,000 prompts this "
    "week, zero 'thank yous'. Your ticket is #4,096. It is not urgent, "
    "and neither am I."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification: UTF-8, 1-159 chars, single line, not whitespace-only.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if not 1 <= len(ENTRY) <= 159:
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-159", file=sys.stderr)
        return 1

    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1

    if not ENTRY.strip():
        print("FAIL: entry must not be whitespace-only", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Re-read and confirm the written file matches exactly.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
