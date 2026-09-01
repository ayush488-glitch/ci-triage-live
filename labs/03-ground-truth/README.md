# Phase 03 — is the label even true?

```
Start -> Cost -> Measure -> [Truth] -> Data -> Splits -> Observers -> Fusion -> Handoff
```

Somewhere there is a dataset with a column that says whether a test is flaky. Before you
train anything on that column, one question: how does anyone know?

Nobody looked at these tests and judged them. The label came out of a procedure — run the
test many times, and if it both passed and failed on identical code, call it flaky.

That procedure works in one direction and not the other.

## What this phase is

Still no data downloaded. This is an argument, not a computation, and it is the phase that
decides how much you are allowed to believe about every number in the rest of the lab.

## What you will produce

`decisions/03-label-procedure.md`, `experiments/03-rerun-bias.md`, an `ai-ledger/` entry,
and `knowns/03-ground-truth.md`.

## Time

About 45 minutes. Rubric level 3 — you interpret first, the coach explains after.

## Check

```bash
uv run lab.py check 03
```
