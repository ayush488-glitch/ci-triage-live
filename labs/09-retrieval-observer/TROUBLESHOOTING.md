# Troubleshooting

**Precision@k is suspiciously close to 1.0** — either the query is in the index, or the
index is single-class. Both are real bugs and both look like success.

**Cross-project evaluation has no eligible rotations** — record the class coverage and the
reason it cannot be scored. A missing evaluation is not evidence that retrieval transfers.

**Embedding is slow** — batch it, and use a small sentence model. This is not the phase to
be clever about encoders.

**Logs are near-identical across different causes** — that is real, and it is the finding
that motivates the fusion layer. Two failures with identical logs can have different causes;
the log alone does not carry it.

**`sentence-transformers` is heavy to install** — TF-IDF plus cosine similarity is a
legitimate substitute and you should note the substitution in your decision file. It will
also turn out to be relevant in phase 11.

**k is ambiguous** — report several. The shape of the curve is more informative than any
single k.
