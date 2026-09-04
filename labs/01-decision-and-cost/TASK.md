# Task

## Design the slice — before anything else

Write `design/01-decision-and-cost.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the external contract**.

The contract the rest of the world sees. For each of your outputs: who consumes it, what
they do differently on receiving it, and what the caller must handle.

The hard question: **what does the caller have to do when the system abstains?** If the
answer is "nothing special", abstention is not wired to anything and you have added an
output that no one acts on.

Do not write code until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses.

---


**1. Derive the output space.**

Start from three outputs. Then find a case the three cannot honestly cover, and say what
the system should emit in that case. Write down what the extra output is *for*, and what
happens downstream when it fires.

Do not start from a list of four. Derive it. In `decisions/01-output-space.md`, show the
case that forced it.

**2. Build the cost table.**

One row per (true cause, system output) pair that leads to a wrong action. For each: what
happens, who pays, and roughly what it costs. Use hours, incidents, or currency — pick one
and stay in it.

Then state two properties of your table:

- is it symmetric, and why not;
- what does the extra output cost, and why is it cheap rather than free.

**3. Write the objective.**

One line: the quantity this system minimises. It is not accuracy. Say why not, using your
own table.

**4. Reject something.**

Record one plausible proposal that is wrong for your context, why you reject it, and the
reason in `ai-ledger/01-decision-and-cost.md`.
