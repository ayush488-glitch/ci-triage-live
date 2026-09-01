# Task

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
