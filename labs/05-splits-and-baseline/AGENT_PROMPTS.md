# Prompts to adapt

```text
I have test-run rows from 25 projects. Do not recommend a split. List every
splitting strategy that is defensible here, and for each one, state the
production question it corresponds to.
```

```text
Write a grouped cross-validation splitter over the project column using sklearn.
Then write a test that fails if any project id appears in both train and test
for any fold. The test matters more than the splitter.
```

```text
I got AUC 0.60 grouped and 0.95 random on identical model and features. Give me
three explanations for that gap. Rank them by how much I should believe them,
and tell me what would distinguish them.
```

```text
Argue that I should use the random split because it gives a better number.
Make the strongest case you can. Then tell me what that case assumes about
production.
```
