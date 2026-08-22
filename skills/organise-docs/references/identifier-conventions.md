# Shared Identifier Convention

Use this reference only when creating, changing, locating, or reconciling durable identified items or the project area vocabulary. Resolve it through [the project-first convention rules](convention-resolution.md): a targeted project override supersedes the matching rule here, while unmentioned rules remain the global default. `organise-docs` owns this convention; `personalise-working-system` may update it after confirming a global change; domain skills own the meaning and lifecycle of their item types.

## Grammar

New identifiers use a typed base identity followed by optional area-routing suffixes:

```text
<base-id>[.<PrimaryArea>[.<SecondaryArea>[.<SecondaryArea>]]]
```

- Simple base IDs contain no dash: `B14`, `FR7`, `A13`, `RK4`, `E4`.
- A story inside an epic is `S<story>-E<epic>`, for example `S2-E4`. Its story number is local to that epic. A genuinely standalone story may use `S3`.
- A dot has one meaning only: everything after the first dot is area routing, for example `B14.Invoicing`, `A13.Invoicing.Delivery`, or `S2-E4.Customers`.
- The base ID is the stable identity. Adding, removing, or correcting an area suffix does not create a new item.
- When a document convention includes an ID in a filename, use the stable base ID unless that convention explicitly says otherwise; keep mutable area routing in the document's canonical heading and current cross-references.
- In user-facing conversation, pair the ID with its title. Do not refer to work as only `S2-E4` or `A13` when a person could lose the thread.

Numbers are positive integers without decorative zero-padding. This convention does **not** define how the next number is allocated. Use a project-owned allocator or an already authoritative key set. If neither exists, retain the title or existing legacy key and report the allocation gap; do not infer `max + 1`, invent a counter, or create a `next` field.

## Prefixes and writers

| Prefix | Meaning | Structural writer |
| --- | --- | --- |
| `B` | Backlog item | `agent-pm` backlog planning |
| `FR` | Functional requirement | `agent-pm` PRD |
| `E` | Epic | `agent-pm` epics and stories |
| `S` | Story | `agent-pm` epics and stories; delivery owners preserve it |
| `A` | Architecture decision | `agent-architect` architecture decisions |
| `D` | Project-defined or legacy general decision | No default writer; preserve only unless the project explicitly assigns one decision-record owner |
| `RV` | Durable generic review finding, only where a current review artifact needs stable finding identity | `check-work` |
| `OB` | Compliance obligation | `agent-compliance` obligations register |
| `RK` | Compliance or assurance risk | `agent-compliance` obligations register |
| `CT` | Compliance control | `agent-compliance` obligations register |
| `EV` | Compliance evidence item | `agent-compliance` obligations register |

Do not introduce a new prefix merely to label prose. Add a type only when items recur, survive title/order edits, need cross-document references, and have one clear structural writer and lifecycle owner. Update this table and affected consumers together through `upskill`.

## Canonical project areas

The project-local registry is `reference/identifier-areas.yaml`. It holds vocabulary, not item metadata:

```yaml
version: 1
areas:
  - name: Invoicing
    description: Customer charging, invoices, credits, and payment allocation.
  - name: Delivery
    description: Fulfilment, dispatch, tracking, and proof of delivery.
    aliases:
      - Fulfilment
```

- Use the smallest durable set of main product or system areas. Area names are full, readable UpperCamelCase labels such as `Invoicing` or `OrderManagement`, not short codes.
- Give an item one primary area and at most two secondary main areas. Put the primary area first; sort any secondary areas by canonical name.
- Add an area only when no current canonical area fits truthfully and periodic review of the new area would be useful. A writing skill may update the registry when the taxonomy changes, not for every new item.
- An alias maps a genuine alternate user term or former name to one canonical area. Omit aliases until real usage or a rename earns them. Aliases never appear in IDs and are not legacy-ID mappings.
- Do not store IDs, counters, status, priority, owners, relationships, or a `next` value in this registry.

When no registry exists, do not improvise competing spellings. For substantial project setup, `manage-project-context` may bootstrap the smallest evidence-backed registry near the end of establishment or rebaseline. For a bounded writer, create it only when the request authorises the needed project documentation and durable area routing will recur; otherwise use an existing title/ID and report the missing vocabulary owner.

## Writer behaviour

1. Preserve an existing base identity and any progressed or externally referenced legacy identity.
2. Resolve intended areas against `reference/identifier-areas.yaml`, including aliases.
3. Add only areas for which a periodic area review should reasonably triage the item. Do not use suffixes as exhaustive tags.
4. If none fits, define one clear reusable area in the registry instead of forcing a misleading match. Change the registry only once for that taxonomy change.
5. Keep the canonical ID with the item heading or structured row. Use the same complete canonical form in current cross-references.

## Reader and area-review behaviour

For an area-scoped read:

1. Read the small project area registry first and resolve an alias to its canonical name.
2. Search current authoritative sources for the exact dotted segment, for example `.Invoicing`, matching it as a complete segment whether primary or secondary. A practical first pass is `rg -n '\.Invoicing([.]|[^[:alnum:]_]|$)'` over current documentation paths.
3. Treat matches as routing candidates, not proof of relevance or authority. Group them by type and source, read the matched sections first, filter out stale lifecycle entries, and follow explicit relationships.
4. Exclude archive folders, superseded whole documents, generated output, and history by default. When adoption is partial or a material omission is plausible, run a bounded secondary search for the canonical area name and declared aliases in current headings, filenames, and likely authoritative sources. Treat un-suffixed matches as migration or discoverability candidates, not automatically relevant items.
5. Broaden beyond the exact area when dependencies, cross-cutting risks, or conflicts make it necessary.
6. For money movement, authentication, authorisation, security, destructive behaviour, privacy, safety, or compliance, use the match only to find the source; read the fuller relevant authoritative material before deciding or acting.

This search model deliberately pays a small triage cost during occasional area reviews instead of a write and token tax for a project-wide per-item index.

## Legacy and lifecycle

- Preserve progressed, heavily referenced, or externally meaningful legacy IDs. Do not re-key history for cosmetic consistency.
- Add canonical area suffixes to a current legacy item when useful, for example `CW6.2.Customers` or `F85.Customers.Orders`; the legacy base remains its identity.
- Leave archived and completed historical records untouched. New adopted work may record a concise lineage link to the legacy source.
- When a decision is superseded, preserve its ID and point to the replacement. Never recycle a retired number.
- A cleanup sweep may remove an area only when no current ID uses it, no current document declares it, no alias or current product language needs it, and no active near-term work needs it. Archives remain unchanged.
