# Completed-Work Retrospective

Turn evidence from a completed body of project work into a few improvements worth carrying forward. This is an optional milestone review, not mandatory ceremony or a simulated team meeting.

## Resolve the boundary and scope

- Use current correction when the primary evidence is one live interaction or delivery mistake and the goal is agent-behaviour prevention.
- Use `close-session` for routine state reconciliation and handoff maintenance.
- Use ordinary conversation for a quick reflection that does not need cross-work evidence or a durable record.
- Use `check-work` implementation readiness when the primary goal is to decide whether a future planning set is coherent enough to build.
- Use `agent-pm` course correction when new evidence may invalidate product scope, priority, planning, or active delivery.

Accept an epic, release, milestone, date-free work block, or explicit set of stories or changes. Infer the smallest clear scope from the request and current artifacts. Ask only when two plausible scopes would materially change the findings.

Read only evidence inside the selected scope: intended outcomes, story or change completion records, delivery status, relevant commits, test and review results, incidents, user or stakeholder feedback, and the most recent matching retrospective. Read project context only when needed to establish the intended outcome, durable constraints, or authoritative source paths. Treat missing evidence as a limitation, not permission to invent a team view.

If the work is materially incomplete, name the incomplete portion and ask whether a partial retrospective is still useful. Do not infer completion from an optimistic status label.

## Review the work

1. Establish the intended outcome and the evidence that can show whether it happened.
2. Extract specific successes, failures, surprises, rework, blockers, quality signals, unresolved debt, and outcome evidence.
3. Identify a recurring pattern only when it appears across more than one item or one consequential event justifies system-level prevention. Separate observation, user interpretation, and inference.
4. Check previous retrospective commitments against current evidence. Mark each met, partly met, not met, or not assessable; do not treat an absent record as failure.
5. Discuss the important findings in ordinary conversation. Frame causes as systems, decisions, and conditions rather than blame, and use specific examples. Ask for the user's perspective where records cannot explain motivation, trade-offs, or impact. Apply expert lenses inline; use a multi-perspective workflow only when the user explicitly asks for one.
6. Agree at most five improvements. Give each an observable outcome and one real destination:
   - a durable, almost-always-needed project fact to the project-context owner;
   - committed corrective work to its active story or change package;
   - genuinely uncommitted work or priority to `agent-pm` backlog planning;
   - an artifact or workflow correction to its current owner; or
   - a supported agent-behaviour correction to current correction after this workflow finishes.
7. Check whether the evidence conflicts with the next planned stage. If so, name the exact conflict and route a cross-artifact assessment to `check-work` implementation readiness or a product/delivery decision to `agent-pm` course correction. Do not silently rewrite planning artifacts.

A valid result may contain no durable improvement. Do not manufacture actions merely to fill the limit.

A retrospective request authorizes the review and its own saved record when the conditions below apply. It does not by itself authorize changes to other owners' artifacts. Apply only an exact downstream change already established and authorized before the review; otherwise finish the review, present the proposed destination and consequence, and obtain fresh authority after the exact change is known.

## Save only when useful

Respect an explicit no-write instruction. Otherwise stay in chat unless the user asks to save the review, the selected work already has a retrospective history, or agreed improvements need a durable accountability record.

When saving:

1. Resolve the `retro` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md). If it is unavailable, update an existing matching path when one is clear; otherwise return the review in chat and name the missing convention instead of inventing one.
2. Use the selected scope and a stable descriptive slug.
3. Update an existing matching review, including a legacy `epic-*-retro-*` file, rather than creating a duplicate.
4. Include only the scope and intended outcome, evidence and limitations, recurring successes, recurring problems or root causes, previous-commitment follow-through when applicable, agreed improvements with destination and observable outcome, and any next-plan conflict.

Do not reproduce dialogue, assign fictional persona owners, invent metrics, or save generic celebration.

If the current delivery tracker has one unambiguous exact retrospective key for the reviewed scope, mark only that key `done` with a minimal structure-preserving edit after the review is saved. For a partial retrospective, do so only when the user explicitly confirms that this review fulfils the tracked retrospective. Otherwise leave tracking unchanged and report any ambiguous mapping. Never use the retrospective to infer or alter epic, story, package, or release completion.

## Verify the result

- Findings cite concrete project evidence and distinguish inference.
- A one-off annoyance is not called recurring without consequential justification.
- Previous commitments are assessed only where current evidence supports a verdict.
- Improvements are few, observable, and routed to current owners.
- Project facts do not enter the global lessons queue.
- Saved output and tracker changes follow their current contracts without creating duplicate state.
