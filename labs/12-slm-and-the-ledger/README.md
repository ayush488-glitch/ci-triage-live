# Phase 12 — does the fine-tune beat the boring baseline?

```
Fusion -> [Explanation] -> Handoff
```

Every component so far outputs a verdict and a probability. None of them says *why*. An
engineer at 02:47 with "flaky, 0.83" still has to go and read the logs.

Test whether a small language model can explain this system's outputs.

Before you rent a GPU, work out the memory and training-data costs, measure the majority and
cheap text baselines, and define the stop gate. Fine-tuning is optional evidence-gathering,
not an automatic next step.

## What this phase is

Half arithmetic, half a hypothesis you have to be willing to lose. The arithmetic is the
part that transfers: knowing which line of the memory ledger each technique attacks is the
difference between choosing LoRA and repeating that LoRA is good.

## What you will produce

`experiments/12-finetune-vs-tfidf.md` (written before anything runs),
`experiments/12-distillation-cost.md`, `artifacts/results/distill-corpus.json`,
`artifacts/results/slm.json`, `decisions/12-memory-ledger.md`, an `ai-ledger/` entry, and
`knowns/12-slm-and-the-ledger.md`.

No GPU? `precomputed/` has the runs. The hypothesis still gets written first, and the
arithmetic still gets done by hand.

## Time

About 95 minutes.

## Check

```bash
uv run lab.py check 12
```
