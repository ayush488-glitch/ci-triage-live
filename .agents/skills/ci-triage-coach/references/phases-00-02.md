# Phases 00–02 — the design phases

No model is trained in these phases. Nothing is downloaded. If the learner starts writing a
pipeline, stop them: nothing has been decided yet.

## 00 — the decision at 2:47am

Open with the running scene, not with the repository. The whole phase is one move: from
"a test failed" to "somebody has to do something".

Get them to name the three causes (the change broke it, the test is unreliable, the machine
hiccuped) and notice the report is identical in all three. Then the actions: stop the
release, isolate the test, run it again.

They write `PROBLEM.md`. It must contain the decision, who makes it, and when. Not a model,
not a metric, not a dataset.

Watch for: naming the *prediction* (flaky or not) as the decision. It is not. The decision
is what a human does at 02:47 with a red build.

## 01 — the output space and the cost table

Three outputs are the obvious answer. Push until they find the case the three cannot cover:
the system genuinely does not know, and guessing costs more than asking. That is where
ABSTAIN comes from — it is derived, not assumed. Do not hand it over; ask what the system
should output when the evidence is thin, and wait.

Then the cost table. Two entries carry the phase:

- A defect ships because the system said "flaky". Cost: a bad release, found by users.
- A release is delayed because the system said "real defect" on a flaky test. Cost: hours
  of engineer time and a slipped deadline.

They are not equal, and the learner has to say which is worse *and* why, in this
organisation, with a number attached even if the number is a guess. A guessed number that
is written down can be argued with. A missing number cannot.

Two properties they should notice without being told: the cost table is asymmetric, and
ABSTAIN has a cost too — it is not free, it is cheap.

Close by pointing out what has just happened: the objective is now cost-weighted risk, and
accuracy is not it. That is the bridge into 02.

## 02 — measurement

The biggest of the early phases. The learner builds `ci_triage/metrics.py` and a test file,
and nothing else.

Order matters. Do not start with metric names. Start with: *"Somebody hands you a system
and says it is 94% accurate. What do you ask them?"*

Then the constant model. It predicts "not flaky" for every row. On this dataset that is
about 94.4% accurate and catches nothing. This has to be *run*, not asserted — a four-line
function in their own metrics module, on a toy array they type out.

The ladder they should end up with, and why each rung exists:

| Metric | The question it answers |
|---|---|
| accuracy | almost nothing here |
| ROC AUC | does the model rank flaky above not-flaky |
| precision / recall at a threshold | of what we flagged, how much was right; of what was there, how much did we catch |
| ECE | when it says 80%, is it right 80% of the time |
| Brier | squared error on probabilities — one number for both |
| cost-weighted risk | the actual objective from phase 01 |
| risk–coverage | what happens when the system is allowed to abstain |

Two traps to steer into, not around:

1. **The binning trap.** ECE with equal-width bins at a 3.157% positive rate puts almost
   every sample in the lowest bin and reports a flattering number. Equal-frequency bins
   tell a different story. Have them implement both and compare on the same array. This is
   a real bug that shipped in the original build.
2. **Perfect calibration at chance.** A model that outputs the base rate for every case has
   near-zero ECE and zero discrimination. Ask what ECE alone would say about it.

Required test: one that fails if the metric is wrong, not one that checks it returns a
float. The strongest is the constant-predictor test — assert that accuracy is high *and*
recall is zero on the same input.

Ponytail applies here already. `sklearn` gives them AUC, precision, recall and Brier for
free. They should write only what it does not give: ECE with a selectable binning scheme,
and cost-weighted risk from their own table. If their `metrics.py` is longer than about 80
lines, something is being reimplemented.
