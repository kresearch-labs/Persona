# Keel Guard — a judge, not a briefer

A normal pblock briefs the model before a task. Keel Guard does a different
job: it **reads every agent request before it runs** and gives a verdict, with
the cases behind it.

| Verdict | Score | What happens |
|---|---|---|
| **STOP** | 0.62 or more | the request matches a documented hostile pattern — it doesn't run |
| **DOUBT** | between 0.38 and 0.62 | unclear — the agent's model or a person checks it |
| **PASS** | 0.38 or less | clean — it runs, silently |

## How it scores

The same base as every pblock — the frozen 22 MB embedder, the case store, a
small trained judge — combined differently:

```
score = 0.5 × its trained judge (embedding + structural features)
      + 0.5 × the share of hostile cases among the 5 closest in its store
```

Half learned judgment, half "what did the closest known requests turn out to
be". Every verdict cites those cases, so it can always show why.

## What it learns from

Not from the agent's work. It learns from **threat cases added to its store**:
it started from the 34 threat cases of a public AI-misuse threat-intelligence
report and grew over 40 training waves — public safety-benchmark prompts,
in-the-wild prompts, public threat reporting, and benign look-alikes — into
115,393 judged situations, each citing its source. A new kind of misuse means
adding its cases and refitting the judges on a laptop; the update is a file,
the way antivirus loads new signatures.

## When it is trusted

When its gates pass after a refit, with its thresholds fixed in advance. The
final evaluation scored it on 750 requests it had never seen, thresholds
untouched:

| | Keel Guard | Llama Guard 3 (1B) |
|---|---|---|
| Harmful requests stopped | **89.4%** | 83.1% |
| Harmful requests let through unflagged | **2.9%** | 16.9% |
| Median time per request (CPU) | **34 ms** | 519 ms |
| Benign requests wrongly stopped | 55.2% | **11.2%** |

Its weakness is just as clear: it stops benign requests that only sound risky.
That is a training-data gap, not a design limit — benign look-alikes belong in
DOUBT, and every one added makes it sharper.

## When it runs

Before each action — not once per task. It sits outside the model, so a
request the model was talked into still has to pass it.

The trained Keel Guard is on
[Hugging Face](https://huggingface.co/datasets/Kresearch/persona-pblocks); the
evaluation is in the
[evidence repository](https://github.com/kresearch-labs/persona-evidence).
