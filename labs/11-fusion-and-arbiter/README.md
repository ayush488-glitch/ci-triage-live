# Phase 11 — what happens when the LLM arbitrates

```
Observers -> Architecture -> [Fusion] -> Handoff
```

Three observers, three probabilities, one decision. When they agree, easy. When they
disagree — and the disagreement is the interesting case, because it is where the cheap
components have run out — somebody has to resolve it.

The obvious answer in 2026 is: give it to a language model. It can read the logs, weigh the
evidence, explain its reasoning. It is the most capable thing in the system.

Build five fusion strategies and compare only the strategies that completed on the same,
frozen cases. A language-model strategy that is unavailable or incomplete is an unranked
result, not evidence that it won or lost.

## What this phase is

The experiment that informs the architecture, plus three failure modes worth guarding
against explicitly.

## What you will produce

`ci_triage/fusion.py`, `tests/test_fusion.py`, `experiments/11-fusion-comparison.md`,
`artifacts/results/fusion.json`, `decisions/11-arbiter-rules.md`, an `ai-ledger/` entry, and
`knowns/11-fusion-and-arbiter.md`.

## Time

About 75 minutes.

## Check

```bash
uv run lab.py check 11
```
