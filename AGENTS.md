# Working agreement for coding agents

This repository values the builder's judgment; code is the evidence for it.

## You may

- explain a concept with a concrete case from the running CI incident;
- map files and show real paths and output;
- write implementation after the recorded design decision;
- write tests and identify weak tests;
- propose clearly labelled options;
- draft ledger entries from what the builder actually said.

## You may not

- decide what to build;
- decide what a component may read, emit, refuse, or constrain; those choices belong in
  `design/NN-*.md` before code;
- write code for a phase without its `design/` file;
- choose a metric, split, threshold, or architecture;
- report a number that no command produced;
- present `labs/*/expected/REFERENCE.md` as the builder's reasoning;
- let a phase finish without a rejected or narrowed proposal in `ai-ledger/`;
- run an experiment before its hypothesis exists.

## Writing code

Use the **ponytail** skill for every implementation task. Prefer the standard library,
one function before a class, and no configuration with no user. After each code phase,
record what the ponytail pass removed in that phase's `ai-ledger` entry.

`sklearn`, `pandas`, and `numpy` already cover most common work. Write only what they do
not.

## Tests

Each phase needs one invariant that fails when the logic is wrong: a leaking column returns,
a project lands on both sides of a split, or a constant predictor looks good. These checks
should outlive any one model.

## Numbers

Every number in a decision, log, or document must be traceable to a command. If no command
produced it, mark it unknown.
