# Packet Close

Use this workflow only after Agent Dev finishes or stops one coordinated or staged implementation packet and the user has not separately requested a full close. Preserve the minimum reliable continuation, return the next fresh-session prompt, and end the current session.

## Confirm the boundary

Use the current session's evidence. Do not rerun checks, reread broad sources, survey project documents, or inspect the whole repository.

Confirm that:

- no later packet has started;
- the packet safety gate passed, or its exact failure was recorded;
- the owning story or change package identifies the current packet; and
- the record contains the packet outcome, files or contracts changed, gate and result, material decisions or discoveries, unresolved risk or blocker, and exact next boundary.

Repair only a small unambiguous omission in that owning record. If ownership is unclear or the checkpoint would require reconstruction, leave the packet unresolved and name the missing state rather than creating another record.

## Preserve learning without expanding

Save only facts that change remaining work. Put story-specific discoveries, rejected approaches worth not repeating, changed constraints, and any broader learning candidate in the owning story or package. Keep the candidate concise and evidence-based so a later full close or story-completion session can route it properly.

Do not update broader project documents or invoke another skill. Do not run a retrospective, documentation sweep, backlog reconciliation, story completion, archive close-out, independent review, commit, push, pull request, or deployment. Do not create a session log, handoff file, or standalone lesson note. Replace stale continuation fields instead of appending a session diary.

## Produce the next prompt

Resolve exactly one next action:

1. resume the same packet when its safety gate failed or it stopped incomplete;
2. satisfy a human checkpoint or material decision when one blocks dependent work;
3. start the next ready implementation packet; or
4. when no implementation packet remains, start a separate story-completion session for integrated checks, the complete story diff, assurance, lifecycle reconciliation, and any authorised commit or landing.

Return one compact checkpoint sentence naming the packet, gate result, owning record, and any learning saved. Then add a `### Handoff` blockquote of at most two lines:

- For implementation: `> **New session:** Implement <packet> from <record>. Run its packet safety gate, update the record, invoke close-session packet close, and stop.`
- For story completion: `> **New session:** Complete <story> from <record>: run integrated verification, inspect the full story diff, reconcile lifecycle state, and commit or land once if authorised.`
- For a user or external blocker, use `> **You:**` or `> **Waiting for <actor>:` and state only the action that clears it.

Do not restate packet contents, list later work, or ask the user to prompt the close that Agent Dev has already invoked. End the session after this output.
