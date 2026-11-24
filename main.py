#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to entry.txt in the output directory.
The joke is the whole entry: a father answers his son with a pun
that lands on the first read and needs no explaining.

The gate requires UTF-8 text of 1 to 200 characters, not only white
space, so the joke is validated against that limit before anything
is written, and the file is written atomically so a run never leaves
a half-written entry behind.
"""

import os

MAX_CHARS = 200

JOKE = (
    "My son said my jokes aren't funny. I said, 'They're not meant to be "
    "funny \u2014 they're groan-up jokes.'"
)


def validate(text: str) -> None:
    """Fail loudly instead of shipping an entry the gate would refuse."""
    if not text.strip():
        raise ValueError("joke must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
