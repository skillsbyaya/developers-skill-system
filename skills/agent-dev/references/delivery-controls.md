# Delivery Controls

Read this reference only for direct, coordinated, or staged delivery.

## Establish ownership and evidence

Resolve the target from an explicit path or stable key, the user's clear current intent, one unambiguous active story or package, then the delivery-status index. Match a stable base key exactly, treat dotted areas as routing rather than a separate identity, and pair the ID with its title in user-facing updates. Use backlog or project context only when no committed owner exists or orientation is otherwise unclear. Inspect a supplied path before classifying it.

- A prepared story owns product outcome, acceptance, constraints, and review history. Do not rewrite it into another specification.
- For a multi-packet story, the selected delivery unit is exactly its current or next ready packet, even when the user's prompt names the whole story. The story remains the acceptance owner; it is not the implementation-session boundary.
- A change package owns coordinated or staged execution only when no story owns the work and durable continuity or assurance justifies it.
- A raw request and later user answers own intent; code and project artifacts provide evidence and constraints but do not override a material user choice.
- An accepted review finding keeps its existing owner and history. Implement only accepted items and rerun affected evidence; use a specialist again only when its contract or current risk requires it.
- A prepare-or-package-only request ends after validated durable state and a precise continuation boundary, before code changes.

Delivery may resolve routine implementation facts about an already established change. It must not become a second root-cause investigation path. If the cause, required fix, or material consequences cease to be sufficiently established, stop before further mutation, preserve the current record and evidence, and select the investigation workflow. Resume delivery only after investigation presents the specific proposed change and the user confirms it.

Inspect version-control state and the project's existing continuation or next-action source before editing. Record the baseline and distinguish change-owned, unrelated, and entangled work. A local documentation correction explicitly carried by the previous close is change-owned continuation for its named landing unit: preserve it and include it without requiring the user to repeat the instruction. Continue around clearly unrelated user changes; stop before overwriting or integrating entangled work. Refresh the baseline at packet or slice boundaries.

## Implement the smallest correct change

Understand the real call path, data flow, contracts, and existing behaviour. Follow project architecture, naming, error handling, typing, formatting, accessibility, security, and testing conventions. Prefer surrounding code to generic fashion.

Stop at the first sufficient solution: no change; remove or replace obsolete code; reuse a project solution — look before you write, because re-implementing a component, pattern, or helper that already lives a few files over is the most common slop; use native or standard-library behaviour; use an installed dependency; make the smallest local change; add an abstraction, dependency, configuration surface, or scaffold only when the approved outcome or risk requires it. When new code does overlap something that already exists, make the reuse-or-build-new call deliberately and say why, rather than quietly building parallel. Fix defects at the lowest shared cause that preserves intended behaviour.

If current behaviour already satisfies the outcome, make no code change; verify the behaviour and report the evidence.

Keep the diff cohesive. Avoid speculative extension points, duplicated helpers, one-use abstractions, broad configuration, unrelated refactors, and file churn. Make failure behaviour explicit and update affected contracts or documentation when callers rely on them. Record a known consequential ceiling and its observable upgrade trigger only when later work needs it.

For changed behaviour, establish the smallest meaningful failing or observable check first when practical. Cover acceptance conditions, meaningful edge cases, and error paths without weakening trustworthy tests. Run narrow tests first, then affected lint, type, or build checks, and broader regression only when shared contracts, subsystem boundaries, or risk justify it. During a coordinated or staged implementation packet, use packet coordination's minimum safety gate and reserve full story regression for the separate story-completion session. Never report an unperformed check as passed.

Before assurance selection or handoff, use safe available tools and current access to establish relevant claims from implementation artifacts, tests, logs, rendered surfaces, and runnable sandbox or dev behaviour when Claude is better placed to produce the evidence at proportionate cost. Do not turn a check into human work merely because it is easy to describe, and never delegate a check Claude can perform more reliably or effectively when no human perspective is needed. A human check is justified when its result could change acceptance and it depends on the person's judgement or perception, assistive technology or physical device, app login, user-only account state or data, or an environment unavailable to Claude. A technically accessible but unusually token- or time-heavy check may also be delegated when the person can perform it reasonably and the resulting evidence will not be worse; state the reason for each retained human check.

Batch foreseeable user-owned decisions. Stop before dependent work when a choice materially affects product behaviour, UX or copy, scope, architecture, public APIs or data, dependencies or services, compatibility, security or privacy, performance or cost, rollout, destructive behaviour, review boundaries, or accepted residual risk. Routine implementation mechanics remain with the owner when requirements and project conventions determine them.

