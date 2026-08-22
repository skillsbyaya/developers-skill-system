# Packet Coordination

Read this reference only for coordinated or staged delivery with several implementation packets.

Give each packet a stable ID, one bounded technical outcome, acceptance coverage, dependencies, expected path or contract surface, non-goals where scope could drift, narrow verification, and one state: `pending`, `ready`, `in-progress`, `blocked`, `done`, or `invalidated`.

Default to one packet in progress and one packet per delivery session. Allow more than one packet in the same session only when separating them would force material duplicate setup or destroy a meaningful verification boundary, no durable checkpoint can safely sit between them, and the owning record states that reason before work starts. Independence is a reason to use fresh sessions, not a reason to bundle packets. Execute dependent packets in order. A corrected or invalidated packet invalidates downstream completion whose evidence no longer holds.

A broad request to build, continue, or finish a multi-packet story selects only its current or next ready packet unless the user explicitly names a wider packet set after seeing the checkpoint. It does not authorise silently carrying every remaining packet in one conversation. A human checkpoint is always a hard stop: finish the preceding packet, preserve its evidence, and do not begin the following packet until the checkpoint has resolved.

Before a packet, confirm its decisions and dependencies, refresh the repository baseline, and mark it in progress. After it, record accepted evidence, files changed, checks, material decisions or discoveries, newly ready or invalidated work, and the exact next boundary. A packet is an execution unit inside the story or package; it never becomes a separate sprint item, story, review lifecycle, or product owner.

At the packet boundary, leave the owning record sufficient for a fresh session: completed outcome, accepted evidence, files or contracts changed, checks, material decisions, unresolved risk, and one exact next ready packet. Stop the delivery session there by default, even when context remains. Use a bounded worker only under the worker reference. Continue into another packet only under the documented inseparability exception above; a pause in the same conversation does not reset context.
