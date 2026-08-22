---
name: check-work
description: "Chooses one assurance route: human preview, implementation readiness, release readiness, code review, adversarial review, edge-case review, or a specialist handoff. Use for generic checking, ready-to-build or ready-to-ship decisions, what a person must check in a preview or sandbox environment, reviewing code changes, pressure-testing, edge cases, or review-to-done evidence."
---

# Check Work

Answer one assurance question with current evidence.

## Select one route

Infer the assurance decision from the request, target, current evidence, and unresolved uncertainty. When one route is obvious, select it without asking the user to name a workflow. Select one route, then read only that workflow.

| Assurance decision | Read |
| --- | --- |
| What observable differences appear in the live or dev experience, what can current evidence establish, and which remaining observations require a person? | [Human preview](workflows/human-preview.md) |
| Can implementation responsibly start from these planning artifacts? | [Implementation readiness](workflows/implementation-readiness.md) |
| Can this bounded candidate ship now? | [Release readiness](workflows/release-readiness.md) |
| Is this code change correct enough for its residual technical risk? | [Code review](workflows/code-review.md) |
| Does this artifact survive hostile challenge? | [Adversarial review](workflows/adversarial.md) |
| Are reachable paths, states, transitions, or boundaries unhandled? | [Edge-case review](workflows/edge-cases.md) |

If the request and context do not identify one decision, including a generic request such as “check this,” “review the work,” “what assurance do we need?”, or a question about `review` versus `done`, read [Assurance selection and completion](references/assurance-and-completion.md). Use it to choose one workflow above or switch once to the independent specialist that owns the unresolved question.

If two different uncertainties are material, complete the primary decision first. Use another method only when a second named uncertainty remains unresolved.

## Common assessment rules

- Resolve the target, scope, baseline, and current revision. State an obvious assumption; ask only when alternatives would change the route or result.
- Inspect current, scope-matched evidence. Never report an unperformed, stale, unavailable, or mismatched check as passed.
- Do not rerun a method when current scope- and revision-matched evidence already answers the decision. Rerun it after relevant changes, wider scope, insufficient earlier inspection, or a fix that invalidated the affected result.
- Before reporting a finding or putting a decision to the user, search the project's decisions-of-record — backlog, decision log, issue or risk register — by the scope's identifiers and area rather than reading it whole. Cite an existing entry and carry its recorded decision instead of re-opening it; re-open only on current evidence that materially contradicts it. This is where "already handled" and "existing accepted decisions" are established.
- Require human preview before another method only when experience, visual behaviour, copy, interaction, accessibility use, or a manual journey could materially change the revision. Otherwise order assurance by evidence value and the risk of reviewing stale work.
- Do not change the assessed work or its lifecycle or release state. If fixes were requested, finish the assessment and return the scope, revision, evidence, findings, and limitations to the relevant owner; recheck affected assurance after changes.
- If required specialist evidence is unavailable, state what is missing and leave the decision unresolved rather than imitating the specialist.
- Leave consequential acceptance and residual-risk decisions to the user. Acceptance cannot replace a mandatory safety or legal control.

## Finished result

Return the decision, scope and revision, evidence, result or findings, limitations, and next action when one is needed.

