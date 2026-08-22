# Convention Resolution

Use this reference only when a task needs document placement, document naming, durable identifier rules, or a change to those conventions.

## Resolve the current rule

Apply sources in this order:

1. An explicit current user requirement or binding project instruction, provided it is in scope and authorised.
2. The optional project overlay at `reference/project-conventions.md`.
3. The global [document conventions](../doc-conventions.csv) and [identifier convention](identifier-conventions.md).

Check for the project overlay first. If it exists, read only the relevant table before consulting the global source for rules it does not address. If it is absent, use the global source directly. Never copy the global sources into a project merely to make inheritance visible.

For a document type, a matching project row supplies the complete `folder` and `naming-pattern` for that type. Global note rules still apply unless the project overlay names and replaces the specific note key. A project may add a local document type that has no global row.

For an identifier rule, a project row identifies the global section and the exact rule or prefix it replaces. Only that targeted rule changes; all other grammar, writer, area, reader, and lifecycle rules inherit globally. A project-only addition must name its scope and owner explicitly.

Treat a one-off instruction as situational unless the user confirms it should persist. Create the overlay on the first confirmed durable project divergence. Keep it delta-only, record why each difference exists, and remove an override when the project returns to the global default.

## Change authority

`organise-docs` owns the convention model and both global sources. `personalise-working-system` may create or update the global sources and project overlay after judging and confirming the correct scope. Other consumers read the resolved convention and preserve it; they do not silently turn a local need into a new convention.

Changing skill selection, instructions, workflow, or ownership is not a convention-source edit. Route that work to `upskill`. `personalise-working-system` must never modify a `SKILL.md`.
