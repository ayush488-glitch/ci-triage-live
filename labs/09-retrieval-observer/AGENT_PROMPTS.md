# Prompts to adapt

```text
I want to retrieve similar past CI failures for a query failure. Do not write an
index class. Give me the smallest thing that embeds, searches, and votes, using
libraries that already exist.
```

```text
What should go into a retrieval index for this task? List what should be in it
and what should be excluded, and for each exclusion say what breaks if I include
it.
```

```text
Write a test that fails if my retrieval index contains only one label class.
Then write a test that fails if a query can retrieve itself.
```

```text
Within one project my precision@5 beats the majority baseline by a wide margin.
Holding out a whole project, it falls below the baseline. Same code. Tell me what
I am entitled to conclude from the pair, and what neither result alone supports.
```
