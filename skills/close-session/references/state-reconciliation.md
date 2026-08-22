# State Reconciliation

Read this reference when a tracked story was touched or the session changed delivery state, backlog state, or a durable project-context fact.

Resolve the registered delivery-status, backlog, and project-context document types from current document conventions when available. Otherwise preserve the project's existing obvious paths.

## Resolve scope and one forward owner

Use this order:

1. an explicit story or change-package path or stable key;
2. one unambiguous active story or package;
3. the delivery-status entry that locates that record; or
4. the backlog only when no committed delivery owner exists.

Use that owner to derive continuation. Separately collect every story whose lifecycle changed during the session so each completed story receives close-out even when it is no longer the forward owner.

The current work record owns execution detail. Delivery status is a narrow index of unfinished committed work, not completed history. The backlog owns only uncommitted work and priority. Project context may point to delivery status for unclear or resumed work; it never owns the current task.

When sources conflict, prefer the more specific current record only when concrete evidence supports the later legal state. Otherwise stop and report the conflict.

Do not assume a mismatch is stale. Rule out concurrent work or another active session before editing a shared record; stop when ownership is uncertain.

## Delivery state and close-out

Reconcile only the current owner and session-touched items. Preserve unrelated rows and do not rename, reorder, re-key, downgrade, reopen `done`, or infer acceptance. Removing a status entry is permitted only as the required close-out of a story proven complete under the rules below.

- Dev-owned implementation may move a story through `backlog → ready-for-dev → in-progress → review`.
- `review` means implementation evidence exists but the selected completion condition is outstanding.
- A strict routine item may become `done` only when current acceptance is supported, affected checks are green, the complete finished change was inspected, and no critical trigger, material finding, unresolved decision, or consequential evidence gap remains.
- A material or critical item may become `done` only from explicit current human, independent, or specialist evidence that covers the selected completion condition, with requested fixes incorporated and affected evidence refreshed.

Never infer `done` from completed task boxes, a clean worktree, an old review, silence, or lack of objections. Release readiness controls shipping, not ordinary completion. Implementation readiness never completes delivery.

Completing a story to `done` includes its close-out in the same pass:

1. record the supported `done` state and final continuation-relevant evidence in the story;
2. move the finished story record from the active delivery folder to the project's delivery archive;
3. remove the story's row from active delivery status, updating the status document's `last_updated` only when the document remains; and
4. apply the commitment-transfer rule below to any matching backlog item.

`done` is a lifecycle result preserved in the archived story, not a permanent row in active delivery status. Leave an explicit no-active-delivery state when the status document remains but has no current entries; remove the document only when the resolved project convention and user authority permit it. Remove a parent epic's status row only when authoritative evidence proves its accepted outcome and all of its stories are closed; otherwise retain its current unfinished state.

Archiving follows the `done` gate above — it is not a new way to infer completion. A `done` status row without an archived story is an inconsistency, not independent completion evidence. Reconcile every story confirmed complete earlier in the session rather than leaving it for later cleanup. If ownership, evidence, the archive target, or a concurrent edit makes close-out unsafe, do not manufacture consistency: preserve the last supported state and report the exact mismatch.

Update a story or package with only the current lifecycle state, evidence needed for continuation or acceptance, files materially changed when that record owns them, and one exact unresolved boundary. Keep narrative history out of living state.

## Commitment transfer

If committed or completed work still appears in the backlog, invoke `agent-pm` backlog planning within the same close to remove the duplicate or narrow it to genuinely distinct uncommitted work. Do not merely recommend that cleanup for a later session. A completed or adopted item leaves the living backlog; do not move it into a completed-backlog archive. Never copy active story or delivery-status state into the backlog.

If the backlog itself is the current owner, it may retain one `(in progress)` item. Completing or adopting that item removes it rather than archiving it.

Before finishing reconciliation, verify every story completed during the session against the active delivery folder, delivery archive, active delivery-status index, and living backlog. A completed story must exist once in the archive, not remain in the active folder or active index, and have no backlog duplicate unless that line is explicitly narrowed to distinct uncommitted work. Preserve and report any mismatch that cannot be resolved safely.

## Project context

Make only bounded updates to durable, almost-always-needed facts directly established by this session. Preserve unrelated structure. Correct the stable delivery-status pointer when its target changed and is unambiguous.

Exclude current story status, next action, review evidence, backlog order, completed work, and session recap. A project-wide rebaseline belongs to `manage-project-context`.

## Continuation

Derive the next action from the active story or package, then delivery status, then backlog — what someone would actually do first, not the scope label covering the work. For a multi-packet owner, select exactly its current or next ready packet. A broad request to continue the story does not widen this boundary. Preserve the packet's outcome, prerequisites, evidence, and stop boundary in the owner so a fresh session needs no previous conversation. Report the one-packet prompt in the conversation only; do not save a separate handoff.
