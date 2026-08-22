# Solve a Business Problem

Use this workflow for an observed non-software operational or business problem whose cause and intervention are not yet known. It diagnoses before prescribing. Software defects and incidents belong to technical investigation; broad option generation belongs to brainstorming.

Infer the lightest suitable mode: quick diagnosis, guided problem solving, multi-participant workshop, or a focused named exercise. Apply an explicitly requested exercise directly. Do not force a workshop or framework when a direct answer will do.

## Use the exercise catalogue when it changes the work

Reassess catalogue need after framing the problem, after diagnosis, before comparing interventions, and when defining a pilot or rollout. Read the [business problem exercise catalogue](../references/business-problem-exercises.csv) once when:

- the user asks for a workshop, methods, or a named problem-solving exercise;
- the problem shape makes a specialist diagnostic or analysis method material, such as uneven occurrence, interacting feedback, measured cause distribution, adoption resistance, or reliability risk;
- the work needs to escape a contradiction or narrow solution space, compare material interventions across criteria, cost, risk, or feasibility, or design a consequential pilot, rollout, adoption, dependency, or measurement approach.

Do not load it for a straightforward case when the method is obvious and the catalogue would not change the reasoning. After loading, use only relevant rows: check `best_for` to confirm fit, adapt `facilitation_prompts` to the case, and use `output_pattern` to structure the reasoning. Do not recite every prompt or produce decorative framework output.

For a workshop or delegated method choice, recommend two to four strong matches with reasons and include a credible lightweight option. Let the user choose or delegate; then use the minimum exercise set that resolves distinct uncertainties.

## Define the problem from evidence

Establish the undesirable outcome, affected stakeholders, scope, timing, frequency or magnitude, and evidence that it occurs. Separate symptoms, interpretations, and proposed solutions. Define a useful baseline and what improvement would look like; label unavailable measurements instead of inventing precision.

Map the relevant current process, decisions, handoffs, incentives, constraints, and recent changes. Include people who experience the problem as well as process owners and decision-makers.

## Diagnose

Choose the smallest diagnostic exercise that fits the uncertainty:

- **Five whys:** follow one evidence-supported causal chain without treating the fifth answer as automatically root cause;
- **Process and handoff map:** find delay, rework, ambiguity, queues, or lost ownership;
- **Cause categories:** test people, process, information, incentives, tools, policy, and environment without assuming equal weight;
- **Constraint analysis:** identify the bottleneck that limits the whole outcome;
- **Pattern comparison:** compare affected and unaffected cases, time periods, locations, or cohorts;
- **Causal hypothesis test:** state what should be observable if a proposed cause is real and seek disconfirming evidence.

For a quick diagnosis, select an obvious fit and explain it in one line. When the catalogue gate has fired, use a matching diagnosis or analysis row instead of defaulting to the embedded list. Do not treat a weighted score as objective.

Combine exercises only when one leaves a distinct material uncertainty. Rank causal hypotheses by evidence and decision relevance. Distinguish a cause from a factor that merely correlates with the symptom.

## Design a bounded intervention

Reassess the catalogue gate before developing options and again before defining the pilot or rollout. Use synthesis rows when supported diagnosis still leaves a stuck or narrow solution space, evaluation rows when choosing among material alternatives, and implementation rows when adoption, dependencies, learning cycles, or measures need structured design.

Generate interventions tied to supported causes. Compare expected effect, stakeholder burden, dependencies, reversibility, cost, timing, and risks. Prefer a bounded pilot when evidence is incomplete and a safe test can resolve it.

For the recommended intervention, define:

- causal hypothesis and intended mechanism;
- owner and affected stakeholders;
- smallest viable change or pilot;
- leading and outcome measures with a baseline when available;
- dependencies, guardrails, and stop conditions;
- review point and what decision the result will support.

Do not turn the answer into a full delivery plan or execute the intervention unless asked.

## Finish

Return the problem definition, evidence and gaps, diagnosis with confidence, rejected explanations, intervention options, recommendation, stakeholder effects, and the smallest useful next action or test. If the evidence cannot distinguish material causes, leave the diagnosis unresolved and specify what evidence would do so.

For a workshop, also capture agreements, disagreements, evidence disputes, parking-lot items, owners, and unassigned actions without inventing consensus.
