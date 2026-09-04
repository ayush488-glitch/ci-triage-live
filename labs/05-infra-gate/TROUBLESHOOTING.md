# Troubleshooting

**The archives are large** — use only the three-project subset in
[data/README.md](../../data/README.md): `square-okhttp`, `tootallnate-java-websocket`, and
`kevinsawicki-http-request` (589 MB total). Do not substitute the old small-project route;
the subset was selected for the later labs' class balance.

**You cannot see `maven.log` in `data/raw/`** — it is nested: the project `.tgz` contains
per-run `.tgz` files, and each run archive may contain `maven.log`. Read both archive layers
in memory or extract one run. The subset may not expose every failure mode; record an
unobserved verdict instead of inventing one or fetching a fourth archive.

**The same test appears twice in one run** — some suites execute a test both individually and
as part of an aggregate suite, and the two can disagree. Decide which one counts, and exclude
the aggregate from your failed-fraction arithmetic or a single suite-level failure inflates it.

**Your threshold feels arbitrary** — it is. Write the number, write the reasoning underneath,
and record it as a known-unknown. That is more honest than a number with a confident
justification invented after the fact.

**Untarring fills your disk** — extract one project at a time and delete as you go, or read
from the archive without extracting.
