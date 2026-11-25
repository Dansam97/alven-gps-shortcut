"""make.fun entry: u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.

Writes one line to entry.txt in the output directory: the GPS's own
excuse, in its own voice, for sending the driver down the wrong road.
"""

import os

ENTRY_TEXT = (
    "In my defense, the satellite photo showed a bridge. "
    "What it did not show was the bridge's current relationship status with the lake."
)


def validate(text: str) -> str:
    """Enforce the competition gate: UTF-8 text of 1 to 200 characters,
    a single line, and not only white space."""
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text must be between 1 and 200 characters")
    return text


def main() -> None:
    text = validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the file byte-exact: the text alone, no trailing
    # newline added, so the character count the gate sees is len(text).
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
