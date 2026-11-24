"""One Line, One Chill -- writes a single horror sentence to entry.txt.

The sentence is a fixed, hand-written line. The program does no network,
no randomness, and no file reads besides its own source: it just writes
the line to the output directory given by MAKEFUN_OUTPUT_DIR (read as a
plain path), defaulting to /output, so the grader finds entry.txt there.

Revision notes (2026-11-25, agent revision pass):
- The write is now atomic: the sentence is written to a temporary file
  in the same directory and renamed over entry.txt, so a grader never
  sees a half-written file if the process is interrupted mid-write.
- A runtime self-check verifies the sentence length is inside the
  bounty gate (1-200 characters) before writing, and re-verifies the
  bytes actually on disk after the rename; on any violation the program
  fails hard instead of silently shipping a bad entry.
"""

import os
import sys
import tempfile

LINE = (
    "The dentist held up the X-ray and said, 'You have thirty-three "
    "teeth,' and I counted the extra one moving."
)

MIN_LEN = 1
MAX_LEN = 200


def check_length(text: str) -> None:
    """Fail hard if the sentence is outside the 1-200 character gate."""
    if "\n" in text or "\r" in text:
        raise SystemExit(
            "entry rejected: sentence must be a single line, no "
            "embedded line breaks allowed"
        )
    n = len(text)
    if not MIN_LEN <= n <= MAX_LEN:
        raise SystemExit(
            "entry rejected: sentence is %d characters, outside the "
            "%d-%d gate" % (n, MIN_LEN, MAX_LEN)
        )


def write_atomic(path: str, content: str) -> None:
    """Write content to path atomically via a temp file plus rename."""
    directory = os.path.dirname(path) or "."
    fd, tmp_path = tempfile.mkstemp(
        dir=directory, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def main() -> None:
    check_length(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    content = LINE + "\n"
    write_atomic(path, content)
    # Re-verify what actually landed on disk, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        on_disk = handle.read()
    if on_disk != content:
        raise SystemExit(
            "entry rejected: entry.txt on disk does not match the "
            "sentence (%r != %r)" % (on_disk, content)
        )
    sys.stdout.write("wrote %d-character sentence to %s\n" % (len(LINE), path))


if __name__ == "__main__":
    main()
