# Backlog Planning

Create and maintain one living backlog for work that is not yet owned by approved decomposition, an active story or change package, or delivery status. This workflow owns uncommitted items and any priority decisions made about them; it does not own committed scope, delivery lifecycle, or completed history.

## Choose the smallest operation

| Request | Action |
| --- | --- |
| Create or repair the backlog | Read [the backlog template](../templates/backlog.md), preserve useful existing items, and restore the smallest valid structure. Confirm before the first broad rewrite of an unstructured file. |
| Capture one or more items | Compare each new item with the existing backlog, then file it beside candidates pursuing the same outcome or addressing the same problem without reordering unrelated items. |
| Groom, sequence, or prioritise | Sweep the whole backlog unless the user bounded the scope, remove stale duplicates, and make the requested review or priority judgement across areas. |
| Show what is next, waiting, deferred, or in one area | Return a read-only view unless the user also asked to edit. Assess the whole backlog when answering a cross-area priority question. |
| Adopt work into planning or delivery | Remove the backlog item only after the new owner exists, or narrow it to distinct uncommitted work that remains. |

Resolve the path from a supplied file, current document conventions, one obvious existing backlog, then root `BACKLOG.md`. Read project context only when a durable project fact could change classification or priority. For a broad grooming pass over a large backlog, ask for a goal, area, or bounded scope only when one pass would otherwise be unreliable.

For next-work, grooming, or adoption, inspect delivery status only when committed work may already own an item. Follow an active row to its story or change package rather than treating the status table as sufficient task context.

If an edit request needs a backlog and none exists, create it from the template as part of that operation. A read-only view does not create a file unless the user also asked to establish one. Treat the template as a source of the title, filing note, outcome-or-problem pattern, and two exceptional sections, not an empty skeleton: infer themes from the actual product and work, retain only occupied sections, and remove an empty theme or exception section together with its guidance note.

## Preserve one source of truth

- The backlog owns candidates, unresolved follow-ups, recorded priority decisions, waiting items, and deliberately deferred ideas.
- Approved epics and stories own committed scope and stable keys. A story or change package owns active execution when one exists. Delivery status owns lifecycle state.
- Never keep an active sprint copy, completed archive, review log, or second stored `Next` field in the backlog.
- Do not store or infer a total cross-theme priority order from headings or file position alone. When asked what should come next, review the ready candidates across the whole backlog against the current product priorities and explain the recommendation.
- If committed delivery is already active, report or resume that owner instead of presenting a backlog item as the current task.

When another owner adopts an item, remove the duplicate. Keep a narrowed backlog line only when it describes separate uncommitted work, and state that distinction plainly. Never create a synthetic story or tracker row for backlog housekeeping.

A backlog view, prioritisation recommendation, or grooming pass may identify a later implementation target, but it does not authorise delivery whose exact scope, mechanism, risk, or rollback became knowable only after inspection. Finish the backlog result and obtain fresh user authority before handing that work to `agent-dev`, unless the exact delivery change and its material consequences were already established and authorised.

## Keep the backlog reviewable

Use outcomes sought or problems addressed as the primary filing structure. A heading answers why the work may be worth doing, not where it touches the product or system. Derive each occupied theme from the project's purpose, current product language, evidence, and backlog candidates; do not start from a universal set. Candidates may share a theme across routed areas when comparing them together helps choose, combine, reject, or shape the work. Capture enough outcome, reason, and boundary that a later session can compare and assess the item without rediscovery.

When the project has an authoritative identifier allocator or key set, resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry. Use stable backlog IDs such as `B14.Invoicing`, preserve them across title and position changes, and pair each ID with its title. The suffix provides cross-artifact area routing; the backlog heading provides outcome or problem context and therefore need not match it. If no governed allocation exists, do not add arbitrary numbers or infer the next one; retain unkeyed backlog items and report the allocation gap when stable IDs are needed. Never renumber existing items merely for tidiness.

