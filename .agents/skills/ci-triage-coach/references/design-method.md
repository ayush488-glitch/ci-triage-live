# Design method

Every phase designs one slice of the system. Thirteen slices, and by phase 12 they are the
whole architecture. The student designs the slice; the agent implements behind it.

## Why the design comes first, every time

A component built before its interface exists gets an interface reverse-engineered from
whatever the implementation happened to do. That is how systems end up with observers that
read each other, probabilities nobody knows the calibration state of, and a fusion layer
that cannot distinguish "no evidence" from "evidence pointing everywhere". Every one of
those is a real bug from this build, and every one of them is an interface that was never
designed.

So: `design/NN-<slug>.md` exists before any code in that phase. The gate enforces the file;
you enforce the order.

## The division of labour

This is the point of the whole lab, and it should be visible in every phase.

| The human decides | The agent does |
|---|---|
| what the slice is responsible for | how it is implemented |
| what it may and may not read | the library call, the loop, the data wrangling |
| the shape of what it emits | the tests that check the contract holds |
| the constraint it must never violate | the boilerplate around all of it |
| what it costs and what that buys | making it fast |
| when it should refuse to answer | making it readable |

The left column is not delegable. When a learner asks the agent to decide something in the
left column, that is the moment to stop and interview instead. When the agent volunteers a
decision from the left column, that is the phase's plant, and the learner should catch it.

## What a slice document contains

Six sections. Short — this is an interface, not an essay. Half a page is a good length.

```markdown
# Slice NN — <name>

## Responsibility
One sentence. What this part of the system is for. If it needs "and", it is two slices.

## Reads
Exactly what it is allowed to see. Naming this is what makes independence checkable
later rather than aspirational.

## Emits
The shape of the output, including the fields that are not the answer: calibration
state, confidence, cost, what it read.

## Refuses
What it does when it cannot answer. "It always answers" is a design decision and has to
be defended, not assumed.

## Constraint
The one thing that must never be true. This becomes a test in the same phase.

## Connects to
Which earlier slice it depends on, and which later slice will consume it.
```

`Connects to` is what makes thirteen documents into one architecture. Every phase from 01
onward must name a slice that already exists. If it cannot, either the slice is not needed
yet or something was skipped.

## The running architecture

`docs/architecture.md` is written in phase 09 and updated in 12. It is assembled from the
slice documents; it is not a separate design effort. If a slice contradicts the assembled
picture, the contradiction is the finding — record it rather than quietly editing the older
slice.

## What forces real thinking

Three questions, per slice, in the interview. They are hard to answer without designing:

1. **"What is this slice not allowed to know?"** — Forces the boundary. Most students
   design what a component does; almost nobody designs what it is forbidden to see. This is
   the question that produces the independence rule in phase 09 four phases early.
2. **"What does it do when it cannot answer?"** — Forces the refusal path. A slice with no
   refusal path pushes its uncertainty silently downstream, where it turns into confidence.
3. **"Which earlier slice breaks if you change this one?"** — Forces the coupling to be
   visible while it is still cheap to change.

If a learner answers all three, they have designed the slice. If they cannot answer the
first, they have described an implementation.

## Do not accept a diagram as a design

A box-and-arrow picture with no `Reads`, no `Refuses`, and no `Constraint` is a drawing of
a system, not a specification of one. Ask what each arrow carries and whether the receiving
box is allowed to see it.
