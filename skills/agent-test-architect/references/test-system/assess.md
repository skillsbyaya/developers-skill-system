# Assess

Assessment is read-only.

For a vague routing request, inspect only enough evidence to determine whether framework and commands are coherent, representative test levels exist, tests run, and an obvious critical gap or reliability defect changes the next step. Return one recommended operation without turning the check into a repository-wide audit.

For a requested health or gap assessment:

1. Inventory the relevant frameworks, scripts, levels, fixtures, helpers, CI execution, and measured coverage configuration.
2. Run canonical tests when safe. Separate configuration or collection failures, deterministic failures, suspected flakes, skips, performance problems, and unavailable dependencies.
3. Sample across risk-relevant routes, APIs, modules, stories, specifications, or recent changes.
4. Classify the highest-value needs as infrastructure, missing behaviour coverage, obsolete or low-signal tests, broken execution, or an interacting suite-level problem.

Return what exists, what works, the highest-risk gaps, evidence and limitations, and the recommended next operation. Create or update a durable test review only when requested, an existing review owns the scope, or continuation and handoff genuinely need it; resolve the `test-review` row through [the convention-resolution rules](../../../organise-docs/references/convention-resolution.md).
