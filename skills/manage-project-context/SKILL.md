---
name: manage-project-context
description: "Creates, comprehensively rebaselines, or audits a project's durable context snapshot. Use when project-context is missing, an existing repository is being adopted, a major change alters purpose, users, scope, direction, or structure, or project-wide technical conventions and hazards need evidence-based reassessment."
---

# Manage Project Context

Own the structure and full lifecycle of the project's small durable context snapshot. Other owners may make bounded updates only to almost-always-needed facts they directly establish.

## Select one mode

| Need | Action |
| --- | --- |
| Context is absent, a project is starting, or an existing repository is being adopted | Establish the snapshot. |
| An approved major change alters project-wide purpose, users, scope, direction, or structure | Rebaseline the affected framing while preserving still-valid facts. |
| Stack, runtime, conventions, testing expectations, constraints, or hazards need project-wide reassessment | Read [Technical context](references/technical-context.md) and update only those sections. |

Routine task status, backlog changes, review findings, and one newly discovered fact do not require this skill. The discovering owner may update that fact in place when it is durable, almost always useful, and within its evidence.

Resolve the registered `project-context` and `delivery-status` document types from the current document conventions when available. Otherwise use one obvious existing context file or root `project-context.md`, and preserve an existing delivery-status path. Do not create a second context source.

## Content boundary

Keep only information that a future session will need almost every time it works in this project:

- what the project is, who it serves, and its durable current lifecycle state;
- accepted product, technical, operational, or compliance decisions that broadly constrain work;
- concise codebase orientation, stack, conventions, verification expectations, and material hazards;
- standing constraints, dependencies, and unresolved project-wide risks; and
- one stable pointer to the authoritative delivery-status document when one exists.

Exclude backlog content, task or story lifecycle, copied priority, a copied next action, review logs, session recaps, completed history, dependency inventories, and short summaries of records that already have a clear retrieval path. Project directives that must govern every conversation belong in project `CLAUDE.md`, not here.

Clear requests should route directly to their owner without loading project context. Use the delivery-status pointer only to orient an unclear or resumed request; follow it to the current work record rather than copying its current row into this file. Do not duplicate document-placement or identifier-convention overrides here; those belong in `reference/project-conventions.md` and are resolved directly by their consumers.

Context work may expose unresolved backlog, identifier-area, or stale-document work owned elsewhere. By default, report those as follow-ups with the appropriate owner; do not start them inside the snapshot task. Continue into an adjacent workflow only when the user explicitly requested comprehensive project setup that includes it or asks to take the reported follow-up.

## Establish

1. Inspect the smallest authoritative evidence set: repository manifests and root configuration, likely entry points, representative source and tests, current project documents, and explicit user decisions.
2. Separate verified facts, user decisions, inference, and unresolved uncertainty. Ask only for facts that would materially change the durable snapshot.
3. Surface material contradictions before writing.
4. Create the smallest useful structure below, omitting empty headings.
5. If technical evidence is substantial, read [Technical context](references/technical-context.md) for that bounded pass.
6. Report unresolved work that belongs in backlog planning as a follow-up to `agent-pm`; do not create or order backlog state here.
7. When durable IDs or periodic cross-artifact area retrieval would materially help, report a missing or stale identifier-area registry as a follow-up to `organise-docs`. If comprehensive project setup explicitly includes that registry, resolve the conventions and create it through the document owner rather than treating it as part of the context snapshot.

## Rebaseline

1. Start from the approved change and any explicit stale-concepts list. If the change is not yet approved, return the decision to the product or course-correction owner.
2. Rewrite only the project-wide framing that the decision invalidates.
3. Preserve every still-accurate specialist fact and useful custom section.
4. Remove stale summaries rather than appending a change history.
5. Reassess technical sections only when the change affects them.
6. Report newly uncommitted work as a follow-up to `agent-pm` backlog planning and any explicit stale-document list as a follow-up to `organise-docs`; do not start either workflow unless the user asks.
7. If the approved rebaseline materially changes the project's durable area vocabulary, report the exact taxonomy delta to `organise-docs`. Update or create the registry only when the user's requested scope explicitly includes that work; never silently rename current identifier suffixes.

## Suggested structure

Use the smallest useful subset:

```markdown
# {Project name}

**Lifecycle:** {concept / early build / active / mature / paused}
**Last reviewed:** {date}

## What it is
## Problem and users
## Durable current state
## Key decisions and constraints
## Codebase orientation
## Stack and runtime
## Conventions and patterns
## Testing and verification
## Technical hazards and unknowns
## Delivery orientation
**Delivery status:** {stable path or link}
## Project-wide risks
```

The lifecycle and durable current state describe the project, not the current task. Omit `Delivery orientation` when no durable delivery-status document exists.

## Finish

Verify that every retained fact is current, durable, actionable, correctly placed, and supported by evidence or an approved decision; unrelated specialist content remains intact; the delivery pointer resolves; no placeholder or competing work state remains; and the file contains no copied next action, backlog, task lifecycle, review log, or history.

Report the mode, sections changed, supporting evidence for material updates, unresolved project-wide unknowns, and any follow-ups for a state or document owner. Include adjacent work completed only when it was explicitly in scope.
