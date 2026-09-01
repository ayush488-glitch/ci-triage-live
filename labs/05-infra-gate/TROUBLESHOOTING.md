# Troubleshooting

**The archives are large** — take the four small projects from [data/README.md](../../data/README.md).
`apache-commons-exec` at 36 MB is the right one to start on; it is also the control, because
almost all of its runs are clean.

**You cannot find a run with mass failures** — `Alluxio-alluxio` is the interesting one, but
it is 152 MB. `commons-exec` is deliberately boring; if your gate fires on it, your gate is
over-triggering.

**The same test appears twice in one run** — some suites execute a test both individually and
as part of an aggregate suite, and the two can disagree. Decide which one counts, and exclude
the aggregate from your failed-fraction arithmetic or a single suite-level failure inflates it.

**Your threshold feels arbitrary** — it is. Write the number, write the reasoning underneath,
and record it as a known-unknown. That is more honest than a number with a confident
justification invented after the fact.

**Untarring fills your disk** — extract one project at a time and delete as you go, or read
from the archive without extracting.
