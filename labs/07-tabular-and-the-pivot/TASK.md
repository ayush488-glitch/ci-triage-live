# Task

## Design the slice — before anything else

Write `design/07-tabular-and-the-pivot.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **observer 1**.

The first observer, to the full slice template. Inputs read, output shape, calibration
state, cost, latency, and its failure mode.

The hard question: **what does this observer do on a project it has never seen?** You are
about to find out that the answer matters enormously. Design the behaviour before you
measure it, so the measurement can contradict you.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses.

---


**1. Predict what calibration does.** Before you calibrate anything, write in
`experiments/07-calibration-tradeoff.md`: what will happen to ECE, and what will happen to
AUC. Commit to a direction for both.

**2. Build the observer.** A gradient-boosted tree over the tabular features, on your
grouped split. Report AUC, ECE, Brier, and cost-weighted risk from your phase 02 module.

**3. Calibrate it and measure again.** Same metrics, same folds. Put both rows in
`artifacts/results/tabular.json`. Then explain the direction of each change. If you
predicted wrong, leave the prediction in the file and say why you were wrong.

**4. Face the number.** Your grouped result is weak. In `decisions/07-the-pivot.md`, list
every honest response:

- accept it and ship a weak component;
- get better features;
- get more data;
- change the question.

Then pick one and say what it costs. One of them is much better than the others here, and
the argument for it comes from your `PROBLEM.md`, not from the metric.

**5. Run the pivot.** Whatever you chose, run it and report the number on the same metrics.

**6. Test.** At least one test that fails if the model is fitted on data that includes the
held-out projects.

**7. Record the review.** Summarise the evidence and decision in
`.ci-lab/interviews/07.md`: what calibration changed, what question the pivot answers, and
which claim the new scope no longer supports.
