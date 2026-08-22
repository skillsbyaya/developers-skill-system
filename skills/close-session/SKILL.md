---
name: close-session
description: "Runs end-of-session project housekeeping. Use when the user says to wrap up, close or end the session, stop for today, or otherwise clearly signals that the working session is ending."
---

# Close Session

Close only on a natural session-end signal, not a mid-task acknowledgement. Keep the result proportionate to the work completed and the attention still needed.

## Establish the close scope

1. Identify what this session actually changed, which durable facts or decisions remain unwritten, and whether work is complete, in review, blocked, or interrupted.
2. Resolve one forward work owner for the handoff: an explicit story or change package, one unambiguous active record, the matching delivery-status entry, or the backlog only when no committed owner exists. Separately collect every story whose lifecycle changed during this session; completing several stories must not make all but one invisible at close.
3. Inspect version-control state when the project uses Git. Separate session-owned changes from unrelated or entangled work, and classify the session's work as uncommitted, on `dev` only, or on `main` when those branches exist. Inspect dev-only commits so the close can say what `dev` contains that `main` does not. Note local-only versus pushed commits when that distinction matters.
4. Detect conditional work:
   - a session-touched story reached `done`, or its archive, active delivery-status entry, or backlog counterpart may be inconsistent;
   - active delivery, backlog, or project context otherwise needs reconciliation;
   - a clear behaviour correction should be processed by `learn-lessons`;
   - broad document drift or an approved stale-concepts list warrants `organise-docs`; or
   - Git changes from the session may need commit or push handling.

If a previous close already ran in this conversation, inspect only changes since that close and produce a fresh continuation result.

When context is unusually large, keep the same correctness gates but inspect only the current owner, session-touched files, and version-control evidence. Do not launch broad optional audits. A lesson that depends on the live exchange must be handled now or explicitly left unresolved; a fresh session cannot reconstruct it reliably.

## Reconcile current state

When a tracked story was touched, or delivery, backlog, or project context changed, read [State reconciliation](references/state-reconciliation.md). Update only state that this session made unambiguously stale. Before finishing, verify the close-out invariant for every story completed during the session even when another workflow already marked it `done`: the finished record is archived, its active delivery-status entry is gone, and no completed or committed duplicate remains in the living backlog. Fix an unambiguous mismatch in the same close; otherwise report it as unfinished or skipped rather than silently treating the close as a no-op.

Update a project document only when:

- this session changed the truth it owns;
- the new fact is durable and belongs there; and
- the edit does not create a competing summary, history, or task record.

Project `CLAUDE.md` holds hard project directives, not session status. Project context may receive a bounded durable fact or corrected delivery-status pointer, but never a copied next action. Use `organise-docs` only for broader structure, pruning, or stale-document work; close session does not sweep the document set itself.

**Write durable state by replacement, not accretion.** This applies to every record the session writes for its own future: project documents, delivery-status entries, and saved memory alike. When a record already covers what this session changed, rewrite the part now superseded instead of adding a fresh entry beside it — a record that gains a paragraph per session becomes a journal, which buries the current answer and charges every later session to read the whole history. Keep outcomes, absolute dates, and decisions that still bind; drop the narrative of how the work got there, which version control and archived records already hold.

**When a body of work closes, distil the record that tracked it.** Its durable residue is what still governs work not yet done: unresolved decisions, reusable seams, constraints, and lessons that outlive the delivery. Relocate anything durable to its proper owner first — a lasting rule belongs in project context, not in a record about finished work — then cut the record to that residue and update whatever indexes it. Verify the residue against its owner before cutting; a closed record left at full length is re-read at full cost for months.

If a confirmed behaviour correction surfaced, invoke `learn-lessons` before context is lost. Do not infer a lesson from ordinary friction or a simple factual correction.

## Handle Git conditionally

If session-owned Git changes remain uncommitted or session-created commits remain local-only, read [Git close](references/git-close.md) to determine their correct landing state. Do not skip that procedure merely because the user did not separately ask to commit or push. Do not commit unrelated changes merely to leave a clean worktree. A dirty worktree can be the correct close when scope, branch policy, user intent, or required evidence is unresolved.

## Finish

**Route work to the user only when it genuinely needs them.** Before an action enters an attention row or the handoff, test it against three grounds: their **judgement** — a real choice between options with different consequences; their **eyes** — verification only a person in front of a running system can perform; or their **access** — credentials, permissions, or an approval the project explicitly reserves for them. An action resting on none of those is Claude's to perform now rather than to report, and its result belongs under `What changed`. Being blocked does not transfer ownership: name the blocker and keep the action. Whatever survives the test should be as short as it can be and still move the work.

**Resolve the close to one next action.** Before writing anything, take the current owner's continuation and walk backwards through whatever must clear before it can start: a decision, an answer, an external result, missing evidence, a review, a Git landing. The action at the front of that chain is the next action, and it is the only one this close proposes. The rest of the chain appears solely as that action's prerequisites; work that merely comes afterwards does not appear at all. A close offering two things to do next has not finished this step — either one blocks the other, in which case lead with the blocker, or they are genuinely parallel, in which case which to take first is the user's call and belongs in the question below rather than in a list.

