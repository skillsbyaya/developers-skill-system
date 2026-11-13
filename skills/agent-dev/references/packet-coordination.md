# Packet Coordination

Read this reference for a named packet in a multi-packet story or change package, including when direct delivery implements it.

## Packet size

Use as few packets as the work allows. Split only at a boundary you can see in the plan: a human step sits between the parts (the user configuring an external account), or a later part needs an earlier part landed and proven first (a schema change before the screens that use it). Parts with neither boundary are one packet, however many screens or rows they touch, and only a packet that must land first lands before the story. Short chats may resume the same packet; a chat boundary does not require a new packet, review or landing.

Give each packet a stable ID, its outcome, the boundary that separates it from the packet before, the acceptance it covers, dependencies, likely change surface, non-goals where scope could drift, verification, and one state: `pending`, `ready`, `in-progress`, `blocked`, `done`, or `invalidated`. Packets are not tracker items.

Exactly one packet is in progress at a time. A broad request to build, continue, or finish a story selects its current or next ready packet. When that packet's gate passes, the same session continues to the next ready packet unless a human checkpoint, a decision that is the user's, unavailable required independent evidence, or the core's running-out rule intervenes; the user may also choose shorter chats without changing delivery boundaries. A corrected or invalidated packet invalidates downstream completion whose evidence no longer holds. A human checkpoint is a hard stop before dependent work.

## Fresh-session continuation

At a handoff, preserve a state a fresh session, in Claude Code or Codex, can resume from the remote branch. Keep one execution area in the owner holding only what the next session needs to act: repository, remote working branch, story base revision, changed paths, the current packet and next step, open decisions and risks, any wait as the check that ends it (“`npm view <package> version` reads 3.1.0 or later”, never “waits for 3.1”), and reusable evidence as one line each (the check, its revision, and what would invalidate it). A finished packet collapses to one line. Delete fixed review findings, landing details and anything else that only explains the past; commits and pull requests keep that history. Record the base revision before the first packet and keep it until the story is finished. Keep the area under about 8 KB (roughly 1,200 words), or the project's cap, since every later session reads it in full.

Before editing, read the selected packet, shared constraints, current execution state, and only necessary code. Confirm its decisions and dependencies, mark it in progress, and resume that same packet after an interruption. Verify the recorded repository, remote branch, checkpoint revision, and any current tracked or untracked changes; never assume a new chat or worktree shares local-only files. Treat recorded earlier-packet changes as owned continuation, preserve unrelated work, and resolve missing or entangled state before dependent edits. Do not reconstruct the previous conversation or re-review unchanged earlier packets because the session is new.

Establish a packet-start baseline for touched paths: an existing revision where it matches their starting content, otherwise temporary copies taken before editing (including absence for new files and the originals for deletions or renames). Inspect this delta separately from the cumulative story diff; do not use Git staging or a commit solely as a baseline. Keep its revision or snapshot location in the owner while the packet is incomplete. If the snapshot is unavailable, inspect the cumulative diff for the affected paths and reconcile ownership from the record; never claim the packet delta was verified from `HEAD` alone when earlier packets changed those paths. Refresh the working state before integration to detect concurrent changes.

## Packet safety gate

Keep planning, implementation, targeted tests, and failure diagnosis together. Before dependent work relies on the packet or it is marked done, run the smallest current check showing that later work can build on it: its targeted acceptance or regression check, otherwise the narrow compile, type, lint, contract, render, or observable check for the changed surface, plus a critical-path check for a critical domain. If no runnable check exists, record the gap and the alternative evidence. A failed or deferred gate leaves the packet incomplete; a handoff may checkpoint it with the check and next step recorded. Do not force tests merely because the chat is ending.

Inspect the complete packet delta, including its record updates, and refresh affected checks after fixes. Do not repeat the full story suite, cumulative diff review, or independent assurance at every packet: independent review happens once per story, after the last packet, unless the record names a specific risk later packets build on (a schema or access rule). Reuse earlier evidence unless its surface, contract, dependency, environment, or acceptance oracle changed; a new session or a commit alone does not invalidate it. A resumed session that finds the gate already passed on the current code reruns nothing and continues the batch. Keep unavailable manual observations as pending evidence, not an automatic human-preview request.

Maintain the delivery controls' completion-assurance note, changing it only when consequence, completion uncertainty, reusable evidence, or invalidation changes. Record the packet outcome, changed paths or contracts, checks and results, material decisions, unresolved risk, newly ready or invalidated work, and the exact next boundary. Update known stale documents with the code. Packet `done` means its gate passed, not that its code is committed or its owner complete.

Continue to the next ready packet without a mandatory commit or push. At a preservation boundary use `close-session` and its open-batch checkpoint route; a failed or unchecked packet remains `in-progress` or `blocked`. Its handoff is the only final response when the chat stops. Use a bounded worker only under the worker reference.

## Story review and completion

One session finishes the story, starting from the current execution state and completion-assurance note rather than replaying packet history:

- **When the note requires independent review,** obtain it after the last packet: run the recorded method (normally `check-work` code review) on the complete story diff, apply its fixes in the same session, recheck each fixed surface, then complete the story and land it through `close-session`. Use code review's fix and re-review boundary for any changed critical surface.
- **Otherwise** the last packet's session completes the story once its gate passes.

Either way: reuse valid packet evidence, run outstanding integrated acceptance and regression checks, and inspect the complete story diff against its recorded base, including untracked files and checkpoint commits. Keep the recorded consequence floor unless the complete diff disproves it. Fix a defect found here in the same session unless it needs a packet of its own. Then apply the completion rule in the delivery controls and land through `close-session`.
