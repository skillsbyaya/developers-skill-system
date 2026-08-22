# Distillation Method

Create high-signal working context, not a summary of every passage. Preserve information that could reasonably change the downstream consumer's decision, implementation, validation, or interpretation.

## Preserve and omit

Preserve when relevant:

- decisions and their rationale
- rejected options whose reason still constrains the present
- requirements, scope boundaries, success criteria, and named user needs
- constraints, dependencies, ordering, ownership, and system boundaries
- evidence, material examples, and specific names, numbers, dates, versions, or percentages
- risks, mitigations, assumptions, conflicts, and unresolved questions
- dated history only when it explains a current decision, constraint, obligation, risk, or active commitment

Usually omit:

- repeated introductions, summaries, transitions, and explanations
- rhetoric, persuasion, self-reference, generic background, and decorative formatting
- routine progress narration, completed-task journals, and resolved discussion with no continuing consequence
- historical alternatives or incidents that no longer affect a decision, constraint, risk, obligation, or named consumer

When uncertain, keep one compact item and label the uncertainty. Never invent missing rationale, merge conflicting claims into false consensus, or turn a provisional statement into a decision.

## Compress

- Replace long prose with self-contained bullets that preserve the necessary actor, action, reason, condition, and consequence.
- Deduplicate repeated facts and keep the shortest version that retains decision-relevant detail.
- Group related material under thematic headings rather than repeating category labels.
- Use compact forms such as `Decision: X; rationale: Y`, `Rejected: X; reason: Y`, and `If X, then Y` when they remain clear.
- Preserve source-specific disagreement explicitly, for example: `Brief says X; discovery notes say Y; unresolved`.
- Omit an executive-summary point when the fuller retained item already contains everything the consumer needs.

Do not remove useful orientation, examples, evidence, or qualification merely to maximise a compression ratio.

## Output

Use only sections warranted by the sources, commonly:

- `## Decisions`
- `## Requirements and scope`
- `## Constraints and dependencies`
- `## Evidence`
- `## Risks`
- `## Open questions`

Add frontmatter:

```yaml
---
type: distillate
sources:
  - "relative/source.md"
downstream_consumer: "general"
preservation: decision-relevant
created: "YYYY-MM-DD"
source_token_estimate: 2400
output_token_estimate: 700
parts: 1
---
```

Use paths that remain meaningful from the saved artifact. Every bullet must be traceable to at least one source.

## Split only for independent use

First remove low-value material. If the useful result is still too large for its downstream task, choose semantic boundaries such as functional area, stakeholder, current versus future state, scope, or implementation phase.

The package `_index.md` contains orientation, source provenance, a topic manifest, cross-cutting decisions and constraints, and high-level scope. Each topic file states what it covers, remains understandable when loaded alone, and points to another part only when necessary.

Do not split by arbitrary token intervals or duplicate cross-cutting material into every part.

## Coverage check

Build a compact source-derived checklist of:

- decisions and rejected options
- requirements and scope boundaries
- constraints, dependencies, and owners
- evidence and material names, numbers, dates, and versions
- conflicts, assumptions, risks, and open questions

Check each item against the finished artifact. Repair material omissions or distortion. Then check the reverse direction: every output item must be supported by a source, and uncertainty or conflict must not have disappeared during compression.
