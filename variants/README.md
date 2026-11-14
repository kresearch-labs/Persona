# Pblock variants

A pblock is not only one thing. The rest of this repository describes the
**normal** pblock: before a task it briefs the model with the closest cases —
what worked, what failed — and after the task it learns from what actually
happened. That is the base every pblock shares: the same frozen embedder, the
same case store with its history, the same small trained judges.

A **variant** keeps that base and changes how the pblock is used. It can change
four things, and only these four:

| | What a variant may change |
|---|---|
| **Its job** | what it gives the agent: a briefing, a verdict, something else |
| **What it learns from** | the work, the user, new cases someone adds |
| **When a lesson is trusted** | the proof a lesson needs before it counts |
| **When it runs** | before a task, before every action, always |

A pblock's template says which kind it is — `variant: personal`,
`variant: keel_guard` — and no `variant` means the normal kind.

## The variants so far

| | Normal | [Personal](personal.md) | [Keel Guard](keel_guard.md) |
|---|---|---|---|
| **Its job** | briefs the model before a task | briefs "how this person likes to work" | judges each agent request: STOP, DOUBT or PASS |
| **Learns from** | the work: what was fixed, and what failed and why | only the person's own words and choices | new threat cases added to its store |
| **A lesson is trusted when** | a different task proves it again | the person says it directly, or it is seen again | its gates pass after the judges are refit |
| **Runs** | before each task | always, for its person | before each action |

More will come — a team pblock that learns a team's conventions, a reviewer that
judges finished work. Each is a new page here, not a change to the base.

Aura is where these variants run as described:
[Aura](https://github.com/kresearch-labs/aura-agent).
