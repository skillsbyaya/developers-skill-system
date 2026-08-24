# Evidence Disposition

Classify and carry forward evidence that already exists. This is a light bookkeeping route, not a fresh review, readiness gate, environment inspection, or request for a person to run checks.

## Resolve the evidence

Use the supplied check, result, packet note, limitation, or clear current record. Inspect only the owning entry and enough surrounding context to establish its scope, revision, source, and dependency. Do not search decision registers, reread planning artifacts, rerun commands, inspect the whole change, or invoke another assurance route merely to classify it.

Classify each item as one of:

- **Current evidence** — performed evidence still matches the relevant scope and revision.
- **Pending observation** — a specific unperformed observation that could still affect acceptance.
- **Known limitation** — unavailable or deliberately omitted evidence whose consequence is understood.
- **Failed evidence** — a performed check exposed a defect or unresolved finding.
- **Invalidated evidence** — a later change affected the checked surface, dependency, environment, or oracle.
- **Proposed check** — an idea for possible assurance, not evidence and not yet required work.

When the source does not establish what was run, where, or against which revision, do not promote it to current evidence. Preserve the uncertainty instead of reconstructing a review.

## Accumulate rather than reassess

This route does not gain record-writing authority. When the current task already owns a story, package, or packet record, keep one compact entry there: item, status, scope, revision or packet, result or limitation, and the condition that would invalidate it. Update the existing entry instead of producing a second assessment record; otherwise return the record-ready disposition to its owner.

Evidence from an earlier packet remains usable unless later work changed the surface, contract, dependency, environment, or acceptance oracle it established. A new packet does not by itself invalidate earlier evidence. At story completion, consume the accumulated entries once, reuse current scope-matched results, and run only the integrated or delta checks needed for the complete story.

Recording a pending manual observation does not trigger human preview. Preserve what must be observed, why existing evidence cannot establish it, and when it could affect acceptance. Select human preview only when an assurance or completion decision is now being made, the observation remains material on the current candidate, and a relevant environment is available.

## Finish

Return the disposition and the smallest next action, if any. Do not emit a findings report, score, readiness verdict, checklist, or lifecycle decision. Escalate to another route only when the user requested that decision or the evidence exposes a consequential unresolved question that cannot responsibly remain a recorded limitation.
