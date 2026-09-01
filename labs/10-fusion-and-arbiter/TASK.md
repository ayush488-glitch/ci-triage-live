# Task

**1. Predict, in writing.** In `experiments/10-fusion-comparison.md`, before you build: rank
your five strategies by expected accuracy and by expected calibration. Say where you expect
the LLM arbiter to land on each.

**2. Measure disagreement properly.** Two observers can output the same label and completely
different beliefs. Compare the distributions, not the labels. Implement a divergence measure
and say why you picked it.

**3. Build five strategies.** At minimum: the most confident wins, a mean, a threshold rule,
one that escalates only on disagreement, and one that hands everything to a language model.

**4. Compare them.** Same cases, same metrics, accuracy and ECE together. Write all five rows
to `artifacts/results/fusion.json`.

**5. Print the prompt.** Before you believe any arbiter result, print the fully rendered
prompt the model actually received and read it. Every character. Paste it into your ledger.

**6. Write the arbiter rules.** In `decisions/10-arbiter-rules.md`: what the arbiter is
allowed to see, what it is allowed to output, and what it is forbidden from doing. Three
rules minimum, each tied to a failure it prevents.

**7. Test for false consensus.** `tests/test_fusion.py` must fail if the pipeline reports
unanimous agreement when the observers are not actually distinct.
