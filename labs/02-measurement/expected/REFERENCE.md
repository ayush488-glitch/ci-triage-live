# Reference notes

## The constant model

Predicting the majority class on a dataset with about 3.157% positives gives roughly 94.4%
accuracy, precision undefined or zero, recall exactly zero, F1 zero. Every alert it raises
is correct, because it raises none.

This is the number every later result must beat, and it is why the baseline comparison is a
requirement rather than a courtesy.

## The ladder, and what each rung is for

**ROC AUC** — the probability that a randomly chosen flaky case is ranked above a randomly
chosen non-flaky one. It is threshold-free. It answers "does this thing order cases
correctly", which is the right question when you have not yet chosen a threshold.

**Precision and recall** — threshold-dependent, and the pair you need once you have. Of
what we flagged, how much was right; of what was there, how much did we catch. On a rare
class these move violently with the threshold, which is exactly why AUC is reported first.

**ECE** — take the cases where the model said 80% and ask how many were actually positive.
Average the gap across bins, weighted by bin size. It says nothing about ranking. A model
that outputs the base rate for every case has near-perfect ECE and is worthless.

**Brier** — squared error on the probability. One number that moves with both calibration
and discrimination, which makes it useful as a summary and useless as a diagnosis.

**Cost-weighted risk** — your lab 01 table, applied. This is the objective. Everything
above it is a diagnostic.

**Coverage and risk–coverage** — once abstention exists, a system has two dials. Risk on
answered cases, and the fraction it was willing to answer. Reporting one without the other
hides the trade entirely: a system that abstains on 95% of cases and is excellent on the
rest has not solved the problem.

## The binning trap

At a 3.157% positive rate, most predicted probabilities cluster near zero. Ten equal-width
bins put nearly every sample in the first bin. The weighted average is then dominated by
one bin where the model is roughly right, and ECE reports a flattering number that reflects
the binning, not the model.

Equal-frequency bins put the same count in each bin and expose the gaps in the sparse upper
range where the decisions actually happen.

On a 3.16%-style clustered distribution the two disagree by roughly **4x**:

```
equal-width   ECE = 0.0287
equal-mass    ECE = 0.1145
```

Same predictions. Same labels. One of those numbers would have gone in a slide.

This is not hypothetical. It is a bug that shipped in the original build of this system and
had to be found and fixed.

## The two-model question

Near-zero ECE with chance-level AUC is a **degenerate** model: it has learned the base rate
and nothing else. It is perfectly honest about knowing nothing. There is nothing to
threshold, so there is nothing to ship.

Good AUC with poor calibration is a model that has learned something and reports it on the
wrong scale. That is fixable, and lab 06 is where you find out what fixing it costs —
which is not nothing.

Ship the second. Calibrate it, and check what calibration did to the ranking.

## The test

```python
def test_constant_predictor_is_accurate_and_useless():
    y = np.zeros(1000); y[:32] = 1          # 3.2% positive
    pred = np.zeros(1000)
    assert accuracy(y, pred) > 0.94
    assert recall(y, pred) == 0.0
```

That single assertion pair is the whole lesson of the phase, and it will keep being true
about every model you build after this.

## A proposal worth rejecting

*"Use F1"*, or *"balance precision and recall"*, or *"oversample the minority class so
accuracy becomes meaningful"*. The last one is the interesting trap: resampling changes the
base rate the model sees, which changes its calibration, which breaks the metric you have
just spent an hour building. It will also interact badly with the
split. Refuse it here and you will not have to unpick it later.
