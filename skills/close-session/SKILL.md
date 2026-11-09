---
name: close-session
description: "Closes a working session, preserves work in Git, and reports the outcome with a handoff when needed. Use whenever finished repository work is ready to merge or ship, including after a review with no edits; after agent-dev finishes or stops delivery; or when the user says to wrap up, close, end the session, or stop for today. Owns commits, pushes and merges for the skill system."
---

# Close Session

Save what later work needs, preserve the task's work, and report where it stands. Delivery owns implementation, assurance and story completion; close-session does not invent more work or relax those boundaries.

A chat ending is a preservation boundary, not a delivery boundary. A **delivery batch** is one coherent outcome carried on the same working branch across chats. Use the existing story, pass or agreed change set; name its stopping condition in its existing record. Do not create a batch tracker, collect unrelated work, or keep adding scope to postpone completion. A standalone request with no continuing batch finishes normally.

A **packet close** saves a checkpoint while work continues. A **full close** ends the chat; it can also be only a checkpoint. Neither means the batch is ready to land. A packet boundary alone needs no Git operation while work continues in the same chat. Preserve remotely before a handoff, a long wait or a risky operation, and when explicitly requested.

Every commit, push and merge goes through step 2. Reuse current evidence and retrieve only missing or changed facts; after an earlier close, cover only the delta.

## 1. Save missing continuity

Use the project's declared state owners, otherwise the existing story, package or plan. Save unfinished work, decisions, constraints and findings that later work needs once with their owner. Link existing records, replace stale text, and update other documents only where this work made them wrong. Send distinct follow-up work through backlog planning to reuse any existing owner.

Preserve unresolved defects, recurring failures and workarounds that leave a future cost. If the cause is unknown, save the evidence and next diagnostic rather than inventing a fix. Expected failures and already-resolved transient mistakes need no backlog item. Do not repeatedly dismiss a real defect because its workaround succeeds.

Reconcile only affected status and next-action entries, preserving unrelated work. Replace settled questions with their decisions and sources; repair affected links. If reconciliation cannot finish safely, save the exact remaining edit with its owner. Send a confirmed agent-behaviour correction through `learn-lessons` current correction only when it would otherwise be lost. Create no session diary or separate handoff document.

## 2. Preserve or land

Skip Git when no task-owned edits, unpushed commits or authorised landing remain. A clean review may still need to preserve or publish existing commits.

1. **Choose the boundary.** Follow the project's branch and target policy. Checkpoint an open batch, even when this chat's small change is finished. Land when its stopping condition is met, the user requests landing, or a named dependency needs the change integrated before further work. Do not infer a landing requirement from permission to land. Do not hold an otherwise complete standalone request for hypothetical future work.
2. **Establish scope.** Include owned continuation commits and preserve unrelated work. Resolve entangled ownership or an unclear target before staging. Honour an outstanding preview or material decision before landing; safe checkpointing can precede that decision. Report unreported behaviour changes briefly, with a diff or changed-file links, without another approval gate.
3. **Commit safely.** Coordinate known overlap when messaging is available and permitted. Stage explicit owned paths or hunks, then recheck the branch and staged diff immediately before committing. Never force-push. A checkpoint needs ownership, secret/generated-file safety and a resumable record; it does not require a green tree, full tests, independent review, a PR or the landing script. Preserve missing or failed evidence honestly, with its next required boundary. Do not rerun checks merely to save progress.
4. **Checkpoint an open batch.** Commit and push to its existing non-live working branch; use `checkpoint:` while the batch is incomplete. Reuse an existing owned commit when only its push remains. If no working branch exists, create one under project policy; keep it and its checkout for continuation. Verify the remote holds the checkpoint, then stop this step. Do not open a PR just to save work: pushes to an open PR may trigger CI. If branch pushes themselves trigger expensive checks, surface that configuration mismatch rather than bypassing gates or claiming a cheap checkpoint.
5. **Land a ready batch.** Run outstanding completion and landing assurance once against the combined candidate, reusing evidence that still matches its inputs and environment. Carry the authorised direct-push, PR or landing-script route through to completion. Do not add a checkpoint branch or PR to a permitted direct publication. For a PR, push before waiting for required gates and merge only the reviewed, checked head. Apply accepted fixes and refresh affected evidence. Read a red gate before retrying; fix defects in this session and allow one rerun for a named environmental cause. Do not wait on unrelated deployments or leave an authorised mergeable PR open.
6. **Verify and clean up after landing.** Verify remote publication and any required merge. Remove only this task's disposable worktree, after checking concurrent use and local files including ignored files; Git status alone is insufficient. Never force removal. Retain uncertain worktrees. Return the main checkout to its base only when current work and ownership permit it.

Tags, releases and deployments retain their own authorisation. If preservation or publication fails, state what reached Git and what remains local; never claim remote continuation is ready when it is not.

## 3. Choose a continuation only when needed

Resolve user-owned decisions needed for this task before dependent work, batching questions where possible. If evidence must come first, record that dependency. Do not ask for a new project direction just to fill a handoff.

Delivery owns when evidence is needed: before dependent work, at batch completion, or at release. A checkpoint does not bring those checks forward. Carry pending checks with that boundary in the existing record; do not call the batch complete or land it with required evidence missing.

Choose at most one next action: unblock this unit, resume its unfinished work or required assurance, then the next ready packet or unclaimed item in the existing agreed plan. When relevant parallel sessions already carry the continuation, name them and their known state instead of assigning their work again. When the requested outcome is complete and nothing needs continuation, end without a handoff.

## Output

Normally use a few sentences:

- **Outcome:** what finished and any material verification limit. For repository work, give this task's actual branch and preservation or landing state, distinguishing repositories when more than one is involved.
- **Problems, when present:** every unresolved issue affecting the user's immediate decisions, its practical impact and the needed action. A saved record does not replace surfacing a material blocker; link it instead of repeating its detail. Do not repeat a problem already explained in this response.
- **Continuation, when needed:** one action with its owner. A user action, decision or wait is one plain sentence. An agent handoff is a prompt for the next session in exactly this shape:

  ````markdown
  **Next session**

  ```text
  <what the next session is about, in plain words>. On <verified working branch>, <verb> <unit> with <skill> from <existing record path>.

  Model: <capability class>
  Effort: <level>
  ```
  ````

  Omit a branch or record that does not apply. Do not require a new chat or invent a record. Include Model and Effort when project policy asks for them or they help the continuation; otherwise High/high for consequential judgement and Standard/medium for settled work, naming the class, never a product.

Report relevant parallel sessions from session evidence, not branch names; label unknown state honestly. When the user or project requests a branch inventory, fetch and list non-permanent remote branches as **Remote branches**, with commit age and verified merge state. Distinguish that inventory from active sessions; if retrieval fails, report it as unavailable rather than empty. Do not perform a repository-wide census on every close.

No empty sections, repeated change report, routine check list, or manufactured next task.
