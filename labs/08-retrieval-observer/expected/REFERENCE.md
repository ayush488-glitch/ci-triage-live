# Reference — read after your attempt

## The numbers

**Precision@5 ≈ 0.896** against a majority-vote baseline of **≈ 0.521** on the same queries.
The strongest single component in the system, and the only one that needs no training.

## Why it wins

Two reasons, and the learner should get both.

**The index keeps the instances.** A trained model compresses the dataset into parameters
and throws away everything that did not survive the compression. With 825 positives, that
compression is lossy in exactly the places you care about. A retrieval index keeps every
case intact, so a rare failure mode with three examples is still findable — where a gradient
step on three examples out of 26,000 is noise.

**The task is genuinely a lookup.** "Has anything like this happened before, and what was it"
is a nearest-neighbour question. Fitting a decision surface to answer it is a detour.

## The trap: a single-class corpus

If the index contains only FAILURE observations, then every neighbour of every query is a
failure, every vote is unanimous, and precision@k is 1.0 by construction. The number
measures the index, not the retriever.

This shipped in the original build. It was found because the number was too good, which is
a poor detection mechanism — it depends on somebody being suspicious. The test is the
detection mechanism:

```python
def test_index_is_not_single_class():
    assert len(set(index_labels())) > 1
```

The index must contain both resolved-flaky and resolved-real cases, or the vote is not a
vote.

## Self-retrieval

A query that retrieves itself scores perfectly and proves nothing. Exclude by identifier,
and test it — this is the retrieval version of the split leakage in phase 05, and it is
equally invisible in the metrics.

## What this component cannot do

It answers "what happened last time something looked like this". If the current failure is
genuinely novel, the nearest neighbours are not near, and the vote is confident nonsense.

That is why the distance to the neighbours has to travel with the answer, and why this
component is a strong argument for abstention: retrieval is the one observer that can tell
you it has nothing relevant. Carry that into phase 09.
