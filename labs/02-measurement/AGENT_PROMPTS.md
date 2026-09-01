# Prompts to adapt

```text
Write the smallest possible function that predicts the majority class, and a
scoring call that reports accuracy and recall together. Do not add a class, a
config, or a base estimator. Then tell me what this proves about accuracy on a
3% positive rate.
```

```text
Implement expected calibration error twice: once with equal-width bins and once
with equal-frequency bins. Same signature, one argument selects the scheme. Then
run both on an array where 3% of labels are positive and most predicted
probabilities are below 0.05, and show me the two numbers.
```

```text
Here is my metrics.py (paste it). Run a ponytail pass. Which of these functions
already exists in sklearn and should be deleted?
```

```text
Write me a test for cost_weighted_risk that would fail if I swapped the two cost
constants by mistake. Not a test that it returns a number — a test that catches
that specific bug.
```
