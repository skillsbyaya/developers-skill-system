# Staged Delivery

Use this workflow when delivery needs comprehensive source context, several review slices, multiple clean-context stages, or durable multi-session continuation. A tracked story may also be prepared here when approved scope already exists.

Read [Delivery controls](../references/delivery-controls.md) before editing.

## Adopt and prepare the record

Resume the existing story or change package first. If approved epics contain the selected story but no implementation-ready story record exists, prepare it before slicing per [Story preparation](../references/story-preparation.md), without changing product intent. For reconciliation-heavy, new-UX/UI-pattern, or multi-slice work, complete the [Prepare story](prepare-story.md) workflow and write the durable story before code; continue into delivery in the same session only under that workflow's explicit continuation rule. If no story owns the work, create one change package only when durable continuation or assurance earns it; never create a synthetic tracker item for a package.

Keep the record useful for continuation: outcome and acceptance, relevant constraints and sources, material decisions, review slices or execution packets, current evidence, status, and the exact next incomplete boundary. Do not copy whole upstream artifacts or maintain a session diary.

Read [Packet coordination](../references/packet-coordination.md) before starting the first packet.

If an active delivery-status index exists, update only the item this workflow prepares or implements and only through its legal lifecycle and completion close-out. If the index is missing, bootstrap it only when one authoritative epics document exists and the project's PM structural convention supplies an unambiguous structure; otherwise stop and route structural creation to the PM owner.

## Deliver in reviewable slices

Select the current or next ready slice and assemble only its needed context. Define its owned paths or contracts, dependencies, acceptance evidence, decision points, and completion boundary. Keep packet boundaries internal to the story or package; they do not create new product ownership or tracker entries.

At each slice boundary:

1. refresh the version-control baseline and detect concurrent edits before integration;
2. run the packet safety gate in packet coordination, including its complete packet-owned diff inspection;
3. update the owning record with decisions, evidence, residual risk, and exact continuation state that later work needs;
4. obtain user or independent feedback only when the uncertainty or consequence requires it; and
5. incorporate only accepted findings, then refresh affected assurance; and
6. invoke `close-session` packet close and stop at the fresh-session-safe checkpoint; never start another slice in the same session.

If considering a clean-context implementation or verification worker, read [Worker execution](../references/worker-execution.md). Do not load it for inline delivery. After the last implementation slice, the packet-close handoff starts a separate story- or package-completion session to run required integrated checks before applying the completion rule and delivery handoff in the delivery controls. When context ends or a block remains, leave the story or package at one precise safe boundary rather than creating a separate handoff log.
