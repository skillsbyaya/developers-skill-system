---
name: close-session
description: "Closes a working session, preserves work in Git, and reports the outcome with a handoff when needed. Use whenever finished repository work is ready to merge or ship, including after a review with no edits; after agent-dev finishes or stops delivery; or when the user says to wrap up, close, end the session, or stop for today. Owns commits, pushes and merges for the skill system."
---

# Close Session

Save what later work needs, preserve the task's work, and report where it stands. Delivery owns implementation, assurance and story completion; close-session does not invent more work or relax those boundaries.

A **packet close** preserves one named packet, slice or checkpoint within its existing scope. When authorised work continues in this session, perform steps 1–2 and return to delivery without a final handoff. A **full close** reports the outcome when work actually stops.

Every commit, push and merge goes through step 2. A project's landing script is one way to perform that step. Reuse current session evidence; retrieve only missing or changed facts needed for the next action. After an earlier close, cover only the delta.

## 1. Save missing continuity

Use the project's declared state owners, otherwise the existing story, package or plan. Save unfinished work, decisions, constraints and findings that later work needs once with their owner. Link existing records, replace stale text, and update other documents only where this work made them wrong. Send distinct follow-up work through backlog planning to reuse any existing owner.

Preserve unresolved defects, recurring failures and workarounds that leave a future cost. If the cause is unknown, save the evidence and next diagnostic rather than inventing a fix. Expected failures and already-resolved transient mistakes need no backlog item. Do not repeatedly dismiss a real defect because its workaround succeeds.

Reconcile only affected status and next-action entries, preserving unrelated work. Replace settled questions with their decisions and sources; repair affected links. If reconciliation cannot finish safely, save the exact remaining edit with its owner. Send a confirmed agent-behaviour correction through `learn-lessons` current correction only when it would otherwise be lost. Create no session diary or separate handoff document.

## 2. Preserve and publish

Skip Git only when there are no task-owned edits, commits to preserve, or authorised landing operations outstanding. A clean working tree or a review with no edits can still need a push or merge.

1. **Establish scope.** Follow the project's Git workflow and existing authority. Include the agreed deliverable and its already-committed work; preserve unrelated edits and commits. Resolve entangled ownership or an unclear target before staging or publishing. Reuse checks valid for the current change; refresh affected evidence after changes.
2. **Resolve decisions and report.** Honour any requested preview and unresolved material decision before publication. Watched changes have had their preview. Briefly describe unreported behaviour changes, including changed instructions and consequential choices, and provide the diff or changed-file links. Quote exact rules when the user requests them or their wording needs a decision. Do not repeat an adequate report or add another approval gate.
3. **Commit safely.** When messaging is available and permitted, notify relevant sessions sharing the repository or affected resources before committing: branch, paths and intended landing. Resolve known overlap first; an announcement is not a lock. Stage explicit owned paths or hunks. Immediately before committing, recheck the branch and staged diff, including after coordination, so no unrelated work enters the commit. If shared state cannot be isolated safely, stop and report the conflict. Never force-push.
4. **Preserve incomplete work.** Commit and push a safe checkpoint to a non-live working branch before handing off or waiting on remote gates. Use `checkpoint:` for incomplete or failing work, state the missing or failed evidence, and do not land while it remains incomplete or its gates fail. Reuse an existing owned commit when only its push remains. Changes solely recording this unit's continuation stay on its working branch.
5. **Publish completed work.** Carry the project's authorised route through to completion: direct push, pull request, or landing script. Do not invent a checkpoint branch or PR when the project permits direct publication. A packet lands only when the project permits packet landing. Before landing, required assurance and acceptance must be current. For a PR, push the candidate before waiting on required gates and merge only the reviewed, checked head. Incorporate accepted comments before merging and refresh affected evidence. Read a red gate before retrying: return defects to delivery in this session; allow one rerun for a named environmental cause. Keep remote waits interruptible. Do not wait on unrelated previews or deployments, or leave an authorised mergeable PR open as a handoff.
6. **Verify, then clean up.** Verify the intended commit reached the remote and any required merge completed. Remove only a disposable worktree owned by this task after checking for concurrent use and local files that must survive, including ignored files; Git status alone is insufficient. Never force removal. If ownership or preservation is uncertain, retain it and report why. Return the main checkout to its base branch only when doing so respects its current work and owner.

Carry authorised publication through without separate requests for each step. Tags, releases and deployments require their own authorisation. If preservation or publication fails, report what actually reached Git and what remains local; do not claim a remote continuation is ready.

## 3. Choose a continuation only when needed

Resolve user-owned decisions needed for this task before dependent work, batching questions where possible. If evidence must come first, record that dependency. Do not ask for a new project direction just to fill a handoff.

Required completion or landing assurance retains the boundary set by its owner. Defer only checks already established as unnecessary for that boundary, recording when they become necessary; group release-only checks that share that point. A merge is not evidence that a required review became optional.

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
