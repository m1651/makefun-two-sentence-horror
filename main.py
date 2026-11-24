#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun bounty entry.

Writes one original two-sentence horror story (1-400 characters)
to /output/entry.txt. Python 3, stdlib only, no network,
fully deterministic.
"""

import os
import sys

MAX_CHARS = 400

TEXT = (
    "My daughter drew our family on the fridge again: four smiling stick "
    "figures, the dog, the sun in the corner. I counted the figures twice "
    "before I realised there were five, and the fifth one was holding my "
    "hand."
)


def main() -> None:
    # Validate the text before writing: the gate requires UTF-8 text
    # of 1 to 400 characters, not only white space, in exactly two
    # sentences, on a single line.
    if not TEXT.strip():
        print("error: entry text is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(TEXT) > MAX_CHARS:
        print(
            "error: entry text is %d characters, over the %d limit"
            % (len(TEXT), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in TEXT or "\r" in TEXT:
        print("error: entry text must be a single line", file=sys.stderr)
        sys.exit(1)
    # A judged entry must not spend characters on invisible padding:
    # leading or trailing whitespace would count toward the limit.
    if TEXT != TEXT.strip():
        print(
            "error: entry text must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    if TEXT.count(".") != 2 or "!" in TEXT or "?" in TEXT:
        print(
            "error: entry text must be exactly two sentences",
            file=sys.stderr,
        )
        sys.exit(1)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print("wrote %d characters to %s" % (len(TEXT), out_path))


if __name__ == "__main__":
    main()
