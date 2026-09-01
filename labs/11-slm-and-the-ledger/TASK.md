# Task

**1. Write the ledger by hand.** For a 3-billion-parameter model at 16-bit precision, work
out in `decisions/11-memory-ledger.md`:

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
phase 10 about what happens when a language model decides. Write the argument.

**4. The hypothesis, before you spend anything.** In `experiments/11-finetune-vs-tfidf.md`:

- the claim you are testing;
- the baseline you will compare against — the cheapest thing that could possibly work;
- the number that would make you keep going;
- the number that would make you stop.

**5. Run the baseline first.** TF-IDF plus a linear classifier, on the same split. Costs
nothing, takes seconds. Get that number before the fine-tune exists.

**6. Then the fine-tune.** Report both, plus the majority baseline, on the same split, in
`artifacts/results/slm.json`.

**7. Say what you would do.** Given the three numbers, what ships?
