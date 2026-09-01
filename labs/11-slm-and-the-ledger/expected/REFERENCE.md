# Reference — read after your attempt

## The ledger

For a 3B model at bf16, roughly:

| Line | Arithmetic | Size |
|---|---|---|
| weights | 3e9 × 2 bytes | ~6 GB |
| gradients | one per weight, same precision | ~6 GB |
| optimiser state | Adam keeps two moments, often fp32 | ~24 GB |
| activations | depends on batch, sequence length, layers | several GB |

Full fine-tuning is dominated by **optimiser state**, not by the weights everyone quotes.

**Quantisation** attacks the weights line — 4-bit takes ~6 GB to ~1.5 GB — and costs
precision, which shows up as degraded output quality rather than as a crash.

**Freezing the weights and training a small adapter pair (LoRA)** attacks gradients and
optimiser state together, because you only carry them for the adapter. Two low-rank matrices
against a large weight matrix is a small fraction of the parameters, and the two big lines
collapse to almost nothing. This is why LoRA is the technique, and knowing *which lines* it
removes is what lets you predict when it will not be enough.

**Recomputation** attacks activations, trading compute for memory. Take it when activations
dominate, which happens with long sequences.

## Decide or explain

Phase 10 gave you the evidence: as a decider, the language model came last, and was worse
than the majority baseline on both accuracy and calibration. Its role is **explanation** —
turning a verdict plus its evidence into something a human can read at 02:47.

That is a genuine capability nothing else in the system has, and it is a job where being
wrong is recoverable, because a human reads it.

There is a second reason. Training a decider on this data teaches the model the skewed label
distribution, and a model that has learned "almost nothing is flaky" produces exactly the
degenerate behaviour phase 02 warned about.

## The result

| System | Accuracy |
|---|---|
| LoRA fine-tune | **47.6%** |
| majority baseline | 52.4% |
| TF-IDF + linear, same split | **90.5%** |

The fine-tune **collapsed**. It lost to the constant predictor. A TF-IDF classifier that
costs nothing and trains in seconds beat it by more than 40 points.

## What that means

Not "small models are bad". It means this task, on this data, at this volume, is dominated
by lexical features that TF-IDF captures directly, and the fine-tune had 825 positives to
learn from — which is not enough to move a 3B model off its priors in a useful direction.

The transferable rule: **the cheapest baseline runs first, always, and it runs before the
expensive thing exists.** Not because it usually wins, but because when it does win you find
out for the price of a few seconds instead of the price of a GPU-day plus the sunk-cost
reluctance to report the result.

The abandonment condition, written in advance, is what makes reporting it possible. Without
it, a 47.6% result becomes a training problem to be debugged indefinitely rather than an
answer.
