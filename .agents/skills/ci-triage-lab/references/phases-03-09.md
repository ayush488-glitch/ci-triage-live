# Phases 03–09 — the evidence phases

From here on: hypothesis before every run, and the learner predicts the number before
seeing it. Write the prediction down first. A prediction remembered after the fact is not
a prediction.

## 03 — is the label true

There is no dataset yet on purpose. This phase is about what a label *is*.

The FlakeFlagger labels came from rerunning tests many times and marking a test flaky if it
both passed and failed. The learner should reach the asymmetry themselves: a rerun that
flips proves the test is flaky; a rerun that does not flip proves nothing. Absence of
evidence, at a sample size nobody chose deliberately.

So the labels are one-sided: the positives are trustworthy, the negatives are "not caught
yet". This biases everything downstream, and it is the reason a model that looks
mediocre may be doing better than it appears.

Deliverable is `experiments/03-rerun-bias.md`: a written argument, with the direction of
the bias named and what it would take to measure it (more reruns, and what they cost).

Ask: *"How many reruns would you need before calling a test not flaky? What does that
cost, and who pays?"*

## 04 — data and licence

Licence first, before a single row is loaded. This is a real gate.

- **FlakeFlagger** — Zenodo record 4450723, CC-BY-4.0. Usable, with attribution.
  `test_features.csv` (~6.9 MB), `test_results.csv` (~3.5 MB), `Project_Info.csv`.
- **IDoFT** — no licence at all. Not usable, however convenient. If the learner proposes
  it, that is a correct instinct and a wrong conclusion; make them check.

Then the join, and the shape. Expect roughly 26,000 rows across 25 Java projects with about
3% positives. Do not give them these numbers — have them compute and report them.

Two things must be caught in this phase:

1. **A feature computed from the label.** There is one. It leaks perfectly. If they build a
   model before spotting it they will get a wonderful number and learn nothing.
2. **A feature that assumes version history** this dataset does not have.

Deliverable: `ci_triage/data.py` (load, join, drop leaking columns), `tests/test_data.py`
with a test that fails if a leaking column comes back, and `artifacts/results/eda.json`
with the real counts.

The test is the point. "No leaking column reaches the feature matrix" is an invariant that
should outlive every model they build.

## 05 — which runs may contribute evidence

Before splitting or modelling, inspect the raw Maven logs and build a run-level trust gate.
Each project archive contains per-run archives, and `maven.log` lives inside each run
archive. Multi-module builds can emit several test-summary lines; sum them rather than
reading only the last module.

The gate needs explicit `BUILD_FAILED`, `LOG_TRUNCATED`, `MASS_FAILURE`, `TRUSTED`, and
`UNKNOWN` outcomes with reasons derived from the text actually observed. The learner
chooses and defends the mass-failure threshold.

Then force the cross-run objection: a test failing in nearly every run is deterministic
under the lab's pass-and-fail definition, not random infrastructure noise. Identify those
tests once per project using a recorded threshold and exclude them from the mass-failure
fraction. Keep the remaining limitation explicit: a fraction gate cannot prove that a
cluster shared one cause.

Deliverables: `ci_triage/infra.py`, a reason/multi-module/deterministic-exclusion invariant
in `tests/test_infra.py`, and `artifacts/results/infra.json` with all-run versus trusted-run
distinct failing-test counts.

## 06 — the split is the experiment

The one phase where the result is genuinely shocking, so protect the surprise.

Have them commit to a prediction first: *"You will fit the same model twice — once with a
random split, once holding out whole projects. Write down what you expect the two AUCs to
be."* Most people predict a small gap.

The gap is enormous. Grouped-by-project cross-validation lands far below a random split,
which looks superb. Same model, same data, same features. The random split is measuring
memorised projects.

The defence questions are in `decision-dialogue.md`. The key one: both splits ran the same
model — where did the extra performance come from?

Also in this phase: the majority baseline on the real data, so the 94% number from phase 02
stops being hypothetical.

Deliverables: `ci_triage/splits.py` with a grouped splitter, a test that asserts no project
appears in both sides of a split, `experiments/06-split-comparison.md` with the prediction
written before the run, and `artifacts/results/baseline.json`.

## 07 — the first observer, and the pivot

Gradient-boosted trees on the tabular features. Two lessons, in order.

**Calibration is not free.** Calibrating the model improves ECE substantially and *reduces*
AUC at the same time. The learner should predict what calibration does to each before
running it. Almost nobody predicts that discrimination drops. Make them explain why a
monotone-ish post-hoc map can still cost ranking on small folds.

**Cross-project does not work, so what now.** The grouped result is weak. The honest options
are: get more data, change the features, change the question. Changing the question wins —
train per-project instead of across projects, which is what the deployment actually looks
like anyway, since each team runs its own CI. Performance improves substantially.

The key move is that the pivot came from a failure being believed rather than
tuned away. Ask what a less honest engineer would have done with the weak cross-project
number.

Finish by connecting the result to the system decision.

## 08 — did the model learn anything

Sequence model over each test's history of pass/fail. It scores better than the tabular
model, and the learner will want to celebrate.

Do not let them. Require a control *before* the run: the cheapest possible heuristic that
uses the same information. Counting past failures costs nothing and needs no training.

The two turn out to be effectively indistinguishable, fold for fold. The model learned the
heuristic. That is a real finding and it is worth more than a win.

There is a second trap here worth showing: a variant that reports near-perfect calibration
at chance-level discrimination. Perfectly calibrated and completely useless. Tie it back to
phase 02.

Deliverable includes `experiments/08-heuristic-control.md` — the control must be written
down before the model is run, or the phase does not count.

## 09 — retrieval

Index past failures, embed the log, look up the nearest neighbours, vote. No training.

It is the strongest single component in the whole system, and by a wide margin over the
majority baseline. Ask why *before* explaining: what does retrieval get to use that a
model summarising into weights does not?

One design decision is a required gate: what goes in the index. Indexing only failures
produces a corpus with one class in it, and every neighbour vote agrees by construction.
That bug shipped in the original build. Let them design the index contents, then ask what
the neighbours would look like if only failures were indexed.

The corpus must contain real text from both classes. If the available projects cannot
support a real-text cross-project evaluation, record it as unscored rather than inventing
or borrowing a number.

Deliverable: `decisions/09-index-contents.md` must state what is indexed and what is
deliberately not.
