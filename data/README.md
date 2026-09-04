# Data

Nothing here ships with the repository. You fetch it in phase 04, **after** you have checked
the licence — that check is the phase, not a formality.

Everything below is here so you can verify you got the right thing. It is not a substitute
for phase 04's task.

## Source

**FlakeFlagger**, Zenodo record **4450723**, licensed **CC-BY-4.0** (attribution required).

```
https://zenodo.org/records/4450723
```

The record contains two kinds of material, and the difference matters enormously for how much
you download:

| | What it is | Size |
|---|---|---|
| the three CSVs | features, rerun results, project info | **~10 MB** |
| the `.tgz` archives | the raw rerun logs, one per project | **6.5 GB across 17 projects** |

Phases 04, 06, 07 need only the CSVs. Phases 08 and 09 read the archives.

## The three-project subset

You do **not** download 6.5 GB. Take these three:

| Project | Archive | archive-scan flaky | archive-scan deterministic |
|---|---|---|---|
| `square-okhttp` | 497 MB | 116 | 118 |
| `tootallnate-java-websocket` | 55 MB | 43 | 0 |
| `kevinsawicki-http-request` | 37 MB | 15 | 0 |
| **total** | **589 MB** | | |

589 MB downloads in a few minutes and the derivation runs on a laptop. You will run the
same pipeline as the full reference, over three projects instead of seventeen. Your
absolute numbers will differ from the reference; record the scope beside every number.

**Take okhttp even though it is the largest of the three.** It is the only project in the
archive scan with useful representation from both classes — 116 flaky and 118
deterministic before trusted-run and real-text filters are applied. Those later filters
deliberately reduce the usable corpus; these are not final model-input counts. Every other
project is flaky-only or empty in this scan.

That matters more than it looks. Several phases need **two classes** to work at all:

- phase 09 builds a retrieval index, and a single-class index scores a fake 1.0;
- phase 11 compares fusion strategies, which needs cases that can disagree;
- phase 12 builds a training corpus, and you cannot fine-tune a flaky-detector on data
  with no flaky examples in it.

A subset chosen by download size alone can give you none of that and make three later
phases appear to succeed or fail for the wrong reason. The constraint that matters is
class balance, not megabytes.

`spring-projects-spring-boot.tgz` alone is 2.6 GB. Do not start there.

## Layout you are building toward

```
data/
  raw/          the three CSVs + your three .tgz archives  (gitignored)
  cache/        derived sequence examples, one JSON per project (phase 08)
  distill/      teacher-labelled corpus (phase 12)
```

`data/raw/` and `data/cache/` are gitignored. Do not commit them. Record the commands that
produce them instead — that is what makes your work reproducible, and a committed CSV is
not.

## Verification targets

Check these after your phase 04 join. If your numbers are far off, the join key is wrong
and everything downstream inherits the error.

Against the **full** CSVs (which you have, regardless of how many archives you took):

```
test_features.csv    26,619 rows x 30 cols     205 positives in `flaky`   (0.77%)
test_results.csv     26,765 rows x  8 cols     828 positives in `IsFlaky`
joined               approximately 26.1k rows 825 positives              (~3.16%)
modelling features   depends on the recorded leak/history exclusions
```

The completed reference produced 26,142 joined rows and 16 modelling features after its
full exclusion policy. A small join-count difference can be legitimate when source
versions differ; a zero or sharply reduced join is not. Record source checksums, exact
exclusions and the command that produced your number.

The two files disagree on **904 tests**. Phase 04 is where you find out why, and which
column is actually the ground truth. One of them is not.

## Attribution

CC-BY-4.0 requires you to credit the source. Put this in your `decisions/04-*.md`:

> Data: FlakeFlagger (Zenodo record 4450723), CC-BY-4.0.
