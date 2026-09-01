# Phase 01 — the output space and what a mistake costs

```
Start -> [Decision & Cost] -> Measure -> Truth -> Data -> Splits -> Observers -> Fusion -> Handoff
```

You have four actions from phase 00. Now: what is the system allowed to *say*?

The obvious answer is one output per cause. Three outputs, three actions, done. That answer
is wrong in a way that matters, and finding out why is most of this phase.

Then the harder half. Two mistakes:

- The system says **flaky**, the release goes out, and a real defect ships.
- The system says **real defect**, the release is held, and it was a flaky test.

Those are not equally bad. Until you say how much worse one is than the other, you have no
objective — you have a preference. And "accuracy" quietly assumes they are equally bad,
which is the one thing you know is false.

## What this phase is

Still no code. Two artifacts: the output space, derived rather than assumed, and a cost
table with numbers in it, even guessed ones. A guessed number that is written down can be
argued with. A missing number cannot.

## What you will produce

`decisions/01-output-space.md`, an updated `PROBLEM.md`, your first `ai-ledger/` entry, and
`knowns/01-decision-and-cost.md`.

## Time

About 50 minutes. Rubric level 2.

## Check

```bash
uv run lab.py check 01
```
