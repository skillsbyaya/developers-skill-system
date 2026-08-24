# Release Readiness

Decide whether a bounded feature, epic, or release can ship now under its current release contract and evidence. Return `PASS`, `CONCERNS`, or `FAIL`.

## Resolve the candidate and oracle

Resolve the current revision and a bounded release scope from a named release, epic set, feature, changelog, release note, diff, or branch comparison. If exactly one current candidate is obvious, proceed and state the assumption. Ask only when plausible scopes or conflicting sources would change the verdict. Do not turn a feature gate into an unbounded repository audit.

Find what the release should satisfy, in descending precision:

1. an explicit project or candidate release contract and its required gates;
2. story or epic acceptance conditions;
3. PRD, specification, API contract, or other authoritative behaviour source;
4. release note, changelog, or candidate diff; or
5. for brownfield work with no requirements source, inferred user journeys, routes, permissions, and critical actions from the implementation, explicitly labelled lower confidence.

When plausible sources disagree, ask for authority only if the conflict changes the verdict; otherwise record the limitation.

Create a fresh run for the current revision or update a same-run report; never rewrite an old verdict to represent a new candidate. Return the report in the response unless a current convention or supplied path says otherwise.

## Resolve the release contract and risk

Use the project's current release contract first: required checks, acceptance conditions, supported environments, named thresholds, sign-offs, rollout controls, and explicitly accepted exceptions. Apply only requirements that govern this candidate. Do not replace that contract with a generic coverage score or percentage.

For each scoped requirement or critical path, map current evidence as:

- **SUPPORTED** — current evidence establishes the release condition for this candidate.
- **PARTIAL** — some current evidence exists and the material gap is named.
- **UNSUPPORTED** — no current evidence establishes the condition.

Do not guess a mapping when test intent is ambiguous. If the project has no numeric coverage target, do not invent one. Judge sufficiency from the release contract, consequence, reachability, reversibility, and current evidence. Authentication, authorisation, tenant isolation, money, sensitive data, destructive change, migrations, and similarly critical in-scope paths require direct current evidence or the applicable mandatory specialist result even when the project omitted a numeric threshold.

## Confirm current evidence

Run or inspect the smallest project-native test command that genuinely covers the candidate; use the normal full gate for a full release when one exists. Hosted CI may count only when its revision, commands, scope, and actual results match the candidate. Configuration, required-check settings, or an old green run are not results.

Record the command or evidence source, revision, date, outcome, skipped suites, unavailable services, and important environment differences. If required tests cannot run or be inspected, `PASS` is unavailable.

For exposed critical paths, require current evidence that the applicable controls work. This can include endpoint authentication, authorisation and tenant isolation, input validation, migration safety and rollback, dependency vulnerability results, or the relevant specialist result. Check for evidence; do not pretend this gate replaces a security, database, privacy, legal, or compliance specialist. Missing mandatory critical-path evidence blocks `PASS`.

Apply stated non-functional thresholds from current project or release sources. Never invent latency, availability, accessibility, browser, or other targets; mark an unstated material target `UNKNOWN` and name what is needed.

## Decide the gate

| Verdict | Condition |
| --- | --- |
| **PASS** | Applicable release-contract gates and current tests pass; required critical-path evidence is present; and no blocking defect, mandatory gap, or unaccepted release risk remains. |
| **CONCERNS** | Mandatory gates pass, but bounded non-blocking evidence gaps or release risks remain and each has an explicit mitigation or acceptance decision. |
| **FAIL** | An applicable mandatory gate or relevant test fails or is unavailable, required critical-path evidence is missing, or a blocking defect or release risk remains. |

When uncertainty concerns a mandatory gate, current test result, or critical-path evidence, choose the more conservative verdict. Never report unrun checks as green.

Report the revision and scope, release contract and oracle sources, test evidence, requirement and critical-path support, gaps, limitations, and accepted risks. Send test gaps to testing, implementation gaps to technical or specialist review, and planning gaps to their owner. After a fix, rerun only the affected gate plus any integrated check the change invalidated; this verdict controls shipping, not completion.
