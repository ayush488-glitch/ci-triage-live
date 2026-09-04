# Phases 10–13 — the system phases

## 10 — why no observer may read another

Starts with a counting problem, not an architecture diagram. One build produced nearly two
hundred failures. The question "is this test flaky" and the question "should we stop this
release" are different questions at different levels, and conflating them is the first
architectural mistake.

Then independence. Three observers agree. Ask whether that is three pieces of evidence.
If two of them read the same log, it is not — it is one observation counted twice, and
averaging their probabilities makes the system *more* confident on the basis of nothing.

The rules that fall out, which the learner should derive rather than receive:

1. Every observer reports a calibrated probability, or is explicitly marked uncalibrated.
   Downstream must know which.
2. "No evidence" and "evidence pointing everywhere" are different states and must not be
   encoded identically.
3. No observer may read another observer's output. They write to a common record; they do
   not read each other.
4. Cost and latency are measurements the component reports, not constants in a doc.

Deliverable: `ci_triage/contracts.py` — the evidence record every observer writes — plus a
test that fails if an observer's output is missing its calibration flag, and
`docs/architecture.md`.

Finish by connecting the independence argument to the system decision.

## 11 — fusion and the arbiter

Five ways to combine the observers, compared as an experiment rather than chosen by taste.
Freeze one case list first. A strategy is rankable only when it finishes every frozen case
with the same labels and metrics. Timeouts and partial LLM runs are recorded as incomplete,
not extrapolated into a five-way ranking.

Three traps from the original build, all worth reproducing:

- **False consensus from a single observer.** The first pipeline returned unanimous
  agreement because only one observer was actually populated and its value was copied.
  Test for it: assert the observers are distinct before trusting agreement.
- **Mean fusion diluting a real observation.** One observer correctly saw a pass/fail flip.
  Averaging it with three uninformed observers erased it. Ask when averaging is the wrong
  aggregation.
- **An arbiter with nothing to reason over.** The rendered prompt contained the labels but
  not the evidence. It produced fluent, confident, ungrounded output. Have the learner
  print the actual rendered prompt before believing any arbiter result. This is the single
  most transferable habit in the phase.

The escalation rule and the disagreement threshold come after the comparison, not before.

## 12 — the fine-tune and the ledger

Two halves.

**The ledger.** Before renting anything: work out what it costs to hold a small model in
memory. Weights, gradients, optimiser state, activations. Then which line each technique
attacks — quantisation hits weights, freezing and training a small adapter pair hits
gradients and optimiser state, recomputation trades compute for activations. The learner
does the arithmetic themselves. It is the difference between choosing LoRA and repeating
that LoRA is good.

**The gate.** Price distillation first, including one fully rendered real prompt. On one
frozen split, run the corpus-majority baseline and TF-IDF before provisioning a GPU. The
learner must write the prediction, go condition and abandonment condition before spending
anything — that is the whole point of `experiments/12-finetune-vs-tfidf.md`.

If the gate does not justify a GPU, stopping is the result: record both baselines and the
no-fine-tune decision in `artifacts/results/slm.json`. Fine-tune only after a written go
decision, then compare all three results on the same frozen split.

If there is no GPU budget, `precomputed/` has the runs. Using them is fine; fabricating a
number is not. The hypothesis must still be written first, and the ledger arithmetic done
by hand.

## 13 — self-deception, prior work, and the handoff

The exit phase.

**Write the failure register before the failures.** Four families: the system lying about
its performance, the calibrator collapsing, infrastructure contaminating the result, and
the thing breaking in operation. For each, the instrument that would catch it. This goes in
`FAILURES.md` and it is written as a prediction, not a post-mortem.

**Prior work, in the right order.** Reading the literature first produces a design that
copies a paper. The order that works: design until you have a specific doubt, then search
for that doubt. `docs/prior-work.md` records the doubt, the query, what was found, and
what changed — including "nothing changed", which is a legitimate outcome and must be
recorded rather than dressed up.

**Assertions rather than documentation.** Anything that must stay true goes in
`tests/test_invariants.py`. A document saying no leaking feature may be used is a wish; a
test that fails when one appears is a guarantee.

**KNOWNS.md.** Assemble the per-phase knowns files into one table. The known-unknowns
column is the most valuable part of the handoff and should be the longest.

Then the handoff question: can another engineer take this system, reproduce the evidence, and
continue. If the answer is no, name what is missing rather than passing them.
