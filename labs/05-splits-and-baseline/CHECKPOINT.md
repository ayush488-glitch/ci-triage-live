# Checkpoint

Hint: ask what a model could learn from a random split that would be useless in production
but would raise the score. Think about what all the rows from one project have in common.

1. What does a random split measure on this dataset that a grouped split does not?
2. Both splits ran the same model on the same rows. Where did the extra performance in the
   higher number come from?
3. Which split matches your deployment question, and what sentence in `PROBLEM.md` decides it?
4. Your grouped result has a large standard deviation across folds. What does that tell you
   that the mean does not?
5. Someone offers to raise your headline number by choosing the split that scores better.
   What is wrong with that, in one sentence?
