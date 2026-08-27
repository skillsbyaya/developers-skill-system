# Packet Coordination

Read this reference only for coordinated or staged delivery with several implementation packets.

Give each packet a stable ID, one bounded technical outcome, acceptance coverage, dependencies, expected path or contract surface, non-goals where scope could drift, narrow verification, and one state: `pending`, `ready`, `in-progress`, `blocked`, `done`, or `invalidated`.

Allow exactly one packet in progress and one packet per delivery session. A broad request to build, continue, or finish a multi-packet story still selects only its current or next ready packet. Execute dependent packets in order. A corrected or invalidated packet invalidates downstream completion whose evidence no longer holds.

A packet boundary protects against exhausting the model's available context mid-story; user wording does not widen it. A human checkpoint is also a hard stop: finish the preceding packet, preserve its evidence, and do not begin dependent work until the checkpoint has resolved.

Before a packet, confirm its decisions and dependencies, refresh the repository baseline, and mark it in progress. A packet is an execution unit inside the story or package; it never becomes a separate sprint item, story, review lifecycle, or product owner.

## Packet safety gate

Packet evidence accumulates. Do not invoke `check-work` or reassess the story at every packet boundary. Reuse an earlier packet result unless later work changed the surface, contract, dependency, environment, or acceptance oracle it established. Record proposed or unavailable manual observations as pending evidence, not as a trigger for human preview.

Before handing off, run the smallest current check that can show the packet is safe for later work to build on. Prefer its targeted acceptance or regression check; otherwise use the narrow compile, type, lint, contract, render, or observable check for the changed surface. Add a critical-path check when the packet touches a critical domain. Do not repeat the full story suite or broad independent assurance at every packet.

Inspect the complete packet-owned diff. Record the completed outcome, files or contracts changed, check and result, material decisions or discoveries, unresolved risk, newly ready or invalidated work, and the exact next boundary. If no meaningful runnable check exists, record that gap and the evidence used instead. A failed gate leaves the current packet incomplete; preserve the failure and resume that packet in the next session rather than advancing.

Packets are context, evidence, and continuation boundaries, not mandatory commit or pull-request boundaries. By default, keep implementation packets uncommitted and make one reviewable commit or pull request after story-completion evidence is current, subject to the user's delivery authority and project Git workflow. Use a local packet checkpoint commit only when recovery, concurrent work, branch switching, or a large overlapping cumulative diff creates a concrete need; do not push or open a packet-only pull request merely to mark the boundary. Within any landing unit, include the code, record update, status transition, and any orientation pointer that becomes stale with it.

## Story-completion session

When every implementation packet is complete, do not create a synthetic final packet. Start the separate story-completion boundary from the current record: consume the accumulated packet evidence once, reuse results that still match the complete revision, run only the integrated or delta acceptance and regression checks still needed, inspect the complete story-owned diff, make the assurance and lifecycle decision, reconcile final records, and commit or land once when authorised. If verification exposes an implementation defect, invalidate and resume the responsible packet rather than repairing it invisibly inside completion.

At the packet boundary, load `close-session` and run packet close without waiting for the user to prompt it, regardless of which delivery route implemented the packet. Its checkpoint and paste-ready handoff are the only final response; do not produce another completion summary and do not merely say that close-session should run. Stop after the packet close. Use a bounded worker only under the worker reference; a pause in the same conversation does not reset context.
