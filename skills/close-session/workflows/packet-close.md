# Packet Close

Use this workflow only after Agent Dev finishes or stops one named implementation packet or slice, through any delivery route, and the user has not separately requested a full close. Preserve the minimum reliable continuation, return the next fresh-session prompt, and end the current session.

## Apply the triaged depth

For a routine close, write only missing current state, the exact continuation boundary, and isolated durable facts that later work needs.

For a knowledge-rich close, read [Knowledge capture](../references/knowledge-capture.md) and preserve the material relationships before returning here. Richer capture does not widen this packet boundary into story completion, broad reconciliation, independent assurance, Git landing, or deployment.

## Confirm the boundary

Use the current session's evidence. Do not rerun checks, reread broad sources, survey project documents, or inspect the whole repository.

Confirm that:

- no later packet has started;
- the packet safety gate passed, or its exact failure was recorded;
- the owning story or change package identifies the current packet; and
- the record contains the packet outcome, files or contracts changed, gate and result, material decisions or discoveries, unresolved risk or blocker, and exact next boundary.

For the final implementation packet, the exact next boundary is separate completion of the owning story or package, and its current completion-assurance note must state the consequence floor, exact attention or explicit routine conclusion, reusable evidence and limitations, and selected completion condition. All packets being checked off does not make the owner complete. A tracked story stays active at `review`; a change package stays in its supported pre-completion state. The packet must not mark the owner `done`, archive it, remove its active status, perform completion-only backlog transfer, or advance an orientation pointer to later work. If the session prepared any of those mutations, treat them as a packet-boundary defect and restore the supported pre-completion state before landing; when they are already landed or cannot be safely restored, do not advance and make that correction the exact next boundary.

Repair every small, unambiguous omission the session has made in its owning record or other known authoritative documents. If ownership is unclear or the checkpoint would require reconstruction, leave the packet unresolved and name the missing state rather than creating another record.

## Keep the documentation true

Update every authoritative document already identified by the session that the packet has made materially stale. This includes the owning story or package, a delivery-status or next-action pointer, and a durable project rule or operational fact when the session directly changed it. Use current evidence, replace obsolete wording, and record only facts that improve later action; do not append a session diary.

Do not search for hypothetical documentation work or run a documentation sweep. The boundary is every known document that now needs a change, not a privileged class of files that packet close is forbidden to touch. Put story-specific discoveries, rejected approaches worth not repeating, changed constraints, and any broader learning candidate in their existing authoritative owner when clear; otherwise keep the concise candidate in the story or package for later routing.

Do not invoke another skill during a routine packet close. During knowledge-rich capture, invoke `learn-lessons` only under that reference's confirmed-correction gate; do not expand an ordinary implementation mistake into a retrospective. Do not perform backlog reconciliation, story completion, archive close-out, independent review, commit, push, open a pull request, or deploy. Do not create a session log, handoff file, or standalone lesson note.

The packet's documents landed with its code, so this step normally has nothing left to publish. If verification after landing diverged from what the record anticipated, or the session left something unwritten that the landed unit can no longer carry, make landing that correction the exact next boundary. Do not leave it as uncommitted state for a later unit to adopt: the next session may be on another branch, another story or another worktree, and a dirty tree becomes its problem rather than this one's. Recurring need for this paragraph is a defect in delivery — a record written about the merge instead of about the change.

## Produce the next prompt

Resolve exactly one next action:

1. resume the same packet when its safety gate failed or it stopped incomplete;
2. satisfy a human checkpoint or material decision when one blocks dependent work;
3. start the next ready implementation packet; or
4. when no implementation packet remains, start a separate story- or package-completion session from the current completion-assurance note: reuse valid packet evidence, run unresolved integrated checks, inspect the complete owner diff, apply the recorded method or explicit routine condition, and use `check-work` only when the decision is missing or stale before lifecycle reconciliation and any authorised landing.

Return one compact checkpoint sentence naming the packet, gate result, owning record, any learning saved, and any documentation pending publication. Then add a `### Handoff` blockquote of one line, written as `<subject> — <instruction>`:

- Lead with the subject in plain words: what the next session is about, readable by a person without opening the record or decoding a key.
- After the dash, give one pasteable sentence carrying only the verb, the unit, the delivery skill, and the record path. For implementation: `> **New session:** The template repository and replace path — Implement P2 with agent-dev from <record>.` For owner completion: `> **New session:** <what the owner delivered> — Take <owner> through owner completion with agent-dev from <record>.`
- For a user or external blocker, use `> **You:**` or `> **Waiting for <actor>:` and state only the action that clears it.

Naming the delivery skill carries its procedure, so restating that procedure is the defect. Never spell out the safety gate, the record update, which close to invoke, when to stop, or how completion is assured; Agent Dev owns each of those and reads them itself. Never repeat state already written where the next session will read it, including pending local documentation corrections held in the continuation source. If something the next session needs is genuinely unwritten, write it into the record rather than lengthening the handoff.

The checkpoint sentence and the handoff are the whole output — there is no third part. An attention list, a summary of what was built, or evidence that a check passed has no place here; a passing gate is three words inside the checkpoint sentence. What the user must act on is a blocker and belongs in the handoff; what they must look at later belongs in the project's continuation source, where they will be reading when it matters; everything else belongs in the record and the commit message. Do not restate packet contents, list later work, or ask the user to prompt the close that Agent Dev has already invoked. End the session after this output.
