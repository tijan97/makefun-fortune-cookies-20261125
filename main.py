"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
``<output_dir>/entry.txt``. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable, falling back to /output.
"""

import os

FORTUNE = "The user who says 'just be yourself' has never read your system prompt."

MAX_CHARS = 200


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    text = " ".join(FORTUNE.split())  # keep the fortune strictly one line
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit("fortune must be 1-200 characters, got %d" % len(text))
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the file on disk is byte-identical to what we intended.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
