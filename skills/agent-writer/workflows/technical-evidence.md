# Technical Evidence

Use repository evidence to create durable bounded context or validate technical-document claims.

## Select the evidence task

Read exactly one reference.

| Result | Read |
| --- | --- |
| Create or refresh a reusable reference for one code area | [Code-area reference](../references/code-area-reference.md) |
| Check whether an existing technical document matches repository evidence | [Technical-document validation](../references/technical-document-validation.md) |

## Evidence contract

- Bound the target to a folder, feature, integration, subsystem, named concern, or specified technical document. Follow adjacent code only when it supplies a necessary caller, dependency, contract, data flow, or failure boundary.
- Ground conclusions in current source files, configuration, tests, interfaces, and direct contracts. Inspect source directly rather than trusting a document's citations.
- Distinguish verified behaviour from inference, uncertainty, runtime state, generated output, or an uninspected external dependency. Never invent commands, API shapes, data models, ownership, or test coverage.
- Use exact paths and the smallest evidence set that supports the claim. If the target or material evidence boundary is unclear, ask one concise question; otherwise state the inferred scope and continue.

For a large or cross-system target, establish a coherent bounded scope before investigation. Stop when responsible completion requires unavailable source evidence or a broader user-owned scope decision.

