# SaaS Assurance Frameworks

Read this reference for a customer-ready SaaS baseline, SOC 2 readiness, ISO/IEC 27001-aligned readiness, certification preparation, or another broad SaaS assurance assessment. For a focused control check, read it only when a framework claim or broader domain cross-check is material.

Use it as a domain and evidence guide, not as licensed criteria, legal advice, an auditor's scoping judgement, or proof of conformity. Verify current editions, amendments, terminology, licensing, and formal expectations before making a consequential framework claim.

## Primary anchors

- [AICPA & CIMA SOC suite](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services): SOC services are CPA assurance offerings concerning system-level controls. SOC 2 reporting concerns controls relevant to Security, Availability, Processing Integrity, Confidentiality, or Privacy. Use the current AICPA criteria and description guidance for a formal engagement.
- [ISO/IEC 27001](https://www.iso.org/standard/27001): the requirements standard for establishing, implementing, maintaining, and continually improving an information security management system. Check the current edition and amendments, and use a licensed copy for conformity or certification work.
- [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/cyber-assessment-framework): an outcome-led cyber security and resilience framework primarily designed for essential services and other vital functions. It is a useful resilience cross-check for ordinary SaaS, but do not claim CAF conformance without an applicable profile, scope, and competent assessment.
- [Cloud Security Alliance Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix): a cloud-control and shared-responsibility cross-check. Verify the current version and licensing before reproducing, adapting, or commercialising detailed controls or mappings.

## Framework lenses

### SOC 2 readiness

Treat Security as the common foundation and add Availability, Processing Integrity, Confidentiality, or Privacy only when service commitments, customer needs, and the appointed CPA firm's scope justify them.

Define the system boundary clearly: services, infrastructure, software, people, procedures, data, subservice organisations, and complementary user-entity responsibilities. Readiness assesses whether controls are suitably designed and whether credible evidence exists for their operation. It does not produce a SOC 2 report.

Have the appointed CPA firm confirm the current criteria, report type, categories, system-description boundary, as-of date or period, materiality, sampling, subservice treatment, and evidence expectations. Do not promise sufficiency, timing, or report language from shorthand alone.

### ISO/IEC 27001-aligned readiness

Assess the management system as well as selected controls:

- organisational context, interested parties, and scope;
- leadership, policy, accountability, and objectives;
- risk criteria, assessment, treatment, and applicability decisions;
- competence, awareness, communication, and controlled information;
- operational control;
- monitoring, internal audit or evaluation, and management review; and
- corrective action and continual improvement.

Select controls because risk treatment requires them. Keep risks, treatment decisions, controls, evidence, exclusions, and review visible. Formal conformity and certification require the applicable licensed standard and competent independent assessment.

### Cross-check lenses

Use the NCSC CAF to challenge governance, asset and risk management, supply chain, protection, detection, response, recovery, and lessons learned. It is outcome-led and should not be reduced to a checklist.

Use the CSA CCM to challenge cloud shared responsibility, provider and customer control ownership, cloud-specific security coverage, and evidence gaps. Do not copy its control catalogue into a new internal framework when a smaller risk-led control set is sufficient.

## Shared SaaS control domains

Assess each domain once, then tag the relevant framework lenses.

| Domain | Questions that expose material gaps | Strong evidence examples |
| --- | --- | --- |
| Governance and scope | Who is accountable? What service, data, environments, commitments, and exclusions are covered? How are risk decisions reviewed? | Approved scope, ownership, objectives, risk decisions, management review |
| Assets and data lifecycle | Are systems, repositories, endpoints, data classes, flows, retention, and deletion known and controlled? | Inventories, data flows and classification, retention and deletion results |
| Identity and access | Is access least-privilege, MFA-protected, joiner/mover/leaver controlled, and periodically reviewed? | Identity configuration, access tickets, review samples, deprovisioning evidence |
| Secure engineering and change | Are changes reviewed, tested, approved, traceable, and separated appropriately? Are secrets and dependencies managed? | Pull requests, CI evidence, change and deployment records, scanning and remediation |
| Infrastructure and configuration | Are environments separated, securely configured, patched, and checked against owned baselines? | Infrastructure as code, configuration checks, patch records, cloud findings |
| Application and database security | Are tenant boundaries, authorisation, inputs, APIs, privileged functions, and database controls inspected? | Threat models, specialist security tests, code review, database-security results |
| Vulnerability management | Are assets tested, findings exposure-ranked, fixes tracked, and exceptions time-bound? | Scan or penetration-test scope and results, remediation, exception approvals |
| Logging, monitoring, and detection | Are security events captured, protected, reviewed, and tested against alert and investigation expectations? | Logging configuration, alert tests, investigations, retention evidence |
| Incident response | Can the organisation detect, classify, contain, communicate, recover, learn, and meet duties? | Response plan, contact paths, exercises, incident records, tracked lessons |
| Availability, backup, and recovery | Do promises match architecture? Are backups protected and restores or recovery assumptions tested? | Service objectives, monitoring, restore tests, continuity exercises |
| Suppliers and cloud responsibility | Are critical suppliers identified, risk-reviewed, contracted, monitored, and exitable? Is shared responsibility assigned? | Supplier register, due diligence, contracts, assurance evidence, exit tests |
| Confidentiality, privacy, and commitments | Are classification, encryption, disclosure, deletion, and privacy promises implemented consistently? | Contracts, encryption and key evidence, privacy records, request and deletion samples |
| People security | Are screening where justified, terms, onboarding, training, acceptable use, offboarding, and disciplinary routes proportionate? | Signed terms, training, onboarding and offboarding samples |
| Physical and endpoint security | Are remote work, devices, offices, and inherited datacentre controls addressed? | Device management, encryption, endpoint compliance, provider assurance |
| Assurance and improvement | Are controls measured, exceptions corrected, evidence retained, and learning fed into risk treatment? | Metrics, internal reviews, corrective actions, management review, evidence index |

## Proportional baseline

For a small SaaS provider, a credible control often means one accountable owner, one clear rule, one reliable implementation, and one dated proof per material risk, not a committee or policy library. Scale formality when customer commitments, headcount, privileged access, data sensitivity, incident history, regulated use, or certification goals justify it.

Do not weaken essentials merely because the organisation is small. Privileged-access MFA, prompt offboarding, tenant and data access control, recoverable backups where availability matters, vulnerability remediation, incident ownership, critical-supplier visibility, and honest customer commitments need working controls and evidence.
