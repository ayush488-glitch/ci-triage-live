# Reference — read after your attempt

## Why three outputs are not enough

Three outputs assume the system always has enough evidence to pick one. It does not. A
failure with an uninformative log, on a test with no history, in a project the system has
never seen, is a case where every one of the three is a guess, and a confident guess is
worse than no answer — because a confident guess gets acted on.

## Abstention

The fourth output says: *I do not know, and someone should look.* It is derived, not
assumed. It exists because there is a case the other three cannot honestly cover.

It is **cheap, not free**. It costs a human's attention, at 02:47, which is the most
expensive attention in the company. A system that abstains on everything has solved
nothing. This is why coverage becomes a metric in phase 02 — the fraction of cases the
system was willing to answer is part of how you judge it.

## The output space

Four outputs, each tied to an action:

| Output | Action |
|---|---|
| real defect | stop the release |
| flaky | isolate the test, continue |
| infrastructure | run it again |
| abstain | wake a human |

## The two costs

A defect that ships is found by users, after release, at the worst moment, and costs a
rollback plus the reputational cost of the incident. A release delayed by a false positive
costs engineer-hours and a slipped deadline.

Most teams rate the shipped defect several times worse. Some do not — a team shipping to
internal users many times a day may rate the delay worse. The point is not which answer is
right. The point is that the answer is a property of the organisation, has to be elicited,
and cannot be inferred from the data.

## Two properties of the table

It is **asymmetric** — that is the entire reason it exists. If it were symmetric you could
use accuracy and stop thinking.

It has a **non-zero cost for abstaining**. Leaving that cell empty makes abstention free,
and a system optimising against that table will abstain on everything.

## The objective

Minimise expected cost-weighted risk: the sum over cases of the cost of the action taken,
given the true cause. Accuracy counts every mistake as one mistake. Your table says they
are not one mistake each. That is the whole argument.

## What the coach probably proposed and you should have rejected

Some version of *"use accuracy, or use F1, it balances precision and recall"*. F1 is a
balance chosen by someone who never saw your cost table. If your two costs differ by a
factor of ten, F1 is asserting they differ by a factor of one.
