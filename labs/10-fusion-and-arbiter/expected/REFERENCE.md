# Reference — read after your attempt

## The comparison

Three cheap strategies all land at **90.5% accuracy**. `fuse_llm_naive` — hand everything to
the model and take its verdict — lands at **43.2% accuracy with ECE 0.458**. The majority
baseline on the same split is **52.4%**.

The LLM fusion is worse than the majority baseline on accuracy *and* far worse on
calibration. Being worse on both simultaneously is diagnostic: a model that is merely
mistaken tends to be miscalibrated in one direction; one that is worse on both is confidently
wrong about cases it has no basis to judge.

Calibrating the LLM output lifts it to **78.4%**, which is a large improvement and still
last place.

## Why

Print the prompt. In the original build, the rendered arbiter prompt contained the three
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
mean is the wrong aggregation. This is where phase 09's "absence is not uniformity" rule
earns its place: had the uninformed observers been encoded as *absent* rather than as
uniform distributions, the mean would have had nothing to dilute with.

## The arbiter rules

1. **It sees evidence, never labels alone.** If the prompt does not contain what the
   observers actually read, the arbiter is guessing with extra steps.
2. **It escalates, it does not overrule.** An arbiter that can silently reverse a calibrated
   observer removes the only component whose numbers you trust.
3. **Its output is marked uncalibrated** unless it has been calibrated and measured. By
   phase 09 rule 1, downstream has to know.

A fourth is worth adding: it runs only on disagreement. That is where the cheap components
have run out, it is a small fraction of traffic, and it is the only place its cost is
justified.

## What this says about the design

The most capable component in the system is the worst-performing one, and it is the most
expensive. That is not an argument against language models. It is an argument for measuring
before deploying, and for the cost ladder in phase 11: capability is not free, and it is not
automatically better.

Three cheap strategies tie at 90.5%. Ship one of those. Use the model where it is actually
better than the alternatives — explanation, in phase 11 — rather than where it is most
impressive to say you used it.
