# Rubric

Score each dimension 0–4. A 2 is functional but incomplete judgement. A 4 is strong
evidence and an explicit trade-off.

| Dimension | What a 4 looks like |
|---|---|
| Problem selection | Closes a real known-unknown from your own `KNOWNS.md` |
| Decomposition | Small scope with explicit non-goals, written before code |
| Hypothesis discipline | Prediction and abandonment condition written before the run, and honoured |
| Control | The experiment could have lost, and you say against what |
| AI usage | Bounded prompts with real context, not a sequence of vague repair requests |
| Holding the line | Caught a plausible AI mistake and can explain the tell |
| ML judgement | Split, metric, threshold and interpretation match the question asked |
| Testing | A test that fails for the real bug, verified by breaking it |
| Simplicity | Small coherent diff; existing components reused; ponytail pass recorded |
| Handoff | Another engineer reproduces the result and knows what is still unknown |

## Automatic rejection

- target leakage;
- selecting on the final test set;
- a number that no command produces;
- a citation to a paper that does not exist;
- deleting a safety check or an invariant test without saying why;
- a submission that does not run.

## What scores well that people do not expect

A refuted hypothesis, kept, with the refutation reported and the scope narrowed in response.
A known-unknown that got larger because you understood the problem better. A component you
removed because you proved it was not earning its cost.

None of those look like progress on a status update. All of them are.
