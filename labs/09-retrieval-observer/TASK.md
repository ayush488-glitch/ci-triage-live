# Task

## Design the slice — before anything else

Write `design/09-retrieval-observer.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **observer 3**.

The third observer, plus something the other two did not have: a stateful dependency. The
index is a thing that gets built, goes stale, and has contents somebody chose.

The hard question: **who builds the index, when does it refresh, and what is in it?** The
third part of that question is the whole phase.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses.

---


**1. Answer the question first.** Before building: why might retrieval beat a trained model
here? Write two sentences. One about what the index retains that weights discard, one about
what a 3% positive rate does to gradient-based learning.

**2. Decide what goes in the index.** In `decisions/09-index-contents.md`, state explicitly
what is indexed and what is deliberately not. The corpus must contain real text from both
label classes; labels, placeholders, or synthetic text are not a retrieval control. Then answer:
*if the index contained only failures, what would the neighbours of a query look like?*

**3. Build it.** A sentence embedding model, a nearest-neighbour search, a vote over the top
k. Ponytail hard here — `sentence-transformers` plus `sklearn`'s neighbours is the whole
component. If you are writing an index class, stop.

**4. Test the thing that actually breaks.** `tests/test_retrieval.py` must fail if the index
contains only one class. That is the invariant, and it is the bug.

**5. Measure it where the data supports it.** Record the evaluation population, eligible
projects, and skipped projects in `artifacts/results/retrieval.json`:

- **within a project** — index and query the same project, grouped by test method;
- **across projects** — only if enough held-out projects and their training indexes contain
  real text from both classes; hold out a whole project, index the rest, and query it.

Report precision@k and the majority baseline for every completed evaluation. If the
cross-project evaluation is not performable, record why and leave it unscored; do not invent
a cross-project number or reuse a reference result.

**5b. Count distinct tests, not just neighbours.** Five neighbours that are the same test
seen five times are not five opinions. Report the distinct-test count beside k.

**6. Query leakage.** Make sure a query cannot retrieve itself. Check it; do not assume it.
