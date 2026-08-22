# SaaS Assurance Readiness

Turn a concrete SaaS trust or assurance demand into an evidence-backed readiness verdict and the smallest credible improvement path. Assess the security programme across people, process, suppliers, technology, and operating evidence without claiming certification or attestation.

## Start from the live need

Establish from available context:

- the customer, contract, procurement, diligence, launch, incident, regulated-user, SOC 2, ISO/IEC 27001, or other assurance trigger;
- the service and system boundary, environments, users, data, locations, subprocessors, and shared responsibilities;
- customer promises and security, availability, confidentiality, integrity, and privacy commitments;
- privileged access and the boundaries of identity, endpoints, infrastructure, code, data, support, and operations;
- the requested framework or assurance form, reviewer, deadline, scope period, and current controls and evidence.

Ask only for facts that materially change the target or verdict. A questionnaire may reveal the assurance demand or supply evidence, but do not confuse item-by-item completion with a readiness assessment. If no concrete external or operational need emerges, give a short proportional baseline and stop.

## Select the target

- **Focused assurance check:** one trust commitment or control domain is blocking a contract, launch, diligence request, or decision. Inspect it and directly affected dependencies only.
- **Customer-ready baseline:** an enterprise relationship or recurring diligence need requires an overall defensible security posture.
- **SOC 2 readiness:** the organisation is preparing for a SOC 2 examination or a customer explicitly requires a report.
- **ISO/IEC 27001-aligned baseline:** the organisation wants a risk-led information security management system or recognised security posture without claiming current conformity.
- **Certification preparation:** formal ISO/IEC 27001 certification is intended. Treat the internal assessment as an initial gap view and require the current licensed standard plus an accredited certification route.

For a customer-ready baseline, SOC 2, ISO/IEC 27001, certification, or other broad assessment, read [SaaS assurance frameworks](../references/saas-assurance-frameworks.md). For a focused check, load it only when a framework claim or broader control-domain cross-check is material.

Use one risk-led control set with framework lenses rather than duplicate programmes. Do not claim an exact cross-framework mapping unless it comes from a current authorised source or the appointed assessor confirms it.

## Assess design and operation

1. Reuse current scope-matched project context, applicability findings, assurance reports, architecture, vendor evidence, security records, and compliance register entries. Flag stale, contradictory, or scope-mismatched material.
2. Verify the current framework edition, amendments, formal terminology, and scoping expectations from primary official sources when the requested verdict depends on them.
3. Write a compact scope statement covering trigger, boundary, people, data, subprocessors, commitments, exclusions, target, deadline, assumptions, and customer or user responsibilities.
4. Assess the domains required by the target. For each applicable control, inspect:
   - **design:** accountable owner, rule, process, technical implementation, dependencies, and intended evidence; and
   - **operation:** dated, scope-matched evidence that the control actually happened and exceptions were handled.
5. Classify the result as:
   - material control gap;
   - control exists but operating evidence is missing or too immature;
   - evidence exists but scope, ownership, or consistency is unclear;
   - not applicable, with reason; or
   - verified effective for the inspected scope and period.
6. Rank material gaps by real exposure and assurance-blocking effect. For each, state the affected commitment or domain, current evidence, impact, minimum credible control, stronger option when useful, trade-off, owner, evidence to retain, verification, and dependency.
7. Give one readiness verdict:
   - **Not ready:** one or more material control blockers make the stated assurance goal irresponsible.
   - **Foundation:** material basics are being established, but several controls or owners remain incomplete.
   - **Evidence-building:** material controls appear designed, but operating evidence is not yet sufficient or consistent.
   - **Ready for external scoping:** no known material blocker remains for the inspected scope and a qualified external assessor can confirm criteria, period, sampling, and sufficiency.

“Ready for external scoping” is not audit-ready, certified, or guaranteed to pass. Only the appropriately qualified independent provider can issue the formal report, certification, or attestation.

## Evidence standard

- Prefer native dated evidence: access reviews, joiner/mover/leaver records, tickets and approvals, pull requests and deployment records, logs and alert tests, backup and restore results, incident exercises, supplier reviews, training completion, vulnerability remediation, risk decisions, and management review.
- Evidence must identify or reveal scope, date or period, owner, result, exceptions, and follow-up. Redact secrets and unnecessary personal data.
- Separate implementation evidence from operating evidence. A policy, screenshot, configured tool, or compliance-platform badge rarely proves consistent operation.
- Trace every material commitment to a control, owner, evidence, review cadence, and exception path. Reuse one artifact across lenses; do not duplicate it to inflate coverage.
- A compensating control or accepted exception needs the risk, rationale, owner, expiry or review trigger, and evidence that it works.

## Boundaries, handoff, and output

This workflow assesses readiness and may create or update the scope-matched assurance report after resolving the `assurance-audit` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md). It does not issue legal advice, perform an attestation, certify conformity, reproduce licensed standards, guarantee an auditor's conclusion, fill a questionnaire with unsupported claims, or silently change controls.

Select this owner's UK data-protection advice or records workflow directly when substantive privacy judgement or a named privacy record is needed. Select its database access-control audit for live database inspection and its obligations-register workflow for canonical obligation, risk, control, evidence, or accepted-risk entries. Route architecture changes to `agent-architect` and application or infrastructure implementation to `agent-dev`.

Lead with the live need and readiness verdict. Then give scope and assumptions, material blockers in priority order, domain coverage, evidence already usable, the improvement path tied to the deadline when timing matters, external decisions and specialist handoffs, limitations, and the exact evidence required for recheck. Keep the main response decision-sized; draft a policy or procedure only when a named gap needs it and the user separately requests that mutation.
