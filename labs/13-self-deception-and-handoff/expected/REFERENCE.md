# Reference — read after your attempt

## The four families

**1. Lying about performance.** The rare-class illusion — 94.4% accuracy catching nothing.
A degenerate perfect score — near-zero ECE at chance AUC. Pooling calibrated probabilities
across folds, which mixes calibrators fitted on different data and produces a number that
belongs to no model. Leakage of any kind, which is invisible in every metric and visible
only in a test.

The general rule: when a result is surprisingly good, check the construction before checking
the model. Most spectacular numbers are bugs in the harness.

**2. Calibrator collapse.** A calibrator fitted on too few positives can map everything to a
constant. ECE then reports near-perfect calibration and AUC drops to exactly 0.5. Exactly
0.5 is the tell — genuine absence of signal wanders around 0.5, it does not sit on it.
Instrument: assert the spread of calibrated probabilities is non-degenerate.

**3. Infrastructure contamination.** A rule tuned on a handful of projects and applied to
all 25. A gate that removed a project it had never evaluated. Both shipped in the original
build. Instrument: per-project breakdowns for everything, never a single pooled number.

**4. Breaking in operation.** Cost drifting because a price table was hardcoded and a model
changed. Latency exceeding the budget at the tier where most traffic actually lands. An
arbiter escalating on calibration collapse rather than on genuine disagreement — which
happened, and which looked exactly like the system working. Instrument: escalation rate as a
monitored quantity with an alarm, not a number somebody checks when they remember.

## Prior work, in the right order

Reading the literature first produces a design that reproduces a paper. The order that works:

```
design until you have a specific doubt -> search that doubt -> record what changed
```

Five doubts is a reasonable target. The document records doubt, query, finding, and change.
"Nothing changed" is a legitimate row and appears more often than people admit; writing it
honestly is what makes the other rows believable.

Verify every citation. An agent will produce a plausible reference with a plausible author
and a plausible year for a paper that does not exist.

## Assertions rather than documentation

```python
def test_no_leaking_column(): ...
def test_no_project_spans_a_split(): ...
def test_retrieval_index_is_multiclass(): ...
def test_every_observer_declares_calibration(): ...
```

Four tests. Each one corresponds to a real bug from this build. A document describing these
rules degrades the first time somebody is in a hurry; a test fails.

Break each one deliberately once and confirm it fails. A test that has never failed has
never been tested.

## The handoff

The exit question is not "does it work". It is: can another engineer reproduce every number,
find every decision and what it cost, see which hypotheses were refuted, and know what
remains unknown?

The known-unknowns are the most valuable part. A strong list on this project includes: how
much history a new project needs before the per-project model is usable; how much of the
weak cross-project result is label contamination rather than genuine difficulty; whether the
retrieval advantage survives on projects outside these 25; and what the fusion comparison
would look like with an arbiter that received actual evidence.

None of those are failures. They are the next four experiments, and handing them over
correctly stated is worth more than any number in the repository.
