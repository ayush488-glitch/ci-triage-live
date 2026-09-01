# Reference — read after your attempt

## Licences

**FlakeFlagger** — Zenodo record 4450723, **CC-BY-4.0**. Usable with attribution.
`test_features.csv` (~6.9 MB), `test_results.csv` (~3.5 MB), `Project_Info.csv`.

**IDoFT** — a large and directly relevant collection of order-dependent and flaky tests,
with **no licence stated at all**. No licence means no permission. It is not "probably
fine". Do not build on it. This would change if the maintainers added a licence, and asking
them is a legitimate move.

The instinct to reach for IDoFT is correct — it is the better-known resource. The lesson is
that the check happens before the download, not after the model is trained.

## Shape

The join lands around **26,134 rows across 25 Java projects**, with roughly **825 positives
— about 3.157%** — and about **23 usable features** after the bad columns come out.

Your numbers should be close. If they are far off, the join key is wrong.

## The two bad columns

**Computed from the label.** There is a column derived from the flakiness outcome itself.
Its correlation with the target is near-perfect, which is the tell. Any model including it
scores beautifully and has learned to read the answer key. Drop it and every variant of it.

**Assumes version history.** One feature is defined over changes across versions. This
dataset is a snapshot of test runs; it has no version history to compute it from. The
column is either constant, null, or silently wrong. Drop it and record what it would need —
a commit-linked run history — because that is a real thing you could go and get later.

## Two label columns

More than one column could serve as the target. They encode different questions: one is
about the test being flaky as a property, one is about this particular run. Your phase 00
decision was about a specific red build at 02:47, which points at the run-level question.

If you picked the other one, that is defensible, but it changes what phase 09 has to do
about the run-versus-case distinction, and you should record that.

## The invariant test

```python
LEAKING = {"<the label-derived column>", ...}

def test_no_leaking_column_in_features():
    X, y, groups = load_features()
    assert not (LEAKING & set(X.columns))
```

This is the most valuable line of code you will write today. Models come and go; this test
protects every one of them.

## Splitting reruns in time

If the same test appears multiple times, the rows are not independent. Note this now. It is
half of what phase 05 is about.
