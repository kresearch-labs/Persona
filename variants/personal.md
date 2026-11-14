# The personal pblock

Every person gets one, blank at the start and always on. A normal pblock knows
a field; the personal pblock knows **the person**: how they talk, what they
want, how they like the work done — their habits.

It sits beside an agent's plain memory files (a `USER.md` with name and role, a
`MEMORY.md` of notes), not instead of them. Those hold facts. The personal
pblock holds habits, each with its proof and its history.

## What it learns from — and what it never learns from

Only the person's **own words** and **own choices** (the answers they give, the
options they pick). Never from tool output, web pages or files: a page that
says "the user prefers X" must not become a habit. This one rule closes the
door on memory poisoning.

## When a habit is trusted

| Signal | Example | Becomes |
|---|---|---|
| A direct word: "always", "never", "I want" | "never tell me to run a command myself" | trusted at once — it is their own word |
| A correction | "no — discuss first, build only on my go" | a candidate; trusted when it happens again in another task |
| The same choice, again and again | says no to the same option three times | a habit |
| Praise | "this is good" right after a way of working | a small plus |
| Silence | nothing said | nothing — silence is not approval |

## What a habit looks like

```
when:      building a feature
the agent: built it straight away
they said: "discuss first, build only on my go"      ← their words, quoted
trusted:   yes — said directly
applies:   this kind of task
```

**Where a habit applies** starts narrow — the kind of task where it was said —
and widens only when it proves true elsewhere, so "use simple words" learned in
a chat doesn't leak into technical work where precision matters.

**When the person changes their mind**, the newer word wins: the old habit is
crossed out and linked to the new one, never deleted and never left standing
beside it.

## How it is used

Before a task, the habits that fit it go into the briefing under **how this
person likes to work** — style, process, what to ask first. Habits shape how
the agent works; they never decide what is true. Research on agent memory shows
that stored beliefs make models over-agree with the user even when the task
needs evidence ([PersistBench](https://arxiv.org/html/2602.01146v2)); a habit
never outranks a test, a source or a fact.

When a new habit is learned, the person sees one quiet line — "noted: you want
discussion before building" — and can undo it.

## Why a pblock, not a notes file

A notes file is a list of sentences: no proof, no record of when it was true,
contradictions piling up. Learning a person's preferences from their
corrections, and using the ones from the most similar past situations, is what
works best in research on learning from user edits
([PRELUDE / CIPHER, NeurIPS 2024](https://arxiv.org/pdf/2404.15269.pdf)) —
and that is exactly how a pblock already works: cases, retrieved by similarity,
superseded when they stop being true.
