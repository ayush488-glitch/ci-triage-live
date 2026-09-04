# Troubleshooting

**Calibration crashes on a fold** — too few positives in the calibration split. Use
cross-validated calibration, and record how many folds were usable.

**Calibrated AUC comes out at exactly 0.5** — this means one of two very different things:
the calibrator collapsed and is emitting a constant, or the model genuinely has no signal.
Check the distribution of the calibrated probabilities. If they are all one value, it is
collapse, and collapse is a bug, not a result.

**Pooled metrics look different from per-fold means** — pooling calibrated probabilities
across folds mixes different calibrators. Report per-fold and say which you are quoting.
This error is easy to make when calibrators differ across folds.

**Per-project training has too few rows for some projects** — expected. Set a minimum row
count, report how many projects met it, and treat the rest as out of scope. Do not silently
drop them.

**You cannot decide on the pivot** — reread `PROBLEM.md`. The answer is in who operates the
system, not in the metrics.
