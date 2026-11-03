---
title: <key> — <title>
status: ready-for-dev
---

# <key> — <title>

## Boundary and authority

Prepared against `<base branch>` at `<short commit>`; <whether a branch for this story already existed>. Outcome, scope and acceptance: `<owning epic or backlog item>`. <One clause per other owner the build needs, such as architecture, UX or data rules, each with its path.>

**Outcome:** <one or two sentences on what is true once the story is done, in the user's terms.>

## Decisions

- **D1 — <the decision as one bold line>.** <Two to four plain sentences: what it means for the build and why, naming the code or rule it rests on. When the decision was the user's, end the bold line with "(<name>, <date>)".>
- **D2 — …**

<Decisions carry the reuse points, change surfaces and contracts the build depends on, and any security, data, performance or deployment constraint it must hold. Number decisions once and never renumber them; a withdrawn decision keeps its number and says it was withdrawn. Name each rejected alternative in one sentence inside its decision, only when a later session might otherwise propose it again.>

## Acceptance

1. **Given** <state>, **when** <action>, **then** <observable result>.
2. <Or an observable statement, when Given/When/Then adds nothing.>

<Each item can be checked by a test or by looking. Point to the owning acceptance rather than copying it; restate an item only to make it observable or to apply a decision above.>

## Preserve

- <Behaviour, contract or earlier decision this story must not break, with its source path.>

## Packets

| Packet | Scope | Depends on | Model / effort |
| --- | --- | --- | --- |
| **P1 — <name>** | <what it builds, the files or functions it touches, its tests> | — | <capability class> / <effort>; <the review it needs, if any> |

## Verification

- <Which checks prove which acceptance items, and where they run. Include a timing or size check when the change could approach a limit.>

## Execution

**Current state:** <one line, replaced, never appended to.>

**Completion assurance:** <consequence floor and why; what needs attention at completion; the condition that completes the story. Say plainly when the plan is routine and needs no independent review.>

**Next:** <the exact next step>. **Model:** <capability class>. **Effort:** <level>.
