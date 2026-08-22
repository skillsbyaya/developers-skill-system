# Database Access-Control Audit

Inspect Supabase or Postgres access control using current live metadata, policies, grants, and security configuration. Produce evidence-backed findings, a confirmed-safe view, and, when authorised, a bounded hardening migration with post-change verification.

## Establish the audit target

Identify the project and environment, connection or tool boundary, schemas and services in scope, data sensitivity, exposed APIs, application roles, privileged paths, current incidents or concerns, and whether the user wants assessment only, a migration draft, or an already-defined change applied.

Confirm before inspecting production or other consequential environments when the target is not explicit. Use the narrowest available read-only access. Never reveal secrets, credentials, tokens, unnecessary personal data, or sensitive row contents in commands, logs, findings, or reports.

If live inspection is unavailable, state the missing evidence and provide only a bounded review of supplied schema, policy, grant, or migration material. Do not label an uninspected database safe.

For a live Supabase or Postgres audit, read [the database audit queries and checks](../references/database-audit-queries.md) and adapt only the queries relevant to the actual platform and scope.

## Inspect the real enforcement paths

Use available platform advisors and Postgres metadata as leads, not as the whole audit. Inspect the paths relevant to the scope, including:

- schemas exposed through APIs or application connections;
- roles, memberships, login and bypass privileges, default privileges, and direct grants;
- row-level security enablement, forced-RLS needs, policy commands, roles, `USING` expressions, `WITH CHECK` expressions, and interactions between policies;
- ownership and privileged functions, triggers, views, `SECURITY DEFINER`, executable grants, and safe `search_path`;
- service, support, migration, scheduled-job, and administrative access paths;
- storage or platform-specific policies when they share the database authorization model;
- tenant boundaries and whether anonymous, authenticated, service, or internal roles can read or change another tenant's data; and
- auditability, change traceability, and controls around emergency or exceptional access.

Test effective access rather than inferring it from names. A table with RLS enabled can still be exposed by a permissive policy, privileged role, function, view, owner path, or direct grant. A clean advisor result is not proof of correct authorization.

Treat common advisor findings with judgement:

- RLS disabled in an exposed schema is a credible live exposure until the reachable roles and data prove otherwise.
- An always-true or permissive policy is not automatically a defect; state exactly which roles can perform which operation and whether open access is intended.
- A flagged privileged function or view requires source, owner, executable grants, caller binding, and `search_path` inspection before it can be called safe or unsafe.
- Configuration lints such as mutable function paths or extensions in an exposed schema may be hardening rather than immediate data exposure; rank them by reachability and consequence.

## Classify and report

For each material path, classify:

- confirmed unsafe or over-privileged;
- likely unsafe but requiring one named verification;
- correctly restricted for the inspected role and operation;
- intentionally privileged with a supported control and evidence; or
- unresolved because live access, role simulation, or context is missing.

Give each finding the affected object and role, reachable action, evidence, plausible consequence, smallest corrective direction, dependencies, and verification. Include a compact confirmed-safe section for important controls actually checked so the result is not only a defect list.

Resolve the `assurance-audit` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md) for a substantial reusable report. Update the existing report for the same environment and scope rather than creating duplicates.

## Draft or apply hardening

Assessment is report-only by default. A request to “audit and fix” does not authorise an unknown schema change. After inspection, present the exact proposed grants, revocations, RLS changes, policies, function changes, affected roles and operations, compatibility risks, migration and rollback approach, and verification plan. Obtain explicit confirmation before applying any database security change.

When drafting or applying an authorised migration:

1. Prefer the smallest explicit, reviewable, and repeatable change.
2. Preserve required application, support, migration, and recovery paths.
3. Avoid broad grants, role-name assumptions, destructive policy replacement, or disabling RLS as a shortcut.
4. Include safe ordering, transaction boundaries where appropriate, preconditions, and a rollback or forward-fix plan proportionate to the change.
5. Do not modify application code, secrets, general infrastructure, or unrelated schema.

Enabling RLS with no applicable policy creates default-deny behaviour for ordinary access. Pair enablement with the required policies in one reviewed migration. Before tightening a policy, inspect current policy patterns and application access so the fix does not invent an incompatible authorization model.

Confirm one live-data security change at a time unless the changes are inseparable parts of one bounded control outcome. Do not bundle unrelated fixes into a single approval.

After any applied change, rerun the affected metadata and effective-access checks, exercise allowed and denied paths with safe test identities or equivalent evidence, inspect advisors again when available, and report residual risk. A successful migration command without behavioural verification is not completion.

## Finished result

Return the environment and scope, evidence inspected, confirmed-safe controls, findings by exposure, unresolved paths, report or migration location, exact changes applied if any, post-change verification, compatibility limits, and next owner. Route required application or infrastructure changes to `agent-dev` and architecture decisions to `agent-architect`.
