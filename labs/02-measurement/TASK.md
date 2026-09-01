# Task

**1. Run the constant model.**

Before anything else, write it: a function that predicts "not flaky" for every input.
Score it on a toy array you type out by hand with roughly 3% positives. Report accuracy and
recall together. Look at the two numbers side by side.

**2. Build the ladder.**

For each measurement, write one line saying what question it answers, then implement or
import it:

| Measurement | Get it from |
|---|---|
| accuracy | sklearn |
| ROC AUC | sklearn |
| precision, recall at a threshold | sklearn |
| Brier score | sklearn |
| expected calibration error | write it — with a selectable binning scheme |
| cost-weighted risk | write it — from your phase 01 table |
| coverage and risk–coverage | write it |

Ponytail applies. Anything sklearn already does, do not rewrite. If `metrics.py` is much
past 80 lines, something is being reimplemented.

**3. Both binnings.**

Implement ECE with equal-width bins and with equal-frequency bins. Run both on the same
array at a 3% positive rate. Explain the difference you see. One of them is misleading here
and you should be able to say which and why.

**4. The test that matters.**

At minimum: a test that asserts the constant predictor scores high on accuracy *and* zero
on recall, on the same input. A test asserting a metric returns a float is not a test.

**5. Reject something.**

Coach proposes, you dispose. Record it.
