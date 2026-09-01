# Prompts to adapt

```text
Before we build anything: I want a control for a sequence model over test run
histories. Propose the cheapest possible predictor that uses the same
information and no training. One function, no class.
```

```text
Build test-run sequences from this frame, ordered by time, one sequence per test.
Then write a test that fails if any sequence element comes from after the
prediction point. The test is the deliverable; the builder is incidental.
```

```text
Here are per-fold AUCs for my LSTM and for a failure-count heuristic (paste
them). Do not summarise. Tell me whether these two are distinguishable, and what
evidence would settle it.
```

```text
My GRU reports ECE 0.004 and AUC 0.51. Explain what the model is emitting.
```
