# Repair

Restore trustworthy execution without weakening the behaviour contract.

1. Reproduce with the narrowest canonical command and classify configuration or collection, environment, assertion or regression, race or flake, isolation or leakage, timeout or performance, or obsolete expectation.
2. Inspect the test, exercised source, relevant changes, fixtures, setup and teardown, and framework configuration. For a suspected flake, vary order, isolation, repetition, or concurrency only enough to expose the cause.
3. State the root-cause conclusion and evidence before a consequential change.
4. Fix test or configuration defects with event-based waits, deterministic data or time, proper cleanup, isolated fixtures, correct environment, specific assertions, or a better test boundary.
5. Rewrite or delete an obsolete expectation only when an intentional behaviour change is evidenced or the user confirms it.
6. Repeat repaired tests when flakiness was involved, then run the relevant neighbouring or broader suite.

Do not add blanket retries, longer sleeps, global serialization, disabled tests, or weaker assertions as a convenience fix. If the evidence shows a production defect, preserve the failing test as regression evidence when possible and stop with the exact defect and proposed handoff to `agent-dev`.
