# Phase 04 — whose data, under what licence

```
Start -> Cost -> Measure -> Truth -> [Data] -> Splits -> Observers -> Fusion -> Handoff
```

Now you get data. Two questions before a single row loads: may you use it, and can it
answer the question you spent three phases defining?

Both are gates. The licence question has a wrong answer available that is convenient, large,
and directly on topic — and unusable.

## What this phase is

The first real code that touches real data. A join, a hard look at what came out, and two
columns you have to notice and remove before they ruin everything downstream.

One of them is computed from the label. If you build a model before you find it, you will
get a magnificent number and learn nothing at all.

## What you will produce

`ci_triage/data.py`, `tests/test_data.py`, `artifacts/results/eda.json`,
`decisions/04-dataset-choice.md`, an `ai-ledger/` entry, and `knowns/04-data-and-licence.md`.

## Time

About 60 minutes. Rubric level 3.

## Check

```bash
uv run lab.py check 04
```
