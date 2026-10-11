# Staged Delivery

Use this workflow when delivery needs comprehensive source context, several review slices, multiple clean-context stages, or durable multi-session continuation. A tracked story may also be prepared here when approved scope already exists.

Read [Delivery controls](../references/delivery-controls.md) before editing.

## Adopt and prepare the record

Resume the existing story or change package first. If approved epics contain the selected story but no implementation-ready story record exists, prepare it before slicing per [Story preparation](../references/story-preparation.md), without changing product intent. For reconciliation-heavy, new-UX/UI-pattern, or multi-slice work, complete the [Prepare story](prepare-story.md) workflow and write the durable story before code; continue into delivery in the same session only under that workflow's explicit continuation rule. If no story owns the work, create one change package only when durable continuation or assurance earns it; never create a synthetic tracker item for a package.

Keep the record useful for fresh-session continuation across providers: outcome and acceptance, relevant constraints and sources, material decisions, review slices or execution packets, current evidence, status, and the checkout and exact next incomplete boundary. Do not copy whole upstream artifacts or maintain a session diary.

Read [Packet coordination](../references/packet-coordination.md) before implementing or resuming a packet. To finish a story whose packets are done, adopt the current record and use its story review and completion section directly; do not repeat preparation or select another packet.

If an active delivery-status index exists, update only the item this workflow prepares or implements and only through its legal lifecycle and completion close-out. If the index is missing, bootstrap it only when one authoritative epics document exists and the project's PM structural convention supplies an unambiguous structure; otherwise stop and route structural creation to the PM owner.

## Deliver in reviewable slices

Select the current or next ready slice and assemble only its needed context. Define its owned paths or contracts, dependencies, acceptance evidence, decision points, and completion boundary. Keep packet boundaries internal to the story or package; they do not create new product ownership or tracker entries.

At each slice boundary:

1. refresh the version-control baseline and detect concurrent edits before integration;
2. run the packet safety gate in packet coordination, including its complete packet-owned diff inspection;
3. update the owning record with decisions, evidence, residual risk, and exact continuation state that later work needs;
4. obtain user feedback only when a decision blocks the slice, incorporate only accepted answers, and refresh affected checks; when independent review of the slice is required, record the need and leave it for its own session per packet coordination; and
5. invoke `close-session` packet close, push the fresh-session-safe checkpoint, and continue to the next ready slice when packet coordination allows it; otherwise stop.

If considering a clean-context implementation or verification worker, read [Worker execution](../references/worker-execution.md). Do not load it for inline delivery. After the last slice, finish the story as packet coordination's story review and completion section directs. When context ends or a block remains, leave the story or package at one precise safe boundary rather than creating a separate handoff log.
