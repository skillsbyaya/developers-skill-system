# Edge-Case Review

Trace reachable paths, states, transitions, and boundaries in implementation, diffs, specifications, designs, experiences, or processes. Report missing handling, not general quality.

Resolve the supplied artifact or clear conversation context. Ask only when no usable target exists or several plausible targets would materially change the review. A requested focus adds an edge class but does not replace independent enumeration.

Infer the mode:

- **Implementation:** code, function, file, or diff.
- **Specification:** requirements, acceptance conditions, API, or behaviour contract.
- **Experience or process:** design, journey, workflow, operating procedure, or lifecycle.

For a diff, begin at changed lines and trace only directly reachable callers, contracts, shared state, and dependencies needed to judge the change. Do not expand a bounded review into an unrelated whole-system audit. For a full artifact, use the supplied scope.

## Enumerate from the artifact

- In implementation, walk applicable branches, inputs, loops, errors, early exits, state, timing, concurrency, external calls, data boundaries, and affected contracts.
- In a specification, walk actors, permissions, states, transitions, invalid inputs, partial success, failures, retries, recovery, timing, lifecycle, and conflicts.
- In an experience or process, walk entry and exit states, interruptions, abandonment, reversals, partial completion, accessibility conditions, conflicting actors, degraded dependencies, handoffs, and operational recovery.

For each derived condition, decide whether the artifact handles it directly or through a reliable referenced rule. Suppress handled cases.

## Validate and report

Revisit every derived edge class. Keep a finding only when the condition is reachable or relevant within scope, its handling is missing or materially ambiguous, and a plausible consequence follows. Merge duplicates and shared causes. An empty result is valid.

For each surviving finding give the precise location, triggering condition or path, missing guard/rule/state/response/recovery, realistic consequence, and smallest handling direction without applying it. Do not assign severity or priority unless requested. If nothing survives, state `No unhandled edge cases found within the reviewed scope` and name the scope limitation.
