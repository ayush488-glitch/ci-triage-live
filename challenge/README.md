# The 90-minute challenge

You have built the system. Now: extend it, alone, in 90 minutes, with an AI agent, and leave
behind something another engineer can reproduce.

This is not a speed-coding exercise. It tests whether you can hold a design decision against
an agent that is faster than you, more confident than you, and wrong in ways that read
convincingly.

## What you have

Your own repository: the observers, the evidence record, the fusion comparison, every
decision file, every hypothesis including the refuted ones, and `KNOWNS.md` — which is where
you should look first, because the known-unknowns column is a backlog you wrote yourself.

## Pick one thing

| Capability | The question your work must answer |
|---|---|
| Cold-start for a new project | How much history does a project need before the per-project model beats the cross-project one? |
| Abstention policy | Which cases should the system refuse to answer, and what does the risk–coverage curve say about where to set it? |
| Arbiter with real evidence | Phase 10's arbiter was starved. Give it the evidence and re-run the comparison. Does it still come last? |
| Rerun harness | Buying ground truth costs money. Build the stopping rule that decides when a rerun is worth it. |
| Per-project thresholds | Should projects with different costs use different thresholds, and does the data support it? |
| Cost and latency ladder | Measure what each tier actually costs and check the escalation invariant holds. |
| Label contamination bound | Phase 03 said the negatives are contaminated. Put a bound on how much. |
| Retrieval outside the 25 | Does the retrieval advantage survive on a project not in this dataset? |

One. A narrow change with strong evidence beats three unfinished ones. If you have a better
idea from your own `KNOWNS.md`, take it — that is the strongest possible choice.

## Before the timer

```bash
uv run lab.py status
uv run pytest
open progress.html
```

Everything should be green. If it is not, fix that first — it is not part of the 90 minutes.

## Starting prompt

```text
I am doing the 90-minute extension challenge on this repository, which I built.
My capability is: <one sentence>.

Do not write code yet. Read PROBLEM.md, KNOWNS.md, AI_USE.md, and the decision
and experiment files relevant to my capability. Then tell me the smallest place
this change fits, using real file paths.

Then propose: the outcome, explicit non-goals, the files that change, the
invariant that must not break, one test that fails if the logic is wrong, one
controlled experiment with a named control, and the command that reproduces it.
Identify anything that needs my judgement rather than your guess. Small enough
to finish and verify in 90 minutes.

Wait for my review before writing anything.
```

## The 90 minutes

| Time | What you do | What you leave behind |
|---:|---|---|
| 0–10 | Find the extension point | Notes with real paths |
| 10–20 | Write the hypothesis **and the abandonment condition** | `experiments/` entry, before any code |
| 20–45 | One bounded patch, reviewed | A small diff |
| 45–60 | The test that catches the real bug | A test that fails when you break the logic |
| 60–75 | Run the controlled experiment | Command, control, result |
| 75–85 | Review: correctness, ML validity, unnecessary complexity | One rejected suggestion in `ai-ledger/`, plus a ponytail pass |
| 85–90 | Decision and handoff | Reproduction steps and remaining risk |

Guidance, not a rule. If the experiment refutes your idea in minute 60, record that and
narrow the scope. A refuted hypothesis honestly reported scores higher here than a vague
success.

## The rules that carry over

1. Inspect before editing.
2. Hypothesis and abandonment condition before the run.
3. One bounded patch, not a conversation of repairs.
4. Review in separate passes: does it fit the repo, is it correct, is the ML claim valid, is
   any of it unnecessary.
5. A test that fails for the real bug, not one that asserts a function returns.
6. A control the experiment could actually lose against.
7. One rejected AI suggestion, with your reason.
8. A ponytail pass over what you wrote.
9. Handoff: reproduction steps and what you still do not know.

## Done when

Another engineer can answer all of these from what you left:

- What operating problem does this solve, and which `KNOWNS.md` row does it close?
- Where does it fit, and why there?
- What invariant does the test protect?
- What did the experiment compare it against?
- What did you observe, and what does it *not* prove?
- What did the agent propose that you rejected, and why?
- Which command reproduces it?
- What is the next unanswered question?

The submission is incomplete if you cannot explain its code or reproduce its numbers.

Read [ACCEPTANCE.md](ACCEPTANCE.md) before you submit.
