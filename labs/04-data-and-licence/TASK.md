# Task

## Design the slice — before anything else

Write `design/04-data-and-licence.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the ingestion layer**.

Source files to feature matrix. Every transformation named, and the point where the leak
guard sits.

The hard question: **where does the leak guard live so that it cannot be bypassed?** If it
is a step somebody remembers to call, it will be skipped. If it is inside the only function
that returns features, it cannot be.

Do not write code until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses.

---


**1. Licence first.** Find at least two candidate datasets for flaky-test research. For each:
who published it, what licence, and what it obliges you to do. Write it in
`decisions/04-dataset-choice.md` before you download anything. One of the obvious candidates
cannot be used. Say which, and why, and what you would need for that to change.

**2. Load and join.** Two CSVs have to be joined to produce one row per test run. Work out
the join key yourself. Write `ci_triage/data.py`. Ponytail: pandas already does all of this.

**3. Report the shape.** Rows, projects, positives, positive rate, feature count. Write them
to `artifacts/results/eda.json` from a command, not by hand.

**4. Find the two bad columns.**

- One column is computed from the label. It will produce a perfect model. Find it, drop it,
  and say how you spotted it.
- One column assumes a kind of history this dataset does not contain. Find it and say what
  it would need.

**5. Write the invariant test.** `tests/test_data.py` must contain a test that **fails** if
a leaking column reappears in the feature matrix. Not a test that the loader runs — a test
that catches the specific bug. This test should outlive every model you build.

**6. Two label columns.** There is more than one candidate label. Choose, and justify the
choice against your lab 00 decision.
