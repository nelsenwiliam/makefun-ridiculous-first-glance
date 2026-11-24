#!/usr/bin/env python3
"""Write one sentence pitching a bizarre startup idea to /output/entry.txt.

Pure standard library. The sentence is the whole entry: it names the odd
thing being sold, who pays for it, and why the business holds together.
"""

import os

SENTENCE = (
    "We sell naming rights to potholes: drivers pay $5 to name the crater "
    "that ate their tire, cities repair named holes first, and sponsors get "
    "a plaque where the asphalt failed."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
