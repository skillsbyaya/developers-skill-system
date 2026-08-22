# Delivery Controls

Read this reference only for direct, coordinated, or staged delivery.

## Establish ownership and evidence

Resolve the target from an explicit path or stable key, the user's clear current intent, one unambiguous active story or package, then the delivery-status index. Match a stable base key exactly, treat dotted areas as routing rather than a separate identity, and pair the ID with its title in user-facing updates. Use backlog or project context only when no committed owner exists or orientation is otherwise unclear. Inspect a supplied path before classifying it.

- A prepared story owns product outcome, acceptance, constraints, and review history. Do not rewrite it into another specification.
- For a multi-packet story, the selected delivery unit is its current or next ready packet by default, even when the user's prompt names the whole story. The story remains the acceptance owner; it is not automatically the session boundary.
- A change package owns coordinated or staged execution only when no story owns the work and durable continuity or assurance justifies it.
- A raw request and later user answers own intent; code and project artifacts provide evidence and constraints but do not override a material user choice.
- An accepted review finding keeps its existing owner and history. Implement only accepted items and rerun affected evidence; use a specialist again only when its contract or current risk requires it.
- A prepare-or-package-only request ends after validated durable state and a precise continuation boundary, before code changes.

Delivery may resolve routine implementation facts about an already established change. It must not become a second root-cause investigation path. If the cause, required fix, or material consequences cease to be sufficiently established, stop before further mutation, preserve the current record and evidence, and select the investigation workflow. Resume delivery only after investigation presents the specific proposed change and the user confirms it.

Inspect version-control state before editing. Record the baseline and distinguish change-owned, unrelated, and entangled work. Continue around clearly unrelated user changes; stop before overwriting or integrating entangled work. Refresh the baseline at packet or slice boundaries.

## Implement the smallest correct change

Understand the real call path, data flow, contracts, and existing behaviour. Follow project architecture, naming, error handling, typing, formatting, accessibility, security, and testing conventions. Prefer surrounding code to generic fashion.

Stop at the first sufficient solution: no change; remove or replace obsolete code; reuse a project solution — look before you write, because re-implementing a component, pattern, or helper that already lives a few files over is the most common slop; use native or standard-library behaviour; use an installed dependency; make the smallest local change; add an abstraction, dependency, configuration surface, or scaffold only when the approved outcome or risk requires it. When new code does overlap something that already exists, make the reuse-or-build-new call deliberately and say why, rather than quietly building parallel. Fix defects at the lowest shared cause that preserves intended behaviour.

If current behaviour already satisfies the outcome, make no code change; verify the behaviour and report the evidence.

Keep the diff cohesive. Avoid speculative extension points, duplicated helpers, one-use abstractions, broad configuration, unrelated refactors, and file churn. Make failure behaviour explicit and update affected contracts or documentation when callers rely on them. Record a known consequential ceiling and its observable upgrade trigger only when later work needs it.

For changed behaviour, establish the smallest meaningful failing or observable check first when practical. Cover acceptance conditions, meaningful edge cases, and error paths without weakening trustworthy tests. Run narrow tests first, then affected lint, type, or build checks, and broader regression only when shared contracts, subsystem boundaries, or risk justify it. Never report an unperformed check as passed.

Before assurance selection or handoff, use safe available tools and current access to establish relevant claims from implementation artifacts, tests, logs, rendered surfaces, and runnable sandbox or dev behaviour when Claude is better placed to produce the evidence at proportionate cost. Do not turn a check into human work merely because it is easy to describe, and never delegate a check Claude can perform more reliably or effectively when no human perspective is needed. A human check is justified when its result could change acceptance and it depends on the person's judgement or perception, assistive technology or physical device, app login, user-only account state or data, or an environment unavailable to Claude. A technically accessible but unusually token- or time-heavy check may also be delegated when the person can perform it reasonably and the resulting evidence will not be worse; state the reason for each retained human check.

Batch foreseeable user-owned decisions. Stop before dependent work when a choice materially affects product behaviour, UX or copy, scope, architecture, public APIs or data, dependencies or services, compatibility, security or privacy, performance or cost, rollout, destructive behaviour, review boundaries, or accepted residual risk. Routine implementation mechanics remain with the owner when requirements and project conventions determine them.

When repository, test, integration, or validated review evidence proves an implementation plan wrong, classify the conflict before editing its record. A change to outcome, acceptance, scope, or another user-owned constraint requires the user's decision. An objective technical-plan defect may be corrected in place: preserve the working behaviours and tests that remain valid, amend only the bad implementation guidance, invalidate dependent packet evidence, and rerun from the narrowest meaningful check. Fix an implementation defect in code without churning a sound plan; keep an unrelated pre-existing issue outside this delivery unit.

## Scale assurance to consequence

- **Routine:** bounded, reversible, isolated, non-critical, with reliable affected checks. Current implementation evidence may be enough.
- **Material:** shared behaviour, meaningful user journey, moderate blast radius, incomplete evidence, weak rollback, or acceptance uncertainty. Select one assurance method that resolves the material uncertainty.
- **Critical:** authentication or authorisation, tenant isolation, sensitive data, money, destructive behaviour, migrations or data loss, concurrency or consistency, production rollout, safety, legal or compliance exposure, or similarly severe consequences. Require fresh independent specialist evidence, current critical-path checks, and an explicit residual-risk decision.

