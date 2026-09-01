# Reference — read after your attempt

## The three causes

A red build has three families of cause, and the CI report cannot distinguish them:

1. the change genuinely broke the software;
2. the test is unreliable and would fail again on the same code;
3. the machine, network, or container failed.

## The actions

Three responses, one per cause, plus one more that people actually use:

- stop the release;
- isolate the test and let the release continue;
- run it again;
- wake a human up.

The fourth is real and expensive, and it is the reason abstention will earn a slot in the
output space in phase 01.

## The decision versus the prediction

The decision is what the on-call engineer does at 02:47. The prediction is the system's
estimate of *why* the build is red. They are different objects, they have different
consumers, and confusing them is what produces a model nobody can act on.

## Why flakiness is expensive twice

A flaky test costs once when it fails and someone investigates a defect that does not
exist, and again when it trains the team to ignore red builds — at which point a real
defect ships past a signal everyone has learned to disregard. The second cost is larger and
does not appear in any dashboard.

## What a strong PROBLEM.md contains

The decision with a person and a deadline attached. The four actions. The prediction,
stated separately from the decision. Two costs with rough numbers and an admission that the
numbers are rough. No model, no metric, no dataset.
