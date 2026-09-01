# Troubleshooting

**`uv: command not found`** — install uv from https://docs.astral.sh/uv/, then reopen the
shell.

**`uv run lab.py doctor` reports missing phase files** — you are in the wrong directory.
Run it from the repository root, the folder containing `lab.py`.

**`check 00` says `PROBLEM.md` is missing but you wrote it** — check the filename case and
that it is at the repository root, not inside `labs/`.

**The coach is asking about metrics or datasets** — it has skipped ahead. Say so. Phase 00
has no metrics and no data.

**`knowns/00-start-here.md` — the directory does not exist** — create it. Nothing in this
repository is scaffolded for you.