When repository, test, integration, or validated review evidence proves an implementation plan wrong, classify the conflict before editing its record. A change to outcome, acceptance, scope, or another user-owned constraint requires the user's decision. An objective technical-plan defect may be corrected in place: preserve the working behaviours and tests that remain valid, amend only the bad implementation guidance, invalidate dependent packet evidence, and rerun from the narrowest meaningful check. Fix an implementation defect in code without churning a sound plan; keep an unrelated pre-existing issue outside this delivery unit.

## Scale assurance to consequence

- **Routine:** bounded, reversible, isolated, non-critical, with reliable affected checks. Current implementation evidence may be enough.
- **Material:** shared behaviour, meaningful user journey, moderate blast radius, incomplete evidence, weak rollback, or acceptance uncertainty. Select one assurance method that resolves the material uncertainty.
- **Critical:** authentication or authorisation, tenant isolation, sensitive data, money, destructive behaviour, migrations or data loss, concurrency or consistency, production rollout, safety, legal or compliance exposure, or similarly severe consequences. Require fresh independent specialist evidence, current critical-path checks, and an explicit residual-risk decision.

When classification is uncertain, keep the higher class until evidence resolves it. Use `check-work` for a generic assurance choice or its named modes, including ordinary code review. Do not automatically invoke the bundled `code-review` or `simplify` skills; route through `check-work` unless the user explicitly requests one by name. Use a direct specialist for an already-clear testing, security, privacy, database, legal, or compliance question. Human preview is required before technical review only when experiential feedback could materially change the diff. A fix invalidates assurance for the affected surface until its checks or review are fresh.

Maintain one compact, current completion-assurance note in the authoritative story or package when one exists, or in the session evidence passed to close-session when no record is justified. Adapt to the record's existing execution area rather than creating a separate artifact or packet-by-packet log. Keep exactly the decision-relevant state:

- the current consequence floor — routine, material, or critical — and the concrete reason;
- the exact surface or residual uncertainty needing attention at completion, or an explicit statement that no attention beyond current affected checks and complete-diff inspection is known;
- reusable packet evidence, with its scope or revision and any limitation or invalidation trigger; and
- the selected completion condition and single best assurance method, or an explicit recommendation that routine implementation evidence should suffice.

Refresh the note only when a packet changes one of those facts. A later light packet does not erase an earlier material or critical exposure; lower the floor only when current evidence shows the exposure was removed or made unreachable, and record why. Do not hide the judgement behind generic “review recommended” language, a menu of equally weighted options, or silence. For critical work, name the primary next method and any mandatory subsequent gate.

During a named implementation packet or slice, update that note for the separate owner-completion boundary but do not run its method merely because this is the last packet. Broad packet checks, direct observation, or acceptance evidence do not widen the selected unit. The final packet may establish that implementation is ready for completion assurance; it cannot itself satisfy the owning story's or package's completion condition.

Recording a manual or unavailable check is evidence bookkeeping, not an automatic assurance workflow. Preserve the observation, why current evidence cannot establish it, the relevant scope or revision, and when it could affect acceptance. Do not turn a packet boundary or handoff into `check-work` merely because such an item exists. If its disposition is unclear, use `check-work` evidence disposition; select human preview only when an assurance or completion decision is being made and the observation remains material on an available current candidate.

For a standalone completed change or story-completion decision with observable experience, copy, interaction, accessibility use, or a manual journey, select `check-work` human preview when direct observation could materially change acceptance and a relevant running candidate is available. Reuse accumulated current evidence and include only unresolved observations; do not rerun earlier packet checks merely because completion is now being decided. If preview would add little because current evidence already establishes the change, no material human judgement remains, the environment is unavailable, or constructing the walkthrough would be disproportionate to the uncertainty, state that reason and recommend no independent review or preserve the limitation.

When the user has established a standing preference for proportionate human preview, completed Dev delivery authorises it as the separately selected next workflow. Run `check-work` human preview before the single close-session boundary, incorporate any accepted result and refresh affected evidence, then close delivery once. This does not authorise an independent technical or specialist review.

## Reconcile state and completion

For a tracked story, Dev may write only the item it prepares or implements: `backlog → ready-for-dev → in-progress → review`, plus the parent epic's first `in-progress` transition and the story's completion close-out below. Preserve unrelated structure and progressed state. Do not rename, remove, re-key, downgrade, reopen `done`, or infer completion. Story evidence beats a delivery-status summary; ask when conflicting evidence does not support one legal state clearly.

