# Reference — read after your attempt

## The numbers

Per-project LSTM over test-run histories: **AUC ≈ 0.782**. Better than the per-project
tabular observer at ≈ 0.737, and much better than cross-project at ≈ 0.605.

The failure-count heuristic — count how often this test has failed before, rank by that —
scores **the same, in every fold**. Not close on average. Effectively identical fold by
fold.

## What that means

The LSTM learned the heuristic. Everything the sequence contains that the count does not —
ordering, run length, the specific pattern of alternation — contributed nothing measurable
on this data.

That is a real finding about the problem, not a failure of the model. It says the predictive
content of a test's history, at this data volume, is roughly its failure rate. It also
tells you that the order-dependent flakiness from phase 03 is not visible in a single test's
own history, which is consistent: a test that only fails after a particular neighbour
cannot be predicted from its own sequence at all.

## What to do with it

Remove the component, or keep it and be honest that it is a costly reimplementation of one
line. The original build withdrew it. Either is defensible; quietly keeping it and reporting
0.782 as a modelling achievement is not.

The reason to run the control before the model is that this conclusion is unreachable
afterwards. Having spent a day on an LSTM, nobody voluntarily builds the one-line thing that
makes it redundant.

## The degenerate variant

A GRU configuration reported **ECE near zero with AUC near chance**. Perfectly calibrated
and completely useless: it emits the base rate for every input, so its probabilities are
honest and its ranking is random.

This is the phase 02 two-model question arriving in the wild, wearing a more convincing
costume. ECE alone would have called it the best-calibrated component in the system.

Any calibration number quoted without a discrimination number beside it is unreadable.
