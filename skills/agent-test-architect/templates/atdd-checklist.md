---
documentType: atdd-checklist
scope: "{story key or feature}"
status: "{red-verified | red-unverified}"
updated: "{date}"
sources: []
---

# ATDD Checklist: {story key or feature}

## Acceptance criteria

1. {criterion}

## Red-phase scaffolds

| Test | File | Level | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- |
| {test name} | {path} | {level} | {P0-P3} | {criterion} |

## Fixtures and factories

- `{path}`: {purpose, overrides, and cleanup}

## Mocks and interfaces

- {service or interface}: {required endpoint, contract, success response, and failure response}

## Required UI hooks

- `{data-testid}`: {element and screen or component}

## Implementation sequence

### {test name}

- [ ] Activate the scaffold and run `{narrow command}`.
- [ ] Confirm it fails at `{expected missing-behaviour boundary}`.
- [ ] Implement the smallest production change that satisfies the criterion.
- [ ] Run the narrow test to green.
- [ ] Run `{relevant neighbouring command}` when the shared surface or risk requires it.

## Red verification

- **Skipped-suite command:** `{command}`
- **Result:** {scaffold count skipped and prior tests outcome}
- **Spot-activation command:** `{command}`
- **Expected red observed:** {failure at the behaviour boundary}
- **Returned to skipped state:** {command and result}
- **Unverified prerequisite:** {none or exact limitation}

## Handoff

- **Owning story or change:** {path or none}
- **Scaffold paths:** {paths}
- **Next owner:** `agent-dev`

Activate one scaffold at a time: red, minimum production change, green, then continue. If a scaffold encodes the wrong behaviour, change it consciously against the authoritative acceptance source and record why.
