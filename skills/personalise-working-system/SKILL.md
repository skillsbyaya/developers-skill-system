---
name: personalise-working-system
description: "Reviews and changes durable personal conventions across global and project sources. Use when the user wants concrete choices about current defaults, a cross-project convention change, a project-specific override, or migration after a personal convention changes."
---

# Personalise Working System

Help the user change durable working conventions without creating a competing preference store. Start from the current system and a real recurring need, not a generic productivity questionnaire.

Do not ask for one universal speed, model, token, quality, or ceremony level. Those choices normally depend on the task. Personalise only a durable preference the user genuinely wants future work to follow.

## Inspect the current default

Begin with the user's stated concern. When they name an area, inspect only that area and the sources needed to resolve it.

On a bare invocation or broad personalisation request, start with the design of the global document and identifier conventions. Read the registered global sources and distil their key consequential choices, such as placement model, naming grammar, fixed names, numbering, sidecars, format defaults, identifier grammar, area routing, allocation, and legacy handling. Present the first small coherent group with the current convention, what it solves, credible alternatives, practical trade-offs, and a recommendation. This is a convention-design conversation, not a review of whether the current project's documents comply.

Do not inspect, inventory, compare, rename, move, or migrate the current project's documents during this opening review. Do not read `reference/project-conventions.md` or use project examples merely to explain the global defaults. After the user confirms or changes a convention, decide its intended reach: update the global source when it should become the normal default for future projects; consider a project overlay only when the user identifies a genuinely local need or a project constraint could materially change the decision. Inspect only the relevant project constraint or existing overlay at that point.

After the convention-design tranche is decided or explicitly declined, offer a concise map of the other personalisation areas and continue only with the user's selected area. Read `~/.claude/CLAUDE.md` when the user selects a broader working-style area or when a proposed cross-project directive must always load. Use [the convention-resolution rules](../organise-docs/references/convention-resolution.md) only when resolving a confirmed change or a genuinely local candidate. Inspect only the smallest relevant set of live skill frontmatter, owner instructions, and configuration. Installed skill names and descriptions are the capability catalogue; do not require a separate routing registry.

For a broad review, group the system by recognisable areas such as communication, planning and backlog, delivery and Git, documents, assurance, session continuity, delegation, and system maintenance. Read owner bodies only when their metadata does not reveal the actual default or mutation authority.

Classify each candidate:

- **Fixed convention:** a system invariant or tool requirement; explain it and change only through a deliberate redesign.
- **Global personal convention:** a repeated cross-project choice with credible alternatives and meaningful trade-offs; update its existing global source.
- **Project-specific convention:** a durable exception caused by that project's users, domain, legacy, external contracts, tooling, or explicit working model; update its project source without changing the global default.
- **Situational judgement:** the owner should decide from current risk, evidence, and outcome; do not freeze it into a preference.

Include a choice only when the current system actually encodes a default and a realistic alternative would change future work.

## Work through consequential choices

For each choice, state:

- the current default and its source of truth;
- the problem it solves;
- credible alternatives and practical trade-offs;
- whether existing projects or artifacts would be affected; and
- a recommendation grounded in the user's observed working style.

Ask in small coherent groups. Preserve an already confirmed preference unless new evidence creates a material conflict. If the owner already makes the choice contextually, leave it contextual and explain why.

For a document or identifier choice, make the scope judgement before proposing a mutation:

- prefer a global change only when the preference should govern future projects generally;
- prefer a project overlay when the difference is caused by this project's domain, users, legacy, contracts, tooling, or declared working model; and
- leave the rule inherited when the project has no durable reason to diverge.

Judge scope from the intended reach and stated cause, not from an unsolicited audit of the current project. State whether the change would edit the registered global source or create/update `reference/project-conventions.md`. Do not ask the user to choose a storage location without first making and explaining this judgement.

## Route each confirmed change

There is no central preferences profile. Use one owner per rule:

| Change | Source of truth or owner |
| --- | --- |
| Cross-project directive that must always load in Claude Code | `~/.claude/CLAUDE.md` |
| Reusable skill behaviour, trigger, workflow, or ownership | Stop personalisation and switch to `upskill` on the owning skill |
| Global document or identifier convention | The registered global convention source owned by `organise-docs` |
| Project-specific document or identifier convention | `reference/project-conventions.md`, created on the first confirmed durable divergence |
| Review whether project documents follow the current conventions | Stop personalisation and switch to `organise-docs` |
| Document-set migration | `organise-docs` and the resolved current conventions |
| Backlog structure, ordering, or uncommitted-work behaviour | `agent-pm` backlog planning |
| Project Git branching, review, or release convention | `agent-dev` Git-workflow consultation and project instructions |
| Session-end reconciliation or handoff behaviour | `close-session` |
| Project-wide facts, constraints, conventions, or hazards | `manage-project-context` or the discovering owner within its bounded authority |
| Model and effort selection rules | `choose-model` when the choice is truly durable and surface-specific |
| How Claude delegates a bounded task or independent pass to Codex | `use-codex` |

Present one change plan grouped by owner before mutation. Identify affected consumers, project instructions, configuration, documents, and existing artifacts. Do not duplicate a rule into consumers that already read or follow its owner.

Personalisation may create or update approved global and project convention sources directly, including `~/.claude/CLAUDE.md`, `organise-docs/doc-conventions.csv`, `organise-docs/references/identifier-conventions.md`, and a project's `reference/project-conventions.md`. A registered convention resource remains a convention source even when it is stored inside the owning skill directory.

Personalisation must never create, edit, rename, move, or delete any `SKILL.md`. If a requested result requires changing skill selection, instructions, workflow, ownership, or another non-convention skill resource, stop this route and switch to `upskill`; do not make that mutation under personalisation. Project mutations outside the convention sources go through their operational owner. Preserve unrelated customisation.

## Migrate existing projects deliberately

Treat migration as part of the convention decision:

1. Agree the projects or artifacts in scope; do not assume every existing project should change.
2. Inventory affected current files and references through the new owner.
3. Separate mechanical edits from ambiguous transformations, destructive changes, and history rewriting.
4. Preview collisions, exceptions, reference changes, and projects better left on the old convention.
5. Apply only the approved scope through the owning workflow.
6. Verify sources of truth, consumers, references, configuration, and representative future behaviour.

Prefer forward adoption when bulk migration has little practical value. Do not cosmetically rewrite stable history, identifiers, or external paths merely for uniformity.

## Finish

Report the defaults reviewed, decisions retained or changed, owners and source files updated, migrations completed or deferred, intentional exceptions, and any unresolved owner work. A successful result leaves one source of truth per rule and no new preference artifact.
