# Course Correction

Use this workflow when new evidence may invalidate agreed product scope, an artifact, decomposition, priority, or active delivery. Routine defects, implementation friction, and small changes that fit the accepted promise stay with their current owner.

## Diagnose before changing state

1. Identify the new evidence or proposed change, its confidence, and the current authoritative artifact or active delivery record.
2. State what the evidence actually invalidates: assumption, requirement, scope boundary, UX decision, UI/design-system decision, architecture decision, epic/story decomposition, priority, delivery plan, or product promise.
3. Separate contained correction from material course change:
   - **Contained:** preserves the target user, product promise, accepted scope boundary, stable keys, and active priority; it can return directly to the current owner.
   - **Material:** changes one of those commitments, invalidates several artifacts, re-keys progressed work, reopens completed work, or requires comprehensive epic redesign.
4. Compare the smallest viable responses, including doing nothing, against user value, commitments, cost of delay, reversibility, and downstream invalidation.
5. Recommend one response and name the decision owner. Do not use sunk cost as a reason to preserve invalidated work.

Keep an explicit list of concepts, claims, decisions, or approaches the approved correction makes stale. A documentation owner may use that list to remove stale substance; never ask it to infer what died. When the approved change alters project-wide purpose, users, scope, direction, or structure, pass the before/after decision and stale-concepts list to the project-context owner rather than rewriting that source during diagnosis.

Stop for the user's decision before a scope cut, priority change, rollback, product-promise change, destructive removal, re-keying of progressed work, reopening completed work, or another consequential trade-off not already approved.

## Apply only an approved bounded correction

When the user asks to apply an approved contained correction:

- update only the affected requirement, plan, status row, or related product text;
- preserve stable keys and progressed lifecycle state;
- never infer `done`, silently downgrade status, or reconcile unrelated tracker structure;
- list invalidated downstream artifacts or reviews without rewriting their owners' content; and
- identify a duplicate backlog entry when the same committed work is unambiguously owned by the active artifact or tracker. If backlog reconciliation was requested, finish the correction and then select backlog planning; otherwise report the exact removal or narrowing needed.

If the change requires comprehensive requirements rewriting, epic redesign, backlog reprioritisation, UX, UI/design-system work, architecture, implementation, or assurance, stop with a compact handoff to the selected workflow or neighbouring owner. Carry the approved decision, affected paths or stable keys, current revision, invalidated assumptions, and unresolved constraints. Return to the prior active owner when the correction is contained.

Finish with the diagnosis, approved decision or unresolved choice, exact changes made, invalidated work, and current owner. Do not create a proposal document unless durable comparison or approval genuinely needs one.
