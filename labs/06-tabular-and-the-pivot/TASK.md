# Task

**1. Predict what calibration does.** Before you calibrate anything, write in
`experiments/06-calibration-tradeoff.md`: what will happen to ECE, and what will happen to
AUC. Commit to a direction for both.

**2. Build the observer.** A gradient-boosted tree over the tabular features, on your
grouped split. Report AUC, ECE, Brier, and cost-weighted risk from your phase 02 module.

**3. Calibrate it and measure again.** Same metrics, same folds. Put both rows in
`artifacts/results/tabular.json`. Then explain the direction of each change. If you
predicted wrong, leave the prediction in the file and say why you were wrong.

**4. Face the number.** Your grouped result is weak. In `decisions/06-the-pivot.md`, list
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

**7. Graded interview.** The coach interviews you on everything from phase 00 to here and
writes a scored verdict to `.ci-lab/interviews/06.md`. The phase does not check off without it.