**A fresh-session handoff addresses one packet; it does not describe it.** When the next action is delivery work, write a paste-ready prompt naming exactly one owning record and exactly one current or next ready packet. **The record path and the packet name are the whole payload.** Everything else the next session needs — the packet's outcome, its constraints, its evidence requirements, its stop boundary — is already preserved in that record, one file-open away from the session you are addressing. Copying any of it makes the prompt long, and makes it wrong the moment the record changes. Name a prerequisite or constraint only when a fresh session would act incorrectly before the record could tell it, which is rare. End with a short fixed boundary: `Do not start a later packet; checkpoint the record and close when it is done.` A human checkpoint is its own entire handoff. If a multi-packet story has no usable packet definition, the prompt asks only to prepare or select its next bounded packet.

Validate the prompt before output. **Two lines is the budget** — roughly forty words after the actor label, stop boundary included. If it will not fit, the surplus is not handoff material: a fact the next session needs belongs in the owning record, and context the user needs belongs under `Where things stand`. Should the next session genuinely need setup no record can carry, give it a short section of its own above the handoff and keep the blockquote to the action. Never buy the extra room by lengthening the blockquote. The prompt must contain one imperative outcome and one stop boundary. Reject one that restates the packet's own contents, or that joins work with `then`, `and then`, an arrow, a sequence of story or packet IDs, or words such as `all remaining`; dependency IDs may appear only as prerequisites, never as additional actions. A broad story label is not a substitute for the next packet.

**Ask the question that unblocks; do not park it in the handoff.** When the front of the chain is a decision the user can answer now from what they already know, put it to them with `AskUserQuestion` during the close, then write the handoff from their answer — an unblocked action beats an accurate description of a blockage. Never write a handoff instructing them to decide something you could have asked. Record their answer in the document that owns the subject in the same close, so the next session inherits the decision rather than the question. If instead the blocker needs investigation, an external result, or evidence that does not exist yet, do not ask: that unblocking work is itself the next action.

Present the close as a visual summary, not a prose recap. Use only the rows and detail the actual state needs. Use these sections in this order, omitting optional sections that do not apply:

1. `### What changed` — a `File or record | Change` Markdown table. If no close-time edit was needed, include one `None` row rather than replacing the table with prose.
2. `### Where things stand` — include this section when there is Git state, an attention item, or an outcome of the session the tables alone would not make plain. Write outcomes in plain English, without "owner", "lifecycle", commit hashes, or agent-workflow terms.
   - **This section owns the readable account of where the work got to.** When the tables would leave that unclear, open with at most two sentences saying what happened and what it means for the user. Prose that explains, qualifies, or gives the background to the next action belongs here, never in the handoff box. Drop the sentences entirely when the tables already say it — this is context, not a session log.
   - For a Git project, add a `Git state | Detail` Markdown table only when relevant work exists. Include only non-empty rows, in this order: **Uncommitted**, **On Dev Only**, **On Main**. Place each item only in the furthest state it has reached. When `dev` exists, name what its dev-only commits contain rather than merely saying "committed" or "saved". Within **On Dev Only**, distinguish `Committed locally` from `Pushed` when relevant. Within **On Main**, distinguish `Merged` from `Committed directly` when relevant. Do not add a separate Git-status preface that repeats the table, and do not show `Nothing` or absent-branch rows.
   - Add an `Attention | Detail` Markdown table only when at least one attention item exists. Include only applicable rows: **Checks** for failing checks or vulnerabilities; **Unfinished** for half-done or blocked work; **Waiting on you** only for an item that passed the routing test above; and **Skipped** for deliberately omitted work that needs the user's attention. Do not report passing checks, successful security results, or `Nothing` rows.
3. `### Lessons` — a short list only when `learn-lessons` ran or left a lesson unresolved.
4. `### Handoff` — always last, in a blockquote so it reads as a visual box, and **at most two lines**. State exactly one immediate next action as an instruction: what to do, and which record it starts from. Prefix it with `> **New session:**` when the user should paste the action into a fresh Claude or Codex session, `> **You:**` when it genuinely requires the user's judgement, eyes, access, or approval, or `> **Waiting for <named person/system>:**` when an external actor must move first. **Open with the action, never with what this session finished.** Completed work belongs under `What changed` and `Where things stand`; it may appear here only as the few words needed to locate the action. For delivery work, use the validated one-packet prompt above verbatim after the actor label. Name one action — a scope label covering several pieces of work, or a chain joined by "then", is a plan, not a handoff. A pasted prompt does need to stand alone, and **the record path is what achieves that** — do not inline the record's contents chasing self-containment. Do not add a route, plan, downstream step, or second handoff line.

Leave a blank line between headings, tables, lists, and the handoff box.

Do not create a session log or durable handoff document. Do not choose a new priority merely because the session is ending. If no committed owner exists, take the next backlog item when backlog order makes it unambiguous; when it does not, that ordering is the decision to put to the user under the rule above, not a note telling them prioritisation is required.
