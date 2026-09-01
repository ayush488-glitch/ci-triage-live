# Reference — read after your attempt

## The circularity, first

This is the trap, and it is bigger than the heuristic comparison.

`IsFlaky` is **defined** as "this test failed in at least one of ~10,000 reruns of a single
fixed commit". So if you feed rerun outcomes in as features and predict `IsFlaky`, the model
is reading the label's own definition. It scores near-perfectly and has learned nothing.
Nothing in the pipeline warns you; the number just looks wonderful.

The non-circular formulation:

> Given the outcomes of the **first `k` reruns** of a test, predict whether that test fails
> at least once in the reruns **after** the prefix.

Prefix is features, suffix is label, and by construction they never share a run. That
reframing also turns the model into something an engineer can act on — *"after k reruns, is
this test flaky?"* — which is a rerun-budget decision, rather than a tautology.

If your first sequence model scored above 0.9, this is why.

Only runs your phase 05 gate marked CLEAN may contribute an outcome to either half. One
infra-poisoned run can manufacture dozens of failing tests; letting one into a prefix
injects that noise into features and label at the same time.

## The result

Full archive, 16 projects, project-grouped 5-fold CV, LSTM cell, majority baseline 94.4%:

| prefix | model AUC (raw) | heuristic AUC | folds model ahead |
|---:|---|---|---:|
| 5 | 0.6139 | 0.6138 | 1 of 5 |
| 10 | 0.6239 | 0.6239 | 0 of 5 |
| 25 | 0.6391 | 0.6391 | 0 of 5 |

The heuristic is *count the `False` outcomes in the prefix*. No training, no parameters.

Paired sign-flip permutation test at prefix 5: mean per-fold difference **3.6e-05**,
p = 1.0. They are not close. They are the same thing to four decimal places.

## What that means

The LSTM learned the failure count. Ordering, run length, the pattern of alternation —
none of it contributed anything measurable at this data volume.

That is a finding about the problem, not a failure of the model. It also lines up with
phase 03: order-dependent flakiness, where a test only fails after a particular neighbour
runs, is not visible in a single test's own history at all. There is no reason the sequence
should carry more than its rate.

The original build **withdrew the component**. Keeping it and reporting 0.639 as a modelling
result would not have been false, exactly — it would have been a number with the control
left out.

## TRAP #14 — an AUC of exactly 0.5 means two different things

Two of five folds at prefix 50 reported calibrated AUC of exactly **0.5**. From that number
alone it is indistinguishable from "the model learned nothing".

It was not. Re-derived outside the eval pipeline — refit the fold, inspect the isotonic
calibrator's output directly — raw AUC in that fold was **0.57**, and the calibrator, fit on
a small project-disjoint slice, had collapsed to a **single distinct predicted probability**.
All rank information destroyed after calibration.

The model had learned something. The calibrator erased it.

Note the tell: **exactly** 0.5. Genuine absence of signal wanders around 0.5 across folds;
it does not land on it. Compare the raw fold values — 0.767, 0.585, 0.512, 0.682, 0.523 —
against the calibrated ones, where three folds sit on 0.5 precisely.

This is the same "calibration costs discrimination" trade from phase 07 (0.605 raw → 0.542
calibrated), arriving here in its most extreme form: total collapse rather than partial.

The fix is not to stop calibrating. It is to **report both**, always: raw AUC, calibrated
AUC, and the number of distinct calibrated probabilities. A single distinct value is a
collapsed calibrator, and it is a bug, not a result.

## What your four-project run will show

Your absolute numbers will differ — fewer projects, fewer folds, more variance. What should
reproduce is the *shape*: the model and the heuristic tracking each other fold for fold, and
at least one fold where the calibrated AUC collapses to exactly 0.5 while the raw AUC does
not. Report your own numbers, not these.
