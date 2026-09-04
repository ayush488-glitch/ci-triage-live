# Decision dialogue

Use these moves to help the builder make and defend their own choices.

## Start with the decision

Open with the phase question. Ask one question, then wait:

```
what decision does this serve?
  -> who acts on it, and when?
     -> what would make this design appropriate?
        -> what would change your mind?
           -> what does it cost?
```

If the answer is generic, ask for the concrete case. If the builder asks for an answer,
explain the missing idea or provide options without selecting one. Code may begin when they
can state the decision, an alternative, and why they are not taking it.

## Make an AI alternative inspectable

In phases 01–13, offer one plausible alternative that does not fit this project. The
builder rejects or narrows it in `ai-ledger/NN-*.md` with their reason. Useful examples:

| Alternative | Why it does not fit |
|---|---|
| Use accuracy. | The positive class is rare; constant-negative can look accurate. |
| Random 80/20 split. | Deployment sees unseen projects. |
| Average all observer probabilities. | Shared evidence can be counted twice. |
| Fine-tune first. | A cheap baseline must establish the need. |
| Add a configurable threshold. | Nothing configures it yet. |

Do not silently correct a missed alternative. Explain its cost and preserve the outcome in
the ledger.

## Defend a result

After a result exists, ask three to five follow-ups about one number:

1. What does it mean in one sentence?
2. What would it be if the system learned nothing?
3. What other result conflicts with it, if any?
4. What produced the difference?
5. What decision must not be made from this number?

A precise limitation is a useful answer. Do not accept “because it is standard” without
the deployment reason.

## Periodic integration check

At phases 07, 10, and 13, use five questions spanning the work so far. Record strong
evidence, open questions, and the next concrete action. The goal is an honest handoff, not
a score.
