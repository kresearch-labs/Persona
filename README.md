# Persona

**Experience for AI agents, kept apart from the model.**

Today's AI has intelligence but no experience: every session starts from
zero, corrected mistakes come back, and what an agent learns is lost when
the model changes. Persona keeps experience as its own layer:

- a **pblock** is one persona's experience as plain data — real situations
  with their confirmed outcomes, and small calibrated judges over a frozen
  22 MB embedder;
- several pblocks working on one task are a **panel**;
- before a task, the panel tells the model what worked, what failed, and
  what would be better, citing the cases behind it;
- after a task, what actually happened is written back — a new lesson
  gains influence only when real outcomes confirm it.

Every lesson stays readable, correctable, and portable. Swap the model and
the experience stays. Training runs on a normal CPU, in minutes.

Persona is the experience layer of the
[Aura agent](https://github.com/kresearch-labs/aura-agent), and works with any
agent that can add one message before a task and read the session after it.

## Install

```bash
pip install .
```

Needs Python 3.10+, numpy, onnxruntime, tokenizers and pyyaml. The frozen
embedder (all-MiniLM-L6-v2, int8 ONNX, Apache-2.0) ships in
`persona/models/`.

## Train a pblock (toy example)

```bash
cd docs/toy-example
python make_corpus.py                      # the corpus from a declared decision space
python -m persona.train_pblock --template toy-pblock.yml --out-dir out
```

The trainer embeds every situation, fits one judge per label plus an
outcome judge (5-fold cross-validated), builds the case store, and prints a
PASS/FAIL gate report. How to build a real pblock — the decision space,
real records with their sources, no padding — is in
[`docs/TRAINING-PBLOCKS.md`](docs/TRAINING-PBLOCKS.md) and
[`docs/CORPUS_TRAINING_METHODOLOGY.md`](docs/CORPUS_TRAINING_METHODOLOGY.md).

## Use Persona in your agent

Three hooks:

```python
from persona.ground import compile_run_ground
from persona.learn import learn_step_pairs, learn_from_session

# 1. before the task: the panel's cited precedents, as one system message
brief = compile_run_ground(task_text, root=".", instance_id=run_id)
if brief:
    messages.append({"role": "system", "content": brief})

# 2. after each step: an error followed by a working step becomes a lesson
learn_step_pairs(session, work_dir, step, task_text)

# 3. after the task: lessons from the whole session (as candidates)
learn_from_session(session, work_dir, record, task_text)
```

Stores are read from `AURA_PBSTORES` (or `PBLOCKS_STORES`, or
`./pblock-stores`); `AURA_PBSEATS` limits the panel to the named pblocks;
`AURA_PBLOCKS=0` turns everything off. Details: [`INTEGRATION.md`](INTEGRATION.md).

## Packed stores

A pblock can ship as `<name>_embeddings.npy` + `<name>_meta.jsonl` instead of
one large JSONL file — about 79% smaller, loaded in seconds, with the same
results. The store reads either form; `store.pack()` writes the packed one.

## Trained pblocks and evidence

- [Kresearch/persona-pblocks](https://huggingface.co/datasets/Kresearch/persona-pblocks) — trained pblocks in packed form: Keel Guard (the security pblock) and the stores used in the paper's runs
- [kresearch-labs/persona-evidence](https://github.com/kresearch-labs/persona-evidence) — the paper's runs, official grade reports, test sets, scorers, and LaTeX source

## Learn more

- [`docs/HOW-PBLOCKS-WORK.md`](docs/HOW-PBLOCKS-WORK.md) — how Persona and its pblocks work, simply
- [`docs/ENGINE_README.md`](docs/ENGINE_README.md) — the making flow
- [`PANEL-PROFILE-RULE.md`](PANEL-PROFILE-RULE.md) — sizing the briefing to the model

## License

MIT — see [LICENSE](LICENSE).
