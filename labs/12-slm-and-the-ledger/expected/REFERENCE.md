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

Phase 11 gave you the evidence: as a decider, the language model came last, and was worse
than the majority baseline on both accuracy and calibration. Its role is **explanation** —
turning a verdict plus its evidence into something a human can read at 02:47.

That is a genuine capability nothing else in the system has, and it is a job where being
wrong is recoverable, because a human reads it.

There is a second reason. Training a decider on this data teaches the model the skewed label
distribution, and a model that has learned "almost nothing is flaky" produces exactly the
degenerate behaviour phase 02 warned about.

## Distillation — the purchase before the purchase

There is no labelled explanation corpus. You have to make one, by having a strong model
label cases — distillation. The real run:

```
1,436 of 1,440 candidates labelled     $9.586 total     $0.00668 per call
zero parse failures
```

The cost came in **~2.5x over the estimate**. Two reasons: the labeling model ran adaptive
thinking by default, so output tokens ran 300+ per call rather than
the ~193 assumed; and the estimate had been taken from a short synthetic case, while real
prompts carry real stack traces and real per-observer evidence. **Price on a rendered
prompt, never a toy one.**

There is a second cost lesson here. The per-token rate for the labeling model could not be
verified — the public pricing page did not list the model, and the hosted rate is known to
differ from the first-party rate by roughly 2x for the same model era. The rule that was
followed: **never hardcode a rate you have not verified.** A stand-in rate was used, and the
fact that it was a stand-in was written down. A wrong hardcoded price silently corrupts
every cost number in the system while looking perfectly correct.

And the finding that decides everything downstream:

```
labeler outputs: 1,376 FLAKY / 60 NOT_FLAKY  (95.8%)
```

The labeler output is massively skewed — and it is skewed because of a design detail, not by
accident: this corpus's retrieval observer was still using an older label mapping, so the
labeler was partly answering a different question than the one the fine-tuned model faced.

Either way, the majority baseline is **~95.8%, not 50%**. A model scoring 94% here is worse
than a constant predictor.
Phase 02, arriving again, four phases later, in a place nobody expects it.

## A reference run after the gate

This run passed its written go condition and is an example, not an instruction to fine-tune.
If your majority and TF-IDF gate does not justify a GPU run, stopping is the correct result.

LoRA r=8/alpha=16 on `q_proj`/`v_proj`, Qwen2.5-Coder-3B-Instruct, one RTX 4090. The
minority class was **oversampled 12x** so the model saw ~34% NOT_FLAKY rather than 4%.
First attempt OOM'd at batch size 4 — the vocab-driven `logits.float()` upcast alone is
~2.3 GB — fixed with batch size 1, gradient accumulation 8, gradient checkpointing.
Training converged cleanly: loss 1.248 → 0.494 → 0.167 → ~0.13. Adapter 7.4 MB. ~11 minutes.

Evaluated on 189 held-out examples, majority baseline **95.24%**:

```
model accuracy       95.24%   (180/189)   beats_majority: FALSE
predictions          FLAKY 189   NOT_FLAKY 0
```

It **exactly ties the majority baseline** by predicting FLAKY on every single case.

Then the slice that settles it — 116 tests that are genuinely deterministic, where the
correct answer is NOT_FLAKY every time:

```
model accuracy       0.0%   (0/116)
predictions          FLAKY 116   NOT_FLAKY 0
```

**Zero.** Not one right.

## What the clean training loss was measuring

Loss fell smoothly and converged. That is real — the model learned the JSON output format
and the corpus's class bias very well. Neither is per-case discrimination.

A converging loss curve tells you the model is fitting *something*. It never tells you what.

## The pattern, confirmed six times

Every approach tried against this corpus collapsed to the majority class:

1. tabular XGBoost's isotonic calibrator (TRAP #14)
2. the MLP's isotonic calibrator (TRAP #14)
3. the sequence LSTM converging to the trivial heuristic (phase 08)
4. zero-shot Qwen2.5-Coder-3B
5. few-shot Qwen2.5-Coder-3B
6. the LoRA fine-tuned model

Different model classes, different calibration methods, different training techniques, same
failure. The common factor is not any component's design: **only 51–60 real NOT_FLAKY
examples exist in the entire corpus.**

Six independent architectures failing identically is strong evidence the ceiling is **data
volume, not modelling choice**. That conclusion is unavailable from any one experiment. It
only exists because six were run and all six were reported.

## The verdict

The SLM does not earn its place on this corpus as built. The route to a real yes is not a
different model or a better recipe — every recipe hit the same wall. It is more NOT_FLAKY
training data.

Which is a decision about **buying evidence**, not about modelling, and it costs money you
can now estimate: you know the per-call price and roughly how many labels you need.

## What you should have written before spending anything

The abandonment condition. Without it, 95.24% becomes a training problem to debug
indefinitely instead of an answer. With it, the run is 11 minutes and $9.59 and produces a
finding you can defend.
