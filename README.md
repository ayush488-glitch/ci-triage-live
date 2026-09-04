# CI flakiness triage

Author: Ayush Singh

A build goes red at 02:47. One test failed. The change may be broken, the test may be
unreliable, or the machine may have hiccupped — and the report looks identical in each
case. Build the system that helps decide whether to stop the release.

You begin with an empty `ci_triage/` directory. This repository supplies the evidence,
the phase sequence, and a small standard-library harness. You make the system decisions;
an AI coding agent can help inspect, draft, test, and simplify the implementation.

## Start

```bash
git clone https://github.com/ayush488-glitch/ci-triage-live.git
cd ci-triage-live
```

You need [uv](https://docs.astral.sh/uv/) and a coding agent that reads `.agents/skills/`.
Open the agent in this directory and paste this single prompt:

```text
Read .agents/skills/ci-triage-lab/SKILL.md and follow it.

Run `uv --version`, `uv run lab.py doctor`, and `uv run lab.py next`; report each result.
I own the design decisions, including what each component may read and emit, when it
refuses, its constraints, the metric, split, threshold, and architecture. Explain an
unfamiliar idea with the running CI incident before asking about it. Ask one question at a
time and wait for my answer. Do not invent evidence or run an experiment before its
hypothesis is written.
```

That is all the setup. There is no install step and no `pyproject.toml`; `lab.py` uses only
the standard library.

## Work through the phases

```
decide -> design -> hypothesis -> draft -> review -> patch -> test -> evidence -> record
```

Each phase focuses on one system slice: its responsibility, allowed inputs, outputs,
refusal behavior, and invariant. Record those choices before code. Record a hypothesis
before an experiment. Keep one AI proposal you rejected or narrowed in every phase; it
makes the trade-off inspectable later.

```bash
uv run lab.py status          # current work
uv run lab.py next            # open the next phase
uv run lab.py show 05         # inspect a phase
uv run lab.py check 05        # verify its required artifacts exist
uv run lab.py progress        # rebuild progress.html
open progress.html
```

Progress is based on files on disk, not a claimed result.

## Save your work

Work on your own branch:

```bash
git checkout -b lab/my-ci-triage
git add -A && git commit -m "phase 05"
git push -u origin HEAD
```

## What you will build

A CI-triage system with rules, tabular, sequence, and retrieval observers; a fusion layer;
an arbiter; and an evidence record for every verdict. The project is organized across 14
phases plus a 90-minute challenge.

| Directory | Contents |
|---|---|
| `design/` | one system slice per phase, written before code |
| `ci_triage/` | implementation |
| `tests/` | invariants that fail when the logic is wrong |
| `decisions/` | decisions and their costs |
| `experiments/` | hypotheses written before runs |
| `knowns/` | supported conclusions and remaining uncertainty |
| `ai-ledger/` | AI proposals and your review |
| `artifacts/results/` | command-produced results |

## Data

In phase 04, you download FlakeFlagger from Zenodo record 4450723 after checking its
CC-BY-4.0 licence. A convenient alternative has no licence; whether it may be used is part
of the work.
