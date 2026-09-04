# Reference notes

## The verdicts

Five, with precedence in this order:

1. **BUILD_FAILED** — the build did not succeed. Every test outcome in the run is
   meaningless, whatever else is also true.
2. **LOG_TRUNCATED** — the log is cut off. Tests that had not run yet look like they failed.
3. **MASS_FAILURE** — an implausible fraction of the suite failed at once.
4. **TRUSTED** — none of the rejection conditions applies.
5. **UNKNOWN** — the log is missing or cannot be parsed without guessing.

Precedence matters because a run often matches several. The reason string is what a future
engineer reads, and `build_succeeded is False` is a more useful thing to be told than
"lots of tests failed", which is the *consequence* of the build failing rather than the
cause.

## The two parser checks that matter

The project `.tgz` contains per-run `.tgz` archives; `maven.log` is inside the run archive.
Within one log, multi-module builds emit several `Tests run:` summaries. Sum every module;
using only the final line is a real under-counting bug.

A run-level fraction also has a cross-run blind spot. In the completed square-okhttp
reference, 102 tests failed in at least 90% of archived runs. They are deterministic under
the pass-and-fail label definition, so they are excluded before computing the mass-failure
fraction. The threshold is a recorded decision, not a universal constant.

## The result to report

Run the gate against the three-project subset from `data/README.md`. Report the count for
each verdict and the distinct failing tests before and after filtering to trusted runs, per
project. The values are observations from your archive and threshold; do not replace them
with a number from a different project.

The completed square-okhttp reference read 7,908 runs: 7,869 `TRUSTED`, 36
`LOG_TRUNCATED`, and 3 `MASS_FAILURE`. It found 202 distinct failing tests across all runs,
178 in trusted runs, and excluded 102 cross-run deterministic tests from the mass-failure
fraction. These are comparison values, not expected output for a different archive or
threshold.

The comparison matters because an infrastructure-contaminated run can inflate the number of
tests that appear to fail. A gate that rejects every run is not useful, so inspect clean
runs as well as rejected ones.

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

Excluding runs as build failures may discard genuine flakiness along with the noise. That
objection remains open and is the strongest thing a reviewer can say about the gate.

It belongs in `knowns/05-infra-gate.md` as a known-unknown, written plainly. A number this
large, resting on an unanswered objection, has to travel with the objection attached.

## Why this phase comes before splits

A single poisoned run can manufacture dozens of failing tests. Those tests then appear in
your labels, your sequences, and your retrieval index. Every measurement after this one
inherits them, and no metric you have will show you that it happened.

This is also why the gate is upstream of every observer rather than inside one of them.
An observer that filters its own inputs is filtering only its own inputs.
