# Lab 06 — the split is the experiment

```
Start -> Cost -> Measure -> Truth -> Data -> [Splits] -> Observers -> Fusion -> Handoff
```

You are about to fit the same model twice on the same data with the same features, and get
two answers that are not close to each other. The only thing that changes is how the rows
are divided.

One of the two answers is a measurement of your model. The other is a measurement of how
well your model memorised which project a row came from.

Before you run it, you are going to write down which you expect and by how much. Most
people predict a small gap.

## Your focus

The phase that decides whether anything else in this lab means anything. Every number after
this inherits the split.

## Deliverables

`ci_triage/splits.py`, `tests/test_splits.py`, `experiments/06-split-comparison.md` (written
*before* the run), `artifacts/results/baseline.json`, `decisions/06-split-choice.md`, an
`ai-ledger/` entry, and `knowns/06-splits-and-baseline.md`.

## Suggested pace

About 60 minutes. Predict first, then defend the result with the recorded evidence.

## Check

```bash
uv run lab.py check 06
```
