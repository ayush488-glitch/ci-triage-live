# Task

## Design the slice — before anything else

Write `design/08-sequence-observer.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **observer 2**.

The second observer, same template. Then the part that matters:

The hard question: **what does this observer read that observer 1 does not?** If the honest
answer is "the same information in a different shape", you have designed a reimplementation,
and this phase is going to prove it numerically.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---

**1. Find the circularity before you build.** Re-read how `IsFlaky` was defined — it is in
your phase 03 notes. Then ask: if I use rerun outcomes as features to predict it, what am I
actually feeding the model?

Write the answer in `experiments/08-heuristic-control.md` before you write code. If you
cannot see it, build the naive version, look at the AUC, and then work out why a number that
good is impossible.

**2. Reformulate so features and label never share a run.** Prefix predicts suffix is one
way. State yours explicitly, and say what question the reformulated task answers for an
engineer — it should be something someone can act on.

**3. Gate on phase 05.** Only runs your infra gate marked CLEAN may contribute an outcome to
either half. One poisoned run in a prefix injects noise into features and label at once.

**4. Write the control first.** The cheapest predictor using the same information, no
training. Then, in the same file, before any model exists: what result would make you keep
the sequence model, and what result would make you throw it away. Write the second one in a
form somebody could hold you to.

**5. Test the ordering.** `tests/test_sequences.py` must fail if any run appears in both the
prefix and the suffix of the same example. Break it deliberately once and confirm it fails.

**6. Train the model.** LSTM or GRU, project-grouped split, at least two prefix lengths.

**7. Report raw AND calibrated AUC, plus the count of distinct calibrated probabilities.**
All three, per fold. A calibrated AUC of exactly 0.5 means two completely different things
and you cannot tell which without the other two numbers.

**8. Run the control on the same folds.** Side by side in `artifacts/results/sequence.json`.
If they are close, test whether they are distinguishable at all rather than eyeballing means.

**9. Decide.** Keep the component or withdraw it. Either is defensible. Reporting the model
number without the control is not.
