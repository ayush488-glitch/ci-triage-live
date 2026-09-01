# Reference — read after your attempt

## Two experiments, two different answers

This is the important part, and it is why the phase asks you to run both.

**Per-project, on okhttp, grouped by test method:** mean precision@5 = **0.896** against a
majority baseline of **0.521**. The strongest per-component margin of any observer in the
system.

**Cross-project rotation, holding out a whole project:** mean precision@k = **0.474**
against a mean majority baseline of **0.715**. It **loses to the baseline.**

Same component. Same code. Opposite conclusions.

If you ran only the first, you would ship retrieval as the crown jewel. If you ran only the
second, you would delete it. The honest statement needs both: *retrieval is strong within a
project it has seen and does not transfer to an unseen one* — which is the same boundary
the tabular observer hit in phase 07, arriving from a completely different direction.

Two independent components failing at the same boundary is evidence about the **problem**,
not about either component.

## Why it wins where it wins

**The index keeps the instances.** A trained model compresses 26,000 rows into parameters
and discards whatever did not survive. With 825 positives, that compression is lossy exactly
where you care. An index keeps every case intact, so a failure mode with three examples is
still findable — where three examples out of 26,000 is a gradient step indistinguishable
from noise.

**The task is genuinely a lookup.** "Has anything like this happened before, and what was it"
is a nearest-neighbour question. Fitting a decision surface to answer it is a detour.

## TRAP #7 — the single-class corpus

The first version indexed only FAILURE observations. Every neighbour of every query was
therefore a failure, every vote was unanimous, and precision@k was 1.0 **by construction**.
The number measured the index, not the retriever.

Look at what the raw data does to you here. Running the flaky-vs-deterministic scan across
projects gives, per project:

```
Alluxio-alluxio        FLAKY 243   DETERMINISTIC 0     has_both_classes: false
apache-httpcore        FLAKY  18   DETERMINISTIC 0     has_both_classes: false
doanduyhai-Achilles    FLAKY   5   DETERMINISTIC 0     has_both_classes: false
apache-commons-exec    FLAKY   0   DETERMINISTIC 0     has_both_classes: false
```

Most projects yield **no deterministic class at all**. The single-class corpus is not an
implementation slip you avoid by being careful — it is the default state of this data, and
only an explicit check keeps you out of it.

```python
def test_index_is_not_single_class():
    assert len(set(index_labels())) > 1
```

That is the phase's invariant. Only three of the projects had both classes, which is why the
cross-project rotation above scored just three rotations.

## Self-retrieval

A query that retrieves itself scores perfectly and proves nothing — the "neighbour" is the
answer key. Exclude by identifier and test it. With a corpus of a few hundred vectors, a
handful of duplicate occurrences of the query's own test dominate the vote entirely.

There is a subtler version worth knowing: in one real case, retrieval's "5 neighbours"
turned out to be **the same test occurring 5 times across different runs, with disagreeing
labels** — not five independent opinions. Five neighbours is not five pieces of evidence
unless they are five different tests. Report the distinct-test count alongside k.

## Exact search, not approximate

The corpus is a few hundred vectors, so exact inner-product search over normalised
embeddings costs nothing. Approximate indexes (HNSW, IVF) are non-deterministic across
builds — traversal order and pruning depend on insertion order — so two runs over the same
corpus can return different neighbours for the same query, which makes the leave-one-out
ablation this observer exists for unreproducible.

Reach for approximate search when the corpus is millions. Not here.

## What this component cannot do

It answers "what happened last time something looked like this". On a genuinely novel
failure the nearest neighbours are not near, and the vote is confident nonsense.

So the distance has to travel with the answer. Retrieval is the one observer that can tell
you it has nothing relevant — which makes it the strongest argument for abstention in the
whole system. Carry that into phase 10.
