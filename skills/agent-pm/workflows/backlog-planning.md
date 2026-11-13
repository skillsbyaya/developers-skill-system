# Backlog Planning

Maintain one living backlog for uncommitted work. Approved decomposition owns committed scope; the story or change package owns execution and evidence; the project's delivery-status source owns lifecycle. Follow the project's declared ownership when it combines these roles.

## Choose the operation and read only what it needs

Resolve the path from a supplied file, declared documentation conventions, one obvious existing backlog, then root `BACKLOG.md`. An edit may create a missing backlog from [the template](../templates/backlog.md); a read-only request does not. Confirm the first broad rewrite of an unstructured file. Preserve useful items and omit empty sections.

- **Capture:** search IDs, source references, problem, outcome and related terms across the backlog and likely active owners. Read plausible matches and the relevant outcome themes, including alternatives from other areas. Widen the search if terms or ownership are uncertain; a title-only miss is not enough to create a duplicate. Do not reread every item's full detail by default.
- **Groom or prioritise:** assess the whole backlog unless the user bounded the scope. For a large backlog, scan headings and concise candidate lines, then deepen the plausible choices across themes. If a reliable pass is still too large, agree a bounded goal or area.
- **Show next, waiting, deferred or one area:** return a read-only view unless an edit was requested. For next work, follow current delivery status to its owning record and respect approved dependencies and priorities. Started work that can move comes before any unstarted item, whatever their order in the queue; test a recorded wait instead of repeating it. Do not present a candidate as the current task when committed work already owns it.
- **Adopt:** create or locate the authorised planning or delivery owner before removing or narrowing the candidate.

Read other project context only when a durable fact could change classification or priority. Use area context review when sources outside the backlog may conceal material decisions, constraints or dependencies.

## Capture and classify

Before adding an item, distinguish the same work from an alternative, complement or overlap. Attach a new source or finding to the existing owner when it describes the same work; repeated intake must not create another item. Keep distinct candidates separate even when they share an outcome.

Record a concise title, problem or intended outcome, source, and enough scope and evidence to distinguish the work. Keep material uncertainty visible. A captured suggestion or an imported claim of approval does not authorise implementation; preserve the actual decision and the scope it permits.

When governed IDs are in use, follow [identifier conventions](../../organise-docs/references/identifier-conventions.md) and the project area registry. Pair each ID with its title; preserve it across regrouping and title changes. Use the authoritative allocator or approved key set, never an inferred next number. Without one, keep items unkeyed and report the gap only when stable IDs are needed.

An unqualified candidate is available for assessment, not automatically approved to build. Qualify only exceptions that change treatment:

- `(needs shaping — owner or workflow)` for unresolved definition or requirements. An available owner can resolve this work; it is not an external wait.
- `(waiting — blocker; check date or event)` for an external party, event or missing evidence. State what would unlock it. After an unsuccessful scheduled check, retain the blocker and set the next check; reaching a date does not satisfy the dependency.
- `(not now — whose decision and why)` for work the user has deliberately set aside. "Until it is first needed" is not a reason: work known to be needed takes its place in the order, and is built when that place comes up.

Ask a user-owned decision when it can be resolved now rather than parking it as waiting. Route UX, UI or architecture judgement to its specialist, approved decomposition to epics and stories, and authorised implementation to Dev. Keep a deadline, earliest-start date, hard prerequisite, preferred order and priority distinct. Do not hide an actionable decision or overdue blocked commitment in a passive waiting item.

## Keep it in build order

The backlog is the plan for everything not yet started, so its order is the order of work: unless the project declares another owner for sequence, file position is priority. Use a few tiers named for what each protects or unlocks, most important first, in the project's own product language. Inside a tier, list sessions in order: a batch of items that share set-up and checks ([Delivery batch planning](batch-planning.md)), or one item or story on its own. Place every new item in a tier and a session at capture; nothing waits in an unordered pile. Do not group by area, size, team or epic; use identifier suffixes for area routing.

Order by importance: what protects people already relying on the product, then what the next milestone needs, then approved breadth, with work that lowers the cost of every later session taken at a stated rhythm rather than left to the end. Record a prerequisite only for something that cannot be done sooner: an earlier item, a release that must be live, an account, purchase or date, or a choice the user has yet to make. A release date alone, or the first customer who will use the feature, is not a prerequisite.

Keep three exception sections, each only while occupied: **Waiting on something outside the work** for an account, purchase, date or another party's act, naming what ends the wait; **No session of their own** for work done inside whatever next touches the same code, and for an unreproduced failure whose evidence capture is already built; **Unframed candidates** when the outcome is unclear, stating the missing framing question. Started work is not in the backlog: it lives in the project's delivery-status owner, so the two never list the same work.

Use the project's existing ownership convention for active uncommitted work. If it uses `(in progress)` markers, identify the owning session or record and preserve its scope. Non-overlapping work may proceed within project concurrency limits; competing claims require resolution. An active marker does not control where an unrelated candidate is filed, and a marker alone is not a concurrency lock.

When organising selected candidates, distinguish one shared outcome needing a story from independent fixes that can share delivery checks. Route approved shared acceptance to epics and stories; do not invent a story merely to bundle fixes. For numbered delivery groups and the next executable sequence, use [Delivery batch planning](batch-planning.md). The backlog owns batch membership and order. Show assigned batch IDs beside item IDs in requested work lists. Capture alone does not allocate a batch.

## Transfer without losing scope

When work is adopted, keep a concise lineage reference in its new owner. Remove only the adopted scope; retain distinct uncommitted work under its existing identity, linked to the new owner. State which scope and any milestone commitment transferred. For example, authorising a fictional-file shaping exercise does not approve a real-input build or remove its missing-input dependency.

Reconcile affected sources using the PM ownership rules: preserve unique evidence, replace duplicate maintained actions with owner links, and apply settled decisions to obsolete questions. Do not keep active sprint copies, completed history, review logs or a second stored next action in the backlog. Do not create a synthetic story or tracker row for housekeeping.

A recommendation or backlog edit does not itself authorise delivery. Continue into implementation only when the user's authority covers the established scope and material consequences; otherwise finish the planning result and ask the remaining consequential choice.

## Finish

Check touched items and references: one owner per action, no lost residual scope or evidence, stable IDs, valid links, supported qualifiers and no unrelated priority or lifecycle changes. A cross-area recommendation must consider ready alternatives across the backlog, not just the first theme. If nothing is actionable, name the decision, dependency or revisit condition that prevents progress; do not remove qualifiers without evidence.

Report a compact receipt: added, linked, narrowed, removed or unchanged; ID/title and location; next permitted action and any material uncertainty. Include a priority recommendation only when requested. Leave already-correct state untouched.
