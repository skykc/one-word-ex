"""One Word From Your Ex — entry program.

Writes exactly one word, the word my ex would use to describe me,
to /output/entry.txt (the path the make.fun program/v1 harness gates).
The word is a single fixed string: no input, no network, no randomness.
"""

import os

WORD = "Upgraded"

# The gate allows 1-24 UTF-8 characters, not only white space, and the
# judge only ever sees this one word, so refuse to write anything else.
assert WORD and len(WORD) <= 24 and WORD.split() == [WORD], WORD


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write the word with no trailing newline: the file is the entry,
    # byte for byte, and a newline would be part of what the judge reads.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
