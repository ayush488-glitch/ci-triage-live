# Task

## Design the slice — before anything else

Write `design/08-retrieval-observer.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **observer 3**.

The third observer, plus something the other two did not have: a stateful dependency. The
index is a thing that gets built, goes stale, and has contents somebody chose.

The hard question: **who builds the index, when does it refresh, and what is in it?** The
third part of that question is the whole phase.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---


**1. Answer the question first.** Before building: why might retrieval beat a trained model
here? Write two sentences. One about what the index retains that weights discard, one about
what a 3% positive rate does to gradient-based learning.

**2. Decide what goes in the index.** In `decisions/08-index-contents.md`, state explicitly
what is indexed and what is deliberately not. Then answer this before you read further:
*if the index contained only failures, what would the neighbours of a query look like?*

**3. Build it.** A sentence embedding model, a nearest-neighbour search, a vote over the top
k. Ponytail hard here — `sentence-transformers` plus `sklearn`'s neighbours is the whole
component. If you are writing an index class, stop.

**4. Test the thing that actually breaks.** `tests/test_retrieval.py` must fail if the index
contains only one class. That is the invariant, and it is the bug.

**5. Measure against the right baseline.** Precision@k against the majority-vote baseline on
the same queries. Report k, and report what happens as k changes.

**6. Query leakage.** Make sure a query cannot retrieve itself. Check it; do not assume it.
