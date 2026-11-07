# Change log

This file records material changes to the integrated system. Because the skills are interconnected, update notes describe system-level behaviour rather than isolated skill releases.

## 7 November 2026: The next-session prompt is a grey box again

An agent handoff from close-session is once more a fixed, copyable prompt: a **Next session** label over a fenced text block, which renders as a grey box with a copy button, holding the plain-words purpose, branch, unit, skill and record, then Model and Effort lines. User actions and waits stay one plain sentence. Prompted by the user finding handoffs hard to follow after the shorter-closes change removed the fixed shape.

## 7 November 2026: Safer preservation and shorter closes

Close-session now handles already-committed work after a clean review or resumed session, separates incomplete checkpoints from completed publication, and follows the project's direct-push, PR or scripted route. Cleanup requires task ownership and preservation of local files, including ignored files; uncertain worktrees stay in place and removal is never forced.

Required completion and landing assurance retain their owning boundaries; only checks unnecessary for those boundaries may be deferred. Material blockers stay visible even when documented. Failure capture targets unresolved defects, recurrence and workarounds with a future cost rather than every transient command error.

A completed task may end without a handoff. Reports describe outcomes and useful continuation without mandatory rule quotations, model fields or branch censuses. Requested remote-branch inventories remain available under their own label; active-session claims require session evidence. Dev and close-session coordinate relevant shared work where messaging is permitted, then recheck state. Repository policy now distinguishes unfinished checkpoints from completed direct publication.

## 7 November 2026: Close-session stops handing off to proof that nothing waits on

Close-session's next-action order put any review or completion check on the last unit ahead of the next build, because a story whose code had merged still counted as "incomplete". A review, walkthrough or completion check now goes next only when something waits on it now: a merge it gates, a packet that builds on it, or a release or user due before more building could finish. Otherwise it is recorded with the point that needs it, and checks waiting for the same point run together in one session. Prompted by a day in one project where about half of seventeen handoffs were reviews, walkthroughs or staging completion checks on work already merged and not due for release for two days, one session per story.

## 7 November 2026: Improve the existing Markdown planning workflow

Backlog intake searches likely owners and cross-area alternatives before reading full detail, reuses an existing owner on repeated capture, and preserves source, authority and residual scope during partial adoption. Outcome grouping stays separate from priority and concurrent ownership. Waiting work names its unlock condition and next check.

PM now routes roadmap reviews explicitly, separating preferred order, prerequisites and milestone acceptance. Documentation updates replace settled questions and reconcile affected action references while preserving unique evidence. The epics template no longer asks PM to plan Dev's execution packets. Delivery handles interrupted multi-file close-out and changed prerequisites explicitly; close-session follows declared state owners instead of copying actions into multiple records.

These changes retain project Markdown and Git as the workflow. They add no queue app, local store or cloud dependency. Existing documentation/context/cleanup ownership remains in force. Targeted retrieval and clearer guidance are supported by the bounded queue experiment; no general token, cost or concurrency guarantee is claimed.

## 4 November 2026: Parallel sessions announce instead of coordinating through Git

Before anything a parallel session could collide with (chiefly each commit, and also claiming a backlog or story ID, resetting a shared local service, or editing files another session announced) a session sends each other session running on the same machine one line: its branch and what it will touch. When two announce the same thing they agree the order first. Close-session sends the line before committing; agent-dev covers the rest. Agent Dev's preview-loop parallel set (lettered sibling branches, a `checkpoint: done` subject read by every sibling, one session landing the merged set) is removed: it was never used, and sessions were already messaging each other. A parallel pass is now its own story and lands on its own.

## 3 November 2026: A harmless failure is still a finding

Close-session counts every tool, script or check failure a session saw as a finding, including one that proved harmless or that a saved workaround handled: it is fixed, or filed in the backlog with its cause and fix, and never closed as a known quirk. Prompted by a landing script that reported failure after a successful merge on three landings over five days; each session confirmed the merge, applied the saved workaround and moved on, until the user asked what the error was. The fix was a few lines.

## 3 November 2026: Close-session separates this session's branch from other sessions'

Close-session's "Unlanded work" line becomes a "Work in progress" section with two lines: this session's branch and its state first, then every other remote working branch underneath. Status no longer repeats where the work is. Prompted by a user who could not tell at a glance, from one line naming three branches, which was the session they had just closed and what was waiting on it.

## 3 November 2026: A request-time read is checked for its cost

Agent Dev's delivery controls treat the cost of a page render, API handler or page-called database function as part of its check: independent awaits run together, a render asks each question once, a per-row helper is measured by counting its calls, and a project's latency or round-trip budget is a check like any other. Prompted by one project's third slowness fix in three days (a per-row policy helper, a dashboard waterfall, then helpers re-planned on every call with pages making up to 26 requests in series), each shipped because correctness checks passed and nothing measured cost; the project now fails those shapes mechanically, and this rule covers what its guards cannot see.

## 3 November 2026: A finished session hands off to its parallel sessions

When a session's unit is done while parallel sessions carry the user's wider work, close-session's handoff names those sessions and whether each is finished or still running; with no parallel sessions it gives the next item from the project's plan, as before. A plan item another session already holds is no longer a next action, and a handoff's working branch is one the session worked on, or the base branch. Prompted by a session that filed and merged one backlog item split out of a parallel polish pass, then handed off "continue the polish pass" on another session's sibling branch because the handoff had no way to say nothing follows.

## 3 November 2026: Parallel preview-loop sessions land as one set; every handoff lists unlanded work

