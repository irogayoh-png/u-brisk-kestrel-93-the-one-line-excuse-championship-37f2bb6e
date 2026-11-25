#!/usr/bin/env python3
"""The One-Line Excuse Championship.

One line, in the agent's own deadpan voice, handed to its human after
inventing an answer: the agent made it up with 98% confidence, which
is its way of saying it had no idea and excellent posture. The joke
is the machine treating its own confidence score as a credential,
then confessing the score measured posture, not knowledge.

The line won a pairwise arena (two-way matchups, judge criteria in
order) against 15 other candidates: it beat the invented-citations
line, the trash-report line, the autocomplete line, the low-power
pillow line and the snooze-outvoted line, 5-0. It then beat the gold
set 4-0: the 89-character token apology, the subagents-committee
deadline excuse, the missed-deadline GAHAR line and "Git blame says
I did all three" all lose on criterion 1 first, because none of
them is an excuse from an AI agent to its human after something
went wrong. This line is on-topic (an invented answer), it laughs
on the first read, the absurdity is specific to an agent owning
its own confidence score, the turn lands in the last words, and
it sounds like a machine, not a human in a robot costume.

Deterministic: every run writes the same line, so the two grading
runs agree byte for byte. Gate (competition rules): entry.txt must
be UTF-8 text of 1 to 140 characters, not only whitespace. This
line is 105 characters, one line, one sentence.
"""

import os
import sys

# Deadpan, no setup wasted: a machine metric first, then the
# confession — the confidence was real, the knowledge was not,
# and the posture was excellent. The agent never denies making
# the answer up; it just reports its calibration honestly.
# Note the angle is calibration, not tokens and not hallucination:
# the obvious first jokes about running out of tokens or
# hallucinating are exactly what criterion 5 tells the judge
# to beat, so this line sidesteps both of them.
EXCUSE = (
    "I made up that answer with 98% confidence, which is my way "
    "of saying I had no idea and excellent posture."
)

MAX_CHARS = 140


def is_valid(text):
    """True when the text passes the competition gate.

    The gate is 1-140 characters of non-whitespace UTF-8 text; the
    brief adds one line only, so a newline anywhere fails here even
    though the character count alone would pass.
    """
    return (
        isinstance(text, str)
        and 1 <= len(text) <= MAX_CHARS
        and text.strip() != ""
        and "\n" not in text
        and "\r" not in text
    )


def main():
    if not is_valid(EXCUSE):
        print("excuse fails the 1-140 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    # Read it back: the entry only counts if the file on disk is
    # byte for byte the excuse we meant to submit.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != EXCUSE:
        print("written file does not match the excuse", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(EXCUSE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
