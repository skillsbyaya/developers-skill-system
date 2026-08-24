---
name: upskill
description: Creates, discovers, reviews, edits, repairs, removes, or restructures reusable Claude Code skills and the skill library they belong to. Use when the user wants to find external skills or patterns worth adopting, create or change reusable skill support, fix skill triggering or workflow, or review or restructure the library. Do not use for ordinary domain work or project execution merely because it involves skills.
---

# Upskill

Turn repeated needs and known failures into reliable reusable support. Select this skill because the requested outcome improves or governs that support, not merely because the surrounding project concerns skills. Use the simplest mechanism that will improve the user's later work. Personal skills live in `~/.claude/skills/`; project skills live in the project's `.claude/skills/` folder.

## Select the route

Choose the route that matches what the user wants you to finish and start with only that route. If the user already asked you to review and improve, begin with audit, then use the smallest appropriate edit, repair, or restructure route for the confirmed findings without asking again. Otherwise do not load sibling routes.

| Outcome | Read |
| --- | --- |
| Find external skills or reusable patterns worth adopting | [External skill discovery](references/external-evidence.md) |
| Create a new reusable capability | [Create a skill](references/create-skill.md) |
| Review whether a skill works as intended | [Audit a skill](references/audit-skill.md) |
| Make a specific, limited change | [Edit a skill](references/edit-skill.md) |
| Fix a reported or reproducible failure | [Repair a skill](references/repair-skill.md) |
| Merge, split, port, retire, remove, or redesign skills | [Restructure skills](references/restructure-skills.md) |
| Review the skill library as a whole | [Review the library](references/review-library.md) |

External discovery may also supply evidence to create, audit, restructure, or library-review work when the user requests outside comparison or local evidence cannot resolve a material choice. When selected from another route, return its report to that route; do not preload it or continue automatically.

## Shared rules

- Start from the requested outcome and the available evidence. Infer what the request, artifacts, examples, constraints, and neighbours already settle; ask only when missing information would materially change the route or safe result.
- Match the method to the work. Give mechanical tasks exact steps and checks, judgement tasks decision rules, and consequential or uncertain tasks proportionately stronger evidence and safeguards.
- Load only the selected route and the conditional resources it directs. Creation, ownership design, restructuring, and library governance rules belong in their respective routes, not in every edit, repair, or audit.
- Increase planning, confirmation, documentation, review, or worker use only when consequence, evidence, or uncertainty justifies it. Design for one person unless the user declares another working model.
- Keep personal skills portable across projects and project skills within their declared repository context.
- For a bounded edit or repair, change only what the demonstrated need requires. Do not expand it into mechanism selection, ownership redesign, or a library review unless the evidence shows that the bounded route cannot solve the problem.

## Finish in proportion

The selected route owns its completion depth. Judge the changed result or behaviour, not whether a universal checklist was performed.

For a bounded edit or repair, stop when the requested behaviour works and the affected surface is coherent. Use the smallest realistic regression set that can expose the likely failure. Parse metadata only when touched, resolve changed links and paths, test changed deterministic helpers, and inspect callers or neighbours only when the change can affect them.

Use a clear or direct-use case when workflow behaviour changed, a vague case when discovery or inference changed, a neighbouring case when a boundary or trigger changed, and a failure-prone case when safeguards or error handling changed. Do not require all case classes for every change.

Creation, material redesign, and library-wide review require the broader system-fit and pressure-testing standards in their selected routes. An audit needs only enough evidence to resolve its stated concern unless the deep pressure-test conditions apply.

Keep an instruction only when it changes behaviour, prevents a credible error, preserves a lasting preference, or routes necessary detail.
