# Architecture Decisions

Create, update, or validate a durable technical architecture artifact that guides consistent implementation without duplicating product requirements, UX decisions, UI/design-system decisions, delivery state, or specialist standards.

## Choose the operation

- **Create:** no current architecture artifact owns the scope and a durable record will improve implementation, maintenance, or later assurance.
- **Update:** a current artifact owns the scope. Preserve still-valid decisions and stable identifiers; change only what new evidence or an authorised decision affects, and reconcile dependent sections.
- **Validate:** assess the current architecture for coherence, decision completeness, evidence honesty, and usefulness to implementation. Return findings without editing unless revision is requested.
- **One-pass or headless:** produce the best complete artifact from supplied evidence without a staged interview. Label assumptions, deferred choices, and missing evidence. Record evidence-backed recommendations as proposed; stop rather than silently marking a material product, security, compliance, operational, or unresolved architecture choice as accepted.

One-off advice belongs in consultation. A formal request selects this workflow directly; consultation is not required first.

A request to create or update the artifact authorises writing it, but not silently accepting a consequential unresolved choice. Mark a decision accepted only when current authoritative evidence or the user's decision supports that status.

For a broad “validate and update,” “review and fix,” or similar request, validate first. If the assessment determines the target, scope, mechanism, risk, reversal condition, or accepted trade-off of the change, present the exact proposed artifact edits and obtain fresh confirmation before writing. Continue without another confirmation only when the requested edits and their material consequences were already bounded and authorised.

## Resolve scope, authority, and sources

1. Identify the architecture scope, intended downstream use, current artifact, current system or baseline, accepted decisions, and the revision being changed or assessed.
2. Inspect supplied and clearly relevant current sources: requirements, UX decisions, UI/design-system decisions, research, existing architecture or decision records, project context, code and infrastructure for brownfield work, delivery constraints, and specialist findings. These are inputs, not mandatory predecessors.
3. Distinguish binding requirements, observed current state, accepted architecture decisions, proposals, assumptions, and recommendations. Preserve user-owned choices and specialist decisions unless current evidence materially conflicts.
4. When sources conflict, identify the exact incompatible claims and their owners. Resolve from established authority and recency when possible; otherwise stop on the decision rather than hiding the conflict in prose.
5. Research only volatile choices that could change the architecture. Prefer official documentation, standards, and primary vendor sources; record the source and access date near the affected decision. Verify version compatibility as a set, not as isolated “latest” numbers.

Read each selected authoritative source deeply enough to preserve every architecture-affecting decision and constraint. Do not claim coverage from a filename, index, generated summary, or partial scan.

Do not require a PRD, UX specification, UI specification, epic set, starter template, greenfield structure, or fixed artifact sequence when the scoped decision can be made responsibly from other evidence.

## Define the architecture

Cover only decisions the scope earns. Typical decision areas are:

- purpose, scope, constraints, quality attributes, and explicit non-goals;
- system decomposition, component or service responsibilities, ownership, and dependency direction;
- interfaces, protocols, external integrations, contracts, and compatibility;
- data ownership, model boundaries, consistency, lifecycle, retention implications, and migrations;
- identity, trust boundaries, authorisation, secrets, threat-relevant controls, and specialist dependencies;
- failure modes, retries, idempotency, resilience, degradation, recovery, and disaster considerations;
- runtime, framework, storage, infrastructure, environments, deployment, configuration, and observability choices;
- performance, capacity, scalability, operational burden, and cost controls;
- rollout, migration, coexistence, rollback, and reversibility;
- implementation consistency rules only where independent implementers could otherwise make incompatible choices; and
- test seams, evidence needs, assurance implications, unresolved decisions, and review triggers.

Use diagrams, directory trees, schemas, or matrices only when they materially clarify boundaries, sequence, data flow, deployment, ownership, or requirement coverage. Define enough structure to enforce the architecture; do not predict every future file.

For each consequential decision, record:

- a stable identifier and status such as proposed, accepted, deferred, superseded, or rejected;
- the decision and scope;
- rationale and evidence;
- viable alternatives and why they were not selected;
- implementation, operational, security, data, migration, cost, and testing implications that are material; and
- assumptions, risks, reversal conditions, and the next review trigger.

When drafting or structurally rewriting, read [the architecture template](../templates/architecture.md). Adapt it to the scope and omit sections that add no decision value.

When decisions use durable IDs, resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry. Preserve current and legacy identities. Use forms such as `A13.Invoicing.Delivery` only when an authoritative project allocator or approved key set supplies the base number; this workflow does not infer the next architecture number.

## Write safely

Resolve the `architecture` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md) when available. Reuse one current artifact for the same scope and update it in place. If several plausible artifacts exist and authority cannot be inferred, ask the user to choose. If no convention exists, use a supplied path or agree one before creating a durable file.

A different durable architecture scope may earn a separate area-specific architecture document under the registered naming convention. Decision base IDs remain project-stable across those documents; area suffixes route retrieval and do not restart or replace identity. Do not append unrelated architecture areas into one file merely to avoid another document.

Preserve accepted decisions, identifiers, source links, and unaffected content. Replace stale claims rather than appending a workflow diary. Mark superseded decisions and point to their replacement when history is needed for interpretation; version control remains the default history.

Do not copy detailed architecture into project context or delivery state. If a newly accepted project-wide constraint belongs in the almost-always-needed context snapshot, return a bounded before/after handoff to `manage-project-context`.

## Validate and finish

Check:

- the design addresses the scoped outcomes, constraints, and quality attributes;
- decisions are mutually compatible and do not contradict authoritative product, UX, UI/design-system, or specialist sources;
- boundaries, interfaces, data ownership, failure handling, security, operations, migration, observability, cost, and testability are covered where material;
- implementers can tell what is fixed, flexible, deferred, prohibited, and likely to reverse;
- assumptions and evidence limits are visible;
- the architecture is neither under-specified at conflict points nor over-specified where implementation should remain free; and
- open critical decisions are not disguised as readiness.

For validation, use one verdict:

- **SUFFICIENT FOR THE SCOPED TECHNICAL DECISIONS**
- **USABLE WITH STATED LIMITATIONS**
- **NOT SUFFICIENT**

This is an architecture-only verdict. It does not replace `check-work implementation-readiness`, which compares the complete planning set.

Return the operation, scope, artifact path or assessed source, verdict when validating, decisions added or changed, superseded decisions, evidence and version checks, assumptions, unresolved blockers, downstream impacts, and next owner when another action is actually needed. Do not automatically begin implementation, mutate infrastructure, or start assurance.
