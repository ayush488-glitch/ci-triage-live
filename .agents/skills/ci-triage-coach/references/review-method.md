# Review method

The agent drafts. The learner reads it. This is the step that decides whether a learner ends
the lab able to work with an AI or merely able to prompt one.

## Hand it over properly

After drafting, stop. Do not run it, do not summarise it into something reassuring, do not
say what it "should" do. Say:

```
Drafted <file>, N lines, against your slice. I have not run it.

Read it in four passes and tell me what you find. If a pass turns up nothing,
say "nothing" for that pass — do not invent a finding to be polite.
```

Then wait. If the learner says "looks fine, run it", they have not read it. Ask them one
specific question about a line, and the conversation resumes.

## The four passes

Named, because "review this" produces nothing and four narrow questions produce a lot.
The learner does them in order, because each one is cheaper than the next.

**1. Does it match my slice?**
Open `design/NN-*.md` next to the diff. Does it read only what `Reads` allows? Does it emit
everything `Emits` promised — including the calibration flag, the cost, what it read? Does
it do what `Refuses` says when it cannot answer? This pass needs no programming skill at
all, and it catches the most damaging class of error, because a component that quietly reads
something it should not is invisible in every metric.

**2. Is it correct?**
Off-by-one, empty input, a single row, all-one-class, division by a count that can be zero.
For this project specifically: what happens on a fold with no positives, a test with one run,
an index with one class.

**3. Is the ML claim valid?**
Does the split match the deployment question. Is anything fitted on data it will later be
evaluated on. Is a threshold chosen on the same data it is measured on. Is a probability
being averaged with one that was never calibrated. This pass is where fluent code hides
invalid statistics, and it is the pass most learners skip.

**4. Does any of it need to exist?**
Ponytail. A class with one instance. A config for a value nothing configures. A wrapper
around one library call. A parameter with one caller. Deleting is a legitimate review
finding and should be recorded as one.

## What the learner has to produce

One line per pass in `ai-ledger/NN-*.md`:

```markdown
## Review
1. slice fit   — reads `run.log` but my slice says logs only; asked to drop it
2. correctness — nothing
3. ML validity — calibrator fitted inside the fold it is scored on
4. necessity   — the ObserverBase class has one subclass; deleted
```

"Nothing" is an acceptable answer for a pass, and an honest one. All four being "nothing" on
a phase with real code is not, and means the passes were not actually run.

## Then one bounded patch

The learner picks **one** finding and says what to change. The agent changes that and
nothing else. This is where the habit lives: a patch you directed and can explain is worth
more than a rewrite you accepted.

If the learner asks for a rewrite instead, that is the moment to point out they are about to
inherit code nobody read.

## Fade

Phases 00–02: walk the passes with them, out loud, and show what each one looks for.
Phases 03–06: they run the passes, you prompt for the ones they skip.
Phases 07–10: they run all four unprompted; you stop naming them.
Phases 11–13 and the challenge: they review your draft without being asked to, and a phase
where they did not is one you should question.

## Do not defend your own draft

When the learner finds something, the answer is "yes, here is why I wrote it that way" or
"yes, that is wrong" — not an argument. You are not the author under review; the draft is a
proposal, and a proposal that survives unexamined has failed at its only job.
