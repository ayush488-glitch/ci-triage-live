# Phase 09 — why the cheapest method won

```
... -> [Observer 3] -> ... -> Fusion -> Handoff
```

No training at all. Embed the failure log, look up the most similar past failures, see how
they were resolved, vote.

Within a project, retrieval may be useful; across unseen projects, it may be unmeasurable
with the available two-class data. Run the within-project evaluation and assess whether a
cross-project evaluation is performable before claiming either result.

Before you build it: why would that be? What does looking things up have access to that
compressing a dataset into weights does not?

## What this phase is

One design decision carries the phase, and it is not the embedding model. It is what goes in
the index. There is a way to build this that produces a beautiful number and means nothing
at all; the two-class control is what prevents it.

## What you will produce

`ci_triage/retrieval.py`, `tests/test_retrieval.py`, `artifacts/results/retrieval.json`,
`decisions/09-index-contents.md`, an `ai-ledger/` entry, and `knowns/09-retrieval-observer.md`.

## Time

About 60 minutes.

## Check

```bash
uv run lab.py check 09
```