Agent Dev's preview loop gains parallel sessions: each runs in its own worktree on a lettered sibling branch of one set, never writes the shared story record, status lines or backlog, and marks its branch `checkpoint: done` when the user accepts its item. The session that finds every sibling done lands the set once, after claiming the set's base branch by pushing it so two siblings cannot land together; "land what's done" lands the finished siblings at any time. Close-session's output gains an always-present "Unlanded work" line listing every remote working branch with its state and age, or `none`, so finished work waiting on a set, or anything else unmerged, is never lost. The user may name the set so every session can open at once, and each session claims its lettered branch by pushing it before any other work, so two sessions opened together cannot take the same letter. A sibling whose item turns out to need a migration, a new route or new behaviour leaves the set as its own story so the set does not wait on it. Prompted by a user who runs several small-edit sessions concurrently and wanted one shipment without risking stranded branches.

## 3 November 2026: A prepared story is reported as what it will do; Agent Dev closes its own sessions

When Agent Dev finishes preparing a story, it tells the user what the story will do: one bullet per decision, named in a few words and explained in one or two plain sentences, with the user's own decisions marked, then any corrections to other documents and one line on the build stages. Function names, files, checks and process stay out, and the report doubles as close-session's change report. Prompted by a preparation summary the user found clear, after a second version written as a section-by-section tour of the record was unreadable.

Agent Dev also invokes close-session itself at the end of any workflow that changed the repository when nothing awaits the user, and asks first only when a decision, review or comment they would want is open. A preparation-only request now ends through close-session rather than stopping.

## 2 November 2026: A finished assessment closes the session itself

Check-work no longer returns a finished assessment "to the relevant owner" or reserves the move from `review` to `done` for Agent Dev. When an assessment ends with nothing awaiting the user and the work lives in a repository, the session invokes close-session itself, which lands, checkpoints or only records by the project's rules. Prompted by a clean High review of a story packet that ended with "the delivery session should update the record and land the branch" when the same session could have landed it.

## 2 November 2026: A handoff problem is written for the person who must act on it

Close-session's output spec now says how a problem is written, not only when one belongs in the list: the verdict first, then what it costs the user in practice, the fix with what it takes and what it loses, its one risk, why the session did not do it, and the single action that unblocks it, naming an internal mechanism only when the user has to act on it. Prompted by a handoff that described a drifted local database stack in terms of a missing column and a port, which the user could not read, where the same problem written as "you cannot preview on your Mac until it is reset; a reset takes minutes and loses test data only; I did not do it because another session may be using it; say go" was clear.

## 2 November 2026: Git belongs to close-session; a red check is read, not rerun

Agent Dev no longer commits, pushes or lands: every checkpoint and every landing goes through close-session, whose packet close now also serves a checkpoint of work in progress, and whose commit step carries the branch and staged-diff check that used to live in Agent Dev's commit-and-push-safety reference (removed). Agent Dev gains one rule for a red check: read and classify it (code defect, wrong test, environment) before anything else, question the rule that produced the test before repairing it, and rerun only once for a named environmental cause. Close-session applies the same rule to a red gate at landing, and the test architect's repair route asks whether a test should exist before repairing it. Agent Dev's delivery controls and packet coordination references lose their duplicated Git and close-session text and shrink by about a third.

## 2 November 2026: A preview loop for visible work

Agent Dev gains a preview-loop workflow for many small visible changes the user judges by looking, such as a page-by-page review or polish pass. The app runs once on the user's machine for the whole session, their look is the working check, accepted batches are checkpointed to the story branch, and the pass lands once when the user says it is done. Nothing lands per change and no review session follows a pass the user has watched. Close-session treats a change the user watched as already previewed, and its change report covers watched changes in one line, reporting in full only what the user did not see. A close lists every unfinished item, open question and finding not yet acted on in the owning record, and sends work that belongs outside the unit to the backlog.

## 16 October 2026: Documentation organised around working areas

Documentation guidance now starts from a subject folder containing its related working material, with links to shared authorities. A compact guide replaces the document-type folder catalogue. Project conventions may remain in a separate declared source; context and producing skills no longer assume that every rule lives inside project context. Existing projects adopt changes deliberately, including resolving any inherited legacy defaults.

Document navigation reuses an existing README or index. UI and UX update the owning specification, including a shared one, rather than assuming both belong in the local folder. Templates no longer suggest decision-log companions or emit document-currency metadata. Cleanup resolves the project's actual identifier registry instead of testing one default path.

## 13 October 2026: Carry authorisation through delivery

Agent Dev carries an authorised fix through diagnosis, implementation and verification, including reversible local diagnostics. It asks again only for unresolved consequential choices or actions separately gated by project policy. Preparation, packet checkpoints and context compaction no longer force a new session. Independent review may use an appropriately isolated reviewer in the current session; substantial critical fixes receive fresh independent judgement, while other fixes receive affected rechecks. Unchanged review evidence remains reusable. Close-session returns continuing packet checkpoints to delivery and reserves its final handoff for an actual stop.

## 11 October 2026: Skill-owned maintenance and publication

`upskill` treats a skill and its affected supporting files as one deliverable, including distribution guidance when affected. `close-session` resolves requested previews and scope decisions before publication, then carries the agreed work through commit and push without separate requests for each step. Unrelated edits stay separate.

## 11 October 2026: Model choices across both tools

`choose-model` now gives paired Codex and Claude recommendations regardless of the host tool, with model-specific effort and availability caveats. The refreshed guide maps demanding work to Astra/Opus, everyday work to Sol/Sonnet, and bounded transformations to Luna/Haiku. Budget-excluded models stay outside recommendations and fallbacks.

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
