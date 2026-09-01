# Checkpoint

Hint on the arbiter: before asking why it performed badly, look at what was in its prompt.
Not what you intended to put there — what was actually rendered.

1. Two observers output the same label. Why is that not enough to call it agreement?
2. Your LLM fusion is worse than the majority baseline on accuracy *and* on calibration.
   What does being worse on both at once tell you?
3. Four observers, one of which saw a real pass/fail flip and three of which saw nothing.
   What does the mean do to that observation?
4. Your pipeline reports unanimous agreement. What would you check before believing it?
5. What must an arbiter be given before its output means anything, and what should it never
   be allowed to do?
