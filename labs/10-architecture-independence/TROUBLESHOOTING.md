# Troubleshooting

**Your observers genuinely do share an input** — most systems do. The rule is not that they
must be independent, it is that you must know they are not, and must not treat their
agreement as independent evidence. Record the overlap in `docs/architecture.md`.

**The contract keeps growing fields** — every field must have a consumer. If nothing reads
it, delete it. Ponytail.

**You want an abstract base class for observers** — you have three observers and they are
all written. YAGNI. A dataclass and three functions.

**"No evidence" is hard to encode** — an explicit optional. `None` for the distribution and
a reason string. Do not use a uniform distribution to mean absent; that is the bug.

**Cost is not measurable for the free components** — then it is zero, measured, and recorded
as measured. The point is that the number comes from the run, not from a doc that goes stale.
