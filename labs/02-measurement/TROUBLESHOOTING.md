# Troubleshooting

**No `pyproject.toml` yet** — there isn't one. Create it, or use inline script metadata.
The harness itself has no dependencies on purpose; your code is where dependencies start.
`uv add scikit-learn numpy` after `uv init` is the short path.

**`sklearn` roc_auc_score raises on your toy array** — it needs both classes present. At 3%
positives on a short array you may have zero positives. Make the array longer.

**Equal-frequency ECE divides by zero** — bins with no samples. Skip empty bins; do not
count them in the weighted average.

**Your two ECE numbers are identical** — your predicted probabilities are probably spread
uniformly. Make them realistic: heavily concentrated near zero, with a thin tail.

**`check 02` fails on `tests/test_metrics.py`** — the file has to exist at that exact path.
It does not have to pass yet, but a phase that ends with a failing test should have that
recorded in `knowns/`.
