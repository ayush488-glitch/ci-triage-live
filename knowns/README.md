# knowns/

One file per phase: `NN-<slug>.md`. What moved, and on what evidence.

```markdown
# Phase NN

| Was | Now | Statement | Evidence |
|---|---|---|---|
| unknown | known | the grouped split scores far below a random split | artifacts/results/baseline.json |
| unknown | known-unknown | we cannot separate label contamination from genuine difficulty | — |
```

Three states. **known** needs a file or a command in the evidence column. **known-unknown**
is a gap you have named and cannot currently close, and it is the most valuable column in
the whole repository. **unknown** does not appear here, by definition.

Moving something from unknown to known-unknown is progress and should be logged as such.
