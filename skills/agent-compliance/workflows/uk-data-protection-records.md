# UK Data-Protection Records

Create and maintain the named records that show UK personal-data processing is understood, justified, controlled, and reviewable.

## Select the operation

- **Triage:** decide whether a DPIA, RoPA entry, retention rule, lawful-basis or consent review, or subject-access process is needed. Answer inline unless the user asks to retain the decision.
- **Create or update:** write the requested record or process.
- **Maintain:** update only records affected by a material processing change or review trigger.

An explicit record request selects it directly. Do not require a separate consultation or legal-advice workflow first. Verify current legal claims from official ICO, GOV.UK, or legislation sources when the record depends on them.

## Establish current state

Confirm UK scope and identify the processing activity, data subjects and categories, purpose, sources, recipients and processors, transfers, retention, access, controls, incidents, and evidence relevant to the selected record.

Resolve the matching rows through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md), then inspect existing compliance records before creating anything. Update the existing authority for the same purpose; do not create near-duplicates.

Use the smallest sufficient record set:

- `dpia` for DPIA triage retained by request or a full DPIA;
- `record-of-processing` for the RoPA;
- `retention-schedule` for retention periods, triggers, deletion or anonymisation, and evidence;
- `lawful-basis-consent-review` for lawful basis, consent, notice, capture, and withdrawal choices; and
- `subject-access-process` for SAR/DSAR intake, identity, search, redaction, response, deadlines, and evidence.

## Write a usable record

1. State scope, jurisdiction, processing or change, assumptions, and the decision the record supports.
2. Record source evidence and current official authority where a legal proposition matters.
3. Include only fields needed by the record:
   - DPIA: necessity and proportionality, risks, mitigations, residual risk, consultation, decision, evidence, and review trigger.
   - RoPA: activity, purpose, basis, data and people, recipients and processors, transfers, retention, controls, owner, and review trigger.
   - Retention: category, purpose, period, trigger, deletion or anonymisation, owner, reason, evidence, and cadence.
   - Lawful basis or consent: purpose, basis, notice, capture and withdrawal, alternatives rejected, evidence, and trigger.
   - Subject access: intake, identity, search, exemptions and redactions, response deadline, owner, evidence log, and trigger.
4. Preserve relevant history and unresolved decisions. Add last-reviewed evidence and a concrete next-review or change trigger.
5. Save or update the selected Markdown artifact unless the user asked for chat-only output.

This workflow is the sole writer for these record families. It does not write the general compliance register, change production controls, or implement technical safeguards.

Select this owner's obligations-register workflow for canonical obligations, risks, controls, evidence, or accepted-risk entries; its regulatory horizon scan for ongoing change monitoring; and its database access-control audit for hands-on database inspection. Use the relevant technical owner for application or infrastructure implementation.

Give practical documentation guidance, not legal advice. Flag high-risk, legally unclear, cross-border, or materially harmful processing and recommend qualified advice or ICO guidance.
