# Technical-Document Validation

Check whether a specified technical document's consequential claims match current repository evidence. This is report-only.

Read the document fully. Identify the code area, version or branch when relevant, and the claims that could affect implementation, operation, onboarding, or review. If the document spans an unbounded system or the authoritative source is unavailable, ask for a bounded scope or state the validation limit.

Check consequential claims about:

- behaviour, control flow, state, and data flow
- interfaces, parameters, requests, responses, errors, and contracts
- configuration, dependencies, permissions, and environmental assumptions
- commands, setup, deployment, recovery, and troubleshooting
- constraints, failure modes, security-relevant behaviour, and change hazards
- tests, verification steps, and claimed coverage

Validate every consequential claim in the agreed scope. Combine repeated instances. Classify a problem as inaccurate, misleading, stale, unsupported, or materially incomplete only when evidence supports it. Preserve uncertainty where an external system, generated artifact, runtime state, or unavailable dependency prevents verification.

Lead with `supported`, `supported with corrections`, `not supported`, or `insufficient evidence`, and state the document and source scope covered. Report findings in priority order with document location, claim, repository evidence, impact, and smallest correction direction. Use exact file paths and stable line references where useful.

Do not broaden into editorial review or rewrite the document. If the user wants corrections, ask which findings to apply through write or revise. Recommend a separate editorial review when reader fitness remains uncertain without implying that it was part of the correctness verdict.

Finish by confirming that every material finding is traceable to inspected evidence, unresolved claims are named, and the verdict does not exceed the scope checked.

