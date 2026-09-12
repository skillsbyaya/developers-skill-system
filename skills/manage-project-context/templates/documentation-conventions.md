# Documentation Conventions Template

Use this when establishing or deliberately updating a project's Documentation conventions section, or changing global document preferences through `personalise-working-system`. Do not load it for routine document lookup or writing once the project has adopted its rules.

## Adapt to the project

1. Read explicit user requirements, binding project instructions, the existing context, and enough current documents to identify the real structure. Preserve established paths and external contracts when moving them would bring little benefit. Explicit requirements take precedence over these defaults.
2. Select only document types the project uses or has a concrete need to create. Use the defaults below as starting choices. Write the resulting project rules in full for those types, including any local differences; do not write a delta table that requires consulting this template later.
3. Record one useful general naming rule, actual folder or file patterns, concrete examples, and any justified exceptions. Preserve fixed-name outputs and compound artifact folders. Add pointers only where they identify a current authority that readers need to find; a naming example is not a claim that the file exists.
4. For a new document type, choose from its purpose, lifecycle, existing project structure, and these defaults. Record a durable rule in context when that type will recur; do not expand the section for one-off output. Report material uncertainty instead of inventing project policy.
5. Preserve the project's adopted rules when this template changes. Updating the global template does not migrate existing projects or rename their files. An authorised adoption task states whether a changed rule applies to future documents only or also to a specified existing set; `organise-docs` handles that set's migration and reference repairs.
6. Keep project-specific identifier rules in this same context section when needed. Preserve the existing registry path and link to the project's area vocabulary instead of copying it. Read [identifier conventions](../../organise-docs/references/identifier-conventions.md) only when identifier setup or migration is in scope; domain owners retain item meaning, allocation, and lifecycle.

## Consolidate an existing convention record

Only when adopting this model for an existing project, inspect any convention source named by its instructions, including `reference/project-conventions.md` when present. Preserve every still-valid local placement, naming, format, and identifier rule, plus the defaults actually needed to make those rules complete. Reconcile conflicts against explicit current authority; do not silently replace local decisions with this template's defaults.

Write the adopted rules into the existing project context, update current pointers, and retire the former convention record when the requested migration includes its removal. If removing it is outside the authorised scope, explicitly mark it superseded and point to project context when that edit is authorised; otherwise report the remaining consolidation step. Never declare the migration complete while two files still claim authority. Do not migrate unrelated project files merely to consolidate their convention record.

## Project section to fill

Adapt this shape; remove placeholders and instructions from the finished section. Keep only useful rows and omit optional content that the project does not need.

```markdown
## Documentation conventions

{The naming and format rules adopted for this project, with one concrete example.}

| Document purpose | Location and naming | Example or current authority |
| --- | --- | --- |
| {Relevant document type} | {Actual folder and pattern or fixed path} | {Example, or link to the existing authoritative file} |

{Any material exception and its reason; any forward-only adoption boundary.}
{Optional: project-specific identifier rules and a pointer to its area registry.}
```

## Global starting preferences

- Keep always-read control files at the root; group other working documents by purpose and lifecycle. Preserve fixed-name contracts and established project exceptions.
- Separate filename fields with underscores and words within a field with hyphens: `[type]_[area]_[specifics].md`, for example `prd_ordering_customer-order-form.md`. Order fields from general to specific. An area is a functional module such as ordering or invoicing, not the project name. Omit area or specifics when the remaining fields identify the document clearly.
- Use numbers only for meaningful order or durable workflow keys. Gaps are acceptable once referenced; collisions and competing numbering systems need resolution. Prefer purpose labels where numbers add no information.
- Preserve conventional fixed filenames. Add dates only for genuine point-in-time artifacts.
- Default human-readable working documents to Markdown. Use structured or interactive formats when the artifact needs them, such as YAML for managed state, CSV for compact registries, or HTML for interactive references.
- Put companions beside their parent using `{parent-basename}.{role}.{ext}`, such as `prd.decision-log.md`, `brief.addendum.md`, or `ux.color-themes.html`. Companions do not need separate catalogue rows.
- The catalogue supplies starting patterns, not a mandatory project inventory. Preserve a complete convention for each adopted recurring type. Add a new global type only when repeated use earns it; use `upskill` if its producing skill also needs changing.

## Default document patterns

Names without an extension default to `.md`; fixed filenames and folder contracts keep their stated form. Folder entries are relative to the project root. Select and adapt relevant rows into the project section above.

