# Reference — read after your attempt

## The corrected real-text control

The completed three-project run could perform only the within-project evaluation. On
square-okhttp, one real trusted exception line per test produced 102 deterministic label-0
tests and 76 ground-truth-flaky label-1 tests. Precision@5 was **0.9831** against a
majority baseline of **0.5730**, across 178 scored queries with five distinct neighbours
and no abstentions.

The prediction said precision should drop after replacing synthetic pass templates with
real text on both sides. It did not, so the template-style explanation was falsified. That
does not establish cross-project transfer.

The real-text cross-project evaluation was not performable: the remaining eligible
projects could not form compatible two-class train and held-out populations. Record that
outcome as unscored rather than replacing it with a borrowed number.

The separate 17-project precomputed artifact reports precision@k **0.474** against a
majority baseline of **0.715** for an older cross-project rotation. It is useful historical
evidence, but it used a different corpus construction and cannot be presented as the
missing arm of the corrected real-text experiment.

The honest statement is narrower: *retrieval is strong inside the corrected okhttp corpus;
cross-project behavior remains unknown in this run, while older broader evidence warns
that transfer may fail.*

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

That is the phase's invariant. The broader scan found very few projects with both classes,
which is why corpus eligibility must be reported beside every evaluation.

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
