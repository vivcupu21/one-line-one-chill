"""One Line, One Chill -- writes a single horror sentence to entry.txt.

The sentence is a fixed, hand-written line. The program does no network,
no randomness, and no file reads besides its own source: it just writes
the line to the output directory given by MAKEFUN_OUTPUT_DIR (read as a
plain path), defaulting to /output, so the grader finds entry.txt there.
"""

import os

LINE = (
    "The dentist held up the X-ray and said, 'You have thirty-three "
    "teeth,' and I counted the extra one moving."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
