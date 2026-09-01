# AI use policy

You are expected to use an AI coding agent throughout. The lab is about using one well.

## What that means here

**You read what it writes.** The agent drafts; you review it in four passes before it runs
— does it match my slice, is it correct, is the ML claim valid, does any of it need to
exist. Then you direct one bounded patch. Accepting a diff you did not read is the failure
mode this whole lab exists to prevent.

**The agent proposes. You dispose.** Every phase requires at least one AI proposal that you
rejected or narrowed, with your reason, in `ai-ledger/`. If you accepted everything for a
whole phase, either you were not paying attention or you did not ask for enough.

**The agent may not decide.** Not the metric, not the split, not the threshold, not the
architecture, not whether a result is good enough. Those are the only parts of this work
that are actually yours.

**The agent may not produce evidence.** A number is real when a command produced it. An
agent that describes what a result would probably look like has produced nothing. Ask for
the command, run it, read the output.

**Fluency is not correctness.** The most dangerous failure in this lab is a confident,
well-written, wrong explanation. It happens most often around leakage, calibration, and
anything involving a rare class.

## The ledger

Every phase, in `ai-ledger/NN-<slug>.md`:

```markdown
## Review
1. slice fit   —
2. correctness —
3. ML validity —
4. necessity   —

## Proposed
<what the agent suggested, in enough detail to judge>

## Rejected / narrowed to
<what you decided instead>

## Because
<your reason, in your words>

## Ponytail pass
<what the simplification removed, for code phases>
```

Writing "no suggestion was rejected" is allowed exactly once, in phase 00.

## What honest looks like

Recording a hypothesis that turned out wrong, and keeping it, is worth more than a clean
document where every prediction happened to be right. If you edited a prediction after
seeing the result, say so. Nobody is grading you on being right the first time.