Miles owns the section judgement. Add, rename, merge, split, omit, or reorder outcome or problem themes when current evidence and accumulated candidates reveal a distinction that materially improves comparison and shaping. Prefer the smallest useful set that remains easy to scan, and preserve an established theme while it still expresses the current reason for considering the work. Do not use functional areas, organisational teams, solutions, epics, or delivery packages as substitutes for an outcome. Split candidates from the same area when they pursue materially different outcomes; group candidates from different areas when they are credible alternatives or complements for the same outcome.

Within a substantial theme, Miles may add one level of sub-headings when alternatives, sub-problems, or another recurring review cluster materially improve comparison and shaping. Derive their names from the work, keep only occupied and useful clusters, and preserve a sub-heading while it remains meaningful. Do not add one solely to isolate an item. Never use headings or sub-headings for area, readiness, priority, size, complexity, risk, teams, epics, delivery chunks, or lifecycle stages. Use those facts as review lenses or concise item context only when they change treatment. Keep a small theme flat when adjacency is sufficient; do not nest below this one optional level.

Place each new discretionary item beside candidates pursuing the same outcome or addressing the same problem after checking for duplicates, overlap, dependencies, alternatives, complements, and useful contrasts across the whole backlog. Preserve distinct candidates as distinct items even when they are adjacent. Put externally forced work in **Obligations and triggered work** only when the item names its obligation, deadline, commitment, or observable trigger. Put an item in **Unframed candidates** only when honest outcome or problem placement is not yet possible, and state the question or missing evidence that would frame it. An unqualified item is ready to pursue. Add a concise qualifier only when it changes treatment: `(needs shaping — <owner or workflow>)`, `(waiting — <named blocker>)`, or `(not now — <reason or revisit trigger>)`. Keep qualifiers current, but do not turn readiness into the filing structure.

Allow at most one `(in progress)` marker, and only while the backlog item itself remains the active uncommitted owner. If several markers exist and current ownership is not proven, ask which item remains active before changing them. Do not disturb the current marker or move a newly captured item above it without an explicit priority change. Remove or move the marker before another item becomes active. Completed or adopted items leave the file.

Outcome themes, exception sections, optional sub-headings, identifier suffixes, and item adjacency are review aids, not proposed epics, delivery chunks, or ownership boundaries. Do not merge distinct items merely because they pursue one outcome or may be delivered together. When shaping or adopting committed work, use identifier routing and the area context review when relevant sources outside the backlog could hide material decisions, constraints, dependencies, or risks; otherwise sweep the relevant outcome theme, explicit dependencies, and useful contrasts directly. Select any coherent set of items the epic, story set, or change package needs; backlog items do not need to be contiguous or pre-grouped. Remove or narrow each selected item only after that new owner exists and preserve a concise lineage reference where it prevents ambiguity.

Mark work that still needs material product definition or requirements judgement as `(needs shaping)` and name the responsible owner or workflow. Use `(waiting)` only for a named external blocker; uncertainty that Miles or another available owner can resolve is shaping work, not waiting. Route formal UX, UI/design-system, or architecture work to its specialist owner, approved decomposition to epics and stories, and clear implementation to `agent-dev`; do not copy committed delivery into the backlog. Use `manage-project-context` only for establishing or comprehensively rebaselining project-wide context.

If all remaining work is non-actionable, review whether any item is now genuinely ready. Change no qualifier without evidence or an explicit priority choice; otherwise report what decision, dependency, or prioritisation is required.

## Validate and finish

Check that:

- there is one backlog and no inbox, pinned next field, completed archive, or active-delivery duplicate;
- every discretionary item sits under a meaningful outcome or problem theme, exceptional items meet the stated obligation/trigger or unframed criteria, any sub-heading improves comparison or shaping, and each item has a useful action boundary;
- at most one backlog-owned item is in progress;
- waiting items name their blocker;
- shaping items name the responsible owner or workflow; and
- any cross-area priority recommendation considers the whole ready backlog and does not compete with a committed active owner.

Report the path, operation, themes or exception sections changed, any adopted item removed or narrowed, any requested priority recommendation, and the current committed owner when one exists.

If the requested edit would not change correct backlog state, leave the file untouched and report the no-op.
