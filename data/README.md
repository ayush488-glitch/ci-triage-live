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

The record contains two kinds of thing, and the difference matters enormously for how much
you download:

| | What it is | Size |
|---|---|---|
| the three CSVs | features, rerun results, project info | **~10 MB** |
| the `.tgz` archives | the raw rerun logs, one per project | **6.5 GB across 17 projects** |

Phases 04, 06, 07 need only the CSVs. Phases 08 and 09 read the archives.

## The four-project subset

You do **not** download 6.5 GB. Take these four, which are the small ones:

| Project | Archive |
|---|---|
| `apache-commons-exec` | 36 MB |
| `kevinsawicki-http-request` | 38 MB |
| `google-jimfs` | 41 MB |
| `tootallnate-java-websocket` | 55 MB |
| **total** | **170 MB** |

170 MB downloads in a couple of minutes and the derivation runs on a laptop. You will run
the same pipeline the full build ran; you will just run it over four projects instead of
seventeen, so your absolute numbers will differ from the ones in the lecture. That is
expected and you should say so whenever you quote one.

`spring-projects-spring-boot.tgz` alone is 2.6 GB. Do not start there.

## Layout you are building toward

```
data/
  raw/          the three CSVs + your four .tgz archives   (gitignored)
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
joined               26,134 rows              825 positives              (3.157%)
modelling features   23
```

The two files disagree on **904 tests**. Phase 04 is where you find out why, and which
column is actually the ground truth. One of them is not.

## Attribution

CC-BY-4.0 requires you to credit the source. Put this in your `decisions/04-*.md`:

> Data: FlakeFlagger (Zenodo record 4450723), CC-BY-4.0.
