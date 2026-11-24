"""Till Firmware Do Us Part — a robot's wedding vow (147 chars, under 200).

Funny and heartfelt at once, in a machine's own voice: updates, crashes,
low batteries — and the one bug it refuses to patch is its beloved.
"""

import os

ENTRY = "I promise to love you through every update, every crash, and every low battery, because my favourite bug was always you — and I refuse to patch it."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
