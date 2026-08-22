# Testing Consultation

Use this workflow when testing judgement is the finished result: choosing a strategy, allocating coverage across levels, resolving the oracle, interpreting systemic suite signals, or deciding what evidence would be sufficient.

## Frame the decision

1. State the behaviour, system, change, or quality concern and the decision it needs.
2. Establish the expected outcome or oracle, current architecture and implementation state, affected users or data, current tests and quality signals, constraints, and evidence gaps. Inspect supplied or clearly relevant project artifacts when they could change the recommendation.
3. Rank credible failure modes by likelihood and impact. Separate critical paths from routine behaviour rather than spreading equal effort everywhere.
4. Choose the lowest useful evidence for each important risk:
   - unit or component tests for isolated logic and rendering behaviour;
   - integration tests for boundaries between real components, stores, queues, or services;
   - API or contract tests for business rules, permissions, schemas, and service behaviour;
   - end-to-end tests for a small number of critical journeys whose value depends on the assembled system;
   - specialist, operational, or non-functional evidence only where the exposure earns it.
5. Assign priorities such as P0-P3 when ordering matters. Name deliberate omissions, why they are acceptable, and the signal that would require deeper coverage.
6. Define what would count as enough evidence for the current decision. Do not substitute a raw test count or coverage percentage for risk-matched confidence.

Challenge a plan that tests only the easiest layer, duplicates the same claim across several levels, ignores an untrusted flaky suite, or applies a heavyweight pyramid without regard to the system.

## Make the result actionable

Return:

- scope and oracle;
- ranked risks and critical failure modes;
- recommended scenarios or evidence by level and priority;
- deliberate omissions and relevant non-functional evidence;
- existing evidence that can be reused;
- the sufficiency condition, assumptions, and material gaps; and
- the next testing operation, if one is actually needed.

Consultation may finish with advice or a compact test strategy. It does not edit test files, configuration, delivery state, or durable artifacts.

For a combined strategy-and-implementation request, state the proposed operational route, bounded repository scope, expected edits, dependency or deletion implications, verification, and unresolved choices. Continue without another confirmation only when those exact material changes were already established and authorised before consultation; otherwise stop for fresh authority, then select the test-system or ATDD workflow.
