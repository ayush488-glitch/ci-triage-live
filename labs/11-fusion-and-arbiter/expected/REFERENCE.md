# Reference — read after your attempt

## The comparison

This reference comparison used one aligned split (n_train 55 / n_calibration 55 /
n_test 74), with majority baseline **0.5676**. These rows are rankable because every
strategy completed on the same test cases; do not rank an incomplete strategy.

| strategy | accuracy | ECE | Brier | beats majority |
|---|---|---|---|---|
| `fuse_best_single` | 0.9054 | 0.0905 | 0.0852 | yes |
| `fuse_weighted` | 0.9054 | 0.1015 | 0.0633 | yes |
| `fuse_stacking` | 0.9054 | 0.1426 | 0.0636 | yes |
| `fuse_llm_calibrated` | 0.7838 | 0.1058 | 0.1555 | yes |
| **`fuse_llm_naive`** | **0.4324** | **0.4582** | 0.4025 | **no** |

Total LLM cost for the comparison: **$0.4237**.

Three cheap strategies tie exactly at 90.54%. The naive LLM fusion is **below the majority
baseline on accuracy and five times worse on calibration**. Being worse on both at once is
diagnostic: a merely mistaken model tends to be miscalibrated in one direction, while one
that is worse on both is confidently wrong about cases it has no basis to judge.

Calibrating its output lifts accuracy to 78.4% and ECE to 0.106 — a large improvement, and
still last place.

Note also that the three cheap strategies tie on accuracy and differ threefold on ECE
(0.0905 / 0.1015 / 0.1426). Accuracy alone would have called them identical. If you pick by
accuracy you are picking at random among them.

## Why

Print the prompt. In the reference run, the rendered arbiter prompt contained the three
observers' *labels* and none of the *evidence*. The model was asked to adjudicate between
three words. It produced confident, fluent, well-structured reasoning over nothing at all,
which is precisely what a language model does when given nothing at all.

This is trap #12, and the habit it should install is: **before you interpret any LLM
component's result, print the exact string it received.** Not the template. The rendered
string. This one habit catches more LLM-system bugs than any other single practice.

## The other two traps

**False consensus from a single observer (trap #10).** The first pipeline demo returned
unanimous agreement on every case. Only one observer was actually populated; its value was
being copied into the other slots. Unanimity looked like the system working. Test that the
observers are distinct before trusting agreement.

**Mean fusion diluting a real observation (trap #11).** One observer correctly detected a
pass/fail flip — genuine, decisive evidence of flakiness. Three other observers had nothing
to say. The mean averaged one strong true signal with three uninformed ones and erased it.

Averaging assumes every input is an independent estimate of the same quantity. When one
observer has decisive evidence and the others have none, that assumption is false, and the
mean is the wrong aggregation. This is where phase 10's "absence is not uniformity" rule
earns its place: had the uninformed observers been encoded as *absent* rather than as
uniform distributions, the mean would have had nothing to dilute with.

## The arbiter rules

1. **It sees evidence, never labels alone.** If the prompt does not contain what the
   observers actually read, the arbiter is guessing with extra steps.
2. **It escalates, it does not overrule.** An arbiter that can silently reverse a calibrated
   observer removes the only component whose numbers you trust.
3. **Its output is marked uncalibrated** unless it has been calibrated and measured. By
   phase 10 rule 1, downstream has to know.

A fourth is worth adding: it runs only on disagreement. That is where the cheap components
have run out, it is a small fraction of traffic, and it is the only place its cost is
justified.

## What this says about the design

The most capable component in the system is the worst-performing one, and it is the most
expensive. That is not an argument against language models. It is an argument for measuring
before deploying, and for the cost ladder in phase 12: capability is not free, and it is not
automatically better.

Three cheap strategies tie at 90.5%. Ship one of those. Use the model where it is actually
better than the alternatives — explanation, in phase 12 — rather than where it is most
impressive to say you used it.
