---
name: close-session
description: "Closes a working session, preserves work in Git, and reports the outcome with a handoff when needed. Use whenever finished repository work is ready to merge or ship, including after a review with no edits; after agent-dev finishes or stops delivery; or when the user says to wrap up, close, end the session, or stop for today. Owns commits, pushes and merges for the skill system."
---

# Close Session

Save what later work needs, preserve the task's work, and report where it stands. Delivery owns implementation, assurance and story completion; close-session invents no work and relaxes no boundary.

A chat ending is a preservation boundary, not a delivery boundary. Work continues on one branch across chats as a story, a pass or a numbered batch; the existing record owns its scope and stopping condition, and [batch planning](../agent-pm/workflows/batch-planning.md) owns batch IDs, members and finish conditions. Collect no unrelated work and add no scope to postpone completion. A standalone request with no continuing unit finishes normally.

A **packet close** checkpoints while work continues; a **full close** ends the chat and may be only a checkpoint. Neither means the unit is ready to land. A packet boundary inside one chat needs no Git operation. Preserve remotely before a handoff, a long wait or a risky operation, and when asked. After an earlier close, cover only the delta.

## 1. Save missing continuity

Save unfinished work, decisions, constraints and findings once, with the project's declared state owner, otherwise the story, package or plan. Replace stale text and link existing records; touch other documents only where this work made them wrong. When this work fixed a defect or removed a rule, delete every note, memory and workaround that existed because of it, and leave no record that it went: the commit message carries the reason. Route distinct follow-up work through backlog planning.

Save an unresolved defect or recurring failure as work to fix, through backlog planning: its cause or, when unknown, the evidence and the next diagnostic, not an invented fix. Its workaround is written in that item and nowhere else, so it leaves when the fix lands. Expected failures and resolved transient mistakes need no item.

Reconcile only affected status and next-action entries; replace settled questions with their decisions. If reconciliation cannot finish safely, record the exact remaining edit with its owner. Send a confirmed agent-behaviour correction through `learn-lessons` only when it would otherwise be lost. Create no session diary or separate handoff document.

## 2. Preserve or land

Every commit, push and merge goes through this step. Skip Git when no task-owned edits, unpushed commits or authorised landing remain; a clean review may still need to publish existing commits.

1. **Choose the boundary** under the project's branch, target and landing policy. Checkpoint an open unit, even when this chat's small change is finished. Land when its stopping condition is met, the user asks, or a named dependency needs the change integrated first. Permission to land is not a requirement to land; a complete standalone request is not held for hypothetical future work. A change that only records a result (an acceptance, a clean review, a status line, a captured follow-up) is not a landing unit: checkpoint it on its unit's branch, otherwise on the project's record-only branch (`notes/<topic>` when none is declared), named in the handoff, for the next landing to carry. Land it alone only when it allocates an ID another session could take, or other work needs it on the base branch now.
2. **Establish scope.** Include owned continuation commits; preserve unrelated work. Resolve entangled ownership or an unclear target before staging. Honour an outstanding preview or material decision before landing; a safe checkpoint may precede it. Report unreported behaviour changes briefly, with a diff or changed-file links, without another approval gate.
3. **Commit safely.** Coordinate known overlap when messaging is available and permitted. Stage explicit owned paths or hunks, then recheck the branch and staged diff immediately before committing. Never force-push. A checkpoint needs ownership, secret and generated-file safety and a resumable record, not a green tree, full tests, review, PR or landing script. Record missing or failed evidence honestly with the boundary that requires it; do not rerun checks merely to save progress.
4. **Checkpoint an open unit.** Commit and push to its existing non-live working branch, with `checkpoint:` while the unit is incomplete; create the branch under project policy if none exists and keep its checkout for continuation. Verify the remote holds it, then stop. Never open a PR to save work. If branch pushes themselves trigger expensive checks, surface that mismatch rather than bypass gates or claim a cheap checkpoint.
5. **Land a ready unit.** For a batch, check every member against its acceptance evidence and the finish condition; one finished member does not complete it. Inspect the combined diff from the unit's recorded starting revision, checkpoints included, for missing or out-of-scope changes. Carry record-only branches that still apply, and delete them once the landing is verified. Run outstanding completion and landing assurance once against that candidate, reusing evidence whose inputs and environment still match. Name the batch ID and members in the PR or commit; reconcile the queue row only after verified landing. Carry the authorised route (direct push, PR or landing script) to completion without adding a checkpoint branch or PR to it, and merge only the reviewed, checked head. Read a red gate before retrying: fix defects in this session; allow one rerun for a named environmental cause. Do not wait on unrelated deployments or leave an authorised mergeable PR open.
6. **Verify and clean up.** Verify remote publication and any required merge. Remove only this task's disposable worktree, after checking concurrent use and local files including ignored ones; Git status alone is insufficient. Never force removal; retain uncertain worktrees. Return the main checkout to its base only when current work and ownership permit.

Tags, releases and deployments keep their own authorisation. If preservation or publication fails, state what reached Git and what remains local; never claim remote continuation is ready when it is not.

## 3. Choose a continuation only when needed

Resolve user-owned decisions this task needs before dependent work, batched where possible; if evidence must come first, record that dependency. Do not ask for a new project direction to fill a handoff.

Delivery owns when evidence is needed: before dependent work, at completion, or at release. A checkpoint brings none of those forward; never call the unit complete, or land it, with required evidence missing.

Choose at most one next action, in this order: unblock this unit; resume its unfinished work or required assurance; the oldest other open unit that can now be finished; the oldest that can only move a step; only then the next ready item in the existing plan. Started work is finished before new work starts.

An open unit is a non-permanent remote branch holding work that has not landed. Leave out one a parallel session is working on, named from session evidence only, instead of reassigning its work. Before passing over any other, read the wait its record names and test it now: the version released, the change landed, the date reached. A wait that has ended makes that unit the next action; replace the stale wait in its record. A wait only the user can end goes in **Your action**. A unit with no recorded wait can move; it can be finished when its record leaves only its last step or check.

When the requested outcome is complete and no open unit can move, end without a handoff.

## Output

Give the core handoff in short lines and everyday language:

- Begin the status line with **Done** when this session achieved its requested goal, or **Not done** otherwise. Say what finished and where repository work was saved or landed. State separately if the wider unit is still open.
- **Your action** — the one thing the user needs to do now, stated so they can do it; **None** when the unit is open and the next step belongs to an agent.
- **Next** — when work remains, who owns the next step and what they will do, linking the existing record.
- **Repository** — on a full close, the worktrees and non-permanent remote branches that exist, each with its age and merge state, from a fresh fetch, and for each open unit what it waits for and whether that was tested in this close. A report, not a clean-up: removal belongs to step 2.6. Say when the inventory is unavailable.

Add other information only when it changes how the user understands the result or what to do, placed first when it needs immediate attention; routine evidence stays in the record. A completed task with no next action may need only the status and repository lines.

For a handoff to another session, put **Next session** below the summary, then a fenced `text` block holding only the prompt to paste: the task, batch ID if assigned, verified branch, skill and record. The prompt says what to build, never when to land. Below the closing fence put **Model** and **Effort** on separate lines, naming the model and effort the project's workflow assigns to that step rather than a tier label.
