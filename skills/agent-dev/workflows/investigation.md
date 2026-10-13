# Investigation

Use this workflow to diagnose a software defect or incident, trace a root cause, or build a reliable mental model of unfamiliar code.

## Establish the question and state

Start from the user's symptom, ticket, logs, diagnostic material, code area, recent change, or existing investigation record. Define the decision the investigation must enable and bound the relevant system, environment, revision, and time window. Treat the user's explanation as a hypothesis until the evidence supports it.

Resume an existing investigation record when one clearly owns the case. If it is concluded and no new evidence or question changes the case, surface the current conclusion rather than repeating the investigation.

Create a durable case file only when multi-session continuation, broad or changing evidence, incident recovery, future handoff, or an explicitly requested report makes it useful. Otherwise investigate inline. Use a user-supplied path first, then the project's document conventions. If neither resolves a location, choose and report a suitable path; ask only when placement affects ownership or access. For a new case file, read [Investigation case template](../references/investigation-case-template.md); do not create a record merely to prove that investigation occurred.

## Grade and map the evidence

Use three grades consistently:

- **Confirmed:** directly observed in code, tests, logs, configuration, runtime output, version control, or another authoritative source. Cite a path and line, timestamp, revision, or exact source where practical.
- **Deduced:** follows from confirmed evidence. Show the causal chain and the assumptions it depends on.
- **Hypothesized:** plausible but unconfirmed. State what would confirm or refute it.

Anchor in one confirmed stronghold before expanding: a reproducible failure, exact error, failing test, route, function, state transition, configuration value, log event, or observed output. If none is reachable, state that the case is evidence-light and identify the smallest evidence that would materially distinguish the leading explanations.

Map the available perimeter before deep reading: supplied evidence, relevant source and tests, configuration and environment, recent changes, logs or runtime signals, and external systems at the boundary. Mark material sources available, partial, stale, conflicting, or missing. Run independent read-only searches in parallel when useful.

Keep evidence inspection inline unless one bounded source is large, noisy, generated, or would materially crowd the main context. One clean-context read-only worker may inspect that source only when its tool and mutation boundary can be enforced. Give exact paths or time ranges and one evidence question; require citations, uncertainty, and missing inputs. The main investigator owns scope, hypotheses, grading, durable state, and conclusions. If the boundary is unavailable, inspect a manageable slice inline and expose the remaining gap.

## Trace what matters

For a defect or incident:

1. Reproduce or locate the earliest reliable symptom.
2. Trace backward through the producing call path, data flow, state transitions, configuration, and system boundaries.
3. Reconstruct timing when order, concurrency, deployment, or environmental change may matter.
4. Identify the lowest supported cause that explains the observed behaviour, not merely the nearest failing line.
5. Actively seek evidence that would refute the leading explanation before calling it confirmed.

For unfamiliar-code exploration:

1. Start from the entry point or user goal rather than surveying the whole repository.
2. Map triggers and inputs, outputs and side effects, important dependencies, control flow, state ownership, error paths, and external boundaries.
3. Follow only the branches needed for the requested mental model.
4. Name important invariants, extension points, hazards, and unknowns without turning exploration into speculative redesign.

Update or discard a working theory when evidence contradicts it. In a durable case file, retain materially useful refuted hypotheses with their resolution so later work does not repeat the same dead end.

## Conclude and continue when authorised

Finish when the root cause is confirmed; the best explanation is bounded by a clear evidence gap; the requested code-area model is sufficient; or no available evidence can responsibly advance the case.

For an investigation-only result, report the conclusion, supporting causal evidence, material uncertainty and smallest next step. Link the case file when one exists. When continuing into an authorised fix, give only the conclusion and plan needed before implementation.

When evidence supports a fix, show the bounded change, material trade-offs and verification. A request to fix authorises diagnosis and implementation within that scope; continue into the appropriate delivery workflow without asking again. Ask only when the fix requires an unresolved consequential choice, expands the requested outcome, or needs explicit permission under project policy. Restoring agreed behaviour or copy does not itself create a new decision. For exploration-only requests, return the conclusion without implementing a fix.

Use reversible local instrumentation and diagnostic tests within the authorised investigation. Preserve unrelated work and remove temporary instrumentation when finished. Production changes, destructive diagnostics, schema changes and external effects remain subject to project permissions. Insufficient evidence calls for further diagnosis or a named evidence gap, not a request to approve an unsupported fix.

Reuse settled investigation evidence in delivery. Authorisation for diagnosis does not imply permission to deploy or perform other separately gated actions.
