# Prompts to adapt

```text
Fit a gradient-boosted classifier on this grouped split and report AUC, ECE,
Brier and cost-weighted risk per fold and pooled. Use my metrics module. Do not
tune hyperparameters — I want the baseline behaviour, not the best number.
```

```text
Wrap the model in a probability calibrator and re-run the same evaluation on the
same folds. Show me both rows side by side. Do not tell me which is better.
```

```text
My grouped AUC is 0.605 and my per-project AUC is 0.737. Write the sentence I am
now entitled to claim, and the sentence I am no longer entitled to claim.
```

```text
Pooling calibrated probabilities across folds before computing AUC — is that
valid? Explain what it does to the number and under what condition it is wrong.
```
