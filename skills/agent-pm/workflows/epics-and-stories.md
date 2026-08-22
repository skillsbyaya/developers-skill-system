# Epics and Stories

Turn approved product scope into one authoritative, stable decomposition and its narrow active delivery-status structure. This workflow is the sole structural writer: it creates or reconciles the full approved key set, names and order, and initial status entries for unfinished committed work. It does not own implementation lifecycle, review-to-done evidence, backlog priority, or comprehensive product redesign.

If the bounded scope can be delivered responsibly without durable decomposition or tracker structure, return it to the delivery owner instead of creating planning state.

## Establish scope and authority

1. Resolve the current authoritative requirements, any applicable UX, UI/design-system, and architecture decisions, the planning scope, existing epics document, and delivery-status document.
2. Add work to the current epics document when it belongs to the same product, planning scope, owner set, and lifecycle. Create a second document only for a genuinely independent product or programme with a separate planning lifecycle, access boundary, or authoritative owner.
3. Start from an existing authoritative epics document and tracker when present. Do not regenerate stable keys or replace progressed state for tidiness.
4. Stop on unresolved conflicts that change product scope, acceptance, UX, UI/design-system direction, architecture, dependency feasibility, or priority. Route the decision to its owner rather than embedding a guess in a story.

When creating or structurally rewriting the decomposition, read [the epics-and-stories template](../templates/epics-and-stories.md).

Resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry when stable planning IDs are in use. Preserve valid current and legacy keys. Use the preferred grammar below only when an authoritative project allocator or already approved key set supplies the numbers; this workflow does not calculate or store the next number.

## Design stable decomposition

- Give each epic one valuable, independently understandable outcome and a stable key such as `E4.Invoicing`. Several related epics belong in one authoritative planning document.
- Give each story the smallest coherent user or enabling outcome that can be accepted and delivered without hidden companion work. Use `S2-E4.Invoicing` for story 2 of epic 4 so story numbering restarts within each epic; use a standalone `S3.Area` only when no epic truthfully owns it. Preserve keys across title edits.
- State why the story exists, its in-scope outcome, explicit non-goals where scope could drift, acceptance criteria, dependencies, and material product or specialist constraints.
- Write acceptance criteria as observable outcomes. Include failure, empty, permission, recovery, accessibility, privacy, migration, or rollout behaviour only where relevant to that story.
- Separate genuine dependencies from preferred order. A dependency must name the exact stable key or external decision and the condition it supplies.
- Order work to retire decisive product or technical uncertainty early while still producing coherent increments. Do not disguise priority choices as dependency logic.
- Keep implementation tasks, live progress narrative, review findings, and completed history out of the decomposition.

Size a story as one coherent delivery that benefits from one integrated review, not by estimated human effort, token budget, or one agent's capacity. Keep cross-layer work together when it shares acceptance, integration, test setup, and review reasoning. Split outcomes that can ship, be rejected, rolled back, sequenced, or reviewed independently; split when learning from one should shape the next or when combined risk becomes unsafe to assess.

A story is the acceptance and review boundary, not a promise that all implementation belongs in one session. After fixing the story boundary, shape its execution into internal work packets whenever it cannot responsibly finish in one bounded implementation-and-checkpoint session. Packets are required when a human checkpoint divides the work, when a later part can start safely from durable evidence left by an earlier part, or when separable technical outcomes would otherwise make one session carry unnecessary context. A small story may remain one packet.

Give each packet one coherent technical outcome, exact dependencies, likely change surface, narrow verification, and an explicit stop boundary. Put a hard packet boundary before and after every human checkpoint; no packet crosses one. Also split between human checkpoints when completed work can be recorded and the next part can start in a fresh session without relying on conversation history. Do not bundle every packet between two human checkpoints merely because the user will review only at the end. Packets remain internal execution units, not separate tracked stories, and one delivery session should normally select exactly one ready packet.

## Reconcile the delivery-status structure

Use the project's registered delivery-status convention when available; otherwise preserve an existing format. If no convention or status document exists, use a compact Markdown table with stable key, item, status, and last-updated fields. Delivery status is an active index, not a completed-work ledger.

- Initialise newly approved unfinished entries at `backlog` unless an authoritative current record proves a later active state. Legal active epic states are `backlog` and `in-progress`; legal active story states are `backlog`, `ready-for-dev`, `in-progress`, and `review`. `done` is preserved in the archived owning record and is not a lasting delivery-status state.
- Add approved unfinished keys and align names and order. Remove a never-started entry only when its removal is explicitly approved. Remove a completed entry only when its archived owning record supplies authoritative completion evidence; a `done` row without that archive is a lifecycle inconsistency to route to the delivery owner, not proof to manufacture an archive.
- Preserve every progressed active state and meaningful timestamp. Never downgrade, infer completion, reopen completed work, or overwrite a conflicting later state without concrete lifecycle evidence and the responsible owner's decision.
- Stop before renaming or re-keying a progressed entry, or removing one for any reason other than authoritatively proven completion close-out. Present a lineage-preserving migration delta for approval.
- Exact base-key matching must distinguish values such as `S1-E4` and `S10-E4`, while treating a corrected dotted suffix as routing rather than a new identity. Reject duplicate base keys, missing parents, cycles, dependencies on unknown keys, and stories whose stated acceptance contradicts the authoritative requirement.

When reflecting the decomposition in related navigation, status, or context artifacts, link to the authoritative epics document and state only what readers need to navigate or act. Do not copy derived story totals, terminal key ranges, or similar inventory summaries merely to describe the set; they create a second maintenance point. Include a number only when it materially supports a decision, acceptance condition, or validation result, and derive or verify it from the authority.

## Validate and finish

Validate source-requirement coverage without forcing every sentence into a story; product outcomes, critical constraints, and acceptance obligations must have an explicit destination. Check vertical value, story independence, acceptance testability, dependency validity, order, stable-key uniqueness, artifact/active-index agreement, and preservation of progressed state.

Return the authoritative epics path, delivery-status path when changed, added or reconciled active keys, completed rows removed from the active index when authoritatively supported, preserved progressed state, unresolved decisions, and the next responsible owner. Structural coherence does not by itself prove cross-artifact implementation readiness.
