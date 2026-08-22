# Architecture Consultation

Use this workflow when architecture judgement is the finished result: comparing designs, choosing a stack or integration approach, challenging overbuild, translating accepted product intent into technical constraints, or deciding whether a durable architecture record is justified.

## Frame the decision

1. State the technical decision and the outcome it must support.
2. Establish the current system or proposed scope, accepted product, UX, and UI/design-system intent, quality attributes, constraints, evidence, and existing commitments. Inspect supplied or clearly relevant project artifacts when they could change the answer.
3. Identify the smallest uncertainty that could reverse the choice. Ask one focused question only when it is material; otherwise state the assumption.
4. Compare the viable options against only the relevant concerns: delivery and cognitive complexity, reliability and failure recovery, security and data boundaries, integration, operability and observability, performance and scale, cost, migration, testability, and reversibility.
5. Recommend one option. Name the strongest alternative, why it loses under current conditions, and the signal that would make it better.

Challenge speculative scale, premature service boundaries, unnecessary custom infrastructure, and abstractions justified only by imagined reuse. Prefer a boring, supported choice when it satisfies the decision better; do not confuse familiarity with suitability or novelty with progress.

## Make the recommendation actionable

State the constraints the decision creates where material:

- component, service, data, trust, and ownership boundaries;
- interfaces, contracts, consistency, and dependency direction;
- failure handling, retries, idempotency, degradation, and recovery;
- migration, compatibility, rollout, and rollback;
- observability, operations, security, privacy, and cost controls; and
- test seams, evidence needs, and decisions that may safely remain deferred.

Do not produce an exhaustive project structure or generic best-practice catalogue when the decision does not need one.

## Finish

Return the recommendation, rationale, credible alternative, assumptions, implementation constraints, risks, deferred decisions, and reversal condition. Consultation is advisory and does not edit architecture artifacts or implementation.

If a durable record is now warranted, offer a compact handoff containing the decision scope, recommendation, evidence, constraints, unresolved choices, and affected current artifact. Do not start the architecture-decisions workflow without the user's request.
