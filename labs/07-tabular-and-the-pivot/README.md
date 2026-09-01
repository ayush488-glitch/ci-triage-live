# Phase 07 — the first observer, and what to do when it fails

```
Start -> Cost -> Measure -> Truth -> Data -> Splits -> [Observer 1] -> ... -> Fusion -> Handoff
```

Your first real component: a gradient-boosted tree over the 23 numeric features, producing
a probability that this failure is flaky.

Two things happen in this phase and they are both uncomfortable.

**Calibration is not free.** You will calibrate the model because phase 02 told you to, and
one of the two numbers you care about will get substantially better while the other gets
worse. Almost nobody predicts which.

**The component does not work well enough.** Across unseen projects, it is weakly
informative and nothing you do to the model changes that much. At that point you have three
honest options and one dishonest one, and most projects take the dishonest one.

## What this phase is

The first time a result is bad and you have to decide what that means. This is the phase the
whole course is actually about.

## What you will produce

`ci_triage/tabular.py`, `tests/test_tabular.py`, `experiments/06-calibration-tradeoff.md`,
`artifacts/results/tabular.json`, `decisions/06-the-pivot.md`, an `ai-ledger/` entry,
`knowns/06-tabular-and-the-pivot.md`, and `.ci-lab/interviews/06.md`.

## Time

About 75 minutes. Rubric level 4, and the first **graded interview**.

## Check

```bash
uv run lab.py check 07
```
