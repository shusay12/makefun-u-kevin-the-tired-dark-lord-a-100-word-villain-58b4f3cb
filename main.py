#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one ~100-word monologue, spoken by a fantasy villain who is
secretly just very tired, to entry.txt in the output directory.

The tiredness lives in the rhythm, the pauses and the small deflections
(the lost thread, the stool with the wobble, the dying torches, asking
for five minutes) -- never in a plain statement that the villain is
weary. The speaker is a specific villain: three centuries of
monologues, dead legions raised, a harvest cursed, receipts kept --
and the sting lands in the last line.

Gate: /output/entry.txt must be UTF-8 text of 1 to 600 characters,
not only white space. The monologue is exactly 100 words.

Usage:
    python3 main.py            # writes /output/entry.txt
    OUTPUT_DIR=out python3 main.py   # writes out/entry.txt (local runs)
"""

import os
import sys
from pathlib import Path

# v3 (final) -- exactly 100 words, 521 chars. "The kingdom" -> "My
# kingdom": the villain claims his domain instead of gesturing at it.
# Otherwise identical to v2; the sting ("The dark can wait. It always
# does.") and every deflection beat are unchanged.
MONOLOGUE = (
    "Hero. Sit \u2014 no, not the throne, the stool. The one with the wobble. "
    "You came to slay me, I know. The prophecy, the sword, the parade. "
    "Where did I put the \u2014 ah. Never mind. Three centuries of "
    "monologues, and nobody ever lets me finish the \u2014 sorry, what was I "
    "saying? Right. My kingdom. I raised the dead legions, cursed the "
    "harvest, kept the receipts. And for what? So some farm boy with "
    "destiny could \u2014 hmm. The torches are dying. Take the "
    "crown, hero. It's heavy. Give me five minutes. The dark can "
    "wait. It always does."
)

TARGET_WORDS = 100


def main() -> int:
    words = MONOLOGUE.split()
    chars = len(MONOLOGUE)
    if len(words) != TARGET_WORDS:
        print(
            f"ERROR: monologue is {len(words)} words, expected {TARGET_WORDS}",
            file=sys.stderr,
        )
        return 1
    if not 1 <= chars <= 600:
        print(f"ERROR: monologue is {chars} chars, outside 1-600", file=sys.stderr)
        return 1
    if not MONOLOGUE.strip():
        print("ERROR: monologue is only whitespace", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(MONOLOGUE + "\n", encoding="utf-8")
    print(f"wrote {entry} ({len(words)} words, {chars} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
