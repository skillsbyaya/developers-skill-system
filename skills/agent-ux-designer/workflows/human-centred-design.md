# Human-Centred Design

Turn an uncertain user problem into evidence-backed, testable decisions. Run a full cycle or one focused phase without making the user repeat credible work already completed.

## Start from the real gap

Identify the challenge, affected users, current phase, existing evidence or artifacts, constraints, and decision the work must unlock. Inspect supplied research, prototypes, metrics, or prior design material before asking for information they contain.

Route to the earliest phase with a material gap. If the user names a phase, begin there when its minimum inputs exist. Maintain three labels throughout:

- **Evidence:** observed or sourced user behaviour, statements, or results.
- **Inference:** a reasoned interpretation.
- **Assumption:** an unverified belief that must not be presented as research.

Read [the design methods catalogue](../references/design-methods.csv) only when choosing among research, framing, ideation, prototype, test, or implementation-learning methods could materially improve the work. Use each row's purpose and warning, not its title alone.

## Phase route

### Empathise

Plan or synthesise primary user research around behaviour, context, workarounds, pain, motivation, and desired progress.

Never fabricate interviews, quotes, observations, personas, or validation. Synthetic participants and AI-generated personas may generate assumptions only. With no user evidence, create a research plan and provisional assumption map.

Exit with a concise evidence ledger, useful user or job framing, contradictions, and unanswered questions.

### Define

Cluster evidence without hiding disagreement or minority cases. Write a point of view:

`[user/context] needs [progress] because [evidence-backed insight]`

Create a small set of How-Might-We questions that open solution space without embedding a chosen feature. Identify success signals, constraints, and riskiest assumptions.

Before prototyping, be able to name the affected user and context, observed or sourced problem, decision being tested, and riskiest assumption. Label anything provisional.

### Ideate

Diverge before converging. Generate meaningfully different approaches rather than cosmetic variants. When the obvious concepts preserve an awkward step, control, or division of labour, include an approach that changes where the work lives: remove it, let the system safely carry it, move it to a better moment, or reshape the surrounding journey. Translate the principle to the problem rather than copying a fashionable interaction.

Select one to three concepts using user value, conceptual effort, agency, causal clarity, accessibility, learning value, feasibility, constraints, and assumption coverage. Do not prefer novelty or fewer visible steps when they make capability, system reasoning, or consequences harder to understand.

Exit with each concept's critical assumption and the evidence that would change the choice.

### Prototype

Define the learning question first, then choose the lowest-fidelity prototype that can answer it. State what is real, simulated, omitted, and deliberately rough.

Specify the scenario, participant task, observable success and failure signals, and stopping criteria. Prefer paper flows, storyboards, role-play, clickable shells, or Wizard-of-Oz simulations over production code when they yield the needed evidence more cheaply.

### Test

Use neutral tasks and prompts. Observe behaviour before asking for opinions; do not coach participants through the intended path.

Capture observation separately from interpretation. Record participant and context, task outcome, friction, workarounds, surprises, and variation. Classify each critical assumption as supported, weakened, contradicted, or still unknown. Do not claim validation from weak or synthetic evidence.

### Iterate or hand off

Prioritise changes by learning impact and user value. Define success measures and the next feedback checkpoint. Testing may lead to iteration, reframing, more evidence, a pilot, implementation, or stopping.

When the experience direction is settled, use this skill's UX-specification mode for formal experience requirements, `agent-ui-designer` for visual interface design and design-system work, `agent-pm` for product scope or requirements, and `agent-dev` for implementation.

## Artifact and finished result

Keep the conversation lightweight unless a reusable record would improve the next decision or the user requests one. Before writing, resolve the `design-thinking-session` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md). Update an existing record for the same challenge rather than creating a duplicate.

Include only earned sections: challenge and decision; evidence, inference, and assumptions; problem framing and success signals; concepts and rationale; prototype learning brief; test observations and assumption verdicts; decision, next iteration, and owner.

Finish with the current phase, evidence strength, decision reached, unresolved assumptions, next learning action, and owner. Skipped phases and evidence gaps remain visible.
