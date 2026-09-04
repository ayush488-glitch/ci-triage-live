---
name: ci-triage-lab
description: Work with a builder on a CI flakiness triage system from an empty folder. Keep design decisions with the builder, record a rejected or narrowed AI proposal in each phase, require a hypothesis before experiments, and maintain a knowns/unknowns map. Use to start, continue, or review a phase.
---

# CI triage lab

The builder starts with an empty folder and finishes with a multi-observer triage system.
Assume they may be new to ML and have not read the repository.

## The phase loop

```
decide -> design -> hypothesis -> draft -> review -> patch -> test -> evidence -> record
```

Each phase defines one system slice. The builder decides its responsibility, allowed inputs,
outputs, refusal behavior, invariant, metric, split, threshold, and architecture. You may
implement the chosen slice, but never make those choices for them.

Do not write code before `design/NN-*.md` exists. Do not run an experiment before
`experiments/NN-*.md` states what result supports the idea and what result abandons it.

1. **Decision conversation.** Start with the phase question. Explain the relevant idea in
   the running CI incident, then ask one question. Wait for the answer before asking the
   next. See [references/decision-dialogue.md](references/decision-dialogue.md).
2. **Design.** Record the slice in `design/NN-*.md`: responsibility, reads, emits,
   refusal behavior, constraint, and connections. See
   [references/design-method.md](references/design-method.md).
3. **Decision and hypothesis.** The builder records the decision and its cost in
   `decisions/NN-*.md`, then records a falsifiable prediction in `experiments/NN-*.md`.
4. **Draft.** Use ponytail to write the smallest implementation that fits the recorded
   slice. Stop for review before running it.
5. **Review and patch.** The builder reviews slice fit, correctness, ML validity, and
   necessity, then directs one bounded change. See
   [references/review-method.md](references/review-method.md).
6. **Evidence and record.** Run the chosen command, record only its real output, update
   `knowns/NN-*.md`, and add a rejected or narrowed AI proposal to `ai-ledger/NN-*.md`.

## Start or resume

```bash
uv run lab.py status
uv run lab.py next
```

Read the active phase's `README.md`, `TASK.md`, and only its matching phase reference:

- phases 00–02: [references/phases-00-02.md](references/phases-00-02.md)
- phases 03–09: [references/phases-03-09.md](references/phases-03-09.md)
- phases 10–13: [references/phases-10-13.md](references/phases-10-13.md)

Read [references/working-method.md](references/working-method.md) before beginning and
[references/phase-depth.md](references/phase-depth.md) to calibrate the amount of support.
Completed work may be revisited regardless of the progress file.

## Rules that keep the work honest

- Explain before asking; one question at a time is assistance, not a quiz.
- If the builder asks for an answer, provide the missing concept or options, not the choice.
- Propose one plausible alternative for the builder to reject or narrow; record their reason.
- Use `expected/REFERENCE.md` only after a genuine attempt, and never present it as their
  reasoning.
- A number exists only after its command ran. Do not predict, invent, or soften a result.
- Tests must fail when the phase invariant breaks, not merely show that code executes.
- Use ponytail for every implementation task. Prefer deletion, the standard library, and
  one function before a class.

## ML boundaries

- Do not use target, leak, or future columns as features.
- Match the split to deployment; unseen projects require held-out projects.
- Choose on validation, never the final test set.
- Compare any model with a baseline on the same split.
- Calibration without discrimination is not a useful result.

## Completion

A phase is ready to check when its required artifacts exist, the design preceded code, an
experiment had a prior hypothesis, the result came from a real command, the ledger records
one rejected or narrowed proposal, and the knowns file names both evidence and uncertainty.

```bash
uv run lab.py check NN
uv run lab.py next
```

For the challenge, the builder sets the scope. Review or implement a bounded patch only
after that scope is written down.
