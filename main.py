"""Monday Morning Punchlines — one original joke about Monday mornings.

Writes a single joke (<= 200 characters) to /output/entry.txt.
Standard library only; paths resolved from this file, never process.cwd().
"""

import os
from pathlib import Path

JOKE = (
    "Monday morning, my alarm and I signed a peace treaty: "
    "it rings at six, I rise at nine, and we both blame the coffee."
)

MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"joke is {len(text)} chars"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text + "\n", encoding="utf-8")
    # Verify the round trip: what the grader reads must be exactly the joke.
    round_trip = out_path.read_text(encoding="utf-8").strip()
    assert round_trip == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
