# Task

## Design the slice — before anything else

Write `design/13-self-deception-and-handoff.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the operations layer**.

The last slice: invariants, monitoring, alarms, and the evidence store as append-only.

The hard question: **which of your twelve earlier slices would you find out had broken, and
which would fail silently?** Every silent one needs an instrument. That list is the phase.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---


**1. The failure register.** In `FAILURES.md`, four families. For each: at least two concrete
failures, how each would look from the outside, and the instrument that catches it.

- the system lies about its performance;
- the calibrator collapses;
- infrastructure contaminates the result;
- it breaks in operation.

Write it as a prediction. If you find yourself writing up something that already happened,
that is a different document.

**2. Prior work, doubt-first.** In `docs/prior-work.md`: pick five specific doubts you
actually have about your design. For each, record the doubt, the search you ran, what you
found, and **what changed as a result** — including "nothing changed", which is a real
outcome and must be written as such rather than dressed up.

Do not do a general literature review. The doubt comes first; that ordering is the method.

**3. Invariants as tests.** `tests/test_invariants.py`. Everything that must stay true, as
an assertion. At minimum: no leaking column reaches the features; no project spans a split;
the retrieval index has more than one class; every observer declares its calibration state.

A document saying these things is a wish. A test is a guarantee.

**4. Assemble KNOWNS.md.** Create it at the repository root and merge your per-phase
`knowns/` files into one table:

```markdown
| Phase | Was | Now | Statement | Evidence |
|---|---|---|---|---|
```

The known-unknowns column should be the longest one. If it is short, you have not been
honest about what you do not know.

**5. Exit interview.** The coach interviews you across the whole project and writes the
verdict to `.ci-lab/interviews/12.md`. The question being graded: could another engineer
take this, reproduce your evidence, and continue?
