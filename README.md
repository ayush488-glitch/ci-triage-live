# CI flakiness triage — build it from an empty folder

A build goes red at 02:47. One test failed. Three completely different things could have
caused it and the report looks identical in all three. Somebody has to decide whether to
stop the release.

You are going to build the system that helps them decide. You start with almost nothing:
this harness, and a coach.

There is no starter code. `ci_triage/` does not exist yet. You write it.

---

## Start

You need [uv](https://docs.astral.sh/uv/) and a coding agent (Claude Code, or any agent
that reads `.agents/skills/`). Then paste this into the agent, in this folder:

```text
Read .agents/skills/ci-triage-coach/SKILL.md and follow it. This is a guided lab
and I am the learner.

Set me up first: check I have uv, install the ponytail plugin if it is missing
(/plugin marketplace add DietrichGebert/ponytail then /plugin install
ponytail@ponytail), run `uv run lab.py doctor`, then `uv run lab.py next`, and
open progress.html so I can see where I am.

Then start coaching me from whatever phase that is. I may know nothing about
machine learning. Explain before you question me, one question at a time, and
do not write my design decisions for me.
```

That is the whole setup. The coach takes it from there.

## What you will have at the end

A triage system with four independent observers — rules, a tabular model, a sequence model,
and retrieval — a fusion layer, an arbiter, and an evidence record that makes every verdict
traceable. Roughly 13 hours of work across 13 phases, then a 90-minute challenge.

More importantly: a written record of every decision you made, every AI proposal you
rejected, every hypothesis that turned out wrong, and everything you still do not know.
That record is the actual deliverable. The code is evidence that you earned it.

## How it works

```
interview  ->  decide  ->  hypothesis  ->  build  ->  test  ->  evidence  ->  record
```

Each phase opens with an interview. You cannot write code until you can say what decision
the code serves and what your design costs you. You cannot run an experiment until you have
written down what result would make you abandon your idea. Every phase, you have to reject
or narrow at least one thing the AI proposes — that is a gate, not a suggestion.

## Commands

```bash
uv run lab.py status          # where you are
uv run lab.py next            # open the next phase
uv run lab.py show 05         # look at a phase
uv run lab.py check 05        # gate: do the required artifacts exist
uv run lab.py progress        # rebuild progress.html
open progress.html            # the whole project at a glance
```

Progress is gated on files existing on disk. Saying you understood something does not
advance anything, and neither does the coach agreeing with you.

## The files you will accumulate

| Directory | What goes in it |
|---|---|
| `ci_triage/` | the system |
| `tests/` | tests that fail when the logic is wrong |
| `decisions/` | one decision per phase, with what it cost you |
| `experiments/` | the hypothesis, written *before* the run |
| `knowns/` | what moved from unknown to known, or to known-unknown |
| `ai-ledger/` | what the AI proposed and what you rejected |
| `artifacts/results/` | the real numbers |
| `.ci-lab/interviews/` | your defence of a number, under attack |

## Data

FlakeFlagger, Zenodo record 4450723, CC-BY-4.0. You download it yourself in phase 04, after
you have checked the licence. There is another dataset that would be convenient and has no
licence at all; finding that out is part of the phase.

## If you are running this in class

`labs/manifest.toml` has a `taught_through` line. Phases past it are marked *ahead of
lecture* and `lab.py next` will not open them without `--ahead`. Move the line after each
session; nothing else needs to change.
