# Obligations and Compliance Register

Create and maintain the project's canonical compliance register linking obligations, risks, controls, operating evidence, exceptions, and accepted risk.

## Select the operation

- **Plan:** establish the applicable obligation and control set for a new product, process, jurisdiction, contract, or material change.
- **Update:** add or change supported entries after new advice, regulation, implementation, evidence, incident, or risk acceptance.
- **Reconcile:** repair stale, duplicated, contradictory, orphaned, or one-way links.
- **Review:** assess whether entries remain current, owned, evidenced, and proportionate without rewriting sound content.

An explicit register request selects this workflow directly. A broad missed-risk assessment belongs to compliance consultation; a question about what changed belongs to the regulatory horizon scan. Use their conclusions as evidence instead of repeating them.

## Establish authority and scope

Resolve the `compliance-register` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md), then inspect the existing register before creating anything. Maintain one canonical project register. This workflow is its sole structural writer; other workflows may supply bounded, source-backed changes.

Establish the product, process, jurisdiction, affected people, data or safety exposure, contractual commitments, business model, current controls, evidence horizon, and decision that the register must support. Verify consequential legal or regulatory propositions against current primary official sources. Do not convert a possibility into an obligation merely because it appeared in a checklist or horizon scan.

If legacy obligation, risk, control-evidence, or accepted-risk registers exist, preserve their supported content, identifiers, and decision history while consolidating them into the canonical register. Do not leave competing live sources of truth.

Resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry when durable typed IDs are in use. Preserve existing and legacy identities. Apply the preferred no-dash grammar only when an authoritative project allocator or approved key set supplies the numbers; this workflow does not infer or store the next number.

## Maintain the linked model

Use stable typed identifiers that survive wording and ordering changes: `OB7.Invoicing` for an obligation, `RK4.Invoicing` for a risk, `CT9.Invoicing` for a control, and `EV12.Invoicing` for an evidence item. Preserve existing valid identifiers and accepted-risk history; do not renumber entries to make the document look tidy.

- **Obligation:** source, jurisdiction, status, applicability, accountable owner, effective date or deadline, and review trigger.
- **Risk:** exposure, affected people or commitments, likelihood and impact, current treatment, residual risk, and owner.
- **Control:** outcome, implementation owner, dependencies, operating cadence or trigger, exception path, and verification.
- **Evidence:** artifact or query location, scope, period or date, result, exceptions, and freshness rule.
- **Decision or acceptance:** exact risk accepted, rationale, decision owner, date, expiry or review trigger, and superseding decision when applicable.

Every material relationship must work in both directions: obligations point to their risks and controls; risks point to treatment and acceptance; controls point to evidence; evidence identifies the control and scope it supports. Do not duplicate a privacy record, assurance report, legal note, technical artifact, or incident record inside the register. Link to the authority and retain only the decision-sized fact needed to operate the model.

## Quality and lifecycle

1. Reuse current scope-matched applicability findings, legal advice, horizon-scan entries, assurance reports, specialist audits, policies, technical records, incidents, and accepted decisions.
2. Distinguish currently in-force obligation, regulator guidance, contractual commitment, assurance expectation, proposed change, and internal recommendation.
3. Rank unresolved work by plausible exposure and deadline, not document completeness.
4. Keep one accountable owner per obligation, control, evidence action, and accepted risk. A team name is acceptable only when responsibility is operationally clear.
5. Remove an entry only when it is demonstrably inapplicable, superseded, transferred to another canonical authority, or no longer needed. Preserve the reason and any continuing evidence obligation.
6. Mark uncertainty explicitly. Missing evidence means unverified, not automatically ineffective; a policy or configured tool does not prove operation.
7. End every material entry with a concrete review trigger such as legal commencement, product change, incident, contract renewal, control exception, evidence expiry, or owner change.

Use lifecycle states appropriate to the entry type, such as applicable or superseded for obligations; open, accepted, mitigated, or closed for risks; and planned, operating, ineffective, or retired for controls. A status change must follow evidence or a recorded decision, not elapsed time alone.

## Finished result

Return the register path, operation performed, scope, material additions or corrections, highest-priority open exposures, decisions or specialist conclusions still needed, stale or missing evidence, and next review triggers. Do not silently implement controls or accept risk on the user's behalf.
