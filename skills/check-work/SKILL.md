---
name: check-work
description: "Chooses a proportionate assurance route or lightly disposes existing evidence. Use for generic checking, evidence-status questions, ready-to-build or ready-to-ship decisions, human preview, code review, pressure-testing, edge cases, and review-to-done evidence. Do not use merely because a delivery record mentions a manual or future check."
---

# Check Work

Answer one assurance question with current evidence.

## Select one route

Infer the assurance decision from the request, target, current evidence, and unresolved uncertainty. When one route is obvious, select it without asking the user to name a workflow. Select one route, then read only that workflow.

| Assurance decision | Read |
| --- | --- |
| How should an existing check, result, limitation, or proposed observation be carried forward without rerunning assurance? | [Evidence disposition](workflows/evidence-disposition.md) |
| What observable differences appear in the live or dev experience, what can current evidence establish, and which remaining observations require a person? | [Human preview](workflows/human-preview.md) |
| Can implementation responsibly start from these planning artifacts? | [Implementation readiness](workflows/implementation-readiness.md) |
| Can this bounded candidate ship now? | [Release readiness](workflows/release-readiness.md) |
| Is this code change correct enough for its residual technical risk? | [Code review](workflows/code-review.md) |
| Does this artifact survive hostile challenge? | [Adversarial review](workflows/adversarial.md) |
| Are reachable paths, states, transitions, or boundaries unhandled? | [Edge-case review](workflows/edge-cases.md) |

Merely recording packet evidence, an unavailable check, or a possible future manual observation is not a new assurance decision and does not require this skill. Preserve it in the owning delivery record. Use evidence disposition only when the user or current task asks how existing evidence should count, persist, or be invalidated.

If the request and context do not identify one decision, including a generic request such as “check this,” “review the work,” “what assurance do we need?”, or a question about `review` versus `done`, read [Assurance selection and completion](references/assurance-and-completion.md). Use it to choose one workflow above or switch once to the independent specialist that owns the unresolved question.

If two different uncertainties are material, complete the primary decision first. Use another method only when a second named uncertainty remains unresolved.

## Common assessment rules

These rules apply to assurance routes other than evidence disposition, whose workflow deliberately stays lighter.

- Resolve the target, scope, baseline, and current revision. State an obvious assumption; ask only when alternatives would change the route or result.
- Inspect current, scope-matched evidence. Never report an unperformed, stale, unavailable, or mismatched check as passed.
- Do not rerun a method when current scope- and revision-matched evidence already answers the decision. Rerun it after relevant changes, wider scope, insufficient earlier inspection, or a fix that invalidated the affected result.
- Consult a decision-of-record only when it could resolve source authority, scope, or a candidate finding. Search by the scope's identifier or area; do not scan registers for evidence disposition, clean results, or routine reporting. Carry a relevant accepted decision unless current evidence materially contradicts it.
- Require human preview before another method only when experience, visual behaviour, copy, interaction, accessibility use, or a manual journey could materially change the revision. Otherwise order assurance by evidence value and the risk of reviewing stale work.
- Do not change the assessed work or its lifecycle or release state. If fixes were requested, finish the assessment and return the scope, revision, evidence, findings, and limitations to the relevant owner; recheck affected assurance after changes.
- If required specialist evidence is unavailable, state what is missing and leave the decision unresolved rather than imitating the specialist.
- Leave consequential acceptance and residual-risk decisions to the user. Acceptance cannot replace a mandatory safety or legal control.

## Finished result

For an assurance route, return the decision, scope and revision, evidence, result or findings, limitations, and next action when one is needed. For evidence disposition, return only the classification and smallest next action defined by that workflow.
