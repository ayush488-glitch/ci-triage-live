# Task

## Design the slice — before anything else

Write `design/05-infra-gate.md` using the template in [design/README.md](../../design/README.md).

This phase's slice is **the trust gate**: the thing that decides whether a run's outcomes
may be used at all.

The hard question: **what does a poisoned run look like from the inside, and what does the
gate emit when it cannot tell?** A gate with only "trust" and "reject" has nowhere to put
the runs it is unsure about, and those are the ones that matter.

Note this slice sits *upstream* of every observer you have not built yet. In `Connects to`,
say which future slices depend on it. All of them do.

---

**1. Look at a run before you classify anything.** Untar one project. Find one build that
reports a large number of failing tests. Read it. Do not automate first.

**2. Name the verdicts.** From what you actually saw, define the categories a run can fall
into. You need at least: it was fine, the build never succeeded, the log was cut off, and an
implausible fraction of tests failed at once. Give them names.

**3. Decide the precedence.** A run can match more than one. The order you check them in
changes what gets reported, and the reason for a rejection is what a future engineer reads.
Write the order down and justify it.

**4. Set the mass-failure threshold, and defend the number.** What fraction of a suite
failing is implausible? You are choosing a number that will silently discard data. Say what
you chose, why, and what you would need to know to choose better.

**5. Build it.** `ci_triage/infra.py`. Ponytail: this is a function that reads a run and
returns a verdict plus a reason. It is not a framework.

**6. Test the reason, not just the verdict.** Your test must fail if the gate reports a
reason that does not match what it actually found. A verdict can be right while the audit
trail is fabricated — that is a real bug from this build, and it passed every test that only
checked verdicts.

**7. Measure the damage.** Run the gate over one project's full set of runs. Report, in
`artifacts/results/infra.json`:

- the count per verdict;
- **distinct failing tests using all runs, versus using only trusted runs.**

That second pair is the headline of the phase. Predict it before you run it.

**8. Answer the objection.** You are about to discard a large fraction of your runs. Does
that throw away real flakiness along with the noise? You cannot fully answer this. Say so,
in `knowns/05-infra-gate.md`, as a known-unknown — it is the strongest objection a reviewer
will raise and it is currently open.
