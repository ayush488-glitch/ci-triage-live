# Task

## Design the slice — before anything else

Write `design/00-start-here.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the system boundary**.

Draw the boundary. What is inside this system, what is outside it, and who acts on its
output. One diagram or one list — either is fine, but every actor must be a real role
somebody holds at 02:47.

The hard question: **what is this system not allowed to do?** It does not merge the branch.
It does not delete the test. Naming the things it is forbidden from doing is what stops it
quietly becoming an automation project three phases from now.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses. The agent implements behind that.

---


Write `PROBLEM.md`. It answers four questions:

1. **The decision.** What is being decided at 02:47, by whom, and by when?
2. **The actions.** What are the only things that person can actually do? List them.
3. **The prediction.** What does the system estimate? Say why that is not the same thing
   as the decision.
4. **The cost.** What does a wrong answer cost, in each direction? A rough guess with a
   number is worth more than a careful sentence with none.

Then write `knowns/00-start-here.md` with at least one row.

Nothing about models, metrics, algorithms, or datasets goes in either file. If you find
yourself writing "we will use", stop — nothing has been decided yet.
