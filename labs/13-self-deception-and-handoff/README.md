# Phase 13 — how could this system lie to us?

> **Ahead of the lecture.**

```
... -> Fusion -> [Handoff]
```

You have a working system. Every number in it was produced by a command you ran. Some of
them surprised you and you kept them anyway.

Now the last question, and it is the one that separates a project from a system: **how will
this thing fool you?**

Not how did it fool you. How *will* it. Written before the failure, as a prediction, with
the instrument that would catch each one.

## What this phase is

Three things that only work in this order: the failure register written as a prediction,
prior work located by a specific doubt rather than read up front, and the invariants moved
out of documents and into tests.

Then the handoff. Can another engineer take this and continue.

## What you will produce

`FAILURES.md`, `docs/prior-work.md`, `tests/test_invariants.py`, an assembled `KNOWNS.md`,
an `ai-ledger/` entry, and `.ci-lab/interviews/12.md` — the exit interview.

## Time

About 60 minutes. Rubric level 6. The coach questions and reviews; it does not create.

## Check

```bash
uv run lab.py check 13
open progress.html
```

Then `challenge/README.md`.
