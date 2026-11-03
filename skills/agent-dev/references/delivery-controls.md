# Delivery Controls

Read this reference only for direct, coordinated, or staged delivery.

## Establish ownership and evidence

Resolve the target from an explicit path or stable key, the user's clear current intent, one unambiguous active story or package, then the delivery-status index. Match a stable base key exactly; dotted areas are routing, not a separate identity. Pair the ID with its title in user-facing updates. Inspect a supplied path before classifying it.

- A prepared story owns product outcome, acceptance, constraints, and review history. Do not rewrite it into another specification.
- For a multi-packet story, the delivery unit is its current or next ready packet, even when the prompt names the whole story.
- A change package owns coordinated or staged execution only when no story owns the work and continuity or assurance justifies it.
- The request and the user's later answers own intent; code and artifacts constrain but do not override a material user choice.
- An accepted review finding keeps its owner and history. Implement only accepted items and rerun the affected evidence.
- A prepare-only or package-only request ends after validated durable state and a precise continuation boundary, before code changes.

Delivery may settle routine implementation facts about an established change. It is not a second investigation: if the cause, required fix, or consequences stop being established, stop before further edits, preserve the record and evidence, and select the investigation workflow. Resume under the existing authorisation once evidence supports the fix.

Inspect version-control state and the project's continuation source before editing. Record the baseline and classify work as change-owned, unrelated, or entangled. A documentation correction the previous close carried for this landing unit is change-owned: include it without being asked again. Continue around unrelated user changes; stop before overwriting or integrating entangled work. Refresh the baseline at packet or slice boundaries.

## Show the plan before acting

Once the plan for the unit is formed, show it in a few lines before acting: what will change, where, and any judgement call. It is not an approval gate; carry on unless it contains a decision that is the user's.

## Implement the smallest correct change

Understand the real call path, data flow, contracts, and existing behaviour. Follow the project's architecture, naming, error handling, typing, formatting, accessibility, security, and testing conventions; prefer surrounding code to generic fashion.

Stop at the first sufficient solution: no change; remove or replace obsolete code; reuse a project solution (look before you write: re-implementing a component, pattern or helper that lives a few files over is the most common slop, and new code that overlaps one says why); native or standard-library behaviour; an installed dependency; the smallest local change; an abstraction, dependency, configuration surface or scaffold only when the outcome or risk requires it. Fix defects at the lowest shared cause that preserves intended behaviour. If current behaviour already satisfies the outcome, change nothing and report the evidence.

Keep the diff cohesive: no speculative extension points, duplicated helpers, one-use abstractions, broad configuration, unrelated refactors, or file churn. Make failure behaviour explicit and update affected contracts or documentation when callers rely on them. Record a consequential ceiling and its observable upgrade trigger only when later work needs it.

For changed behaviour, establish the smallest failing or observable check first when practical. Cover acceptance conditions, meaningful edge cases, and error paths without weakening trustworthy tests. A change to a request-time read (a page render, an API handler, a database function a page calls) is checked for cost as well as correctness: independent awaits run together, one render asks each question once, a helper on a per-row path is measured by counting its calls rather than assumed cheap, and the project's latency or round-trip budget is a check like any other. Run narrow tests first, then affected lint, type or build checks, and broader regression only when shared contracts, subsystem boundaries, or risk justify it; inside a multi-packet owner, use packet coordination's safety gate and keep full story regression for completion. Never report an unperformed check as passed.

Establish claims yourself from implementation artifacts, tests, logs, rendered surfaces, and running dev behaviour when you are better placed to produce the evidence at proportionate cost. A human check is justified only when its result could change acceptance and it depends on the person's judgement or perception, assistive technology or a physical device, an app login or user-only account state, or an environment unavailable to you; an unusually heavy check the person can do reasonably well may also be delegated. State the reason for each retained human check.

Batch foreseeable user-owned decisions. Stop before dependent work when an unresolved choice, not already settled by the request or project conventions, materially affects product behaviour, UX or copy, scope, architecture, public APIs or data, dependencies or services, compatibility, security or privacy, performance or cost, rollout, destructive behaviour, review boundaries, or accepted residual risk. Implementation mechanics the requirements and conventions determine stay with you.

When evidence proves the implementation plan wrong, classify before editing its record. A change to outcome, acceptance, scope, or another user-owned constraint needs the user's decision. A technical defect in the plan may be corrected in place: keep the behaviours and tests that remain valid, amend only the bad guidance, invalidate dependent packet evidence, and rerun from the narrowest check. Keep an unrelated pre-existing issue outside this unit.

## Scale assurance to consequence

- **Routine:** bounded, reversible, isolated, non-critical, with reliable affected checks. Implementation evidence may be enough.
- **Material:** shared behaviour, a meaningful user journey, moderate blast radius, incomplete evidence, weak rollback, or acceptance uncertainty. Select one assurance method that resolves the uncertainty.
- **Critical:** authentication or authorisation, tenant isolation, sensitive data, money, destructive behaviour, migrations or data loss, concurrency or consistency, production rollout, safety, legal or compliance exposure. Require fresh independent specialist evidence, current critical-path checks, and an explicit residual-risk decision.

