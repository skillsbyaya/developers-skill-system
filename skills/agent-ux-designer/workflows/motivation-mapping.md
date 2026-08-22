# Motivation Mapping

Create or update a durable motivation map connecting business purpose to the forces that cause people to act. Keep solutions off the map so later product and UX decisions can use it without making it stale whenever implementation changes.

## Establish the decision

Clarify the product or bounded area, the decision the map must support, and which motivations remain uncertain. Reuse one existing map for the same scope and update it in place.

Use supplied research, briefs, requirements, designs, behavioural data, support evidence, interviews, and explicit user decisions as possible inputs, not mandatory predecessors. Preserve fixed goals, groups, and decisions unless new evidence materially conflicts with them.

When evidence acquisition is the primary job, use `research` for current secondary evidence or this skill's human-centred-design mode for primary research and testing. Sparse evidence may support a provisional hypothesis map, but never invented psychology presented as fact.

## Build the map

1. **Business goals:** identify the smallest durable set explaining why the product or area exists. Separate goals from metrics.
2. **Target groups:** retain only groups whose context or motivations differ enough to change a decision, normally no more than four.
3. **Personas:** create one only when its motivations or decision context would change a downstream choice. Include its relation to the problem, values and decision style, active emotional context, route to the product, trust or effort criteria, and observable success.
4. **Driving forces:** include positive pulls and negative pushes. Write each as **what + why + when**, specific enough to guide a decision without prescribing a feature.
5. **Priorities:** score only forces whose ordering could change product or UX scope, sequence, or emphasis.

Distinguish broad life goals from the usage goal active in this context. Reject generic forces such as “wants convenience” or “needs confidence”; state what is needed, why it matters, and when it becomes active.

## Evidence discipline

Label each material claim or force:

- **Evidenced:** supported by a named source or explicit user statement.
- **Inferred:** a reasoned interpretation of available evidence.
- **Assumed:** a hypothesis needing validation.

Record source or rationale, confidence, and a practical validation question when the distinction could change priority. Preserve source conflicts rather than averaging them into false certainty.

## Score decision-relevant forces

Use three 1–5 scores and add them to a total out of 15:

- **Frequency:** how often the force is active.
- **Intensity:** how strongly it drives or blocks action.
- **Product fit:** how directly this product can respond.

| Total | Priority | Interpretation |
| ---: | --- | --- |
| 14–15 | High | Core to user success; design for it first. |
| 11–13 | Medium | Material when feasible; several forces may share one response. |
| 8–10 | Low | Useful but secondary. |
| Below 8 | Deprioritise | Low strategic value here or evidence that the target group may be wrong. |

The score makes judgement inspectable; it is not measured truth. Record rationale and confidence when a score affects a decision. Read the pattern as well as the total: high intensity with low fit signals a product limit, while low frequency with high intensity may need a specialist path.

## Write and update the artifact

For a durable file, resolve the `trigger-map` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md) when available. Otherwise update a supplied path, reuse one obvious existing map, or agree a location before writing.

Use only sections earned by the work:

```markdown
# Motivation Map: {product or area}

## Decision this map supports
## Business goals
## Target groups and personas
## Prioritised driving forces
| Persona | Force (what + why + when) | Pull/push | Evidence and source | Confidence | Frequency | Intensity | Product fit | Total | Priority |
## Validation questions
## Downstream implications
```

Update stable supported content in place and remove stale claims instead of appending history. Return the artifact path, material delta, strongest forces, evidence limits, and any current decision that may need reassessment. Do not automatically continue into product requirements or UX specification.