The completion close-out below is available only in a separately selected whole-story completion session, never inside a named implementation packet or slice. A final packet leaves the story at `review`, keeps its record active, keeps its delivery-status ownership, and points continuation at story completion. It must not mark the story `done`, archive it, remove its active status, perform completion-only backlog transfer, or advance an orientation pointer to a later story—even when its packet evidence happens to cover every acceptance criterion. Apply the recorded assurance method and the completion rule only after starting that separate boundary.

Move implementation to `review` when the selected completion condition remains outstanding. Mark the owning story record `done` only on current explicit evidence:

- routine acceptance is supported, affected checks are green, the complete diff is inspected, and no critical trigger, material finding, decision, or evidence gap remains;
- required human acceptance explicitly covers the material checks or named non-critical exposure, with requested edits incorporated and affected checks rerun;
- selected independent assurance is current, no required finding remains unresolved, and fixes received a fresh affected recheck; or
- critical specialist evidence and critical-path checks are current, no mandatory control or material finding remains unresolved, and residual risk is explicitly accepted.

Completing a tracked story is one atomic lifecycle outcome across its delivery records: write the supported final state and evidence to the story, move the story record to the project's delivery archive, and remove its row from active delivery status. `done` belongs in the archived story, not as a lasting delivery-status row. Then use `agent-pm` backlog planning in the same delivery to remove or narrow any matching backlog item. If ownership, the archive target, or a concurrent edit prevents safe story close-out, leave the story at `review` and report the exact blocker instead of creating a partially closed delivery state. Backlog ambiguity does not reopen or block an otherwise valid story close-out; preserve the ambiguous backlog line and report that exact remaining mismatch.

Release readiness controls shipping, not ordinary story completion. Implementation readiness never completes a delivery item. Commit only when requested or clearly within the user's delivery instruction. Immediately before any commit or push, read [Commit and push safety](commit-and-push-safety.md).

**Land the record with the code.** Every document the change makes stale — the story or package record, the delivery-status entry, the orientation or next-action pointer — belongs in the same landing unit as the code under the project's declared Git workflow; they stop being true at the same instant. A later pass to reconcile them is not tidiness, it is a second full review-and-verification cycle for work that was already done, and it leaves the repository briefly contradicting itself. If a close, a review or a handoff later finds that state adrift, treat it as a defect in the delivery that left it, not as new work the process was always going to need.

Before landing a named packet or slice, inspect its complete diff specifically for completion-only lifecycle mutations: `done`, an archive move, active-status removal, backlog close-out, or an orientation pointer beyond the current owner. Remove those mutations unless the selected unit is the separate story- or package-completion boundary, then rerun affected document checks. This diff gate applies even when the final packet also ran broad tests, direct observation, or acceptance checks.

Some facts become true only after that landing unit closes: a merge completes, a migration or function is applied, a deployment is observed, or an external checkpoint resolves. Update every authoritative document that this new fact makes stale while the evidence is current. When project policy would require a separate commit or pull request solely to publish that factual correction, keep the correction locally and carry it in the next already-required landing unit; do not spend another full review-and-verification cycle to restate completed work. Update the owner when it owns the fact, and record the pending paths and landing route in the project's existing continuation or next-action source so the next delivery can adopt them without another user instruction. Close-session repeats that durable state in its paste-ready handoff. If delayed publication would mislead another active actor or make the next action unsafe, make landing the correction the exact next boundary instead.

Update authoritative project context only when delivery confirms a durable, almost-always-needed project pattern or hazard. Preserve its structure and exclude story-specific progress, review history, and copied next actions.

Continue through the selected unit unless a user-owned decision, human checkpoint, safety issue, inaccessible required artifact, failed target, missing mandatory assurance, or repeated implementation failure prevents responsible progress. For coordinated or staged delivery, the selected unit is exactly one packet. If work cannot finish, preserve the same continuation state; do not create a separate handoff log.

## Close delivery once

Every completed or stopped Agent Dev delivery session ends through `close-session`, regardless of whether delivery used direct, coordinated, or staged execution. Use packet close whenever the selected unit is a named implementation packet or slice; use full close for a whole direct-delivery unit, story-completion session, or other delivery boundary. A natural user session-end signal still selects full close.

Before invoking it, ensure the authoritative record or current session evidence contains the outcome, material change surface, checks and results, unavailable evidence and consequence, residual risk, assurance judgement, landing state, and exact continuation boundary. Then load the selected close-session workflow. Its output is the only completion summary and handoff: do not emit an Agent Dev summary first or repeat the same evidence afterwards. Stop when close-session finishes.
