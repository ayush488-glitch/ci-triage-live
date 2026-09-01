# Task

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

The coach will propose at least one thing that is defensible in general and wrong here.
Find it, refuse it, and write the reason in `ai-ledger/01-decision-and-cost.md`.
