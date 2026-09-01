# Task

**1. Separate the levels.** In `docs/architecture.md`, state the case-level question and the
run-level question, who consumes each, and what goes wrong if you answer one with the other.

**2. Derive the independence rules.** Do not copy a list. Work them out from the failure
mode: what has to be true for two observers agreeing to count as two pieces of evidence?
Write the rules you derive, and for each, the failure it prevents.

**3. Design the evidence record.** `ci_triage/contracts.py` — the single structure every
observer writes. It must carry, at minimum: what was observed, the probability, whether that
probability is calibrated, what the observer read, and what it cost in money and
milliseconds. Ponytail: a dataclass. Not a framework, not a registry, not a plugin system.

**4. Encode the two states that are not the same.** "I have no evidence" and "my evidence
points equally in all directions" are different, and a uniform distribution encodes both
identically. Fix that in the contract.

**5. Test the contract.** `tests/test_contracts.py` must fail if an observer emits a
probability without declaring whether it is calibrated. That flag is the thing downstream
depends on and the thing people forget.

**6. Graded interview.** Covers phases 00–09. The independence argument is what is being
graded. Verdict to `.ci-lab/interviews/09.md`.
