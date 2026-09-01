# Task

## Design the slice — before anything else

Write `design/07-sequence-observer.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **observer 2**.

The second observer, same template. Then the part that matters:

The hard question: **what does this observer read that observer 1 does not?** If the honest
answer is "the same information in a different shape", you have designed a reimplementation,
and this phase is going to prove it numerically.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---


**1. Write the control first.** In `experiments/07-heuristic-control.md`, before any model
exists: define the cheapest heuristic that uses each test's history. State what result would
make you keep the sequence model and what result would make you throw it away.

That second sentence is the phase. Write it in a form somebody could hold you to.

**2. Build the sequence.** Turn each test's run history into an ordered sequence, respecting
time. Any leakage of future runs into the past invalidates everything.

**3. Test the ordering.** `tests/test_sequences.py` must fail if a sequence contains a run
that happened after the one being predicted.

**4. Train the model.** An LSTM or GRU over the sequences, on your per-project split. Report
your full metric set.

**5. Run the control on the same folds.** Not on a different split, not on pooled data. The
same folds, the same metric, side by side, in `artifacts/results/sequence.json`.

**6. Read the comparison honestly.** If they are close, say how close. If they are
indistinguishable, say so plainly. A model that ties a free heuristic is a finding, and it
is a more useful finding than a win.

**7. Watch for the degenerate variant.** If one of your architectures reports near-zero
calibration error, check its AUC before you get excited.
