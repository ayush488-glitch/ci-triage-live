# Prompts to adapt

```text
Here is one CI run's log from a rerun archive (paste a chunk). Do not write code.
Tell me everything in here that would make me distrust the per-test outcomes, and
for each one, the specific evidence in the log that shows it.
```

```text
I have four verdicts for a run: clean, build failure, truncated, mass failure.
A run can match more than one. Argue for a precedence order, then argue for the
opposite order, and tell me which reason a future engineer would rather read.
```

```text
Write a test that fails if my gate returns the right verdict with a reason string
that does not match what it actually found in the log. Not a test of the verdict
— a test of the reason.
```

```text
My gate rejects about 30% of runs as build failures. Argue that I am discarding
genuine flakiness along with the noise. What evidence would settle it?
```
