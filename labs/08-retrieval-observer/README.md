# Phase 08 — why the cheapest method won

```
... -> [Observer 3] -> ... -> Fusion -> Handoff
```

No training at all. Embed the failure log, look up the most similar past failures, see how
they were resolved, vote.

It is the strongest single component in this system, by a wide margin, and it is the one
that costs the least to build.

Before you build it: why would that be? What does looking things up have access to that
compressing a dataset into weights does not?

## What this phase is

One design decision carries the phase, and it is not the embedding model. It is what goes in
the index. There is a way to build this that produces a beautiful number and means nothing
at all, and it shipped in the original build before anyone noticed.

## What you will produce

`ci_triage/retrieval.py`, `tests/test_retrieval.py`, `artifacts/results/retrieval.json`,
`decisions/08-index-contents.md`, an `ai-ledger/` entry, and `knowns/08-retrieval-observer.md`.

## Time

About 60 minutes. Rubric level 5.

## Check

```bash
uv run lab.py check 08
```
