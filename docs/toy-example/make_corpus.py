"""make_corpus.py — toy corpus for the smoke test, built with the enumeration
engine (corpus_builder.py). DEMONSTRATES THE LAW: the row count FALLS OUT of
the declared decision space — nothing here picks a number.

Toy territory: support-ticket triage (small by design — it is a smoke test).
The spec declares its dimensions; the printed count is the result, not an
input. DEMO DATA ONLY — replace with your domain's real confirmed outcomes
(built the same way, with your own spec).
"""
import json, os, sys
from pathlib import Path

HERE = Path(__file__).parent

from persona.corpus_builder import build_corpus

SPEC = {
    "persona": "toy_support",
    "seed": 7,
    "craft_truths": [   # The triage practice rules (toy-sized on purpose)
        "the ticket names the failing component",
        "the response answers the reported symptom, not a guess",
        "the fix is verified by a check, not merely claimed",
        "the resolution states the version where it landed",
    ],
    "negations": [      # The documented failure modes of ticket handling
        "the ticket names no component at all",
        "the response answers a different question than asked",
        "the fix is claimed without any verification",
        "the versions in the thread contradict each other",
    ],
    "dimensions": {     # The axes triage judgment varies across
        "issue": ["billing", "login", "performance"],
        "severity": ["minor", "major"],
        "stage": ["triage", "resolution"],
    },
    "real_records": [],          # A toy has none; real seats declare theirs
    "vocabulary": [],
}

rows = build_corpus(SPEC, out_path=str(HERE / "corpus.jsonl"))
cells = 3 * 2 * 2
print(f"wrote {len(rows)} cases -> {os.path.join(HERE, 'corpus.jsonl')}")
print(f"(count fell out of the declared space: 3 issues x 2 severities x 2 stages "
      f"= 12 cells x 4 truths + interaction + edge rows = {len(rows)}; "
      f"narrow the spec and it shrinks, widen it and it grows)")
