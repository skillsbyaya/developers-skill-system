---
name: clean-up
description: "Removes residue that patched-on changes leave in instructions, memory, documents and skills, and coordinates broad project housekeeping across testing, documentation, project-context health, skill fit, token cost, and backlog. Use for clean up, tidy, housekeeping, or sort-this-project-out requests, and for bloat, stale rules, workarounds, or notes about things already removed or fixed. Not for application-code refactoring."
---

# Clean Up

Run the residue check, coordinate one presence-gated housekeeping sweep, and return one consolidated result. The residue check is this skill's own method; every other area's owner performs its own work.

## Scope the sweep

If the user names one clear area, run only that row and do not broaden the request. For an unqualified cleanup request or two or more named areas, inspect only enough project structure and current evidence to decide which rows are present.

| Order | Area and owner | Include only when |
| --- | --- | --- |
| 1 | Residue → this skill's [residue check](references/residue.md) | Every sweep. |
| 2 | Project-context health → `manage-project-context` | The registered context is missing, or an almost-always-needed project fact is materially stale or contradicted by authoritative current evidence. Age alone is not staleness. |
| 3 | Test health → `agent-test-architect` test-system Review | A test suite exists and a report-only health review would be useful. |
| 4 | Documentation → `organise-docs` | A documentation set exists and its placement, naming, duplication, staleness, size, navigation, identifier-area vocabulary, or temporary `.working/` material needs attention. Include `.working/` only when a file has no current owner or its useful outcome is already incorporated; an empty or absent `.working/` is a valid no-op. |
| 5 | Project skill fit → ordinary reasoning over project evidence and live skill frontmatter | The user explicitly asks which capabilities the project is missing, or a broad sweep has enough current project evidence to assess overlooked skill opportunities. |
| 6 | Skill or token cost → `optimise-tokens` | The project is a skill library, or the user raised context or token cost. |
| 7 | Uncommitted follow-ups and triggered deferrals → `agent-pm` backlog planning | A backlog exists, earlier selected areas produced confirmed work that is not already owned by committed delivery, or an explicit deferral trigger or deadline has demonstrably arrived. |

Do not add assurance, code review, security, compliance, lessons, retrospective, CI, release readiness, or session close merely because they are useful elsewhere. Include them only when the user separately requests that outcome or a selected owner identifies a concrete specialist need.

A sweep where only the residue check applies is complete. Do not manufacture work to widen it.

## Confirm once

Run the residue check first, without confirmation: it changes no live rule, and it shrinks what the other owners read. For two or more other areas, present the proposed order, what each owner may change, and any area skipped for lack of evidence. Ask for one sweep-level confirmation before mutation. The user may trim or reorder the set.

Do not add another confirmation at every owner boundary. Reconfirm only when an owner surfaces a material action outside the confirmed scope, such as deletion, a risky restructure, a comprehensive project rebaseline, or another hard-to-reverse change.

For one other area, switch directly and let that owner apply its normal authority and confirmation rules.

## Run the sweep

1. Execute one selected area at a time in the confirmed order.
2. Pass paths, current evidence, and compact findings rather than copied documents or long recaps.
3. For project-context health, ask the owner to assess the defect and use only the justified mode. Missing or contradictory context does not by itself authorise a comprehensive rebaseline.
4. For testing, request report-only review. Production or test-code repairs become a separate delivery or testing task.
5. For documentation, pass any evidence-backed stale-concepts list already established by current work. Do not ask the user to recreate one when the evidence is sufficient, and do not let the coordinator guess which substantive claims are obsolete.
   When the project has an identifier-area registry, include a vocabulary check only if the documentation inventory shows unused, duplicate, misleading, or drifting areas. `organise-docs` owns any edit and may remove an area only after confirming no current ID, current document language, alias, or active near-term work still needs it; archives remain untouched.
   Treat `.working/` as temporary by convention, not disposable by name. Ask `organise-docs` to remove only material whose useful outcome is incorporated or whose lack of a current owner is proven; preserve active drafts and stop before an uncertain deletion. When no orphaned instance exists, record the no-op and do not manufacture cleanup.
6. For project skill fit, compare evidenced project needs with live skill names and descriptions, keep the result findings-only, and do not infer a missed trigger from non-use. A proposed skill change requires separate work through `upskill`.
7. Inspect living deferral registers and backlog items only for explicit, observable triggers or deadlines that current evidence can verify. Send triggered, still-uncommitted work and other confirmed follow-ups to `agent-pm` backlog planning; leave a deferral that waits on a real prerequisite in place, send one whose only condition is first use to `agent-pm` for a place in the order, and do not copy active story, package, or delivery-status work into the backlog. A trigger arriving authorises lifecycle reconciliation, not implementation.
8. If accumulated context would weaken the next area, checkpoint the completed results and continue area by area in a fresh session rather than forcing one oversized run.

If an optional owner is unavailable, name the skipped boundary and continue the remaining confirmed areas when that is still useful.

## Boundaries

- Do not edit production, feature, runtime, or test code. A workaround whose true fix is in code goes to the backlog owner.
- Do not mutate delivery lifecycle or infer completion.
- Do not load project context merely for orientation. Inspect its health only when current project evidence makes that area relevant.
- Stop at a material blocking decision instead of pushing through it to finish the sweep.
- Run each area at most once per sweep.

## Finished result

Report the residue removed as the residue check specifies, then the areas checked, owners used, material outcomes, skipped or unavailable areas, temporary working material removed or deliberately retained, triggered deferrals promoted or left in place, confirmed follow-ups added to the backlog, and deferred code or test work.

Do not close the sweep by reporting a decision that is the user's to make. Ask it in this run, batching every decision the sweep raised into one round of questions. Only a decision that genuinely cannot be put to the user yet stays written down, and it names what has to happen first.
