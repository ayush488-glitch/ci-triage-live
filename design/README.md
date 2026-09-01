# design/

One slice per phase: `NN-<slug>.md`, written **before** any code in that phase.

Thirteen slices. By phase 12 they are the whole system, and `docs/architecture.md` is
assembled from them rather than written separately.

## Template

```markdown
# Slice NN — <name>

## Responsibility
One sentence. If it needs "and", it is two slices.

## Reads
Exactly what this slice is allowed to see.

## Emits
The output shape, including calibration state, cost, and what it read.

## Refuses
What it does when it cannot answer. "It always answers" must be defended.

## Constraint
The one thing that must never be true. It becomes a test in the same phase.

## Connects to
Which earlier slice it depends on, which later slice consumes it.
```

## Who decides what

You decide the responsibility, what it reads, what it emits, when it refuses, and the
constraint. The agent implements behind that and writes the tests that check it holds.

The left-hand column is not delegable. If you find yourself asking the agent what a
component should be allowed to read, stop and design it.

## The slices

| Phase | Slice |
|---|---|
| 00 | system boundary — what is inside, what is outside, who acts |
| 01 | external contract — the four outputs and what consumes each |
| 02 | evaluation component — separate from every model, on purpose |
| 03 | ground-truth source — provenance and what refreshes it |
| 04 | ingestion — source to feature matrix, and where the leak guard sits |
| 05 | experiment harness — how a run is specified and reproduced |
| 06 | observer 1 — tabular |
| 07 | observer 2 — sequence |
| 08 | observer 3 — retrieval, and its index as a stateful dependency |
| 09 | integration contract — the evidence record and the independence rules |
| 10 | decision layer — fusion, escalation, arbiter |
| 11 | explanation layer — what it may say and what it may never do |
| 12 | operations layer — invariants, monitoring, append-only evidence |
