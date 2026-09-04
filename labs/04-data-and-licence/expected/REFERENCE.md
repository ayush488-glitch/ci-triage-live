# Reference notes

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

## The label trap — this is the phase

`test_features.csv` has a column called `flaky`. It is **not** FlakeFlagger's ground truth.

It carries labels from *other* detection tools — iDFlakies and DeFlaker — and exists in the
dataset for the paper's tool-comparison analysis. It has **205 positives, 0.77%**.

FlakeFlagger's actual ground truth is `IsFlaky` in `test_results.csv`, produced by the
~10,000-rerun campaign you reasoned about in lab 03. It has **828 positives**, and
**825 over the joined set — 3.157%**.

The two disagree on **904 tests**.

Training on `flaky` is not leakage and it is not a bug that crashes. It answers a different
question — "would iDFlakies call this flaky" — and produces numbers that cannot be compared
to any published baseline, including the supplied reference results. Nothing warns you. The column
name is the most natural one in the file.

The tell is the rate. You reasoned in lab 03 that a rerun campaign at this scale should
surface a few percent. 0.77% is too low for that, and the gap between 0.77% and 3.157% is
the two tools' disagreement staring at you from the summary statistics.

**How to catch it in general:** when a dataset ships more than one column that could be the
label, the question is not "which is better" but "which procedure produced each one". Phase
03 was about exactly that, and this is where it pays.

## The join is not trivial

The two files disagree on **both** key formats:

```
features:  project='logback'          test_name='ch.qos...janinoeventevaluatortest.block'
results:   Project='qos-ch-logback'   Test='ch.qos...JaninoEventEvaluatorTest#block'
```

Project names differ (short name vs `org-repo`), and test identifiers differ in both
separator and case. Tests rejoin as `testClassName#testMethodName`; projects match
case-insensitively by suffix.

If your row count is far from 26,134, this is why. A join that silently drops rows is the
most common way to get a clean-looking dataset that is missing exactly the cases that
mattered.

## A feature that assumes version history

One feature is defined over changes across versions. This dataset is a snapshot of test
runs and has no version history to compute it from, so the column is constant, null, or
silently wrong. Drop it, and record what it would need — a commit-linked run history — since
that is a real thing somebody could go and get.

## The invariant test

```python
def test_label_column_is_the_rerun_ground_truth():
    df = load_joined()
    assert df.label.sum() == 825
    assert abs(df.label.mean() - 0.03157) < 0.0005
```

Blunt, and it works. If somebody later "fixes" the loader to use the convenient column, the
positive count moves from 825 to something near 205 and the test fails immediately.

## Splitting reruns in time

If the same test appears multiple times, the rows are not independent. Note this now. It is
part of what lab 05 examines.
