# Reference — read after your attempt

## The two levels

**Case level:** for this one failure, what happened? Consumer is the engineer debugging the
test. **Run level:** for this build, with 197 failures in it, should the release stop?
Consumer is the release manager.

Conflating them produces a system that answers 197 separate questions and leaves the
release decision to whoever is reading the output at 02:47, which is the decision you said
in phase 00 that you were building this to support.

The run-level answer is not a majority vote over case-level answers. One real defect among
196 flaky tests still stops the release.

## The independence rules

Derived from the failure mode, not received:

1. **Every observer reports a calibrated probability, or is explicitly marked uncalibrated.**
   Downstream cannot tell by looking. An uncalibrated 0.9 and a calibrated 0.9 mean
   different things and must not be averaged as if they did not.
2. **Absence and uniformity are different states.** "I have nothing" and "I have evidence
   that points nowhere" produce identical uniform distributions and mean opposite things.
   Encode them separately or the fusion layer cannot distinguish an observer that failed
   from an observer that genuinely does not know.
3. **No observer reads another observer.** Not because reading is bad, but because it
   destroys your ability to interpret agreement. Once B reads A, B agreeing with A carries
   no information, and every fusion strategy built on agreement is measuring an echo.
4. **Cost and latency are measurements, reported by the component per call.** A number in a
   design document is a claim about the past. Phase 12's cost ladder needs the real ones,
   and they must come from the run.

The mechanism that makes rule 3 workable: observers do not talk to each other, they write
to a **common evidence record**. Independence is enforced by the architecture, not by a
convention that erodes the first time somebody is in a hurry.

## The evidence record

One structure per observation. Minimum viable, in ponytail terms:

```python
@dataclass(frozen=True)
class Evidence:
    observer: str
    verdict: str | None          # None means: nothing to say
    probability: float | None
    calibrated: bool             # never optional, never defaulted
    inputs_read: tuple[str, ...] # what this observer actually looked at
    cost_usd: float
    latency_ms: float
    note: str = ""
```

`inputs_read` is what makes rule 3 auditable rather than aspirational — you can compute the
overlap between observers instead of asserting there is none.

`calibrated` has no default on purpose. A default is how it gets forgotten.

## Why this must be settled before fusion

Every result in phase 10 is a comparison between strategies for combining these records. If
the records are ambiguous — if a uniform distribution might mean two different things, or a
probability might or might not be calibrated — then the comparison is between strategies
for combining noise, and the numbers do not mean anything.

The evidence record is also append-only. A verdict is a historical fact about what a
component said at a moment. Editing it destroys the audit trail that made the whole
architecture worth building.
