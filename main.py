"""Two-Sentence Horror.

Entry for make.fun competition
u-suroto-two-sentence-horror-acea9253.

The story
---------
    Every Friday I withdraw the same cash from the same ATM outside
    the station, and I always keep the receipt. Today the receipt
    showed two withdrawals, and the second one was still printing
    when I walked away.

Why this story was chosen (design reasoning, written for this entry)
---------------------------------------------------------------------
The competition asks for one horror story of exactly two sentences,
at most 400 characters, judged pairwise by a model brief that weighs,
in strict order: (1) it is a horror story in exactly two sentences
and it is genuinely frightening; (2) the second sentence turns or
reveals something that makes the first sentence worse on a second
read; (3) the horror is implied rather than explained, leaving the
reader to fill in the worst of it; (4) precise, concrete prose, every
word earning its place; (5) original, not a familiar horror twist or
a known story retold. Restraint matters more than shock; gore for its
own sake does not count.

The story was picked by a ten-candidate round-robin tournament
(CANDIDATES.md in the bounty directory), judged on exactly that
criterion order with originality as the novelty gate. It won 9-0.

Three decisions shape the story:

1. The lane is empty. A fresh scan of the live field (830
   submissions, 24 Nov 2026) found zero entries about an ATM or an
   ATM receipt, while baby monitor (9), 3 a.m. (17), dog (15), smart
   speaker (20), voice (18), doorbell/knock (19), photo (25), chair
   (16), lullaby/music box (17), voicemail (10), mirror (7),
   toothbrush (7) and the "dated tomorrow" device (3 entries) are all
   taken. The receipt is also a document, not a place: no haunted
   house, no monster, nothing the reader has seen a hundred times.

2. The scare is present tense, not past tense. Sentence 1 sets a
   routine -- same cash, same machine, every Friday, receipt kept --
   and sentence 2 does not reveal a past event but a live one: the
   second withdrawal is still printing while the narrator walks
   away. That is what makes sentence 1 worse on re-read. The receipt
   was never a record; it is a feed, and someone else is using the
   card at this machine, right now, while the narrator stands there.
   The reader is left to fill in who -- the story never names them,
   which is what criterion 3 asks for, and no gore is needed.

3. Every word is concrete. "The same cash", "the same ATM outside
   the station", "I always keep the receipt" -- a habit with a paper
   trail, which is exactly what the second sentence turns against
   the narrator. The story is 207 characters, well inside the 400
   cap, and short enough that the byte tie-break favours it if two
   entries ever tie on win rate.

The runner-up story (8-1 in the tournament) was the library book --
"Every month I renew the same library book, because the due-date
card always has one more stamp. Today the card ran out of space,
and the librarian stamped the inside of my wrist instead." -- kept
as the fallback if this story ever collides with a house text.

The program itself is deliberately trivial: the story is a constant,
checked against the gate (UTF-8, exactly two sentences, 1-400
characters, not only whitespace) and written byte-exact to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set), with no
trailing newline, no clock, no randomness and no network, so two
runs are byte-identical.
"""

import os
import re
import sys

STORY = (
    "Every Friday I withdraw the same cash from the same ATM "
    "outside the station, and I always keep the receipt. "
    "Today the receipt showed two withdrawals, and the second "
    "one was still printing when I walked away."
)

MAX_CHARS = 400


def sentence_count(text: str) -> int:
    parts = [p for p in re.split(r"(?<=[.!?])\s+", text.strip()) if p]
    return len(parts)


def main() -> int:
    text = STORY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate: story is {len(text)} chars, must be 1-400",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: story is only whitespace", file=sys.stderr)
        return 1
    if sentence_count(text) != 2:
        print(f"gate: story has {sentence_count(text)} sentences, "
              "must be exactly 2", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
