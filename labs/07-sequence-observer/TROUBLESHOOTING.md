# Troubleshooting

**Sequences are mostly length 1** — many tests appear once. Set a minimum history length,
report how many tests met it, and note that the model is only defined on that subset. This
is a real limit on the component, not a preprocessing detail.

**Training loss goes to zero and the model is useless** — you leaked. Check the ordering
test actually runs and actually fails when you break it deliberately.

**The heuristic beats the model** — that is a legitimate result and it is more interesting
than the alternative. Report it.

**Per-fold numbers are identical to several decimal places** — check you are not accidentally
evaluating the same predictions twice. If the pipeline is correct, identical behaviour is
the finding.

**No GPU** — these sequences are short and the models are tiny. CPU is fine.
