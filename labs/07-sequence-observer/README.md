# Phase 07 — did the model learn anything the heuristic did not?

```
... -> [Observer 2] -> ... -> Fusion -> Handoff
```

A test has a history: pass, pass, fail, pass, fail, pass. Your tabular observer collapses
that into summary numbers. A sequence model reads it as a sequence.

It will score better than your tabular observer, and you are going to want to celebrate.

Do not, yet. Before you run it, you are going to build the cheapest thing that uses the same
information: count how many times this test has failed before. No training, no parameters,
no GPU, runs in a millisecond.

Then compare, fold by fold.

## What this phase is

The control. Almost nobody runs it, because by the time you have a working sequence model
you are emotionally invested in it. The comparison has to be pre-committed or it will not
happen.

## What you will produce

`ci_triage/sequences.py`, `tests/test_sequences.py`, `experiments/07-heuristic-control.md`
(written before the run), `artifacts/results/sequence.json`, an `ai-ledger/` entry, and
`knowns/07-sequence-observer.md`.

## Time

About 60 minutes. Rubric level 4.

## Check

```bash
uv run lab.py check 07
```
