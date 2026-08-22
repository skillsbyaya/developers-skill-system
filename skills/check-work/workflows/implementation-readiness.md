# Implementation Readiness

Decide whether the current planning set is coherent enough for implementation to start, not whether completed work can ship.

## Resolve scope and sources

Identify the initiative, feature, epic set, or other bounded planning scope and the current sources that govern it. Inventory relevant requirements or PRD, UX or journeys, UI or design-system decisions, architecture and technical constraints, epics and stories, delivery sequence, matching entries from recorded-decision and known-defect registers, and test strategy or evidence expectations. Group sharded sources, detect competing whole and sharded versions, and resolve the authoritative set before comparing it. Read every selected source completely; do not infer coverage from filenames, indexes, or summaries. Do not require an artifact merely because it is conventional; record it as absent only when the scoped work needs the decision it should contain.

When the scope is expressed as one canonical project area rather than an explicit source set, resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry. Use the exact dotted area segment to route candidate current IDs across requirements, decisions, architecture, delivery, reviews, and risks; triage out archived, superseded, and false-positive matches, then read every selected authoritative source completely as required above. Follow cross-area dependencies and treat missing suffixes as discoverability gaps rather than proof that a source is irrelevant.

Prefer current authoritative artifacts over summaries. When duplicate or conflicting sources exist, name the exact incompatible claims. Ask the user to choose an authority only when the conflict changes the verdict and cannot be resolved from established ownership or recency; otherwise proceed and record the limitation. Existing accepted decisions are fixed unless current evidence materially contradicts them.

Update an existing readiness report for the same scope when it is clearly current; otherwise return the report in the response or use a supplied path.

## Test readiness

### Requirements and traceability

- Each in-scope outcome and constraint is specific enough to implement and verify.
- Requirements map to epics or stories and acceptance conditions without unexplained gaps, duplication, or scope leakage.
- Exclusions, assumptions, user-owned choices, and source conflicts that could change delivery are explicit.

### Experience and architecture alignment

- Required user journeys, roles, permissions, states, errors, recovery, and accessibility needs appear in implementable work when relevant.
- Architecture, interfaces, data rules, security/privacy constraints, non-functional requirements, and operational needs are reflected in stories or deliberate cross-cutting work.
- UX, UI/design-system, requirements, and architecture do not make incompatible claims about the same behaviour or presentation.

### Epic, story, and sequence quality

- Stories are bounded, vertically useful where appropriate, and have observable acceptance conditions.
- Dependencies, migrations, enabling work, external decisions, and critical ordering are visible; the proposed sequence does not require unavailable work or create avoidable rework.
- Technical enabling work has a user, security, operational, or dependency rationale; schema and infrastructure appear when first needed unless a deliberate earlier foundation is justified. Greenfield setup, brownfield integration, compatibility, and migration work appear when the scoped delivery requires them.
- Material and critical risks have a credible evidence plan. A test framework is not a test strategy; flag unresolved strategy decisions for specialist review.

Build a traceability view only as detailed as needed to expose gaps. Every finding must cite its source or precise absence, state the consequence, and identify the affected artifact or decision.

## Verdict and report

Use one verdict:

- **READY** — the planning set is mutually consistent, required work and decisions are covered, dependencies are safe, and no unresolved finding would make responsible implementation materially uncertain.
- **NEEDS WORK** — implementation can begin only within named limits or after accepting bounded risks that do not invalidate the plan.
- **NOT READY** — a missing decision, contradiction, coverage gap, unsafe sequence, or absent critical evidence would make implementation irresponsible or predictably rework-heavy.

Report the scope and sources, verdict, requirements traceability, conflicts, dependency and sequence issues, story-readiness findings, limitations, and required corrections. Use a coverage matrix when prose would hide gaps, including requirements without implementation coverage and claimed work without an authoritative source. This verdict neither starts implementation nor completes delivery.
