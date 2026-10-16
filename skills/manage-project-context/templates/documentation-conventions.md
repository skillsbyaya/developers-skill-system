# Documentation Conventions

Use when establishing or changing project conventions, or changing global preferences through `personalise-working-system`. Routine readers and writers use the project's declared convention source.

## Start from the working area

Organise around the subjects people work on: a module, service, business function, or other coherent area. Keep the area's current requirements, research, decisions, design, and active work together so that pointing an agent at its folder gives it a useful starting context. Choose boundaries from the actual work; preserve an established structure when changing it would bring little benefit.

Each fact has one owning document. Update that authority; link to shared material from the area that needs it. Shared architecture, design systems, or company policies need not be copied into every area. Respect repository and access boundaries when linking them.

Keep the current working set distinct from retained history. Follow the project's lifecycle for completed work and superseded material. A short README can explain scope, current authorities, and shared dependencies when the folder alone is not clear; do not require an index or a standard set of documents in every folder.

## Record only what future work needs

Follow project instructions to the existing convention source. Keep it in place. With no established source, use a short section in project context, or a linked document if the detail would burden routine reading.

Record the working areas, shared authorities, and recurring naming or lifecycle choices that would otherwise be ambiguous. A compact table is enough; omit columns that add nothing:

| Area or subject | Home and owning documents | Shared dependencies |
| --- | --- | --- |
| Ordering | `ordering/`: brief, requirements, research, active stories | Shared architecture and visual system |
| Shared visual system | `platform/ux/DESIGN.md` | Canonical token source |

These are examples, not folders or artifacts to create. Add concrete naming examples where needed, such as `ordering/prd_ordering.md`. Preserve declared artifact-type keys such as `prd` or `ux` when workflows use them for lookup; a new document type does not require a new catalogue row.

## Starting choices where the project has none

- Keep always-read control files at the root. Place other documents with their working area; give shared material one declared home.
- Use readable, stable filenames. For new recurring types, `[type]_[area]_[specifics].md` remains a useful pattern; omit fields that add no distinction. Preserve conventional fixed names and stable identifiers.
- Use Markdown for ordinary working documents and the format the artifact needs otherwise, including code as the authority for executable design tokens.
- Put current decisions in the document that owns the subject. Create a companion only when it has a distinct purpose, such as a visual preview or derived context; keep it beside its parent.
- Preserve existing compound artifacts and workflow-owned file contracts, such as distillate packages. UX and UI normally use `EXPERIENCE.md` and `DESIGN.md`; their owners may have different scopes and locations.

## Adopt changes deliberately

Apply explicit user decisions and project rules before these starting choices. A template update does not move existing files or replace adopted conventions. For a legacy record that inherits unspecified global defaults, resolve the affected rules during adoption and write the choices the project still needs into its own source.

When changing an existing organisation, state whether the change governs new work only or a specified existing set. `organise-docs` owns moves and reference repairs. Keep one convention authority; consolidation is needed only when sources compete, not merely because the rules live outside project context.
