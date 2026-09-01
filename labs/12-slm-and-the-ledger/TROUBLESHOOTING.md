# Troubleshooting

**No GPU** — use `precomputed/`. Write the hypothesis first. The ledger arithmetic is done by
hand either way and is most of the value.

**Out of memory on the GPU you rented** — your ledger was wrong. Go back and find which line
you underestimated. This is the useful failure, not a setback.

**The fine-tune scores below the majority baseline** — that is the real result, but check the
obvious first: label mapping, the split, and whether the model is emitting a constant.
Distinguish "trained badly" from "trained fine and lost". Both are reportable; they are not
the same finding.

**A striking zero-shot number** — check the harness before believing it. A remarkable
zero-shot result in the original build turned out to be a bug in the evaluation harness, not
a property of the model.

**Distillation to build training data is expensive** — price it before running it. The
original build priced it and withdrew it. Withdrawing something on a cost argument is a
legitimate outcome to record.