| Document type | Folder | Naming pattern | Example |
| --- | --- | --- | --- |
| claude | (root) | CLAUDE.md | CLAUDE.md |
| backlog | (root) | BACKLOG.md | BACKLOG.md |
| project-context | (root) | project-context.md | project-context.md |
| identifier-areas | reference | identifier-areas.yaml | reference/identifier-areas.yaml |
| directory-index | the folder being indexed | index.md | reference/index.md |
| brief | product | brief_[area]_[specifics] | product/brief_ordering.md |
| prd | product | prd_[area]_[specifics] | product/prd_ordering_customer-order-form.md |
| prfaq | product | prfaq_[area]_[specifics] | product/prfaq_ordering.md |
| trigger-map | product | trigger-map_[area] | product/trigger-map_ordering.md |
| brainstorming-session | brainstorming | brainstorming-session-[date]-[time] | brainstorming/brainstorming-session-2026-07-03-1430.md |
| forge-session | brainstorming | forge-[slug]/ (folder exception: holds optional forged-idea.md, forge-report.html, and hidden .memlog.md; do NOT flatten) | brainstorming/forge-ordering/forge-report.html |
| research | product | research_[market\|domain\|technical]_[specifics] | product/research_market_competitors.md |
| domain-fit-assessment | product | domain-fit-assessment_[area]_[specifics] | product/domain-fit-assessment_ordering_regulatory-practice.md |
| applicability-findings | compliance | applicability-findings_[area]_[specifics] | compliance/applicability-findings_data-processing.md |
| assurance-audit | compliance | assurance-audit_[area]_[specifics] | compliance/assurance-audit_data-processing.md |
| compliance-register | compliance | compliance-register.md | compliance/compliance-register.md |
| dpia | compliance | dpia_[area]_[specifics] | compliance/dpia_data-processing.md |
| record-of-processing | compliance | record-of-processing.md | compliance/record-of-processing.md |
| retention-schedule | compliance | retention-schedule.md | compliance/retention-schedule.md |
| lawful-basis-consent-review | compliance | lawful-basis-consent-review.md | compliance/lawful-basis-consent-review.md |
| subject-access-process | compliance | subject-access-process.md | compliance/subject-access-process.md |
| regulatory-horizon-scan | compliance | regulatory-horizon-scan.md | compliance/regulatory-horizon-scan.md |
| architecture | design | architecture_[area]_[specifics] | design/architecture_ordering_data-model.md |
| ux | design | ux-[area]/ (folder exception: holds fixed-name DESIGN.md + EXPERIENCE.md plus companions such as .decision-log.md and .working/ notes; do NOT flatten) | design/ux-checkout/DESIGN.md |
| design-system-guide | design | design-system_[area]_[specifics] | design/design-system_checkout.md |
| design-thinking-session | design | design-thinking_[area]_[specifics] | design/design-thinking_checkout_first-use.md |
| visual-reference | design | visual-reference_[area]_[specifics] | design/visual-reference_checkout-token-preview.html |
| epics | implementation | epics_[area]_[specifics] | implementation/epics_ordering.md |
| story | implementation | [story-base-id]-[slug] | implementation/S2-E4-order-edit.md |
| change-package | implementation | change_[area]_[specifics] | implementation/change_checkout_validation.md |
| code-review-handoff | implementation | code-review_[area]_[specifics] | implementation/code-review_checkout-auth.md |
| delivery-status | implementation | sprint-status.md | implementation/sprint-status.md |
| retro | implementation | retrospective-[scope]-[slug] | implementation/retrospective-epic-3-ordering.md |
| spike | implementation | spike_[area]_[specifics] | implementation/spike_core_supabase-multi-schema.md |
| deferred-work | implementation | deferred-work.md | implementation/deferred-work.md |
| sprint-change-proposal | implementation | sprint-change-proposal-[date] | implementation/sprint-change-proposal-2026-06-28.md |
| atdd-checklist | implementation | tests/atdd_[story-base-id or specifics] | implementation/tests/atdd_S2-E4-order-edit.md |
| test-summary | implementation | tests/test-summary.md | implementation/tests/test-summary.md |
| test-review | implementation | tests/test-review_[area] | implementation/tests/test-review_checkout.md |
| release-readiness | implementation | tests/release-readiness_[area] | implementation/tests/release-readiness_checkout.md |
| guide | reference | guide_[area]_[specifics] | reference/guide_onboarding.md |
| codebase-reference | reference | codebase_[area]_[specifics] | reference/codebase_billing_webhook-flow.md |
| decisions | reference | decisions.md | reference/decisions.md |
| readiness-report | reference | implementation-readiness-report | reference/implementation-readiness-report.md |
