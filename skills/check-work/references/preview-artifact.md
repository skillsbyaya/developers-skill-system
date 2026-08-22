# Preview Checklist Artifact

Publish a human-preview checklist as a working document when the person will work through it away from this conversation: it runs past a handful of steps, will be ticked off over one or more sittings, gets revisited after fixes, or needs printing or reading on another device. A short check or single question belongs in the reply — a chat answer is faster to act on than a page.

Build from [`../templates/preview-checklist.html`](../templates/preview-checklist.html). Copy it, replace the content, keep the behaviour. Load `artifact-design` first, but the template already settles layout, palette, type, and print — spend the effort on content and sequencing, not on restyling a solved page. Keep the page sparse, factual, and easy to scan.

## Required parts

| Part | Purpose |
| --- | --- |
| Checklist label | Small text at the top: `Sandbox Checklist`, or the equivalent environment name when it is not a sandbox. |
| Subject | The item under review as the main heading. |
| Environment link | The actual app URL, clickable, directly below the heading. |
| Description | One compact description of what is being checked. If order matters, add `N.B. Work in order` on its own line. |
| Progress | `Counter: 0 / N checked`, a bar, and a clear button. Count only the active checks still required on this revision. |
| Changes | Only when the checklist has been revised: a short factual summary of relevant fixes or removed test data. |
| Precondition callout | Only when most steps are invisible until setup exists. Say so before the person concludes the build is broken. |
| Numbered sections | Setup and checking sections ordered by dependency phase, then grouped by app page. |
| Page links | Each section heading has one or more direct page buttons naming where to do the work, such as `Internal Outlets`. |
| Critical section | The highest-blast-radius concern — money, access, data, privacy — visually set apart, placed late enough that setup is done. |
| Calls to confirm | Decisions taken during the work that are the person's to accept or change. Not pass or fail; excluded from the count. |
| Already established | Short labels for what current non-human evidence established. This stops the person redoing work Claude has done. No explanation, no reassurance. |
| Passed earlier | On a revised checklist only, compact labels for earlier human checks that still apply and are useful to retain. Keep these outside the checklist and its count. |
| Known gaps | Anything logged rather than fixed, so it is not reported back as a bug. |
| If something's wrong | How to report a failure, and what is still cheap to change versus already shared with the live system. |
| Footer | Date, scope, and the next decision after the checklist passes. |

Drop a part when it has nothing true to say. Do not invent changes, a precondition, a gap, or a critical section to fill the shape.

## Content rules

- Use short, operational copy. State facts and actions; remove scene-setting, reassurance, politeness, narration, and repeated context.
- Keep the description to the release or decision being checked and a compact list of the affected areas. For example: `Checks before OC5 goes live. Outlets, operating parity, day-first ordering, product availability, order sheets, backup fix.`
- When order matters, use the separate line `N.B. Work in order`; do not bury it in conversational guidance.
- Name a revision section `Changes`, not `What changed since you started`. Include only facts that affect the current check. For example: `Section 1 problems were found and fixed. The stranded test order (Counter, Tue 28 July) has been deleted.` Omit the discovery story, reassurance, retained good data, and reset history unless the person must act on them.
- Treat a revised checklist as the current worklist, not a cumulative test record. Reconcile every previous item against the reported result and the new candidate: keep observed problems after their fix, not-run or unclear items, and earlier passes invalidated by the change; remove still-valid passes from the numbered checklist.
- Reset only a retained item whose earlier result no longer establishes the current candidate. Mark its checkbox with a new `data-recheck` token for this invalidating revision. Do not clear unrelated ticks or require a full restart.
- Put still-valid human passes in `Passed earlier` only when the summary helps orientation or traceability. Use compact section or outcome labels, not the old detailed step text. Omit the panel when the history adds no value.
- Never mix already-completed detailed steps among the active checks. The progress counter and numbered route must show only what the person still needs to do now.
- Keep a checklist item only when its result could change acceptance and Claude cannot establish it. Remove routine checks, duplicates, and items included only to make the coverage look complete.
- Give a section one short line saying why it matters only when the heading and checks do not already make that clear. Omit it otherwise.
- Write each step as the action and the observation that proves it: what to open, what to do, what should be true afterwards. Never "test X".
- Use a subordinate note only for information needed to complete the check correctly. Do not add commentary merely because it may be interesting.
- Order by dependency phase first and page second. Start with one setup section, then group all checks of the resulting state by page. Add another setup section only when later checks need a changed state, such as deleting one order, then group those verification checks by page.
- Finish every relevant check on a page before moving to another. Revisit a page only when a later setup action creates a new state to observe. If the same page appears in non-adjacent sections without such a dependency, regroup the sections.
- Keep the existing section title as the heading and add direct page links beside it, for example `Outlets exist and operate` followed by an `Internal Outlets` button. Use multiple page buttons only when the section must span those pages; split the section when that would make the route clearer.
- Say when a single shared value — one date, one customer, one week — makes the checks across pages line up.
- Keep the active route to what a person must still observe. Anything Claude established from the environment, artifacts, tests, or logs goes in the already-established panel as a label, not in the list. Earlier human observations belong in `Passed earlier`, not in the evidence panel.
- Name what is reversible only when that changes how the person should perform or report the check.

## Behaviour to preserve

- Ticks persist in `localStorage`, keyed by a hash of the step text — so inserting, removing, or reordering steps does not scramble unrelated ticks. Give `KEY` a slug unique to this checklist, or two published checklists can share one set of ticks.
- To invalidate one retained step after a fix without changing its wording, use the current template behaviour and add a new revision token to its input, for example `data-recheck="revision-2"`. The template ignores that step's older stored tick, then persists the new pass under the token. Change the token again only if a later change invalidates the result again. When revising an artifact created from an older template, refresh its checklist script from the current template before using a token.
- Items marked `data-opt` are excluded from the required count. Decisions to confirm are not outstanding work.
- Print hides progress and the clear button, and avoids breaking a section across pages.

## Revising after fixes

Reconcile the old results before republishing:

1. Inspect the previous checklist state, the reported results, the fixes, and the running revision.
2. Keep only items that are unresolved, not run, unclear, or invalidated by the fixes. Remove still-valid passes from the active sections and counter.
3. Give each invalidated retained checkbox a new `data-recheck` token so that item alone returns to unchecked. Preserve unrelated ticks.
4. If useful, summarise still-valid human passes in the compact `Passed earlier` panel at the bottom; do not copy their detailed steps there.
5. Republish to the same URL: same file path, and pass the original artifact `url` when this conversation did not create it.

Say in the reply what changed, what remains active, and which steps need rechecking; do not silently reset the page.
