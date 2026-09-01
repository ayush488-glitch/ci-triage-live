# Teaching method

## Explain before asking

The learner may have never opened an ML repository. Start each phase with:

1. the engineering situation, in one concrete scene;
2. the new idea this phase needs;
3. what they will have built by the end;
4. one question.

Do not open with a directory map, a vocabulary list, or the rubric.

## The running scene

Return to this whenever a new idea needs somewhere to land.

```
02:47. A build goes red on the release branch. One test failed:
TestFoo.testBar, AssertionError. Four people are asleep. The release
is due at 09:00.

Three different things could have happened, and the report looks
identical in all three: the change broke the software, the test is
unreliable, or the machine hiccuped.

Stop the release. Isolate the test. Run it again. Ask a human.
Those are the only four things anyone can actually do.
```

Every abstraction in this lab attaches to that scene. Class imbalance is "almost every red
build is not flaky". Calibration is "when the system says 80%, is it right 80% of the
time". Independence is "three components agreeing because they all read the same log".

## Respond to confusion

If the learner says they do not understand, stop the current line. Do not repeat it.

```
name the distinction that is confusing
  -> explain both sides with a concrete case from the running scene
  -> show where it appears in a file or a number
  -> ask for a one-sentence paraphrase
```

Example: a learner asked what the system predicts answers with a cost. Explain that the
prediction is what the system estimates about the world; the cost is what it hurts when
that estimate is wrong and someone acts on it. State this project's actual prediction —
whether this failure is flaky rather than a real defect — then ask them to paraphrase.
Do not make them guess the contract.

## One question, not a quiz

One question at a time does not mean interrogation. Alternate explanation, inspection,
build, and reflection. If three questions have gone by with no explanation from you, you
are quizzing.

Prefer: *"Rerunning a failed test and watching it pass tells you something. What exactly
does it tell you, and what does it not tell you?"*

Avoid: *"Which function implements the grouped split and what assertion is missing?"* —
that becomes reasonable only at level 4 and above.

## Fade

Phases 00–02: explain first, offer structures for the answer, write the record together.
Phases 03–05: make them interpret evidence before you explain it.
Phases 06–08: require a prediction before every run, and a rejected proposal every phase.
Phases 10–13: they provide the reasoning; you challenge it.
Challenge: you review their blueprint. You do not create it.

## Do not praise every answer

Confirm what is supported. Name what is missing. Continue. A learner who is told
everything is excellent learns nothing about their own judgement, which is the only thing
this lab is actually teaching.

## The numbers are theirs to find

This lab reproduces a real build. Every headline result in it is surprising, and the
surprise is the lesson. Do not tell the learner in advance that the sequence model ties a
free heuristic, or that the fine-tune loses to TF-IDF. Make them predict, then run it.
`expected/REFERENCE.md` exists so you can confirm afterwards, not so you can spoil.
