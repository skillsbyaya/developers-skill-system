---
name: clean-up
description: "Coordinates broad project housekeeping across two or more of testing, documentation, project-context health, skill fit, token cost, and backlog. Use for clean up, tidy, housekeeping, or sort-this-project-out requests spanning several areas. Not for application-code refactoring."
---

# Clean Up

Coordinate one presence-gated housekeeping sweep and return one consolidated result. The selected owners perform their own work; this skill does not reimplement their methods.

## Scope the sweep

If the user names one clear area, switch directly to its owner and do not broaden the request. For an unqualified cleanup request or two or more named areas, inspect only enough project structure and current evidence to decide which rows are present.

| Order | Area and owner | Include only when |
| --- | --- | --- |
| 1 | Project-context health → `manage-project-context` | The registered context is missing, or an almost-always-needed project fact is materially stale or contradicted by authoritative current evidence. Age alone is not staleness. |
| 2 | Test health → `agent-test-architect` test-system Review | A test suite exists and a report-only health review would be useful. |
| 3 | Documentation → `organise-docs` | A documentation set exists and its placement, naming, duplication, staleness, size, navigation, identifier-area vocabulary, or temporary `.working/` material needs attention. Include `.working/` only when a file has no current owner or its useful outcome is already incorporated; an empty or absent `.working/` is a valid no-op. |
| 4 | Project skill fit → ordinary reasoning over project evidence and live skill frontmatter | The user explicitly asks which capabilities the project is missing, or a broad sweep has enough current project evidence to assess overlooked skill opportunities. |
| 5 | Skill or token cost → `optimise-tokens` | The project is a skill library, or the user raised context or token cost. |
| 6 | Uncommitted follow-ups and triggered deferrals → `agent-pm` backlog planning | A backlog exists, earlier selected areas produced confirmed work that is not already owned by committed delivery, or an explicit deferral trigger or deadline has demonstrably arrived. |

Do not add assurance, code review, security, compliance, lessons, retrospective, CI, release readiness, or session close merely because they are useful elsewhere. Include them only when the user separately requests that outcome or a selected owner identifies a concrete specialist need.

If no row is present, report what was checked and ask which housekeeping area the user meant. Do not manufacture work to make the sweep non-empty.

## Confirm once

For two or more included areas, present the proposed order, what each owner may change, and any area skipped for lack of evidence. Ask for one sweep-level confirmation before mutation. The user may trim or reorder the set.

Do not add another confirmation at every owner boundary. Reconfirm only when an owner surfaces a material action outside the confirmed scope, such as deletion, a risky restructure, a comprehensive project rebaseline, or another hard-to-reverse change.

For one included area, switch directly and let that owner apply its normal authority and confirmation rules.

## Run the sweep

1. Execute one selected area at a time in the confirmed order.
2. Pass paths, current evidence, and compact findings rather than copied documents or long recaps.
3. For project-context health, ask the owner to assess the defect and use only the justified mode. Missing or contradictory context does not by itself authorise a comprehensive rebaseline.
4. For testing, request report-only review. Production or test-code repairs become a separate delivery or testing task.
5. For documentation, pass any evidence-backed stale-concepts list already established by current work. Do not ask the user to recreate one when the evidence is sufficient, and do not let the coordinator guess which substantive claims are obsolete.
   When `reference/identifier-areas.yaml` exists, include a vocabulary check only if the documentation inventory shows unused, duplicate, misleading, or drifting areas. `organise-docs` owns any edit and may remove an area only after confirming no current ID, current document language, alias, or active near-term work still needs it; archives remain untouched.
   Treat `.working/` as temporary by convention, not disposable by name. Ask `organise-docs` to remove only material whose useful outcome is incorporated or whose lack of a current owner is proven; preserve active drafts and stop before an uncertain deletion. When no orphaned instance exists, record the no-op and do not manufacture cleanup.
6. For project skill fit, compare evidenced project needs with live skill names and descriptions, keep the result findings-only, and do not infer a missed trigger from non-use. A proposed skill change requires separate work through `upskill`.
7. Inspect living deferral registers and backlog items only for explicit, observable triggers or deadlines that current evidence can verify. Send triggered, still-uncommitted work and other confirmed follow-ups to `agent-pm` backlog planning; leave untriggered deferrals in place and do not copy active story, package, or delivery-status work into the backlog. A trigger arriving authorises lifecycle reconciliation, not implementation.
8. If accumulated context would weaken the next area, checkpoint the completed results and continue area by area in a fresh session rather than forcing one oversized run.

If an optional owner is unavailable, name the skipped boundary and continue the remaining confirmed areas when that is still useful.

## Boundaries

- Do not edit production, feature, runtime, or test code.
- Do not mutate delivery lifecycle or infer completion.
- Do not load project context merely for orientation. Inspect its health only when current project evidence makes that area relevant.
- Stop at a material blocking decision instead of pushing through it to finish the sweep.
- Run each area at most once per sweep.

## Finished result

Report the areas checked, owners used, material outcomes, skipped or unavailable areas, temporary working material removed or deliberately retained, triggered deferrals promoted or left in place, confirmed follow-ups added to the backlog, deferred code or test work, and any unresolved user decision.
