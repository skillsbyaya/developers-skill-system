# Full Close

Use this workflow after Agent Dev completes or stops delivery work that is not a named implementation packet or slice, and whenever the user signals that the current working session is ending, including “stop for today.” Close the current session completely: tie up its loose ends, preserve anything later work needs, and make any continuation safe to start in a new session. Do not resume active work after the close output.

## Establish the close surface

Use the current conversation and session evidence to identify:

1. what this session changed and the authoritative record, if any, that owns its state;
2. whether the work is complete, active, blocked, or interrupted;
3. session-owned files or records and any unrelated or entangled changes;
4. concise version-control state: current branch, session-owned uncommitted work, local-only or pushed commits, and an existing pull request or landing only when relevant; and
5. decisions, ideas, constraints, rejected approaches, or corrections that exist only in the conversation.

Inspect only session-touched paths, the current owner, and the minimum version-control evidence needed to classify the state. When the current owner is complete, this scope may also include the single authoritative backlog or plan that orders next work. Do not survey the repository or document set. If a previous full close already ran in this conversation, inspect only changes since that close.

## Choose the necessary depth

Start with a routine close. Escalate to knowledge-rich capture only when the conversation contains several material decisions, ideas, new constraints, or rejected approaches that remain unwritten, or one interconnected decision set whose relationships would be lost by recording a single fact. Message count, elapsed time, and ordinary implementation detail do not justify escalation.

For a routine close, write only a missing current status, exact continuation boundary, or durable fact that later work genuinely needs.

When the knowledge-rich gate is met, read [Knowledge capture](../references/knowledge-capture.md). Do not load that reference for a routine close.

## Tie up actual loose ends

For active or interrupted work, ensure one authoritative owner records the supported current state, evidence later work needs, material unresolved decisions or risks, and one exact next boundary. Update every authoritative document already identified by the session that the work or its post-landing actions made materially stale; use current evidence and correct only unambiguous session-caused omissions rather than surveying for hypothetical documentation work.

Read [State reconciliation](../references/state-reconciliation.md) only when a story's lifecycle changed during this session or concrete evidence shows its active record, archive, delivery-status entry, backlog counterpart, or project-context pointer may disagree. Verify and repair only session-caused, unambiguous drift. If safe repair requires reconstructing history, changing product intent, or resolving ownership, leave the last supported state and make that mismatch the next-session action.

Do not invent a new priority during close. If no unfinished owned work remains, inspect only the authoritative ordered backlog or current project plan needed to identify the next explicit item. Use that item when the order is unambiguous; otherwise the next action is for the user to decide where the project should go next.

## Handle Git conditionally

An active multi-packet story waiting for another packet or its story-completion session remains uncommitted by default. Do not read Git close or create a packet commit merely because the session is ending. Use a local checkpoint commit only when Agent Dev recorded a concrete recovery, concurrent-work, branch-switching, or large-overlapping-diff need.

For other session-owned Git work, read [Git close](../references/git-close.md) only when a completed unit has not reached the landing state already authorised by the user's work request and the declared project workflow. Finish that authorised non-live landing when checks and policy allow it. Never treat a close signal alone as authority for a live push, release, deployment, destructive operation, or unrelated work. If the unit is incomplete, entangled, failing required checks, or lacks landing authority, preserve its exact state for the next session instead of forcing a clean worktree.

When an already-landed unit leaves only factual documentation corrections and project policy would require a new commit or pull request solely to publish them, preserve the corrected local files for the next already-required landing unit. Record their paths and intended landing boundary in the project's existing continuation or next-action source, falling back to the current owner only when no such source exists, and repeat them in the handoff. Do not repeat a full landing cycle merely to record that the previous one completed. If delayed publication would mislead another active actor or make continuation unsafe, make landing those corrections the next action instead.

## Finish the close

Do not ask a new question merely to make the close tidier. A decision that is not required for a safe mutation already in progress becomes the next action for a new session. Route an action to the user only when it genuinely requires their judgement, eyes, access, or approval.

Resolve exactly one handoff: unfinished work from the current owner first; otherwise the next unambiguous item from the authoritative ordered backlog or project plan; otherwise the user's decision about where the project should go next. For multi-packet delivery, name exactly the current or next ready packet and end its prompt with: `Run its packet safety gate, update the record, invoke close-session packet close, and stop.` If every implementation packet is complete, hand off the separate story-completion boundary. Do not include downstream work or infer an unrecorded priority.

Keep the output proportional:

- Open with one concise sentence saying the session is closed and naming the meaningful outcome, verification and landing state, plus a material assurance recommendation only when it changes the next action.
- Add `### Saved` only when close-time edits or knowledge capture occurred; list the authoritative files or records changed.
- Add `### Attention` only for failing checks, unsafe or unresolved state, or an external blocker.
- Always end with `### Handoff`, using a blockquote of at most two lines with `**New session:**`, `**You:**`, or `**Waiting for <actor>:`. When no explicit next item exists or ordering is ambiguous, use `> **You:** Decide where the project should go next.`

Do not present empty tables, “None” rows, a session recap, or more than one next action. The final output ends the session.
