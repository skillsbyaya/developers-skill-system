# Prepare Story

Produce an implementation-ready story from an approved epic or backlog story, reconciled against the current code, so a delivery session can build it without guessing. This is the engineering-ready record — reuse points, change surface, packets, verification — not the product story that `agent-pm`'s epics-and-stories owns. Start from that approved product story; do not re-decide its scope or acceptance.

## Select this as its own boundary when

The change is reconciliation-heavy (the approved spec may be stale against today's code), introduces a new UX/UI pattern or a new shared primitive, or spans several slices or sessions. A bounded, single-surface change needs no separate prep step — adopt the record and go straight to a delivery workflow.

## Prepare before implementation

Follow [Story preparation](../references/story-preparation.md) for the procedure — including resolving the genuine design decisions during prep, via `agent-ux-designer` and `agent-ui-designer`, rather than deferring a new pattern or primitive to a build-time try-it-on-the-sandbox.

Write the `ready-for-dev` story before code. A preparation-only request ends there, closed through `close-session` under the rule in `SKILL.md` → Boundaries. When implementation is authorised, continue into delivery once blocking decisions and dependencies are resolved, by reading the direct or staged workflow before the first edit; delivery ends in `close-session`, which merges and writes the handoff, so never end the session by asking whether to close. Story size alone does not require a new session.

## Report the prepared story

Tell the user what the story will do, in this shape and nothing more:

- One line naming the record and that it is ready to build.
- One bullet per decision: **D<n>, <a few-word name>.** Then one or two plain sentences on what the story will do and why, in the user's terms. Say "(you decided this)" on the ones the user decided. Skip decisions that only settle engineering detail.
- One bullet per correction made to another document, saying what was wrong and what it says now.
- One line on the build stages, named in plain words.

Leave out how the decisions were reached, function and file names, checks and process. This report is the change report `close-session` posts for the preparation; it does not repeat it.

