# Task

## Design the slice — before anything else

Write `design/10-fusion-and-arbiter.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the decision layer**.

Fusion, escalation, and the arbiter. What triggers each, in what order.

The hard question: **what is the arbiter forbidden from seeing, and what is it forbidden
from doing?** Both halves. An arbiter with no forbidden actions can silently overrule the
one component whose numbers you trust.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---


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
