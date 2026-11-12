---
name: close-session
description: "Closes a working session, preserves work in Git, and reports the outcome with a handoff when needed. Use whenever finished repository work is ready to merge or ship, including after a review with no edits; after agent-dev finishes or stops delivery; or when the user says to wrap up, close, end the session, or stop for today. Owns commits, pushes and merges for the skill system."
---

# Close Session

Save what later work needs, preserve the task's work, and report where it stands. Delivery owns implementation, assurance and story completion; close-session does not invent more work or relax those boundaries.

A chat ending is a preservation boundary, not a delivery boundary. A **delivery batch** is one coherent outcome carried on the same working branch across chats, from its prepared record to completion. Use the existing story, pass or agreed change set; keep its stopping condition with the existing owner; when PM has assigned a batch, resolve its ID, members and finish condition from the existing queue or plan ([batch planning](../agent-pm/workflows/batch-planning.md)). Do not collect unrelated work or keep adding scope to postpone completion. A standalone request with no continuing batch finishes normally.

A **packet close** saves a checkpoint while work continues. A **full close** ends the chat; it can also be only a checkpoint. Neither means the batch is ready to land. A packet boundary alone needs no Git operation while work continues in the same chat. Preserve remotely before a handoff, a long wait or a risky operation, and when explicitly requested.

Every commit, push and merge goes through step 2. Reuse current evidence and retrieve only missing or changed facts; after an earlier close, cover only the delta.

## 1. Save missing continuity

Use the project's declared state owners, otherwise the existing story, package or plan. Save unfinished work, decisions, constraints and findings that later work needs once with their owner. Link existing records, replace stale text, and update other documents only where this work made them wrong. Send distinct follow-up work through backlog planning to reuse any existing owner.

Preserve unresolved defects, recurring failures and workarounds that leave a future cost. If the cause is unknown, save the evidence and next diagnostic rather than inventing a fix. Expected failures and already-resolved transient mistakes need no backlog item. Do not repeatedly dismiss a real defect because its workaround succeeds.

Reconcile only affected status and next-action entries, preserving unrelated work. Replace settled questions with their decisions and sources; repair affected links. If reconciliation cannot finish safely, save the exact remaining edit with its owner. Send a confirmed agent-behaviour correction through `learn-lessons` current correction only when it would otherwise be lost. Create no session diary or separate handoff document.

## 2. Preserve or land

Skip Git when no task-owned edits, unpushed commits or authorised landing remain. A clean review may still need to preserve or publish existing commits.

1. **Choose the boundary.** Follow the project's branch and target policy. Checkpoint an open batch, even when this chat's small change is finished. Land when its stopping condition is met, the user requests landing, or a named dependency needs the change integrated before further work. Do not infer a landing requirement from permission to land. Do not hold an otherwise complete standalone request for hypothetical future work. A change that only records a result (an acceptance, a clean review, a status line, a captured follow-up) is not a landing unit: checkpoint it on its open batch's branch, otherwise on a `notes/<topic>` branch named in the handoff, and the next landing carries it. Land it alone only when it allocates an ID another session could take, or other work needs it on the base branch now.
2. **Establish scope.** Include owned continuation commits and preserve unrelated work. Resolve entangled ownership or an unclear target before staging. Honour an outstanding preview or material decision before landing; safe checkpointing can precede that decision. Report unreported behaviour changes briefly, with a diff or changed-file links, without another approval gate.
3. **Commit safely.** Coordinate known overlap when messaging is available and permitted. Stage explicit owned paths or hunks, then recheck the branch and staged diff immediately before committing. Never force-push. A checkpoint needs ownership, secret/generated-file safety and a resumable record; it does not require a green tree, full tests, independent review, a PR or the landing script. Preserve missing or failed evidence honestly, with its next required boundary. Do not rerun checks merely to save progress.
4. **Checkpoint an open batch.** Commit and push to its existing non-live working branch; use `checkpoint:` while the batch is incomplete. Reuse an existing owned commit when only its push remains. If no working branch exists, create one under project policy; keep it and its checkout for continuation. Verify the remote holds the checkpoint, then stop this step. Do not open a PR just to save work: pushes to an open PR may trigger CI. If branch pushes themselves trigger expensive checks, surface that configuration mismatch rather than bypassing gates or claiming a cheap checkpoint.
5. **Land a ready batch.** For a numbered batch, check every included scope against its owning acceptance evidence and finish condition; one finished member cannot complete the batch. Inspect the combined diff from its recorded starting revision, including earlier checkpoint commits, for missing or out-of-scope changes. Resolve missing baseline or ownership before landing. Carry pending `notes/` checkpoints that still apply into this landing, and delete their branches once it is verified. Run outstanding completion and landing assurance once against that candidate, reusing evidence that still matches its inputs and environment. Include the batch ID and member links in the landing PR or commit; reconcile its existing queue row only after verified landing. Carry the authorised direct-push, PR or landing-script route through to completion. Do not add a checkpoint branch or PR to a permitted direct publication. For a PR, push before waiting for required gates and merge only the reviewed, checked head. Apply accepted fixes and refresh affected evidence. Read a red gate before retrying; fix defects in this session and allow one rerun for a named environmental cause. Do not wait on unrelated deployments or leave an authorised mergeable PR open.
6. **Verify and clean up after landing.** Verify remote publication and any required merge. Remove only this task's disposable worktree, after checking concurrent use and local files including ignored files; Git status alone is insufficient. Never force removal. Retain uncertain worktrees. Return the main checkout to its base only when current work and ownership permit it.

Tags, releases and deployments retain their own authorisation. If preservation or publication fails, state what reached Git and what remains local; never claim remote continuation is ready when it is not.

## 3. Choose a continuation only when needed

Resolve user-owned decisions needed for this task before dependent work, batching questions where possible. If evidence must come first, record that dependency. Do not ask for a new project direction just to fill a handoff.

Delivery owns when evidence is needed: before dependent work, at batch completion, or at release. A checkpoint does not bring those checks forward. Carry pending checks with that boundary in the existing record; do not call the batch complete or land it with required evidence missing.

Choose at most one next action: unblock this unit, resume its unfinished work or required assurance, then the next ready packet or unclaimed item in the existing agreed plan. When relevant parallel sessions already carry the continuation, name them and their known state instead of assigning their work again. When the requested outcome is complete and nothing needs continuation, end without a handoff.

## Output

Give the core handoff in short lines and everyday language:

- Begin the status line with **Done** when this session achieved its requested goal, or **Not done** otherwise. Say what finished and where repository work was saved or landed. State separately if the wider batch is still open.
- **Your action** — Give the one thing the user needs to do now. Write “None” when the batch is open and the next step belongs to an agent.
- **Next** — When work remains, name who owns the next step and what they will do. Link the existing record for details.

Lead with the core handoff by default. Include other information when it changes how the user understands the result or what they should do. Put it before the summary when it needs immediate attention. Keep routine evidence in the record. A completed task with no next action may need only a status line.

For a handoff to another session, put **Next session** below the summary. Follow it with a fenced `text` block containing only the prompt to paste. Include the task, batch ID if assigned, verified branch, skill and record when applicable. The prompt says what to build, never when to land: the record's boundaries decide that. Put **Model** and **Effort** on separate lines below the closing fence. Use the project's choices when specified.

Name active sessions only from session evidence. When the user or project requests a branch inventory, fetch and list non-permanent remote branches under **Remote branches**, with commit age and verified merge state. Say when the inventory is unavailable.
