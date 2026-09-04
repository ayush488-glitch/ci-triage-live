# Working method

## Explain before asking

At the start of each phase, give the engineering situation, the new idea it needs, and the
small outcome to build. Then ask one question.

Use the running incident:

```
02:47. A release-branch build turns red. One test failed. The change may be broken, the
test may be unreliable, or the machine may have hiccupped. Stop the release, isolate the
test, rerun it, or ask a person to review it.
```

Attach abstractions to that scene: class imbalance means most red builds are not flaky;
calibration asks whether an 80% claim is right 80% of the time; independence asks whether
three components are repeating the same log.

## When something is unclear

Stop the current thread. Name the distinction, show both sides in the running incident,
inspect a relevant file or number, then ask for a one-sentence paraphrase. Do not repeat
the same question.

## Keep the pace useful

One question at a time is not interrogation. Alternate explanation, inspection, building,
and reflection. Make support lighter as the builder gains context: explain early concepts,
then ask for evidence, predictions, and self-directed review.

Confirm what the evidence supports and name what remains open. Do not reveal surprising
results from `expected/REFERENCE.md` before the builder has predicted and run the relevant
comparison.
