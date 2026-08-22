---
name: research
description: "Researches domains, industries, markets, customers, competitors, and technical options with current external evidence. Use for domain briefings or fit assessments, market entry, demand, buying behaviour, sizing, positioning, competitor research, technology comparisons, build-versus-buy, feasibility, integrations, migrations, standards, or cited research reports."
---

# Research

Acquire and synthesise external evidence for a decision. Answer the question that caused the research, expose uncertainty honestly, and translate the result into practical implications without expanding into an encyclopedia.

## Select one workflow

Infer the evidence needed and read only the selected workflow.

| Need | Read |
| --- | --- |
| Understand a subject, industry, operating model, sector constraint, or regulatory landscape; or assess a project's position against domain evidence and established practice | [Domain research](workflows/domain.md) |
| Understand demand, customers, buying behaviour, segments, alternatives, competitors, market size, positioning, or commercial opportunity | [Market research](workflows/market.md) |
| Compare technologies, frameworks, standards, integrations, migrations, build-versus-buy options, technical feasibility, or project fit | [Technical research](workflows/technical.md) |

An explicit mode or clear research request selects it directly. If several evidence questions are genuinely required, finish or checkpoint one workflow before selecting another and carry forward only the relevant conclusions. Do not preload or combine workflows.

## Common research rules

- Establish the decision or question, scope, current position when relevant, material constraints, and acceptable evidence horizon. Ask only when a missing answer would materially change the research; otherwise state the assumption and proceed.
- Research only claims that could change the answer, choice, requirements, priority, risk treatment, or next action. Existing project artifacts are inputs, not mandatory predecessors.
- Use current web research for external claims whose truth may have changed. Prefer primary and authoritative sources; use secondary analysis to interpret or triangulate. When current verification is unavailable, use supplied evidence where useful, identify what remains unverified, and do not present remembered facts as current.
- Cite evidence beside the claim it supports. Record dates, geography, jurisdiction, versions, configurations, or definitions when they affect interpretation.
- Separate evidence, estimate, inference, assumption, and recommendation. Preserve material conflicts and incompatible definitions instead of averaging them into false certainty.
- Match confidence and output depth to the evidence. A focused answer may remain in conversation; create or update one reusable artifact only when the user requests it or future reuse, breadth, or continuity earns it.
- When writing a durable artifact, use [the convention-resolution rules](../organise-docs/references/convention-resolution.md), reuse an existing report for the same scope, and use a bundled template only when it improves the result.
- Stay inline while the evidence surface is manageable. Use at most one read-only `evidence-reader` under `conditional-cost-gated` policy only when a broad or noisy source set would materially crowd the main context. Give it one bounded evidence question and require a compact claim/source/date/limitation return. The main agent owns scope, source choice, synthesis, judgement, and user communication.
- Continue research that can be resolved independently. Pause for the user only when an unresolved jurisdiction, objective, risk tolerance, or trade-off would make the remaining work build on the wrong premise.

Research may create or update its own requested research artifact; beyond that it is report-only. It may recommend a product, architecture, implementation, compliance, or operational change, but it does not silently make that decision or mutation. For broad requests such as “research and implement” or “assess and apply,” finish the research first. If the result determines or materially changes the exact target, mechanism, scope, risk, rollback, or accepted trade-off, present the proposed next action and obtain fresh authority before handing off to the owner that can act.

Keep neighbouring ownership clear: `agent-ux-designer` owns primary user research, prototypes, and usability tests; `agent-pm` owns product scope and commercial decisions; `agent-architect` owns architecture decisions; `agent-dev` owns code changes and investigation of existing defects; and legal, security, privacy, database, and compliance specialists own substantive determinations and controlled records. If a required owner is unavailable, state the boundary and complete only the responsible research.

## Finished result

Lead with the evidence-backed answer or current best decision support. Include the decisive findings, confidence and limitations, practical implications, and unresolved evidence that could change the result. A handoff states the relevant finding, why it matters, supporting evidence, unresolved question, and expected downstream output. Every material recommendation must follow from cited evidence rather than generic advice.
