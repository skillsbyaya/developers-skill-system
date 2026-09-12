# Packet Coordination

Read this reference for a named packet in a multi-packet story or change package, including when direct delivery implements it.

Give each packet a stable ID, one bounded technical outcome, acceptance coverage, dependencies, expected path or contract surface, non-goals where scope could drift, narrow verification, and one state: `pending`, `ready`, `in-progress`, `blocked`, `done`, or `invalidated`. Size it for implementation, targeted checks, failure diagnosis, and a compact checkpoint within one session; code-writing alone is not the budget. Split at a coherent technical boundary when that is too much, without creating new product ownership or tracker items.

Allow exactly one packet in progress and one packet per delivery session. A broad request to build, continue, or finish a multi-packet story selects only its current or next ready packet. Execute dependent packets in order. A corrected or invalidated packet invalidates downstream completion whose evidence no longer holds. A human checkpoint remains a hard stop before dependent work.

## Fresh-session continuation

Each packet ends with a handoff for a fresh session, which may use Claude Code or Codex. This supports continuation across provider usage limits and resets as well as smaller working context; a pause in the same conversation does not reset context. Do not require a separate administrative session after each packet.

Keep one current execution area in the existing owner: checkout path, branch, story base revision, story-owned changed paths, completed outcomes and reusable evidence, material decisions, unresolved risks, and exact next boundary. Record the base before the first packet; retain it through completion, including across any checkpoint commits. Replace stale state rather than adding session narratives. Keep only earlier packet detail needed by acceptance, dependencies, or remaining uncertainty.

Before editing, read the selected packet, shared constraints, current execution state, and only necessary code. Confirm its decisions and dependencies, then mark it in progress; resume that same packet after interruption. Verify the recorded checkout, branch, and existing tracked and untracked changes. Continue in that same checkout across sessions and providers; another chat or a new worktree does not carry uncommitted files automatically. Treat recorded earlier-packet changes as owned continuation, preserve unrelated work, and resolve missing or entangled state before dependent edits. Do not reconstruct the previous conversation or re-review unchanged earlier packets merely because the session is new.

Establish a packet-start baseline for touched paths: use an existing revision where it matches their starting content; otherwise keep temporary copies before editing, including absence for new files and the originals for deletions or renames. Inspect this delta separately from the cumulative story diff; do not use Git staging or a commit solely as a baseline. Keep its revision or snapshot location in the owner while the packet is incomplete, and retain the original baseline when resuming. If that snapshot is unavailable, inspect the cumulative diff for affected paths and reconcile ownership from the record; never claim the packet delta was verified from `HEAD` alone when earlier packets changed those paths. Refresh the working state before integration to detect concurrent changes.

## Packet safety gate

Keep planning, implementation, meaningful targeted tests, and failure diagnosis together. Before handing off, run the smallest current check showing that later work can build on the packet: its targeted acceptance or regression check, otherwise the narrow compile, type, lint, contract, render, or observable check for the changed surface. Add a critical-path check for a critical domain. If no meaningful runnable check exists, record the gap and alternative evidence. A failed gate leaves the packet incomplete; hand off resumption of that packet, not the next one.

Inspect the complete packet delta, including its record updates, and refresh affected checks after fixes. Do not repeat the full story suite, cumulative diff review, or independent assurance at every packet. Reuse earlier evidence unless its surface, contract, dependency, environment, or acceptance oracle changed; a new session or a commit alone does not invalidate it. Keep unavailable manual observations as pending evidence, not an automatic human-preview request.

Maintain the delivery controls' single completion-assurance note. Change it only when consequence, completion uncertainty, reusable evidence, or invalidation changes. Preserve unresolved material or critical attention across later light packets; keep an explicit routine conclusion when appropriate. Record the packet outcome, changed paths or contracts, checks and results, material decisions, unresolved risk, newly ready or invalidated work, and exact next boundary. Update known stale documents with the code. Packet `done` means its gate passed, not that its code is committed or its owner complete.

## Commit boundary

By default, accumulate packet code and record changes uncommitted in the same checkout, then commit the whole story or package after its separate completion session. An explicit user instruction or declared project policy requiring packet commits overrides this default; it does not change the one-packet session boundary. This default sets commit timing only, not branch, push, deployment, or commit authority. Do not force a clean tree at packet close or load commit procedures without an actual authorised commit to perform.

Use an authorised local checkpoint commit only for a concrete recovery or checkout-transfer need, or when overlapping work cannot otherwise be preserved and reviewed reliably. Do not create one merely because another session or provider is next. Verify a requested checkout transfer includes all story-owned tracked and untracked state before resuming. Under an explicit packet-commit policy, land code and current records together; preserve unrelated work and existing Git safeguards. Never push or open a packet-only pull request merely to mark a boundary.

## Owner-completion session

When every implementation packet is complete, leave the story at `review` or the package in its supported pre-completion state and hand off separate owner completion; do not create a synthetic final packet. Start from the current execution state and completion-assurance note, not story preparation or replay of packet history.

Consume accumulated evidence once: preserve the recorded consequence floor unless the complete current diff disproves it, reuse valid results, run outstanding integrated or delta acceptance and regression checks, inspect the complete owner diff against its recorded base including untracked files and checkpoint commits, and apply the recorded assurance method. An explicit routine note may be satisfied by current affected checks and complete-diff inspection when no upgrade trigger remains. Use `check-work` only when the completion decision is missing or stale.

Prescribed check execution and settled record or Git actions may suit lower reasoning; judging coverage, reviewing consequential changes, and diagnosing failures require capability appropriate to the uncertainty. Never classify all completion work as mechanical. If verification exposes an implementation defect, invalidate and resume the responsible packet with affected downstream evidence; do not repair it invisibly inside completion. Reconcile final records and commit the story or package once when authorised, only after the completion condition is satisfied.

At each packet boundary, invoke `close-session` packet close without waiting for a prompt, regardless of delivery route. Its compact checkpoint and paste-ready handoff are the only final response. Stop after that close. Use a bounded worker only under the worker reference.
