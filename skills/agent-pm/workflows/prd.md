# Product Requirements Document

Create, update, or validate the authoritative product requirements for an agreed scope. A PRD owns product behaviour and acceptance intent; it does not replace UX interaction design, UI/design-system decisions, architecture decisions, delivery decomposition, or execution state.

## Choose the operation

- **Create:** requirements are settled enough to justify a durable specification and no current PRD owns the scope.
- **Update:** a current PRD owns the scope. Preserve valid requirements, identifiers, and accepted decisions; edit only affected sections and reconcile dependent requirements.
- **Validate:** assess the current PRD against its intended use and return findings unless revision is requested.
- **One-pass or headless:** produce the best complete draft from supplied inputs without interaction, clearly marking assumptions, open decisions, and missing evidence instead of inventing them. If the intended artifact or a material scope decision remains ambiguous, return `blocked` with the reason and do not create an artifact; otherwise report `complete` or `partial`, the operation, artifact path, assumptions, and open decisions.

For interactive creation, use a fast full-draft path when the supplied material is strong. Use collaborative coaching when the product thesis, user journey, scope, or trade-offs remain thin. Elicit the user's vision; when they are stuck, offer a concrete hypothesis to react to without silently making their product decision.

When drafting or structurally updating, read [the PRD template](../templates/prd.md). Adapt it to the product; do not fill sections with placeholder prose merely for completeness.

When the PRD uses durable requirement IDs, resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry. Preserve current or legacy identifiers. Use the new grammar only when the project has an authoritative allocator or key set; this workflow does not invent the next requirement number.

## Establish authority and inputs

1. Resolve the product, scope, intended decision or downstream use, current PRD, and accepted source decisions.
2. Reconcile supplied briefs, research, approved course corrections, UX, UI/design-system, or architecture constraints, and existing requirements. Later accepted decisions outrank older prose; specialist artifacts remain authoritative within their domains.
3. Surface a conflict before rewriting another owner's decision. Ask only when the conflict would materially change requirements.

## Define requirements

- State the product outcome, target users, problem, scope, and non-goals.
- Express functional requirements as observable behaviour with project-stable identifiers such as `FR7.Invoicing`. Preserve identifiers across updates; retire rather than reuse an identifier.
- Define measurable success outcomes and product acceptance conditions. Avoid proxy metrics without explaining what they indicate.
- Add counter-metrics when a success measure could drive harmful optimisation.
- Include constraints, policy or compliance needs, data and privacy expectations, accessibility outcomes, dependencies, rollout considerations, risks, assumptions, and open questions only where they affect product behaviour or acceptance.
- Separate required behaviour from implementation suggestions. Refer durable UX, UI/design-system, or architecture decisions to their owners rather than embedding competing specifications.
- Make priorities explicit enough to support trade-offs. Do not silently promote desirable ideas into committed requirements.

Scan for the concerns the product actually carries—such as regulated data, integrations, public APIs, operational service levels, monetisation, hardware, migration, or change adoption—and add only the sections those concerns need. Use stable terminology and a glossary when domain terms could drift. Capture user journeys when sequence, roles, or experiential decisions matter; do not manufacture persona or journey furniture for a simple single-operator tool.

## Validate

Check decision readiness, substance over document theatre, strategic coherence, acceptance clarity, scope honesty, fit to the product's actual shape, internal consistency, evidence honesty, stable terminology and identifier continuity, traceability from user problem to requirement and acceptance, feasibility dependencies, and conflicts with current UX, UI/design-system, architecture, epics, or commitments. Classify findings as blocking, material, or minor according to their effect, not wording quality.

For validation-only work, return a verdict of **ready**, **ready with stated limitations**, or **not ready**, followed by evidence-grounded findings. Do not edit the PRD unless asked. After any fix, reassess affected findings against the current revision.

Return the artifact path or assessed source, operation, verdict when validating, material decisions, assumptions, and unresolved blockers. A valid PRD is not by itself an implementation-readiness verdict.
