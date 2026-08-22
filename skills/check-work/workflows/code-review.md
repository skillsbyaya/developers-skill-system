# Code Review

Independently judge whether a code change is correct enough for its residual technical risk. Report defensible findings and current evidence.

This is `check-work`'s inline review route, not an instruction to invoke Claude Code's bundled `code-review` skill. Do not call that bundled skill from this workflow.

## Resolve the review target

Use, in order:

1. an explicit diff, pull request, commit, branch, file set, story, or change-package path;
2. the user's clearly identified current change;
3. one unambiguous active record in `review`; or
4. one obvious non-default branch or change-owned working-tree diff.

Ask when several plausible targets remain. Do not review an empty or unverified diff.

Establish the source baseline, current revision, changed and untracked files in scope, requirements or acceptance sources when relevant, and material limitations. Read project context only when durable project constraints or hazards could change the review. A review-candidate brief supplies hypotheses and exposed surfaces, never findings.

A specification is optional for code-quality review. When product behaviour or acceptance is in scope, prefer an explicit story or requirement source and preserve unresolved source conflicts.

## Choose depth

Use an explicit request first, then consequence, current evidence, and residual uncertainty.

- **Focused:** one bounded change, one accepted-fix recheck, or one isolated technical uncertainty. Review inline and apply only the relevant lenses.
- **Standard:** a material multi-file or behavioural change, shared contract, meaningful user journey, or incomplete evidence. Cover implementation correctness, directly affected paths and contracts, and acceptance when an oracle exists.
- **Deep:** an explicit thorough review or critical exposure such as authentication or authorisation, tenant isolation, sensitive data, money, destructive behaviour, migrations or data loss, concurrency or consistency, consequential public contracts, broad architecture, production controls, or weak critical-path tests. Use the minimum independent lenses required by the actual risks.

Do not round depth up from file count alone. Strong current tests, narrow scope, and reliable guards reduce residual uncertainty; missing evidence, weak rollback, or high consequence increase it. State the depth and reason, then proceed unless scope is ambiguous.

For a very large change, packet by component, risk surface, or dependency path while preserving cross-cutting contracts and one main-reviewer integration pass. Ask to narrow only when the change cannot be reviewed responsibly as one coherent delivery.

## Review the change

Inspect the actual diff and enough surrounding repository evidence to understand changed call paths, data flow, contracts, failure behaviour, and tests. Review the complete change-owned surface, not only files named in a summary.

Select lenses from the risks:

- **Implementation correctness:** logic, state, error handling, lifecycle, resource use, compatibility, unnecessary complexity, and conformity with sound project patterns.
- **Adversarial:** fragile assumptions, bypasses, hidden coupling, overbuilding, and simpler implementations the change may have missed.
- **Reachable paths and boundaries:** inputs, states, transitions, permissions, retries, failure and recovery, shared callers, and directly affected contracts.
- **Acceptance:** required behaviour, constraints, omissions, contradictions, and unapproved scope.
- **Risk specialists:** security, privacy, database, legal, compliance, accessibility, performance, or other domains only when their specialist standard is actually needed.

Apply code-specific lenses inside this workflow. Do not invoke other generic assurance modes merely to create a review stack. Route to an independent specialist when the unresolved question requires authority or evidence this workflow cannot supply.

Run relevant verification commands when they materially improve the decision, without intentionally mutating source or project state. Inspect any resulting workspace changes. Never report an unperformed, stale, mismatched, or unavailable check as passed.

## Use workers only when they earn the cost

Focused and standard review stay inline by default. For critical work, or an exceptional material uncertainty that the main reviewer cannot resolve as reliably in context, use one bounded read-only evidence worker only when fresh independent judgement or clean-context inspection addresses that named uncertainty and the boundary is enforceable.

Use at most one worker automatically. More than one requires the user's explicit request for separately named review perspectives. Give the worker the current revision, exact paths, one evidence question, relevant oracle or risk, and a compact return format. The main reviewer owns target resolution, depth, source conflicts, risk decisions, deduplication, validation, persistence, user communication, and the final verdict.

If enforced read-only review is unavailable, run inline when that still satisfies the selected assurance. Otherwise name the missing evidence and keep the decision unresolved. Worker output is candidate evidence, not an accepted finding.

## Validate and classify findings

Normalise and deduplicate every candidate. Inspect the cited diff and context, try to disprove it, and keep only findings that survive.

Classify each surviving item:

- **Decision needed:** correction depends on unresolved product, architecture, data, security, or risk intent.
- **Fix:** a defect introduced or exposed by the current change with a responsible corrective direction.
- **Defer:** a real pre-existing or explicitly out-of-scope issue whose separation is safe and visible.

Drop false positives, duplicates, already handled cases, and unsupported claims from the actionable list, but report the dismissed count.

Each confirmed finding includes a concise title, class, exact evidence or location, trigger or violated expectation, plausible consequence, corrective direction, and remaining uncertainty. Do not use severity labels without explaining actual impact and reachability.

A zero-finding result is valid when the selected depth completed and limitations are explicit. It is not proof that the change is defect-free. A clean code review does not establish human experience, specialist approval, or permission to merge, release, or ship.

## Preserve only useful review state

Present confirmed findings before any implementation handoff.

When a story or change package owns the work and unresolved findings need continuity, update one `### Review Findings` section in its existing execution or review area. Preserve its current structure and findings:

- unchecked `[Review][Decision]` or `[Review][Fix]` for unresolved items;
- checked `[Review][Fixed]` only after correction and fresh focused re-review; and
- checked `[Review][Defer]` with the reason and destination when one exists.

When that project already gives durable review findings stable IDs, resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and preserve canonical `RV` identities and area suffixes through fix and re-review. Pair each ID with its finding title. Do not introduce `RV` IDs, infer the next number, or create a finding registry merely for a routine review.

Do not write individual findings into delivery status.

If no owning record exists, keep a clean or fully resolved review in conversation. When unresolved findings must survive another session, use [the convention-resolution rules](../../organise-docs/references/convention-resolution.md) and create or update the smallest `code-review-handoff` artifact. Do not create it merely to archive a review.

## Fix and re-review boundary

Resolve decision-needed items with the user before implementation. When fixes are accepted, pass the owning record, current revision, bounded findings, evidence, requirements, and success checks to `agent-dev`. Do not continue automatically from assessment into mutation.

After fixes, reconstruct the current diff, inspect or rerun affected evidence, and perform a focused re-review of every corrected surface plus any shared contract the fix changed. A prior clean review does not cover a new revision.

Mark a persisted finding fixed only after the correction and fresh affected recheck pass. Report the current result to the lifecycle owner; only Dev or session close may reconcile `review` to `done` from applicable current evidence.

## Finished result

Report the selected depth and reason, scope and revision, requirements oracle when used, checks observed, confirmed findings by class, dismissed count, missing or failed lenses, persistence location, focused re-review result when applicable, and remaining limitations or specialist evidence needed.
