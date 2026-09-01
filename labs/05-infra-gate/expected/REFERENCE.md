# Reference — read after your attempt

## The verdicts

Four, with precedence in this order:

1. **BUILD_FAILURE** — the build did not succeed. Every test outcome in the run is
   meaningless, whatever else is also true.
2. **TRUNCATED** — the log is cut off. Tests that had not run yet look like they failed.
3. **MASS_FAILURE** — an implausible fraction of the suite failed at once.
4. **CLEAN** — none of the above.

Precedence matters because a run often matches several. The reason string is what a future
engineer reads, and `build_succeeded is False` is a more useful thing to be told than
"lots of tests failed", which is the *consequence* of the build failing rather than the
cause.

## The result

Alluxio, 400 runs:

```
CLEAN 275 | BUILD_FAILURE 118 | TRUNCATED 3 | MASS_FAILURE 4

distinct failing tests:  116 using all runs  ->  6 using trusted runs only
```

Roughly a **twentyfold inflation** from infra-contaminated runs. FlakeFlagger reports 116
flaky tests for Alluxio; six survive the gate.

It held from 200 runs to 400. The `commons-exec` control came back 200/200 CLEAN, which is
what tells you the gate is not simply over-triggering — a gate that fires everywhere is not
a gate, and without the control you cannot distinguish the two.

## The trap that passed every test

The original implementation wrote a reason string naming a specific crash signature
**without checking the signature was actually present**. Every verdict was correct. Every
test passed. The headline number was unaffected. And the audit trail was fabricated on
118 of 118 runs.

It was found only because the spec said *report discrepancies rather than adjust
expectations*. The root cause was a transcription error one layer up: the real log reads
`System.exit called ?` with a space before the `?`, and the space had been dropped when the
string was copied into the spec.

Two things to take from this. A verdict being right does not make its explanation right, and
tests that only assert verdicts will never notice. And when a component's output is going to
be read by a human as evidence, the explanation needs a test of its own.

## The open objection

Excluding around 30% of runs as build failures may discard genuine flakiness along with the
noise. That objection was raised against this result and **was never answered**. It is the
strongest thing a reviewer can say about the whole gate.

It belongs in `knowns/05-infra-gate.md` as a known-unknown, written plainly. A number this
large, resting on an unanswered objection, has to travel with the objection attached.

## Why this phase comes before splits

A single poisoned run can manufacture dozens of failing tests. Those tests then appear in
your labels, your sequences, and your retrieval index. Every measurement after this one
inherits them, and no metric you have will show you that it happened.

This is also why the gate is upstream of every observer rather than inside one of them.
An observer that filters its own inputs is filtering only its own inputs.
