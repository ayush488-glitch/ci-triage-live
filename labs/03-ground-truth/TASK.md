# Task

## Design the slice — before anything else

Write `design/03-ground-truth.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the ground-truth source**.

The label source as a component with provenance. Where a label came from, what procedure
produced it, at what sample size, and what would refresh it.

The hard question: **what must the system record about a label's provenance so that a
future engineer can discount it correctly?** A label with no recorded sample size is a
number with no error bar.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---


**1. State the procedure.** In `decisions/03-label-procedure.md`, write down exactly how a
label is produced. Not "it was labelled flaky" — the mechanism, including the number of
reruns as an unknown you have to ask about.

**2. Find the asymmetry.** Two outcomes when you rerun a failing test: it flips, or it does
not. Say precisely what each one proves. One of them proves something. The other does not
prove what people use it to prove.

**3. Name the bias and its direction.** Which class is contaminated, and which way? Write it
in `experiments/03-rerun-bias.md` as a claim someone could disagree with.

**4. Price the truth.** How many reruns before you would accept "not flaky"? Multiply by a
guess at the cost of a CI minute, across a real project's test suite. Write the number. It
is going to be large, and that is the point.

**5. Say what it forces.** Given a contaminated negative class, name one thing you must now
do differently in evaluation. This is the sentence that phase 05 will cash in.
