# Packet Coordination

Read this reference for a named packet in a multi-packet story or change package, including when direct delivery implements it.

## Packet size

Use as few packets as the work allows. Split only at a boundary you can see in the plan:

- a human step sits between the parts, such as the user configuring an external account; or
- a later part needs an earlier part landed and proven first, such as a schema change before the screens that use it.

Never split to fit a session or keep sessions light: session room cannot be predicted, so running out is handled when it happens, as the core describes.

Give each packet a stable ID, its outcome, the acceptance it covers, dependencies, likely change surface, non-goals where scope could drift, verification, and one state: `pending`, `ready`, `in-progress`, `blocked`, `done`, or `invalidated`. Packets are not tracker items.

Allow exactly one packet in progress at a time. A broad request to build, continue, or finish a multi-packet story selects its current or next ready packet first. When that packet's gate passes and its close has pushed or landed it, the same session continues to the next ready packet unless a human checkpoint, a decision that is the user's, a required independent review, or the running-out rule in the core intervenes; a fresh session is for those boundaries, not a cost paid after every packet. Execute dependent packets in order. A corrected or invalidated packet invalidates downstream completion whose evidence no longer holds. A human checkpoint remains a hard stop before dependent work.

## Fresh-session continuation

Each packet ends in a state a fresh session can resume, which may use Claude Code or Codex. This supports continuation across provider usage limits and resets as well as smaller working context; a pause in the same conversation does not reset context. Do not require a separate administrative session after each packet.

Keep one execution area in the owner, holding only what the next session needs to act: repository, remote working branch, story base revision, changed paths, the current packet and next step, open decisions and risks, and reusable evidence as one line each (the check, its revision, and what would invalidate it). A finished packet collapses to one line. Delete fixed review findings, landing details and anything else that only explains the past; commit messages and pull requests keep that history. Record the base revision before the first packet and keep it until the story is finished. Keep the area under about 8 KB (roughly 1,200 words), or the project's cap if it sets one, since every later session reads it in full.

Before editing, read the selected packet, shared constraints, current execution state, and only necessary code. Confirm its decisions and dependencies, then mark it in progress; resume that same packet after interruption. Verify the recorded repository, remote branch, checkpoint revision, and any current tracked or untracked changes. Continue from that remote branch across sessions and providers; never assume a new chat or worktree shares local-only files. Treat recorded earlier-packet changes as owned continuation, preserve unrelated work, and resolve missing or entangled state before dependent edits. Do not reconstruct the previous conversation or re-review unchanged earlier packets merely because the session is new.

Establish a packet-start baseline for touched paths: use an existing revision where it matches their starting content; otherwise keep temporary copies before editing, including absence for new files and the originals for deletions or renames. Inspect this delta separately from the cumulative story diff; do not use Git staging or a commit solely as a baseline. Keep its revision or snapshot location in the owner while the packet is incomplete, and retain the original baseline when resuming. If that snapshot is unavailable, inspect the cumulative diff for affected paths and reconcile ownership from the record; never claim the packet delta was verified from `HEAD` alone when earlier packets changed those paths. Refresh the working state before integration to detect concurrent changes.

## Packet safety gate

Keep planning, implementation, meaningful targeted tests, and failure diagnosis together. Before handing off, run the smallest current check showing that later work can build on the packet: its targeted acceptance or regression check, otherwise the narrow compile, type, lint, contract, render, or observable check for the changed surface. Add a critical-path check for a critical domain. If no meaningful runnable check exists, record the gap and alternative evidence. A failed gate leaves the packet incomplete; hand off resumption of that packet, not the next one.

Inspect the complete packet delta, including its record updates, and refresh affected checks after fixes. Do not repeat the full story suite, cumulative diff review, or independent assurance at every packet. Independent review happens once per story, after the last packet. Review a packet earlier only when the story record names a specific risk that later packets build on, such as a schema or access rule. Any independent review is its own session, never part of the implementation session or a worker inside it, and it applies its own fixes before dependent work starts. Reuse earlier evidence unless its surface, contract, dependency, environment, or acceptance oracle changed; a new session or a commit alone does not invalidate it. A resumed session that finds the gate already passed on the current code reruns nothing and goes straight to the close. Keep unavailable manual observations as pending evidence, not an automatic human-preview request.

Maintain the delivery controls' single completion-assurance note. Change it only when consequence, completion uncertainty, reusable evidence, or invalidation changes. Preserve unresolved material or critical attention across later light packets; keep an explicit routine conclusion when appropriate. Record the packet outcome, changed paths or contracts, checks and results, material decisions, unresolved risk, newly ready or invalidated work, and exact next boundary. Update known stale documents with the code. Packet `done` means its gate passed, not that its code is committed or its owner complete.

## Remote session checkpoint

At the end of every delivery session, commit and push all separable session-owned code and current record changes to the declared non-live working branch. This standing checkpoint authority exists so another local or cloud session can resume from the remote branch; it does not authorise a push to a live or protected branch, a force-push, a merge, a deployment, or inclusion of unrelated work. Project Git policy may require a stronger landing sequence or forbid a particular target, and always wins.

Use explicit paths and include every change-owned tracked and untracked file needed to reproduce the recorded state. Keep unrelated work untouched. A packet whose safety gate failed or which stopped incomplete may still receive a clearly labelled checkpoint commit when its state is coherent, contains no secrets or unsafe generated material, and can be separated safely; record the failing check and keep that packet `in-progress` or `blocked`. Never present a checkpoint as completed or land it into the target branch while its required gate is failing.

If the branch, upstream, policy, staged intent, or ownership is unclear or entangled, do not guess. Preserve the exact local state, record why remote checkpointing was unsafe, and make resolution the next boundary. A packet-only checkpoint does not require a pull request. Verify the remote branch contains the checkpoint before handing off, and resume from that branch rather than relying on one machine's checkout.

## Story review and completion

One session finishes the story, starting from the current execution state and completion-assurance note rather than replaying packet history:

- **When the note requires independent review,** the session after the last packet is that review. Run the recorded method (normally `check-work` code review) on the complete story diff, apply its fixes in the same session, recheck each fixed surface, then complete the story and land it through `close-session`. Start a separate re-review session only when a fix substantially changes a critical surface, such as rewriting an access or data-protection rule.
- **Otherwise** the last packet's own session completes the story once its gate passes.

Either way: reuse valid packet evidence, run outstanding integrated acceptance and regression checks, and inspect the complete story diff against its recorded base, including untracked files and checkpoint commits. Keep the recorded consequence floor unless the complete diff disproves it. Fix a defect found here in the same session unless it needs a packet of its own. Then apply the completion rule in the delivery controls and land through `close-session`, using the project's declared merge strategy for checkpoint commits.

At each packet boundary, invoke `close-session` packet close without waiting for a prompt, regardless of delivery route. Continue to the next ready packet as packet size above allows; when a boundary stops the session, that close's handoff is the only final response. Use a bounded worker only under the worker reference.
