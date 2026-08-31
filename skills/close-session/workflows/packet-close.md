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

Update every authoritative document already identified by the session that the packet or its post-landing actions have made materially stale. This includes the owning story or package, a delivery-status or next-action pointer, and a durable project rule or operational fact when the session directly changed it. Use current evidence, replace obsolete wording, and record only facts that improve later action; do not append a session diary.

Do not search for hypothetical documentation work or run a documentation sweep. The boundary is every known document that now needs a change, not a privileged class of files that packet close is forbidden to touch. Put story-specific discoveries, rejected approaches worth not repeating, changed constraints, and any broader learning candidate in their existing authoritative owner when clear; otherwise keep the concise candidate in the story or package for later routing.

Do not invoke another skill during a routine packet close. During knowledge-rich capture, invoke `learn-lessons` only under that reference's confirmed-correction gate; do not expand an ordinary implementation mistake into a retrospective. Do not perform backlog reconciliation, story completion, archive close-out, independent review, commit, push, open a pull request, or deploy. Do not create a session log, handoff file, or standalone lesson note.

When the packet's landing unit is already complete and project policy would require a separate commit or pull request solely to publish a factual documentation correction, leave the corrected document local for the next already-required landing unit. Record its path and intended landing boundary in the project's existing continuation or next-action source, falling back to the owning record only when no such source exists, and repeat it in the handoff. This is deliberate continuation state, not unrelated work. If delaying publication would mislead another active actor or make the next action unsafe, select publication of the correction as the exact next boundary instead.

## Produce the next prompt

Resolve exactly one next action:

1. resume the same packet when its safety gate failed or it stopped incomplete;
2. satisfy a human checkpoint or material decision when one blocks dependent work;
3. start the next ready implementation packet; or
4. when no implementation packet remains, start a separate story- or package-completion session from the current completion-assurance note: reuse valid packet evidence, run unresolved integrated checks, inspect the complete owner diff, apply the recorded method or explicit routine condition, and use `check-work` only when the decision is missing or stale before lifecycle reconciliation and any authorised landing.

Return one compact checkpoint sentence naming the packet, gate result, owning record, any learning saved, and any documentation pending publication. Then add a `### Handoff` blockquote of at most two lines:

- For implementation without pending local documentation: `> **New session:** Implement <packet> from <record>. Run its packet safety gate, update the record, invoke close-session packet close, and stop.`
- For implementation with pending local documentation: `> **New session:** Implement <packet> from <record>; preserve and land the pending corrections in <paths> with this delivery. Run its packet safety gate, update the record, invoke close-session packet close, and stop.`
- For story or package completion: `> **New session:** Check <owner> at completion from <record>: start from its completion-assurance note, reuse current packet evidence, run unresolved integrated checks and <recorded method or routine condition>, inspect the complete owner diff, then reconcile lifecycle state and land once if authorised.`
- For a user or external blocker, use `> **You:**` or `> **Waiting for <actor>:` and state only the action that clears it.

Do not restate packet contents, list later work, or ask the user to prompt the close that Agent Dev has already invoked. End the session after this output.
