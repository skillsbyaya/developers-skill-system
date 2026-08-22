# Worker Use in Skills

Read this reference only when creating, auditing, editing, repairing, or restructuring worker or subagent behavior.

Use the minimum workers justified by at least one of these conditions:

- an enforced capability or safety boundary;
- genuinely fresh independent judgement required by the assurance question;
- a supported whole-task context benefit for bounded noisy work; or
- an explicitly requested optional perspective.

Parallelism, sophistication, or assumed token savings are not sufficient reasons. Worker output still consumes integration context.

For each worker define the distinct decision or bounded result it owns, the evidence and files it may receive, the tools and mutations it may use, the expected compact return, and the condition for accepting or rejecting its result. Enforce safety and capability limits through actual execution context, permissions, tool availability, or isolation—not prompt claims.

The main owner retains scope, integration, user decisions, durable state, mutations outside the worker's enforced boundary, and final communication. It validates returned findings against the current revision and does not duplicate the full worker task inline without a concrete reason.

Use another worker only for a second distinct uncertainty, not a general desire for confidence. If the required independence or safety boundary cannot be enforced, work inline only when that still satisfies the control; otherwise name the missing evidence or capability and stop before claiming completion.
