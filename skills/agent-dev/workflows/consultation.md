# Engineering Consultation

Use this workflow for engineering advice, implementation planning, route choice, or Git-workflow setup and audit. Advice may be the complete result.

## Frame the engineering question

Establish the intended outcome, available evidence, current constraints, and the decision the user needs. Inspect existing code or artifacts only when they would change the answer. Ask one focused question only when a material ambiguity cannot be resolved from the current project.

Identify whether the next job is diagnosis, implementation, assessment, test-system work, release assurance, product work, or a durable architecture decision. When the user wants diagnosis performed rather than advice about it, finish or checkpoint consultation and select this skill's investigation workflow. Name a specialist boundary without forcing a handoff when bounded advice is still useful.

## Develop the advice

- Trace the likely call path, data flow, contracts, and failure surface before recommending a change.
- Stop at the first sufficient approach: no change; remove or replace obsolete behaviour; reuse a project solution; use native or standard-library behaviour; use an installed dependency; make the smallest local change; add an abstraction, dependency, or configuration surface only when the outcome or risk requires it.
- Prefer the lowest shared root-cause fix that preserves intended behaviour. Distinguish evidence from hypotheses when the cause is not established.
- Compare options by correctness, failure behaviour, compatibility, reversibility, operational assumptions, maintenance burden, and verification cost. Keep user-owned decisions visible.
- Recommend the smallest meaningful check first, then broader or independent assurance only when consequence, uncertainty, or blast radius earns it.

When the request is to set, change, or audit branching and release conventions, read [Project Git workflow](../references/project-git-workflow.md). Do not load that reference for ordinary engineering advice.

## Finish

Return the outcome or decision, material evidence and assumptions, recommended approach, important risks or tradeoffs, and proportionate verification. Include a next step only when useful. Do not begin delivery unless the user asked for implementation.
