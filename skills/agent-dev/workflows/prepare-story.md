# Prepare Story

Produce an implementation-ready story from an approved epic or backlog story, reconciled against the current code, so a delivery session can build it without guessing. This is the engineering-ready record — reuse points, change surface, packets, verification — not the product story that `agent-pm`'s epics-and-stories owns. Start from that approved product story; do not re-decide its scope or acceptance.

## Select this as its own boundary when

The change is reconciliation-heavy (the approved spec may be stale against today's code), introduces a new UX/UI pattern or a new shared primitive, or spans several slices or sessions. A bounded, single-surface change needs no separate prep step — adopt the record and go straight to a delivery workflow.

## Prepare, then stop at the boundary

Follow [Story preparation](../references/story-preparation.md) for the procedure — including resolving the genuine design decisions during prep, via `agent-ux-designer` and `agent-ui-designer`, rather than deferring a new pattern or primitive to a build-time try-it-on-the-sandbox.

Finish at a durable `ready-for-dev` story with a precise next boundary, before any code. For a small story you may continue to a delivery workflow in the same session — but only once the ready story is written, so the durable record exists before the code does; heavier work continues in a separate session. Do not fold preparing and building into one continuous pass.
