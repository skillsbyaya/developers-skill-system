# Investigation: {title}

Use only the sections that improve continuation, evidence review, implementation, or recovery. Keep the record current rather than appending a session diary.

## Case brief

- **Question:** {decision or understanding this investigation must enable}
- **Scope:** {system, environment, revision, and time window}
- **Status:** {active, concluded, or blocked on evidence}
- **Conclusion:** {current evidence-graded conclusion and confidence}
- **Next boundary:** {single unresolved evidence question or recommended action}

## Evidence

| Source | State | Material observation |
| --- | --- | --- |
| {path, log range, test, revision, or other source} | {available, partial, stale, conflicting, or missing} | {observation or gap} |

## Findings

### Confirmed

- {finding with path:line, timestamp, revision, or exact source}

### Deduced

- {conclusion and the confirmed chain supporting it}

### Hypotheses

| Hypothesis | Status | Would confirm | Would refute | Resolution |
| --- | --- | --- | --- | --- |
| {theory} | {open, confirmed, or refuted} | {evidence} | {evidence} | {why the status changed} |

## Causal trace or area model

- **Entry or symptom:** {where the trace begins}
- **Trigger and inputs:** {what initiates the behaviour}
- **Control and data flow:** {important path}
- **State and side effects:** {ownership and mutations}
- **Failure or output:** {how the observed result emerges}
- **Boundaries and dependencies:** {external systems, contracts, and hazards}

## Timeline

Use only when order, concurrency, deployment, or environmental change matters.

| Time or revision | Event | Source | Grade |
| --- | --- | --- | --- |
| {timestamp or revision} | {observed event} | {log, commit, test, or report} | {confirmed or deduced} |

## Remaining evidence

| Gap | Why it matters | Smallest way to resolve it |
| --- | --- | --- |
| {missing evidence} | {decision it blocks} | {collection or check} |

## Recommended direction

{Reproduction, diagnostic, verification, or smallest credible fix direction. Do not record implementation as complete unless a delivery workflow performs and verifies it.}
