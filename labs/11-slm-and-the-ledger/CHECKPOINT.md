# Checkpoint

Hint on the ledger: at 16-bit, each parameter is 2 bytes. Adam keeps two moments per
parameter. Start there and the four lines fall out.

1. Which line of the memory ledger dominates full fine-tuning, and which technique attacks it?
2. What does quantisation cost you that the memory saving does not show?
3. Your fine-tune scores below the majority baseline. Is that a training bug or a result?
   How would you distinguish them?
4. TF-IDF beat the fine-tune by a wide margin on the same split. What does that say about
   the task, as opposed to about the model?
5. What is the small model actually good for here, and what evidence supports that role?
