# Change log

This file records material changes to the integrated system. Because the skills are interconnected, update notes describe system-level behaviour rather than isolated skill releases.

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
