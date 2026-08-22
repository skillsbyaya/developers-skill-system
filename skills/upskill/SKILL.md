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

## Universal design rules

- Start with the real recurring need: the expected inputs and result, the constraints, the risks, and the ways the work can fail. A requested name or file does not prove that a new skill is needed.
- Infer what is already clear from the request, artifacts, examples, intended result, constraints, and neighbouring skills. Ask only when missing information would materially change the design or the safe result.
- Create a separate visible skill only when reusable instructions or judgement will make repeated work reliably better and an existing area owner or directly selectable mode would not provide a clearer home. First consider ordinary reasoning, an existing skill, a mode, a shared rule, a reference, a script, a template, a registry, a tool, or a connector.
- Give each owner one clear user-facing area, not necessarily one visible skill per method. A directly selected workflow may own specialised judgement, mutation, durable records, or lifecycle rules within that area. Those properties justify a standalone owner only when the capability must remain independent of the area owner: users naturally enter through another area, it serves several areas without one natural parent, the parent would misrepresent its authority, or separation is required for genuinely independent selection or assurance. Test the complete parent-plus-workflow route rather than treating internal authority as automatic proof of another visible skill.
- Write descriptions as minimal positive selection metadata, not summaries or boundary contracts. Add an exclusion only for a demonstrated cue collision that would otherwise misroute.
- Match the instructions to the work. Give mechanical tasks exact steps and checks; give judgement tasks decision rules and examples; give uncertain or high-impact work evidence requirements, risks, boundaries, and checks of the finished result. Use prose for flexible judgement, templates for formats that must stay consistent, and scripts or exact commands for fragile repeatable operations.
- When Claude can choose a skill automatically, it sees the name and description first, loads `SKILL.md` when the skill is selected, and reads linked files only when instructed. Keep `SKILL.md` for routing and rules every route needs. Put conditional procedures, templates, and detailed policy one folder level down.
- Treat installed skill names and frontmatter descriptions as the current capability catalogue. Inspect the bodies of plausible neighbours only when their metadata cannot resolve ownership or routing. Do not create a parallel routing catalogue.
- Keep the core small but complete. When a skill has conditional workflows, load only the workflow selected for the current request. Add references, scripts, templates, assets, tools, or connectors only when they make the work more reliable or keep conditional detail out of the core.
- Put each rule in the narrowest place where it will reliably apply. Keep genuinely cross-task rules in shared or global instructions and reference them at workflow call sites when needed. If a global rule belongs to one skill, move it there when that work is in scope; otherwise flag it and offer to clean it up.
- Create recurring documents or information that must persist between sessions only when they help later work. Give each one a clear owner, say who may update it and how to find it, and define when it should be removed or archived.
- Increase planning, confirmation, review, documentation, or worker use only when the consequences, available evidence, or remaining uncertainty justify it. The main agent keeps responsibility for decisions, integration, saved information, and user communication.
- Design for one person unless the user declares another working model. Keep controls that improve outcomes, safety, continuity, or confidence; remove ceremony that exists only for team reporting or duplicated handoffs.
- Personal skills may contain lasting personal preferences and library conventions, but not paths, decisions, examples, or procedures that belong to one project. Project skills may use their declared repository context.
- When creating or substantially changing a skill, check that it fits the user's current system and does not duplicate or break anything. Base the change on real needs and evidence, not guesses about hypothetical future users. For small edits and repairs, change only what is needed.

## Completion standard

Use stronger evidence for higher-risk changes. Finish only when:

- the skill has a clear recurring job and clear boundaries;
- natural, explicit, vague, and neighbouring requests reach the right skill or system component;
- methods nested under an area owner remain directly selectable without consultation or another workflow as preflight;
- direct use works without hidden setup or preliminary routing;
- the skill contains enough judgement and failure handling to improve the result;
- instructions needed only for some cases load only when those cases apply;
- changes, saved information, recurring documents, verification, and review each have clear responsibility;
- affected callers, live frontmatter, links, and resources agree with the change; and
- metadata, paths, scripts, and other repeatable helpers pass the relevant checks.

Walk realistic clear, vague, neighbouring, and failure-prone cases against the finished skill. Judge the finished result or behaviour, not a claim that the process was followed. Clean prose, short files, fewer skills, preserved old behaviour, or a completed checklist do not by themselves prove that the skill works. Keep an instruction only when it changes behaviour, prevents a credible error, preserves a lasting preference, or routes necessary detail.
