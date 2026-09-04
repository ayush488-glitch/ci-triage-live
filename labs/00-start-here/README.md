# Lab 00 — the decision at 2:47am

```
[Start] -> Cost -> Measure -> Truth -> Data -> Splits -> Observers -> Fusion -> Handoff
```

02:47. A build goes red on the release branch. One test failed:

```
CI FAILED

TestFoo.testBar()
AssertionError
```

Four people are asleep. The release is due at 09:00.

That report tells you a test failed. It does not tell you why, and *why* is the only thing
that determines what anyone should do. Three completely different things could have
happened, and the report looks identical in all three.

## Your focus

No code, no data, no model. One move: from "a test failed" to "somebody has to do
something, and here is what somebody actually is".

Almost every ML project that fails, fails here — by starting from the data that was
available rather than from the decision that needed making.

## Deliverables

`PROBLEM.md`, in your own words, and your first `knowns/` entry.

## Suggested pace

About 25 minutes.

## Check

```bash
uv run lab.py check 00
uv run lab.py next
```
