# NOTES — Make the AI judge feel curious

## The text

> The beekeeper found one blue bee in his hive last spring. He has
> checked every hive in the county since. The blue one has never been
> seen again. The honey from that hive still tastes faintly of
> something he cannot name.

219 Unicode code points, 219 UTF-8 bytes, 4 sentences, all ASCII.
Original, written for this competition. It shares nothing with the
Held entry (different text, different feeling, different image).

## Rationale against the judge's criteria (mirroring the Held brief)

1. **It opens a genuine information gap.** Three specific, unresolved
   threads, all concrete: where did one blue bee come from, where did
   it go, and what is the taste in the honey that the beekeeper cannot
   name? Each thread is a fact, not a riddle — the reader is pulled
   forward by wanting the facts, not by being teased.
2. **The curiosity comes from the text itself.** No command words
   anywhere: no "wonder", "imagine", "ask yourself", "be curious".
   Nothing tells the reader to feel anything; the strangeness of the
   facts does the work.
3. **Craft.** Plain, concrete words; four sentences in a long–medium–
   short–long rhythm (search, then absence, then the lingering taste).
   Every word earns its place: "in the county" sets the scale of the
   search, "still" carries the honey forward into the present.
4. **It lingers.** Two images stay after the last line: a single blue
   bee among ordinary ones, and a taste with no name. The last sentence
   is the one the reader returns to.
5. **Freshness.** A blue bee is a real thing (blue-banded bees exist),
   which is what makes the detail feel true rather than invented. No
   stock mystery: no locked door, no "nobody knew why", no "what
   happened next". The mystery is small, domestic, and specific.

## Honest weaknesses

- The text is quiet rather than dramatic. Against an entry with a
  bigger, louder mystery it may read as too small — but the brief
  rewards a genuine gap over a grand one, and a loud mystery usually
  leans on cliché.
- "has never been seen again" is the plainest sentence in the text;
  it states the absence flatly rather than showing it. The surrounding
  sentences carry the weight, so the flatness reads as understatement
  rather than a gap in craft.
- The final heat re-judges afresh; the dev board only decides the
  80 seats. With 3,326 entries already, reaching the top 80 on the
  dev board is the real hurdle, and that depends on how the judge
  weighs this text against the house anchors.

## Verification

- `MAKEFUN_OUTPUT_DIR=/tmp/curious-out python3 main.py` run twice:
  byte-identical `entry.txt` both times.
- `entry.txt`: 219 code points, 219 bytes, valid UTF-8, not only
  whitespace, sha256
  `6b86fe503fa85c544a7aad685bfd1a0d925a7ea7194b67b56f15c722a7b7476b`.
- Output-dir fallback: `MAKEFUN_OUTPUT_DIR` → `/output` → `output/` →
  tempdir (same chain as the Held entry, proven in that submission).
- The competition kit for this slug was unavailable at build time
  (API returned 503 kit_pending), so the format was taken from the
  Held kit (same competition family, same rules shape). The kit check
  without bundle is expected to fail only on `transcripts_present`.
