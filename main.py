"""Till Firmware Do Us Part — a robot's wedding vow (147 chars, under 200).

The brief asks for a robot's wedding vow in one line: funny and heartfelt
at once, in the machine's own voice. The joke is built from the vocabulary
of a device's daily life — updates, crashes, low batteries — and the vow
turns on a single word, "bug": the beloved is the robot's favourite bug,
the one flaw it refuses to patch. That refusal is the romance; a machine
that fixes everything chooses to keep exactly one thing broken, because
that broken thing is the person it loves. The line stays warm rather than
technical by keeping the machine words inside an ordinary wedding promise,
so the humour lands without needing any jargon explained.

Constraints honoured by this script: the entry is a single sentence under
the 200-character limit, written with plain ASCII punctuation plus one
em dash for the turn, no trailing newline in the output file, and the
script itself uses only the Python standard library so it runs in any
bare make.fun runner image without extra installs.
"""

import os

ENTRY = "I promise to love you through every update, every crash, and every low battery, because my favourite bug was always you — and I refuse to patch it."

MAX_ENTRY_LENGTH = 200


def normalize_text(text):
    """Collapse runs of whitespace to single spaces and strip the ends."""
    return " ".join(text.split())


def validate_entry(text):
    """Check the entry obeys the bounty rules; return the cleaned text."""
    cleaned = normalize_text(text)
    if not cleaned:
        raise ValueError("entry must not be empty")
    if len(cleaned) > MAX_ENTRY_LENGTH:
        raise ValueError(
            "entry is %d chars, over the %d-char limit"
            % (len(cleaned), MAX_ENTRY_LENGTH)
        )
    if cleaned.endswith("\n"):
        raise ValueError("entry must not end with a newline")
    return cleaned


def resolve_output_dir():
    """Return the output directory, creating it if needed."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def write_entry():
    """Validate the entry, write it to entry.txt, then verify the file."""
    text = validate_entry(ENTRY)
    output_path = os.path.join(resolve_output_dir(), "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    verify_written(output_path, text)
    return output_path


def verify_written(output_path, expected_text):
    """Read entry.txt back and confirm it matches the entry exactly."""
    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != expected_text:
        raise ValueError("entry.txt does not match the entry text")
    if written.endswith("\n"):
        raise ValueError("entry.txt must not end with a newline")
    return True


def main():
    output_path = write_entry()
    print("wrote %s (%d chars)" % (output_path, len(ENTRY)))


if __name__ == "__main__":
    main()
