# Prompts to adapt

```text
Do the memory arithmetic for full fine-tuning a 3B parameter model at bf16 with
Adam. Four lines: weights, gradients, optimiser state, activations. Show the
arithmetic per line. Do not skip to the conclusion.
```

```text
For each of: 4-bit quantisation, LoRA, and gradient checkpointing — tell me which
line of that ledger it reduces, by roughly how much, and what it costs me in
exchange.
```

```text
Before I fine-tune anything: build the cheapest possible baseline for this
classification task using TF-IDF and a linear model, on the same split. I want
that number first.
```

```text
My fine-tune scored exactly the majority baseline on the held-out set, and
predicted the majority class on every single case. Training loss converged
cleanly. Give me a ranked list of explanations and the check for each. Do not
assume the model is fine, and do not assume it is broken either.
```
