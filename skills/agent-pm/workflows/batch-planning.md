# Delivery Batch Planning

PM owns batch scope, membership and order in the existing queue or plan. Dev owns implementation and acceptance evidence; `close-session` owns checkpoints and landing. A read-only request returns a view; planning does not authorise implementation.

## Choose the simplest structure

Read current membership and the owning records of plausible members: outcomes, readiness, dependencies and assurance constraints. Preserve priority, deadlines, item IDs and active ownership.

- **A story on its own needs no numbered batch.** Its record already holds its scope and finish condition; give it no batch ID or row. Combine backlog candidates into a story only when they share an outcome and acceptance.
- **Batch independent small items that share set-up:** the same code to load, test set-up and review, so one session and one landing carry them. Unbatched, each costs its own session and landing. Do not invent a story to bundle them, or group unrelated work merely because it is small or in the same area.
- **Part of a story joins a batch only at a real delivery boundary:** Dev confirms that an earlier part must land first or a portion is independently acceptable. Identify exact scope; never clone the whole story into several batches.
- **Packets stay with Dev.** They are implementation steps inside a story. A batch is a checking/landing boundary; a chat is neither. Do not insert every layer into every task.

## Plan the boundary

Check hard prerequisites separately from preferred order. Reject cycles, unknown dependencies and conflicting concurrent ownership. Split urgent or independently due work, incompatible rollback, or combined risk too large to assess. Size by a coherent combined diff, not item count or chat/token capacity.

Preserve each member's build authority and assurance requirements. Unapproved candidates can be proposed together but are not ready to build. Critical work retains its specialist evidence and checks. Ask Dev or the assurance owner only when a technical dependency or check boundary is uncertain; PM does not prescribe commands or waive gates.

Define the finish condition: included scope accepted, outstanding integrated checks and required review passed, no blocking decision. Compare the batch with separate delivery; retain it only when its shared outcome or saved setup/review justifies delayed integration. Ask before changing scope, priority or commitments beyond the user's authority.

## Record once and display

Follow [identifier conventions](../../organise-docs/references/identifier-conventions.md). Use one **Delivery batches** section in the existing queue or plan; no batch document or second tracker. It owns membership and order, linking item owners instead of copying acceptance or status.

| Batch | Outcome | Member IDs and owner links | Order / prerequisite | Finish condition |
| --- | --- | --- | --- | --- |
| BAT3 — Invoice totals | Consistent totals | B14 — Rounding; S2-E4 — Output | After BAT2's currency contract | Both scopes accepted; combined checks/review pass |

This is an illustration, not allocated work. Display `BAT3 · B14 — Rounding` in item lists and handoffs, or put the batch once in a grouped heading. Keep item keys and filenames unchanged. Use `Unbatched` when unassigned. Batch numbers are identities, not priority.

Each item or explicitly bounded portion belongs to at most one current batch. Future portions can be planned separately with exact scope and residual-owner links. On adoption into a story, replace the member link with its authorised owner and preserve lineage. Show `proposed` or `waiting — condition` when needed; derive progress from item evidence rather than maintaining another status ledger.

At delivery start, Dev records the branch and starting revision once in the batch entry or linked execution owner. During work, keep the boundary fixed unless the outcome requires a correction or a scope change is authorised. Retitling/reordering keeps the ID; splitting/replacing gets new IDs and a supersession pointer. Before removing a delivered row, retain its ID and member links in the landing PR or commit; item owners retain acceptance evidence.

## Validate and finish

Check unique IDs, two or more members per batch, one membership owner, no duplicate scope, valid owner links, dependency order, build authority, feasible shared assurance and an explicit finish condition. Return the compact table or changed rows, the grouping reason, unresolved decisions and next ready batch. Do not silently start delivery or assign other sessions. An authorised delivery handoff carries the batch ID, member owners, established branch and finish condition.
