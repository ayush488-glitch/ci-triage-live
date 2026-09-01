# Phase 12 — does the fine-tune beat the boring baseline?

> **Ahead of the lecture.** This phase covers material from the deck that has not been
> taught yet. Run it if you want to get ahead; the coach will explain from scratch.

```
Fusion -> [Explanation] -> Handoff
```

Every component so far outputs a verdict and a probability. None of them says *why*. An
engineer at 02:47 with "flaky, 0.83" still has to go and read the logs.

So: fine-tune a small language model on this system's own outputs, and have it explain.

Before you rent a GPU, three things. Work out what it will cost — line by line, in memory.
Work out what the *training data* costs, because there isn't any and you have to buy it.
And write down what result would make you not do either.

## What this phase is

Half arithmetic, half a hypothesis you have to be willing to lose. The arithmetic is the
part that transfers: knowing which line of the memory ledger each technique attacks is the
difference between choosing LoRA and repeating that LoRA is good.

## What you will produce

`experiments/11-finetune-vs-tfidf.md` (written before anything runs),
`artifacts/results/slm.json`, `decisions/11-memory-ledger.md`, an `ai-ledger/` entry, and
`knowns/11-slm-and-the-ledger.md`.

No GPU? `precomputed/` has the runs. The hypothesis still gets written first, and the
arithmetic still gets done by hand.

## Time

About 75 minutes. Rubric level 5.

## Check

```bash
uv run lab.py check 12
```
