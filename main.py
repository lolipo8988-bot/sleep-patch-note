"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep is
fixed to /output/entry.txt. The text is a fixed, hand-written string,
so every run produces byte-identical output.
"""

import os

ENTRY = (
    "Fixed: sleep no longer crashes at 3 a.m. when your brain "
    "replays the embarrassing thing you said in 2019 — in HD, "
    "with subtitles."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
