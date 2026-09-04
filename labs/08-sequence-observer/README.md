# Phase 08 — did the model learn anything the heuristic did not?

```
... -> [Observer 2] -> ... -> Fusion -> Handoff
```

A test has a history: pass, pass, fail, pass, fail, pass. Your tabular observer collapses
that into summary numbers. A sequence model reads it as a sequence.

There is a way to set this up that scores near 1.0 and teaches you nothing. It is the
obvious way. You will probably build it first, and the number will be so good that you will
not question it.

That is the first half of this phase. The second half is a control: before you believe any
sequence model, build the cheapest thing that uses the same information — count how many
times the test has failed before. No training, no parameters, runs in a millisecond.

Then compare, fold by fold.

## What this phase is

Two ways of being fooled, in order. A formulation that reads its own answer key, and a
result that looks like a win because nobody ran the free alternative.

Almost nobody runs the control, because by the time the model works you are invested in it.
So it gets written down first, before the model exists.

## What you will produce

`design/08-sequence-observer.md`, `ci_triage/sequences.py`, `tests/test_sequences.py`,
`experiments/08-heuristic-control.md` (written before the run),
`artifacts/results/sequence.json`, an `ai-ledger/` entry, and `knowns/08-sequence-observer.md`.

## Time

About 60 minutes.

## Check

```bash
uv run lab.py check 08
```
