# Release Readiness

Decide whether a bounded feature, epic, or release can ship now from current test and critical-path evidence. Return `PASS`, `CONCERNS`, or `FAIL`.

## Resolve the candidate and oracle

Resolve the current revision and a bounded release scope from a named release, epic set, feature, changelog, release note, diff, or branch comparison. If exactly one current candidate is obvious, proceed and state the assumption. Ask only when plausible scopes or conflicting sources would change the verdict. Do not turn a feature gate into an unbounded repository audit.

Find what the release should satisfy, in descending precision:

1. story or epic acceptance conditions;
2. PRD, specification, API contract, or other authoritative behaviour source;
3. release note, changelog, or candidate diff; or
4. for brownfield work with no requirements source, inferred user journeys, routes, permissions, and critical actions from the implementation, explicitly labelled lower confidence.

When plausible sources disagree, ask for authority only if the conflict changes the verdict; otherwise record the limitation.

Create a fresh run for the current revision or update a same-run report; never rewrite an old verdict to represent a new candidate. Return the report in the response unless a current convention or supplied path says otherwise.

## Map coverage and risk

For each scoped requirement, map current tests as:

- **FULL** — all expected behaviours are covered;
- **PARTIAL** — some behaviours are covered and the named gaps remain; or
- **NONE** — no current test maps to it.

Do not guess a mapping when test intent is ambiguous. Score probability of failure and impact from 1–3 and multiply them, then assign:

| Priority | Entry | Required coverage |
| --- | --- | --- |
| P0 | Score 6–9, or any exposed authentication, authorisation, tenant isolation, money, sensitive-data, destructive-change, or migration path | 100% |
| P1 | Score 4–5 or a core journey | At least 90% |
| P2 | Score 2–3 or secondary behaviour | About 50% |
| P3 | Score 1, cosmetic, or rarely used | Smoke evidence |

## Confirm current evidence

Run or inspect the smallest project-native test command that genuinely covers the candidate; use the normal full gate for a full release when one exists. Hosted CI may count only when its revision, commands, scope, and actual results match the candidate. Configuration, required-check settings, or an old green run are not results.

Record the command or evidence source, revision, date, outcome, skipped suites, unavailable services, and important environment differences. If required tests cannot run or be inspected, `PASS` is unavailable.

For exposed P0 paths, require current evidence that the applicable controls work. This can include endpoint authentication, authorisation and tenant isolation, input validation, migration safety and rollback, dependency vulnerability results, or the relevant specialist result. Check for evidence; do not pretend this gate replaces a security, database, privacy, legal, or compliance specialist. Missing required P0 evidence blocks `PASS`.

Apply stated non-functional thresholds from current project or release sources. Never invent latency, availability, accessibility, browser, or other targets; mark an unstated material target `UNKNOWN` and name what is needed.

## Decide the gate

| Verdict | Condition |
| --- | --- |
| **PASS** | P0 is 100%; P1 is at least 90%; relevant current tests are green; no critical security, isolation, migration, or other mandatory gap exists; and no P0 evidence is missing. |
| **CONCERNS** | P0 is 100%; P1 is 80–89%, or only minor gaps remain with explicit mitigation and acceptance. Shipping requires acceptance of each listed risk. |
| **FAIL** | P0 is below 100%; P1 is below 80%; relevant tests fail or are unavailable; or a critical security, data-isolation, migration, or other mandatory gap exists. |

When uncertainty concerns P0/P1 coverage, current test results, or critical-path evidence, choose the more conservative verdict. Never report unrun checks as green.

Report the revision and scope, oracle sources, test evidence, coverage by priority, gaps, critical-path evidence, limitations, and accepted risks. Send test gaps to testing, implementation gaps to technical or specialist review, and planning gaps to their owner. After a fix, run the affected gate again; this verdict controls shipping, not completion.
