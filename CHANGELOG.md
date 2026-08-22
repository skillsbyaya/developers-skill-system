# Change log

This file records material changes to the integrated system. Because the skills are interconnected, update notes describe system-level behaviour rather than isolated skill releases.

## 22 August 2026: Token-efficiency update

Claude's token limits for five-hour usage windows were reduced by 50%. The existing delivery workflows could then require several restarts to complete a change.

The skill system was audited and adjusted to reduce token use:

- Product-management work now groups delivery into smaller, implementation-shaped packets instead of batches organised around human checkpoints.
- Development work now completes one packet per session rather than attempting several packets in the same session.
- Documentation practices were tightened to reduce unnecessary context loading and repeated material.

This update was completed before the repository was created and is recorded here as the first public update note.
