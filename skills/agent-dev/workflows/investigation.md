# Investigation

Use this workflow to diagnose a software defect or incident, trace a root cause, or build a reliable mental model of unfamiliar code.

## Establish the question and state

Start from the user's symptom, ticket, logs, diagnostic material, code area, recent change, or existing investigation record. Define the decision the investigation must enable and bound the relevant system, environment, revision, and time window. Treat the user's explanation as a hypothesis until the evidence supports it.

Resume an existing investigation record when one clearly owns the case. If it is concluded and no new evidence or question changes the case, surface the current conclusion rather than repeating the investigation.

Create a durable case file only when multi-session continuation, broad or changing evidence, incident recovery, future handoff, or an explicitly requested report makes it useful. Otherwise investigate inline. Use a user-supplied path first, then the project's document conventions. If neither resolves one clear location, ask before creating the record. For a new case file, read [Investigation case template](../references/investigation-case-template.md); do not create a record merely to prove that investigation occurred.

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

## Conclude without fixing

Finish when the root cause is confirmed; the best explanation is bounded by a clear evidence gap; the requested code-area model is sufficient; or no available evidence can responsibly advance the case.

Return:

- the conclusion and confidence: **High** for a confirmed cause with deterministic evidence, **Medium** for a well-supported deduction with limited uncertainty, or **Low** for a bounded hypothesis;
- confirmed findings, deductions, and unresolved hypotheses with citations;
- the causal trace or code-area model;
- material contradictions, ruled-out explanations, and missing evidence;
- reproduction, diagnostic, or verification steps where useful;
- the smallest credible fix direction or implementation constraints, without editing production code; and
- the case-file path and exact continuation boundary when durable state exists.

When the conclusion supports a mutation, present the specific proposed change, its material scope, important risks or trade-offs, expected verification, and any remaining uncertainty. Then stop and ask the user whether to implement that diagnosed fix. This confirmation is required even when the original request said “investigate and fix,” because the actual change was not known when that request was made. Do not select delivery or mutate project state before the user confirms the proposed fix. If the requested result is exploration only, no responsible mutation is supported, or the evidence remains too weak to propose one, finish with the report-only result and evidence boundary without prompting for implementation.

Do not present an old check, unsupported theory, or completed procedure as proof. If diagnosis requires new instrumentation or changes to application code, tests, configuration, data, or infrastructure, stop with the smallest proposed diagnostic change and the evidence it would distinguish. Ask for confirmation before performing that mutation through delivery, then return its observations to the investigation. Diagnostic-change approval does not also approve the eventual production fix.

The same hard-stop handoff applies to mitigations, workarounds, tracker mutation, commits, and deployment. After the user confirms the specific next change, select direct, coordinated, staged, or the relevant specialist workflow and reuse settled investigation evidence rather than rerunning it.
