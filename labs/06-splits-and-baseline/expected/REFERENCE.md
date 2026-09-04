# Reference notes

## The result

Grouped by project, cross-validated: **AUC ≈ 0.605, standard deviation ≈ 0.102**.
Random row-wise split, same model, same features: **AUC ≈ 0.955, standard deviation ≈ 0.013**.

Majority baseline on the real data: **≈ 94.4% accuracy, zero recall**.

## Where the extra performance came from

Rows from one project share a great deal: naming conventions, framework, test style,
infrastructure, and — critically — the project's own base rate of flakiness. A random split
puts rows from the same project on both sides. The model does not need to learn what makes a
test flaky. It needs to learn which project a row belongs to, and then recall that project's
base rate. That is memorisation, and it is worth about 0.35 AUC here.

The tell is the standard deviation. The leaky number is not just higher, it is far more
stable — 0.013 against 0.102 — because a memorisation task is easy and consistent, while
generalising to a genuinely unseen project is hard and varies enormously with which project
you held out.

## Which split is right

If the system will ever see a project it was not trained on, the grouped split is the only
honest measurement. That is the production situation: new repositories get onboarded, and
the system is expected to be useful on day one.

Note the direction of the temptation. The wrong split is not the one someone chose out of
ignorance — it is the one that produces the number you would rather report. That is why the
deployment question gets answered in writing before either number exists.

## What 0.605 ± 0.102 actually means

It means the model is weakly informative on unseen projects, and the fold-to-fold variation
is large enough that the true value could be materially better or worse. It is not a good
result and it should not be dressed up as one.

Two things follow: get better features, or change the question. Recording this honestly now
makes that choice available later.
Tuning the number up here would have removed it.

## The invariant test

```python
def test_no_project_in_both_sides():
    for train, test in grouped_folds(df):
        assert not (set(df.project[train]) & set(df.project[test]))
```

Leakage across a split is invisible in every metric you have. Only the test catches it.