When classification is uncertain, keep the higher class until evidence resolves it. Use `check-work` for a generic assurance choice or its named modes, including ordinary code review. Do not automatically invoke the bundled `code-review` or `simplify` skills; route through `check-work` unless the user explicitly requests one by name. Use a direct specialist for an already-clear testing, security, privacy, database, legal, or compliance question. Human preview is required before technical review only when experiential feedback could materially change the diff. A fix invalidates assurance for the affected surface until its checks or review are fresh.

At handoff, always make the assurance judgement visible. Name the class, recommend the single best next method, and say which remaining uncertainty it resolves; when current implementation evidence is sufficient, explicitly recommend no independent review. Do not hide the judgement behind generic “review recommended” language, a menu of equally weighted options, or silence. For critical work, name the primary next method and any mandatory subsequent gate.

For a completed change with observable experience, copy, interaction, accessibility use, or a manual journey, prefer `check-work` human preview as the immediate next method when direct observation could change acceptance and a relevant running candidate is available. Treat preview as proportionate when the remaining observations are compact enough for an in-chat check or valuable enough to justify the human-preview working artifact. Do not substitute an ad hoc list of sandbox checks for that workflow; its own rules decide whether the result belongs in the reply or a checklist artifact. If preview would add little because current evidence already establishes the change, no material human judgement remains, the environment is unavailable, or constructing the walkthrough would be disproportionate to the uncertainty, state that reason and recommend a lighter method or no review.

When the user has established a standing preference for proportionate human preview, completed Dev delivery authorises it as the separately selected next workflow; finish the Dev mutation and handoff boundary, then continue with `check-work` human preview without asking the user to choose it again. This does not authorise an independent technical or specialist review.

## Reconcile state and completion

For a tracked story, Dev may write only the item it prepares or implements: `backlog → ready-for-dev → in-progress → review`, plus the parent epic's first `in-progress` transition and the story's completion close-out below. Preserve unrelated structure and progressed state. Do not rename, remove, re-key, downgrade, reopen `done`, or infer completion. Story evidence beats a delivery-status summary; ask when conflicting evidence does not support one legal state clearly.

Move implementation to `review` when the selected completion condition remains outstanding. Mark the owning story record `done` only on current explicit evidence:

- routine acceptance is supported, affected checks are green, the complete diff is inspected, and no critical trigger, material finding, decision, or evidence gap remains;
- required human acceptance explicitly covers the material checks or named non-critical exposure, with requested edits incorporated and affected checks rerun;
- selected independent assurance is current, no required finding remains unresolved, and fixes received a fresh affected recheck; or
- critical specialist evidence and critical-path checks are current, no mandatory control or material finding remains unresolved, and residual risk is explicitly accepted.

Completing a tracked story is one atomic lifecycle outcome across its delivery records: write the supported final state and evidence to the story, move the story record to the project's delivery archive, and remove its row from active delivery status. `done` belongs in the archived story, not as a lasting delivery-status row. Then use `agent-pm` backlog planning in the same delivery to remove or narrow any matching backlog item. If ownership, the archive target, or a concurrent edit prevents safe story close-out, leave the story at `review` and report the exact blocker instead of creating a partially closed delivery state. Backlog ambiguity does not reopen or block an otherwise valid story close-out; preserve the ambiguous backlog line and report that exact remaining mismatch.

Release readiness controls shipping, not ordinary story completion. Implementation readiness never completes a delivery item. Commit only when requested or clearly within the user's delivery instruction. Immediately before any commit or push, read [Commit and push safety](commit-and-push-safety.md).

Update authoritative project context only when delivery confirms a durable, almost-always-needed project pattern or hazard. Preserve its structure and exclude story-specific progress, review history, and copied next actions.

Continue through the selected unit unless a user-owned decision, safety issue, inaccessible required artifact, failed target, missing mandatory assurance, or repeated implementation failure prevents responsible progress. For coordinated or staged delivery, the selected unit is one packet unless packet coordination records the narrow inseparability exception. On packet completion, preserve the current owner, evidence, and exact next boundary, then stop for close-session handoff rather than starting the next packet. If work cannot finish, preserve the same continuation state; do not create a separate handoff log.

## Delivery handoff

Lead with the implemented outcome. Report the material change surface, checks and results, unavailable evidence and consequences, residual risk, and commit or dev-target result when applicable. State the assurance class and recommendation from the rules above. When a record exists, name it and its current state or exact continuation boundary. Do not prepare or run an independent technical or specialist review automatically. Do not give the user unnecessary sandbox or dev checks that Claude would perform better; distinguish those from checks requiring the user's login, environment, device, or judgement and from proportionately delegated high-cost checks. If proportionate human preview is the selected next action, do not reproduce its walkthrough as Dev handoff prose; give only the environment entry point and any prerequisite the preview workflow needs.
