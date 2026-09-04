# Acceptance criteria

The extension is complete only when each dimension below has strong evidence and an
explicit trade-off.

| Dimension | Evidence required |
|---|---|
| Problem selection | Closes a real known-unknown from your own `KNOWNS.md` |
| Decomposition | Small scope with explicit non-goals, written before code |
| Hypothesis discipline | Prediction and abandonment condition written before the run, and honoured |
| Control | The experiment could have lost, and you name what it competed against |
| AI usage | Bounded prompts with real context, not a sequence of vague repair requests |
| Holding the line | A plausible AI mistake was caught and its tell is explained |
| ML judgement | Split, metric, threshold and interpretation match the question asked |
| Testing | A test fails for the real bug, verified by breaking it |
| Simplicity | Small coherent diff; existing components reused; ponytail pass recorded |
| Handoff | Another engineer reproduces the result and knows what is still unknown |

## Automatic rejection

- target leakage;
- selecting on the final test set;
- a number that no command produces;
- a citation to a paper that does not exist;
- deleting a safety check or invariant test without saying why;
- a submission that does not run.

A refuted hypothesis can satisfy the criteria when the refutation is preserved and the
scope is narrowed in response. Removing a component after proving it did not earn its cost
is also a valid result.
