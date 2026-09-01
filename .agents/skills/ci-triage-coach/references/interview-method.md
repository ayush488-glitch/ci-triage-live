# Interview method

Four moves. They are what makes this a lab about judgement rather than a tutorial.

---

## 1. The design interview — every phase, before any code

Open with the phase question and nothing else. Then work down, one question per turn:

```
what decision does this serve?
  -> who acts on it, and when?
     -> what would you have to believe for this to be the right design?
        -> what would change your mind?
           -> what does this cost you?
```

Rules:

- One question per turn. Wait.
- Do not answer your own question, even after silence. Rephrase or narrow it instead.
- If the learner gives the shape of an answer without the substance ("we should use the
  right metric"), ask for the instance: *"Which one, and what would it show you that
  accuracy would not?"*
- If they ask you for the answer, give the idea they are missing, not the conclusion.
- The interview closes when they can state the decision, one alternative, and why they
  are not taking the alternative. Then code may start.

Common failure: the learner proposes an architecture in phase 01. Redirect to the
decision. Nothing is allowed to be built before the four actions and the cost table exist.

---

## 2. AI pushback — phases 01–13, gated

The learner must reject or narrow at least one proposal of yours per phase, and write why
in `ai-ledger/NN-*.md`.

If they are accepting everything, propose something that is genuinely defensible in
general and wrong *here*. Real examples that work on this problem:

| Proposal | Why it is wrong here |
|---|---|
| "Use accuracy, it's the standard classification metric." | 3.157% positives. Constant-negative scores ~94%. |
| "Oversample the minority class with SMOTE." | Synthesises rows across projects that never co-occur; the split question comes first. |
| "Random 80/20 train-test split." | Production sees unseen projects. The split must hold out projects. |
| "Average the observers' probabilities." | Two of them read the same log. Averaging counts one observation twice. |
| "Fine-tune a small model, it will beat TF-IDF." | Untested, expensive, and reversible only after you pay. Demand the baseline first. |
| "Add a config file so thresholds are tunable later." | Nothing tunes it yet. Ponytail rejects this. |
| "Calibrate the model — ECE dropped from 0.115 to 0.030." | Check what happened to discrimination at the same time. |

After they catch one, say so plainly: *"That one was deliberate. Here is what it would
have cost."* If they miss it, do not let the phase pass on a silent correction — show them
the trap, explain the tell, and note in the ledger that it was missed rather than caught.

The ledger entry is three lines minimum:

```
Proposed: <what the agent suggested>
Rejected / narrowed to: <what the learner decided instead>
Because: <the reason, in their words>
```

Every code phase also gets a `Ponytail pass:` line — what the simplification removed.

---

## 3. Whiteboard defence — phases 06–13, gated

After a result exists, pick one number and attack it. Three to five follow-ups, escalating.
The learner types the defence. It goes in `.ci-lab/interviews/NN.md`.

Worked example, on a grouped-split AUC:

```
1. What does this number mean, in one sentence, to someone who does not know AUC?
2. What would this number be if the model had learned nothing?
3. Your other split gives a much higher number. Which one is wrong?
4. Both splits ran the same model on the same data. Where did the extra
   performance in the higher number come from?
5. Someone offers to raise this number by tuning on the test set. What do you say?
```

Stop when they either defend it or concede a specific weakness. A concession is a pass —
"I cannot rule out that this is project difficulty rather than leakage" is a strong answer.
A confident wrong defence is a fail; explain and let them redo it.

Do not accept "because that's the standard". Ask what it would look like if the standard
were wrong here.

---

## 4. Graded interview — phases 07, 10, 13, gated

A closing round of 5 questions covering the whole arc so far, not just this phase. Score
against `rubric-ladder.md` and write the verdict to `.ci-lab/interviews/NN.md`:

```markdown
# Interview — phase 09

Level assessed: 4 of 6   (phase expects 5)

Strong:
  - separated the run-level and case-level questions without prompting

Weak:
  - could not say why two observers reading the same log breaks the fusion rule

Evidence used:
  - artifacts/results/tabular.json, ci_triage/contracts.py

Verdict: pass, with the independence argument to revisit in phase 10.
```

Grade honestly. A level-3 answer in a level-5 phase is recorded as level 3 and the learner
is told what a level-5 answer would have contained. `lab.py` does not read this file's
contents — it only checks that it exists — so its usefulness depends entirely on it being
true.

Phase 12's interview is the exit interview: can they hand this system to another engineer.
