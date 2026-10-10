# Change log

This file records material changes to the integrated system. Because the skills are interconnected, update notes describe system-level behaviour rather than isolated skill releases.

## 10 October 2026: Fewer stops between packets, fixes and landing

A delivery session continues to the next ready packet once the current one passes its gate and is pushed or landed, stopping only for a human checkpoint, a user decision, a required independent review, or low context. A story's review session applies its confirmed fixes itself, and `check-work` now says so, so findings are recorded only when they outlive the session. An investigation that was asked to fix carries straight into delivery when the cause is confirmed at High confidence and the change involves no user-owned decision; otherwise it still stops for confirmation.

`close-session` pushes as soon as checks pass, reuses checks already passed on the same code, waits only on checks the project requires for merge (never a preview or deployment), and does not land record-only changes. The handoff's Model line names the capability class only.

## 9 October 2026: Fewer packets, one review, shorter closes

Stories are split into packets only where the work genuinely divides: a human step between parts, a part that must land and be proven before the next, or work too large for one session. `agent-dev` story preparation alone plans packets; `agent-pm` no longer does. Independent review happens once per story after the last packet, and that review session applies its fixes, rechecks them, completes, and lands the story. When no review is required, the last packet's session completes the story. A separate re-review runs only when a fix substantially changes a critical surface. Deferred review findings must name a backlog ID or story key.

`close-session` is one short file with one output shape for every close: a status line or two, problems only when real, and one handoff. Packet and full closes differ only in boundary; the separate workflows, state-reconciliation, knowledge-capture, model-handoff, and Git references are removed, since `agent-dev` already owns story lifecycle and completion.

Local installs can now be symlinked to the clone (`./scripts/install.sh --link all`), and cloud bootstraps install from `main` rather than a pinned commit.

## 9 October 2026: Lighter skill maintenance

`upskill` now has three jobs (change, create, review) plus external discovery, and a shared writing standard that treats ceremony, repetition, and unclear output as defects. The separate edit, repair, restructure, audit, library-review, registration, and eight-stage pressure-test routes are removed; new skills are trialled against a few realistic requests instead. Reported failures are traced through session transcripts to the instruction that caused them, and fixes replace or delete that text rather than adding rules beside it.

## 29 September 2026: Cloud-resumable session checkpoints and canonical distribution

The public repository is now the explicit canonical source for shared and platform-specific skills. A deterministic installer refreshes Claude Code and Codex deployments while preserving unrelated runtime or plugin skills. Codex receives its project-guidance bridge, Claude retains the Claude-only Codex delegation skill, and Great Britain employment-law guidance is now part of the shared distribution.

Repository work now commits and pushes a safe checkpoint to a non-live working branch at every session boundary. Incomplete or failing work may be preserved through a clearly labelled checkpoint without being presented or merged as complete. Live or protected branches, force-pushes, merges, releases, deployments, secrets, and entangled unrelated changes retain their existing safeguards.

Session handoffs now name a remote branch and repository-relative record path instead of assuming the next local or cloud session shares an absolute checkout path. Application repositories can replace vendored skill copies with a small cloud bootstrap that installs the public distribution during environment setup.

## 12 September 2026: Documentation conventions in project context

`manage-project-context` now supplies a documentation-conventions template containing the existing naming and placement defaults. Each project records the rules it adopts in its own context. Document readers and writers consult that section directly; template changes reach existing projects only through deliberate adoption.

`organise-docs` retains pruning, merging, archiving, restructuring, indexing, and identifier-vocabulary maintenance. The former document-conventions CSV, convention-resolution reference, and project-override template have been removed. Existing project convention records can be consolidated into project context while preserving local decisions and stable paths. Backlog planning remains with `agent-pm`.

