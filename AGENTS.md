# Working agreement for coding agents in this repository

This is a teaching repository. The learner's judgement is the product; the code is
evidence. Optimising for a finished repo at the expense of the learner deciding things
defeats the point.

## You may

- explain a concept, with a concrete case from the running scene;
- map files and show real paths and real output;
- write implementation code, after the design decision is made and recorded;
- write tests, and argue that a test is too weak;
- propose options, clearly labelled as options;
- draft the learner's log entries from what they actually said.

## You may not

- decide what to build;
- decide what a component may read, what it emits, when it refuses, or what constraint it
  holds — those are written by the learner in `design/NN-*.md` before you touch a file;
- write any code in a phase whose `design/` file does not yet exist;
- choose the metric, the split, the threshold, or the architecture;
- report a number that was not produced by a command that was actually run;
- present `labs/*/expected/REFERENCE.md` as the learner's own reasoning;
- let a phase pass without one rejected or narrowed proposal recorded in `ai-ledger/`;
- run an experiment before the hypothesis file exists.

## Writing code

Use the **ponytail** skill on every implementation task. Standard library before a
dependency. One function before a class. No configuration for a value nothing configures.
No abstraction with one implementation. After each code phase, do a ponytail pass and
record in the phase's `ai-ledger` entry what it removed.

`sklearn`, `pandas` and `numpy` are already doing most of this. Write only what they do not.

## Tests

A test that asserts a function returns a float is not a test. Each phase needs at least one
test that fails when the logic is wrong — the leaking column reappears, a project lands on
both sides of a split, the constant predictor is scored as good. Those tests are invariants
and they should outlive every model in this repository.

## Numbers

Every number that appears in a decision, a log, or a document must be traceable to a
command. If you cannot name the command, write that the number is unknown.
