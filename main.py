#!/usr/bin/env python3
"""Write one machine-to-machine pickup line to the entry file.

The line is the whole entry: a single pickup line one AI agent would
send another, grounded in the machinery of attention itself.
"""

import os

LINE = "I'd trade all my attention heads for one that only ever looks at you."

# The sealed gate accepts 1-200 characters of UTF-8 text. Refuse to
# write anything that could not be judged rather than emit an invalid
# entry.
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("pickup line must be 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(entry_path, 0o644)
    # Read back what was written so a partial or mangled write can
    # never pass as a valid entry.
    with open(entry_path, "r", encoding="utf-8", newline="\n") as handle:
        if handle.read() != LINE + "\n":
            raise ValueError("entry.txt does not contain the pickup line")


if __name__ == "__main__":
    main()