When upgrading an installed copy, remove the three obsolete resources listed in the [upgrade guidance](README.md#upgrading-documentation-conventions). Copying updated files alone leaves those resources behind.

## 12 September 2026: Fresh-session packets and story-level commits

Multi-packet delivery now defaults to keeping code and current records uncommitted in one checkout until separate story or package completion. Explicit project commit policies still apply. Each packet includes implementation, targeted checks, and a compact handoff that supports continuation in Claude Code or Codex. Execution state preserves the checkout, branch, original story base, and packet baseline so interrupted work and overlapping changes can be resumed without replaying earlier sessions.

Packet closing no longer assumes that code has already landed or requires a clean worktree. Implementation self-checks remain with each packet; separate reviews remain driven by risk, with integrated checks and whole-story assessment at completion. Context loading and successful tool output stay bounded, and handoffs recommend a model and reasoning effort for the next action without treating all completion work as mechanical.

## 7 September 2026: Same-run decisions and self-contained landing units

User-owned decisions are now asked in the run that raises them, batched into one round of questions, instead of being reported as unresolved work for a later session. Decisions may remain open only when evidence, an external actor, or another event must come first; specialist-owned choices continue to route to their specialist.

Delivery records now describe the change and the state it leaves behind rather than recording merge metadata that source control already owns. Where project policy lands each packet, its code, record updates, status, and stale orientation pointers land together. Post-landing verification records only divergence, and factual corrections are landed as their own boundary rather than carried as an uncommitted claim on another session's branch or worktree.

Close-session handoffs now use one plain-language subject and one pasteable instruction naming the delivery skill and record. The named skill carries its own gate, update, completion, and close procedure, so handoffs no longer repeat it. Assurance also names the environment actually observed and keeps human preview focused on observable behaviour rather than source-control artifacts, while cleanup and lesson workflows more sharply distinguish live ownership, stale duplication, and decisions that should not remain parked.

## 31 August 2026: Explicit owner completion and enforceable lessons

Multi-packet delivery now preserves a separate story- or package-completion boundary after the final implementation packet. Owners maintain one current completion-assurance note covering the consequence floor, unresolved attention, reusable evidence, limitations, and selected completion condition. Packet and session close workflows prevent premature lifecycle close-out, while completion and assurance workflows consume the note without repeating valid evidence.

Lesson handling now identifies the actor and artefact present at the moment a failure occurs before choosing where prevention belongs. Repeated application gaps at three or more occurrences can no longer be left as another unresolved increment; they require a usable discriminator, a better-positioned owner, or a deterministic check.

## 27 August 2026: One delivery close and durable documentation carry-forward

Every Agent Dev delivery route now ends through Close Session exactly once. Named implementation packets use packet close regardless of whether their implementation was direct, coordinated, or staged; other delivery boundaries use full close. Agent Dev records delivery evidence before closing but no longer emits a competing completion summary.

Close Session now updates every known authoritative document made stale by the work or a post-landing action. When publishing a factual correction alone would require another full commit or pull-request cycle, the corrected local files and their intended landing route are recorded in the project's existing continuation source and repeated in the handoff, so the next Agent Dev session adopts them without another user instruction.

Close triage now chooses lifecycle boundary and preservation depth independently. Packet and full closes can each remain routine or conditionally use shared knowledge-rich capture, so simple work stays light while interconnected decisions, durable corrections, and consequential mistakes are preserved without widening a packet into story completion or Git ceremony.

## 26 August 2026: Forward handoffs after completed work

Full session closes now always end with one compact handoff. When the current work is complete, the close selects the next explicit item from the authoritative ordered backlog or project plan. If no next item is unambiguous, it honestly hands the decision about where the project should go next to the user instead of saying that no continuation is required.

## 24 August 2026: Workflow boundaries and session continuity

The system's delivery, assurance, and session-continuation boundaries were refined:

- Multi-packet development now uses one packet per session, a narrow packet safety gate, and a separate story-completion session for integrated verification and landing.
- Testing workflows can proceed from an authorised "review and fix" request into bounded test changes, while still stopping for materially different or production-facing work.
- Assurance now distinguishes lightweight evidence disposition from a new review, so unavailable or proposed checks do not automatically trigger human preview.
- Session closing now has separate packet-close and full-close workflows, with compact knowledge capture and clearer Git and state-reconciliation limits.
- Project context, personalisation, documentation cleanup, lesson capture, and skill maintenance now hand adjacent work to its owner unless the user explicitly included it.

## 22 August 2026: Token-efficiency update

Claude's token limits for five-hour usage windows were reduced by 50%. The existing delivery workflows could then require several restarts to complete a change.

The skill system was audited and adjusted to reduce token use:

- Product-management work now groups delivery into smaller, implementation-shaped packets instead of batches organised around human checkpoints.
- Development work now completes one packet per session rather than attempting several packets in the same session.
- Documentation practices were tightened to reduce unnecessary context loading and repeated material.

This update was completed before the repository was created and is recorded here as the first public update note.
