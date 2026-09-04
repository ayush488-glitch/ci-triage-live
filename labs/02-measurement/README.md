# Lab 02 — how would we know this is any good?

```
Start -> Cost -> [Measure] -> Truth -> Data -> Splits -> Observers -> Fusion -> Handoff
```

Somebody hands you a triage system and says it is 94% accurate.

On this problem, a function that ignores its input entirely and always answers "not flaky"
scores about 94.4%. It catches nothing. It is not a model — it is a constant — and it beats
a great many real attempts on the metric everyone reaches for first.

So 94% is not a result. It is barely a sentence.

## Your focus

The first code. You build `ci_triage/metrics.py` — and only that — plus tests. No data yet,
no model. You are building the instruments before the experiment, which is the reverse of
the order most people work in and the reason most people cannot tell when they have fooled
themselves.

Two traps are waiting in here on purpose. One of them is a bug that shipped in the real
build of this system.

## Deliverables

`ci_triage/metrics.py`, `tests/test_metrics.py`, `decisions/02-metric-ladder.md`, an
`ai-ledger/` entry, and `knowns/02-measurement.md`.

## Suggested pace

About 75 minutes.

## Check

```bash
uv run lab.py check 02
```
