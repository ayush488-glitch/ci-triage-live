# Phase 10 — why no observer may read another

```
Observers -> [Architecture] -> Fusion -> Handoff
```

You have three observers. Before you combine them, two problems.

**One build produced 197 failures.** Is that 197 questions or one question? "Is this test
flaky" and "should we stop this release" are different questions with different consumers,
and a system that answers one while pretending to answer the other is the most common
architectural mistake in this whole design.

**Three observers agree.** Is that three pieces of evidence? Only if they looked at three
different things. If two of them read the same log, unanimity is one observation counted
twice, and averaging their confidence makes the system *more* certain on the basis of
nothing new.

## What this phase is

The first phase with no model in it. You are designing the contract every component writes
to, and the rules that make combining them meaningful. Get this wrong and phase 10's numbers
are uninterpretable.

## What you will produce

`ci_triage/contracts.py`, `tests/test_contracts.py`, `decisions/10-independence.md`,
`docs/architecture.md`, an `ai-ledger/` entry, `knowns/10-architecture-independence.md`,
and `.ci-lab/interviews/10.md`.

## Time

About 60 minutes.

## Check

```bash
uv run lab.py check 10
```
