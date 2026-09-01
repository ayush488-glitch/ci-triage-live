# Troubleshooting

**All observers return the same value** — that is trap #1, and the test in step 7 is what
catches it. Check each observer is actually populated before you interpret any agreement.

**The arbiter's output is fluent and confident and wrong** — print the prompt. Almost always
the prompt contains the observers' labels but not the evidence they were derived from, so
the model is reasoning over three words with nothing underneath them.

**API costs are mounting** — cap the number of arbitrated cases and record the cap. Fusion
comparison does not need the whole dataset; it needs enough cases to distinguish five
strategies.

**Calibrating the LLM output helps a lot** — it will, and it still will not be enough.
Report both rows.

**Divergence is undefined on zeros** — Jensen-Shannon is well-defined where KL is not, which
is one of the reasons to pick it. If you picked KL, this is the problem.
