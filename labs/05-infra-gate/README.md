# Phase 05 — which runs may contribute evidence at all?

```
Start -> Cost -> Measure -> Truth -> Data -> [Infra] -> Splits -> Observers -> Fusion -> Handoff
```

You have the archives now. Inside them is the thing everything downstream is built on: the
outcome of every test, in every rerun.

Some of those runs are lies.

A run where the build never compiled reports every test as failing. A run that was
truncated reports the tests that had not executed yet as failing. A run where the JVM died
halfway through reports hundreds of failures that never happened. All three look, in the
raw data, exactly like a run where hundreds of tests genuinely failed.

Nobody has told you how many of your runs are like this.

## What this phase is

The gate that decides whether a run is trustworthy enough to contribute an observation.
It runs before splits, before every observer, before anything — because a single poisoned
run can manufacture dozens of "flaky" tests, and every phase after this inherits them.

The result on one project is not a rounding error. It is a factor of roughly twenty.

## What you will produce

`design/05-infra-gate.md`, `ci_triage/infra.py`, `tests/test_infra.py`,
`artifacts/results/infra.json`, `decisions/05-infra-gate.md`, an `ai-ledger/` entry, and
`knowns/05-infra-gate.md`.

## Time

About 60 minutes. Rubric level 4.

## Check

```bash
uv run lab.py check 05
```
