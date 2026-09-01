# Prompts to adapt

```text
I have three observers: a tabular model over numeric features, a sequence model
over run history, and retrieval over failure logs. List exactly what each one
reads. Then tell me which inputs are shared between two or more of them.
```

```text
Design the record an observer writes. It must survive being averaged, compared,
and audited six months later. Do not build a registry or a plugin system — I want
one dataclass and the reason each field exists.
```

```text
Argue that letting the retrieval observer read the tabular observer's output
would improve the system. Then tell me what it would do to my ability to
interpret agreement between them.
```

```text
Write a test that fails when an observer emits a probability without saying
whether it is calibrated.
```
