# Troubleshooting

**A fold has no positives** — at 3% positives across uneven project sizes this happens.
Use a grouped splitter that stratifies where it can, and report how many folds were usable.
Do not silently drop them; record it.

**Huge variance across grouped folds** — expected, and informative. Projects differ. Report
the standard deviation alongside the mean and treat a single-fold number as meaningless.

**Your grouped AUC is close to 0.5** — check the feature matrix is not empty and the leaking
column really is gone. A grouped result near chance can be honest; a grouped result of
exactly 0.5 usually means something is broken.

**Random-split AUC is near 1.0** — a leaking column survived. Go back to phase 04's
invariant test and check it actually runs.

**Which model?** — anything simple. Logistic regression or a small gradient-boosted model.
The model is not the experiment here; the split is.
