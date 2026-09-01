# Reference — read after your attempt

## What calibration cost

Uncalibrated, grouped: **AUC ≈ 0.605, ECE ≈ 0.115**.
Calibrated, same folds: **AUC ≈ 0.542, ECE ≈ 0.030**.

Calibration made the probabilities nearly four times more honest and cost about 0.06 of
discrimination. On small, high-variance folds a fitted probability map is itself estimated
from few positives; it is noisy, it is not perfectly monotone in practice, and it reorders
cases near the decision boundary. Ranking pays for honesty.

That is a trade you have to make deliberately. Which one you want depends on what the
consumer does with the output. A threshold-based action needs the calibrated number. A
ranked queue for a human to work through needs the discrimination.

## The degenerate case

Perfect calibration at chance discrimination is a model that has learned the base rate.
ECE alone would call it excellent. It cannot be thresholded into any useful action because
every case gets the same score. You will meet this again in phase 07, from a model that
looks much more sophisticated.

## The pivot

Cross-project: **AUC ≈ 0.605**. Per-project, trained and evaluated within each project:
**AUC ≈ 0.737 on okhttp**, and better across the board.

This is not a better model. It is a different question. Cross-project asks "can we predict
flakiness on a repository we have never seen"; per-project asks "given this repository's
own history, can we predict flakiness in it". The second is easier, and — read `PROBLEM.md`
— it is also what actually happens, because each team runs its own CI on its own history.

What you lose: the system no longer works on day one for a new repository. That is a real
cost and it goes in `decisions/06-the-pivot.md`, not in a footnote. It becomes a
known-unknown: how much history does a new project need before the per-project model is
usable? Nobody has measured that here.

## The move worth learning

The pivot came from believing a bad number. The alternative — the one most projects take —
is to keep tuning the cross-project model until the number looks acceptable, which means
selecting on the evaluation set until it stops measuring anything. Three months later the
system does not work and nobody can say when it stopped.

The weak result was information. Tuning it away would have destroyed the information and
kept the appearance.
