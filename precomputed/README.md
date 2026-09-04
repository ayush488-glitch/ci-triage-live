# Precomputed results

The real runs from the original build, over the **full 17-project archive**. Yours will be
over the three-project subset and will not match — that is expected, and you should say so whenever you
put one of your numbers next to one of these.

| File | What it is |
|---|---|
| `slm-eval.json` | LoRA fine-tune, two held-out slices (phase 12) |
| `fusion-comparison.json` | five fusion strategies, n_test 74 (phase 11) |
| `sequence-eval.json` | LSTM vs failure-count heuristic, four prefix lengths (phase 08) |
| `retrieval-eval.json` | cross-project rotation, per-project + aggregate (phase 09) |
| `flaky-vs-deterministic-scan.json` | class counts per project — the single-class problem (phase 09) |

## The rule

Write your hypothesis **first**. Then run yours. Then open these.

Reading a result before predicting it is not a shortcut, it is the difference between the
lab working and not working. Nobody can tell from your log which order you did it in, which
is exactly why it is on you.

## What each one is good for

If you have no GPU, `slm-eval.json` is how phase 12 gets gated — copy the numbers into your
own results file with a note saying they are not yours. The memory-ledger arithmetic and the
cost estimate in that phase you still do by hand, and they are most of the lesson.

For the other four, run your own on the three-project subset first. Then use these to ask the
more interesting question: **did my three projects show the same shape as seventeen?** Where
they differ, that difference is a finding about sample size, and it belongs in `knowns/`.
