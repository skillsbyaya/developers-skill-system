# Technical Context

Read this reference only for the Technical Context mode or a technical pass inside Establish or Rebaseline.

## Evidence scope

Inspect only evidence needed for the project-wide question: manifests and lockfiles, root configuration, entry points, representative source and tests, authoritative architecture or development documents, and explicit user constraints.

Record a technical fact only when it is:

- supported by representative evidence or an explicit decision;
- durable enough to affect future work repeatedly;
- actionable as a convention, constraint, verification expectation, hazard, or orientation point; and
- not already better owned by a specialist document.

One occurrence is an example, not necessarily a convention. Preserve exact versions only when compatibility depends on them. Do not infer branch, release, security, performance, or test policy from absence.

## Update

Use or add only the affected headings:

- `## Codebase orientation`
- `## Stack and runtime`
- `## Conventions and patterns`
- `## Testing and verification`
- `## Technical hazards and unknowns`

Prefer the smallest evidence-grounded statement that changes future behaviour. Remove stale facts disproved by current evidence. Preserve unrelated sections and useful custom headings.

Do not add dependency inventories, file catalogues, temporary implementation status, review findings, a change log, maintenance instructions, or a copied summary of an architecture or code-area reference.

## Check

Verify every changed statement against its source, distinguish uncertainty plainly, resolve or expose contradictions, leave unrelated content unchanged, and return the changed sections, evidence paths, and material unknowns to the parent mode.
