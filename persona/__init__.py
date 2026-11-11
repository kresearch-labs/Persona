"""Persona — experience for AI agents, kept apart from the model.

A pblock is one persona's experience as plain data: real situations with
their confirmed outcomes (the store) and small calibrated judges (the
heads) over a frozen 22 MB embedder. Several pblocks working together on a
task are a panel. Before a task the panel briefs the model with cited
precedents; after it, what happened is written back.

Modules: store (bi-temporal case store, packed form), orchestrator (panel
selection, compiled briefing), judge_v0 (calibrated heads, honest
abstention), ground (the briefing for a task), learn (lessons from a
session), train_pblock (template -> heads + store), corpus_builder (the
corpus from a declared decision space), selftrain (retrain on staleness),
verdict_link / output_audit (closing the loop), quality (what counts as a
lesson).
"""

__version__ = "0.1.0"