When unsure, keep the higher class until evidence resolves it. Route a generic assurance choice, including ordinary code review, through `check-work`; do not invoke the bundled `code-review` or `simplify` skills unless the user names one. Use a direct specialist for an already-clear testing, security, privacy, database, legal, or compliance question. A fix invalidates assurance for its surface until its checks or review are fresh.

Keep one compact completion-assurance note in the story or package (or in the evidence passed to `close-session` when no record is justified), inside the record's existing execution area: the current consequence floor and its reason; the exact surface or residual uncertainty needing attention at completion, or that none is known; reusable packet evidence with its scope, revision and invalidation trigger; and the selected completion method, or that implementation evidence should suffice. Refresh it only when a packet changes one of those facts. A later light packet does not erase an earlier material or critical exposure; lower the floor only when evidence shows the exposure is gone, and say why. Do not hide the judgement behind "review recommended", a menu of options, or silence. The session that finishes the story runs the note's completion method, as [packet coordination](packet-coordination.md#story-review-and-completion) assigns it.

A recorded manual or unavailable check is bookkeeping, not an automatic workflow: keep the observation, why current evidence cannot establish it, its scope or revision, and when it could affect acceptance. Do not turn a packet boundary or handoff into `check-work` merely because such an item exists; use its evidence disposition when the disposition is unclear.

For a completed change with observable experience, copy, interaction, accessibility use, or a manual journey, select `check-work` human preview when direct observation could change acceptance and a running candidate is available, reusing current evidence and including only unresolved observations. If preview would add little, state the reason and recommend no independent review. When the user has a standing preference for proportionate human preview, run it before the single `close-session` boundary and incorporate accepted results; this does not authorise an independent technical review.

## Reconcile state and completion

For a tracked story, Dev may write only the item it prepares or implements: `backlog → ready-for-dev → in-progress → review`, plus the parent epic's first `in-progress` transition and the completion close-out below. Preserve unrelated structure and progressed state. Do not rename, remove, re-key, downgrade, reopen `done`, or infer completion. Story evidence beats a delivery-status summary.

Only the session that finishes the story applies the close-out: after required review, otherwise after the last packet. No other packet marks the story `done`, archives it, removes its active status, transfers backlog items, or advances an orientation pointer past the owner, even when its evidence covers every acceptance criterion. Before any packet handoff or landing, inspect the delta for such completion-only mutations and remove them unless this session finishes the story.

Move the story to `review` when the selected completion condition is outstanding. Mark it `done` only on current explicit evidence: routine acceptance supported, affected checks green, the complete diff inspected, and no critical trigger, material finding, decision or evidence gap left; or required human acceptance covers the material checks, with requested edits made and checks rerun; or selected independent assurance is current with no finding unresolved and fixes rechecked; or, for critical work, specialist evidence and critical-path checks are current and residual risk is explicitly accepted.

Completing a story is one atomic outcome across its records: write the final state and evidence to the story, move the record to the project's delivery archive, remove its row from active delivery status, then use `agent-pm` backlog planning in the same delivery to remove or narrow any matching backlog item. If ownership, the archive target, or a concurrent edit prevents a safe close-out, leave the story at `review` and report the exact blocker. Backlog ambiguity does not block the close-out; preserve the ambiguous line and report it.

Release readiness controls shipping, not story completion. Implementation readiness never completes an item. **Git belongs to `close-session`:** delivery never commits, pushes or lands. Keep the record current with the code and checkpoint them together through packet close, as [packet coordination](packet-coordination.md) directs. Describe implemented behaviour, lifecycle state, and next work; never claim a commit, push, merge or deployment that has not happened, and do not duplicate Git's merge metadata in the record.

After a landing, verify any required external outcome at the existing authority boundary. A matching observation needs no record rewrite; a differing one is recorded and its correction becomes the exact next boundary.

Update authoritative project context only when delivery confirms a durable, almost-always-needed pattern or hazard; keep story progress, review history and copied next actions out of it.

Continue through the unit unless a user-owned decision, human checkpoint, safety issue, inaccessible required artifact, failed target, missing mandatory assurance, or repeated implementation failure prevents responsible progress. If work cannot finish, preserve the same continuation state; do not create a separate handoff log.

## Close delivery once

Every delivery session ends through `close-session`: packet close at a packet or slice boundary, full close for a whole unit, a story completion, or any session-end signal. Before invoking it, make sure the record or session evidence holds the outcome, change surface, checks and results, unavailable evidence and its consequence, residual risk, the assurance judgement, landing state, and the exact continuation boundary. Its change report and output are the only summary and handoff; do not write a Dev summary first or repeat the evidence afterwards. After a packet close, continue when packet coordination allows; stop after a full close.
