# Prompts to adapt

```text
List public datasets for flaky test prediction. For each: publisher, hosting,
licence, and what the licence obliges a user to do. Do not recommend one. If a
dataset has no licence stated, say so explicitly rather than assuming permissive.
```

```text
Here are the columns in this table (paste them). Do not build a model. Tell me
which of these could not possibly be known at prediction time, and which could
only have been computed from the outcome. Explain your reasoning per column.
```

```text
Write the smallest loader that joins these two CSVs and returns one row per test
run. No classes, no config, no caching layer. Then write one test that fails if
a column named in this list (paste it) reaches the returned frame.
```

```text
I dropped a column because I think it leaks. Argue that I am wrong and it is a
legitimate feature. Then tell me what evidence would settle it.
```
