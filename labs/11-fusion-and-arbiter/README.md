# Phase 11 — what happens when the LLM arbitrates

```
Observers -> Architecture -> [Fusion] -> Handoff
```

Three observers, three probabilities, one decision. When they agree, easy. When they
disagree — and the disagreement is the interesting case, because it is where the cheap
components have run out — somebody has to resolve it.

The obvious answer in 2026 is: give it to a language model. It can read the logs, weigh the
evidence, explain its reasoning. It is the most capable thing in the system.

You are going to build five fusion strategies and compare them, and the language model is
going to come last. Not last by a little.

## What this phase is

The experiment that decides the architecture, plus three traps from the original build that
are all worth walking into deliberately.

## What you will produce

`ci_triage/fusion.py`, `tests/test_fusion.py`, `experiments/10-fusion-comparison.md`,
`artifacts/results/fusion.json`, `decisions/10-arbiter-rules.md`, an `ai-ledger/` entry, and
`knowns/10-fusion-and-arbiter.md`.

## Time

About 75 minutes. Rubric level 5. This is the last phase covered in class.

## Check

```bash
uv run lab.py check 11
```
