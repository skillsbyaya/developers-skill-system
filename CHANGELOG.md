# Change log

This file records material changes to the integrated system. Because the skills are interconnected, update notes describe system-level behaviour rather than isolated skill releases.

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
