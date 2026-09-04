# Task

## Design the slice — before anything else

Write `design/12-slm-and-the-ledger.md` using the template in [design/README.md](../../design/README.md):
responsibility, reads, emits, refuses, constraint, connects to.

This phase's slice is **the explanation layer**.

The explanation component. What it receives, what it may say, and what it may never do.

The hard question: **what happens to the explanation when the verdict is wrong?** A fluent
explanation of a wrong verdict is more dangerous than no explanation, because it transfers
the system's confidence to a human who cannot check it.

No code in this phase until this file exists. You decide what the slice is responsible for,
what it may read, what it emits, and when it refuses.

---


**1. Write the ledger by hand.** For a 3-billion-parameter model at 16-bit precision, work
out in `decisions/12-memory-ledger.md`:

- weights;
- gradients;
- optimiser state;
- activations.

Four numbers, with the arithmetic shown. Then the total, and what that means for which GPU
you would have to rent.

**2. Attack a line.** For each technique, say which line it reduces and by roughly how much:
quantisation, freezing the weights and training a small adapter pair, recomputing
activations instead of storing them. Redraw the ledger after each. Then say what you would
actually rent.

**3. Decide the role.** Should this model *decide* or *explain*? You have evidence from
phase 11 about what happens when a language model decides. Write the argument.

**4. The hypothesis, before you spend anything.** In `experiments/12-finetune-vs-tfidf.md`:

- the claim you are testing;
- the baseline you will compare against — the cheapest thing that could possibly work;
- the number that would make you keep going;
- the number that would make you stop.

**4b. Price the training data — distillation.** There is no labelled explanation corpus. You
make one by having a strong model label your cases, and that model's labels become your
training data. This is a purchase, so it gets priced before it is made.

In `experiments/12-distillation-cost.md`, **before spending anything**:

- render **one real prompt** — the actual string, with real evidence in it — and count its
  tokens. Do not estimate from a short synthetic example; real prompts are longer and
  models that think adaptively emit far more output than you expect.
- price per call from a rate you can cite. Never hardcode a rate you have not verified;
  if you cannot verify it, say which rate you are standing in and that it may be wrong.
- multiply by your corpus size. Write the budget and the number that would make you stop.

Only run distillation if the written budget permits it. If it does, write
`artifacts/results/distill-corpus.json` with examples labelled, examples declined, parse
failures, actual total cost, cost per call, and **the label distribution**. Otherwise record
the priced, unrun decision in that JSON and use an existing or precomputed labelled corpus
for the gate.

That last one is not bookkeeping. The labeler corpus's class balance is **the majority
baseline** — not 50%. Work it out and write it down now.

**5. Apply the pre-GPU stop gate.** On one frozen split, run the majority baseline and
TF-IDF plus a linear classifier. Record both before provisioning a GPU. State the minimum
result that would justify fine-tuning; if neither the baseline comparison nor the available
class balance leaves a defensible path to that result, stop and record the no-fine-tune
decision.

**6. Fine-tune only after a written go decision.** If the gate passes, report the fine-tune,
TF-IDF, and majority baseline on the same frozen split in `artifacts/results/slm.json`. If
it does not, record the two baselines, gate outcome, and why no GPU run was warranted.

**7. Say what you would do.** Given the completed comparisons and any stop decision, what
ships?
