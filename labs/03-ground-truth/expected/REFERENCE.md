# Reference — read after your attempt

## The procedure

Run each test many times on identical code. If it both passes and fails, it is flaky. If it
always fails, it is a deterministic failure. If it always passes, it is not interesting.

## The asymmetry

A rerun that **flips** is proof. The code did not change and the outcome did, so
non-determinism exists. This direction is sound.

A rerun that **does not flip** is not proof. It is absence of evidence at whatever sample
size someone happened to choose. A test that is flaky one time in five hundred will look
perfectly deterministic across a hundred reruns.

## The direction of the bias

The **positive class is clean** — everything labelled flaky really is flaky, because it was
caught flipping.

The **negative class is contaminated** — it contains genuinely deterministic tests *and*
rare-flaky tests that did not flip often enough to be caught. The rarer the flakiness, the
more likely it sits in the negatives.

The discovery curve from large rerun campaigns keeps rising rather than flattening. New
flaky tests keep appearing as reruns increase, which is what a contaminated negative class
looks like from the outside.

## What that does to your measurements

Your model gets penalised for correctly flagging tests the labels call clean. Measured
precision is therefore a **lower bound** on true precision. When a model looks mediocre
here, some of that is the labels, not the model — and you cannot say how much, which is a
known-unknown and belongs in your `knowns/` file as exactly that.

This is also why you should be suspicious of any result on this data that looks excellent.

## Two more sources of non-determinism worth knowing

A test that leaves a file behind, and a test that only fails in a particular order relative
to its neighbours. Both are real, both are order-dependent, and neither is visible in a
single test's own history — which is a hint about what a single-test model can and cannot
see, cashed in during phase 07.

## The price

Reruns are the only way to buy certainty and they scale with suite size times rerun count.
For a real Java project this runs into thousands of CI hours. Ground truth here is an
experimental result with a budget attached, not a fact you look up.

That is the sentence to carry forward: **the labels are an experiment someone ran, at a
sample size someone chose, and you inherited both.**
