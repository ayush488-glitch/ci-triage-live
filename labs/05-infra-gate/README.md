# Lab 05 — which runs may contribute evidence at all?

```
Start -> Cost -> Measure -> Truth -> Data -> [Infra] -> Splits -> Observers -> Fusion -> Handoff
```

Use the three archives named in [data/README.md](../../data/README.md): `square-okhttp`,
`tootallnate-java-websocket`, and `kevinsawicki-http-request`. Inside them is the thing
everything downstream is built on: the outcome of every test, in every rerun.

Some of those runs are lies.

A run where the build never compiled reports every test as failing. A run that was
truncated reports the tests that had not executed yet as failing. A run where the JVM died
halfway through reports hundreds of failures that never happened. All three look, in the
raw data, exactly like a run where hundreds of tests genuinely failed.

Nobody has told you how many of your runs are like this.

## Your focus

The gate that decides whether a run is trustworthy enough to contribute an observation.
It runs before splits, before every observer, before anything — because a single poisoned
run can manufacture dozens of "flaky" tests, and every phase after this inherits them.

Do not assume the archive is flat: each project archive contains per-run archives, and the
`maven.log` is inside each run archive. A multi-module Maven log can also contain several
test-summary lines; they describe modules that must be summed, not competing totals.

## Deliverables

`design/05-infra-gate.md`, `ci_triage/infra.py`, `tests/test_infra.py`,
`artifacts/results/infra.json`, `decisions/05-infra-gate.md`, an `ai-ledger/` entry, and
`knowns/05-infra-gate.md`.

## Suggested pace

About 60 minutes.

## Check

```bash
uv run lab.py check 05
```
