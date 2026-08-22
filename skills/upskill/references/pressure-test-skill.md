# Pressure-Test a Skill

Use this reference for a deep, adversarial review of a complete skill. Load it when the user asks for a thorough, adversarial, edge-case, or high-confidence audit; before accepting a newly created skill; after a merge, split, port, or material ownership redesign; or when evidence shows several interacting failures that a focused audit cannot resolve.

Do not load it for a narrow description check, a known bounded edit, or a contained repair. File length and a general desire for confidence are not sufficient reasons.

## Working rules

- Start with the skill's intended user outcome, boundaries, inputs, finished result, likely failures, and surrounding system.
- Review the complete candidate, including conditional references and helpers, but read neighbouring files only when they can affect a real finding.
- Keep proposed changes separate during Stages 1–6. Later stages may strengthen, weaken, combine, or reject earlier findings.
- Each finding must name the affected user outcome or realistic case, the evidence, the likely impact, and the smallest useful correction.
- Do not repeat the same finding under several methods or create a permanent scorecard by default.
- Run inline unless a separate reviewer has a distinct, justified purpose. A deep review does not require workers by itself.

## Stage 1 — Red Team vs Blue Team

### Red team

Try to prove that the skill should fail. Attack it where relevant:

- the capability does not need a separate skill;
- the capability is a method that should be a directly selectable workflow under its natural area owner, or has been nested despite needing independent authority;
- natural requests will miss it, or neighbouring requests will trigger it incorrectly;
- the skill depends on hidden setup, routing, or another owner;
- its instructions are generic, rigid, incomplete, or unable to handle likely failure;
- it loads unnecessary material or hides required material too deeply;
- it creates unsafe changes, competing saved information, unnecessary documents, or unclear responsibility;
- it assumes tools, permissions, registries, neighbours, or platform behaviour that may not exist;
- it leaks project-specific material into a personal skill; or
- it lost useful judgement, safeguards, preferences, triggers, or resources during replacement or consolidation.

### Blue team

Defend each attack with the actual instructions, current evidence, or a realistic walkthrough. Do not defend something because it existed before, sounds sensible, or matches a preferred file shape. Accept attacks that the evidence does not defeat.

Keep only confirmed weaknesses, confirmed protections worth retaining, and unresolved questions that could change the result.

## Stage 2 — Boundary & Edge Case Sweep

Select cases that could realistically change this skill's behaviour. Do not manufacture irrelevant extremes.

### Routing and intent

- clear natural request;
- explicit skill or mode request;
- vague request from a user who does not know the method;
- explicit method request that must bypass area-owner consultation and sibling workflows;
- neighbouring request that belongs elsewhere;
- request that should not trigger the skill;
- mixed request containing two possible routes;
- mixed request spanning a report-only or advisory result and a later mutation; and
- request whose wording proposes the wrong mechanism.

### Entry state and evidence

- no existing artifact or context;
- partial, stale, or conflicting artifacts;
- completed work that should not be repeated;
- out-of-sequence request;
- reported failure with weak evidence;
- fixed user choice that should not be reopened; and
- missing information that is either safe to infer or material enough to ask about.

### Environment and scope

- personal versus project use;
- empty versus mature surrounding library;
- missing optional neighbour, generator, registry, or document owner;
- unavailable worker isolation or permission boundary;
- changed or uncertain platform behaviour; and
- partial tool failure or a no-op result.

### Loading and completion

- only the selected workflow loads;
- every linked file has a clear loading condition;
- broken, stale, circular, and unnecessary references are exposed;
- the skill stops at its own boundary;
- any transition from advice, diagnosis, or assessment into mutation has a clear terminal result, authority check, handoff, and next owner; and
- the finished-result check distinguishes success from a claim that the process was followed.

Keep failed cases, cases that pass because of an important protection, and boundaries that remain genuinely untested.

## Stage 3 — Failure Mode Analysis

Inspect each component that exists: description, core, route selector, selected workflows, shared references, scripts, templates, assets, tools, saved information, recurring documents, callers, registrations, and links.

For each credible failure, determine:

1. what fails for the user;
2. what causes it;
3. how the finished system would reveal it;
4. the smallest prevention or recovery; and
5. what uncertainty remains.

Check both directions:

- **Under-design:** missing judgement, weak triggering, incomplete failure handling, absent safeguards, stale relationships, or lost predecessor value.
- **Over-design:** unnecessary skill surface, speculative future-user needs, repeated confirmation, forced planning or review, document inflation, default workers, duplicated policy, or validation that does not change a decision.

Then run two deletion tests:

- **Description counterfactual:** read only the skill name and description beside plausible neighbouring live descriptions. Remove each clause in turn. Keep it only when its removal changes the correct selection for a realistic clear, vague, direct-mode, neighbouring, or non-trigger request. A true statement about what happens after selection still fails this test when it does not affect selection. Prefer positive cues; retain an exclusion only for a demonstrated cue collision and keep it to the smallest discriminating phrase. Operational boundaries belong in the loaded skill, not a duplicate routing catalogue.
- **Standalone necessity:** read the skill without project, migration, or predecessor context. Keep each sentence in the core and each instruction in a support file only when removing it would change judgement, safety, failure handling, or the finished result. Put lineage, compatibility mapping, and design rationale in their actual owner unless current operation genuinely needs them.
- **Loaded-pair overlap:** read the core with each support file it can load. Consolidate repeated rules into the narrowest reliable owner so one selected route does not receive the same instruction twice.

Then run the **owner-versus-workflow test**. Start with the user's recognisable area and requested result, not the method's internal authority. A directly selected workflow may own specialist judgement, mutation, durable records, and lifecycle rules within its area; these do not by themselves justify another visible skill.

For every proposed standalone owner, require evidence that its authority must be independent of the plausible parent. Test whether users enter through another or several areas, whether the parent would become misleading or overbroad, whether independent assessment must sit outside the producing area, and whether direct routing, cross-domain use, or representative total context is materially better standalone. Compare the actual parent-plus-selected-workflow route with the standalone route. If the case for separation reduces to “it has state,” “it mutates,” “it is specialist,” “it is high stakes,” or “it has a lifecycle,” reject that argument and test a complete conditional workflow instead.

For every nested method, require immediate explicit selection, no consultation preflight, no sibling loading, and complete workflow-level authority and safeguards. Fewer surfaces do not prove a better result.

Then run the **authority-transition test** wherever advice, diagnosis, investigation, planning, review, or assessment may precede mutation. Name the report-only workflow's terminal result, the facts and choices that become known only after it finishes, the exact mutation proposed, and the next owner. An initial broad request to “investigate and fix,” “review and apply,” or similar does not automatically authorize a specific change that could not yet be described. Require fresh user authority when the first workflow materially determines or changes the target, scope, mechanism, risk, rollback, or accepted trade-off. Continue without another confirmation only when the exact mutation and its material consequences were already established and authorised before the report-only work. Never hide a second report-only workflow inside mutation merely to bypass this transition.

Stop when additional failure modes would not change the candidate or its acceptance.

## Stage 4 — Assumption Audit

List only assumptions the candidate relies on. For each, state the evidence, confidence, impact if false, and the smallest way to resolve it.

Check assumptions about:

- the user's actual recurring need, preferences, frequency, and risk;
- available inputs, artifacts, tools, permissions, and project context;
- neighbouring owners, callers, registrations, documents, and links;
- what belongs in shared policy versus one skill or workflow;
- whether saved information improves later work;
- current platform behaviour; and
- whether a safeguard changes outcomes or merely proves that a process occurred.

Challenge high-impact assumptions with weak evidence first. Do not design for hypothetical future users or reopen a fixed user decision without material conflicting evidence.

## Stage 5 — Outcome and Loss Gate

1. Compare the candidate with the intended user outcome, required capabilities, boundaries, safeguards, and realistic cases.
2. If a predecessor or earlier version exists, inspect it only after the first comparison to find omitted value.
3. Check relevant prior findings, user corrections, resources, callers, and neighbouring skills for missing judgement or safeguards.
4. Accept an earlier behaviour only when the current outcome still needs it and it remains a good mechanism.
5. Rerun the standalone-necessity and loaded-pair overlap tests on every accepted carryover; the loss check must not become an additive ratchet.
6. Identify genuine gains, accepted losses, rejected carryovers, and unresolved material loss.

Use a comparison table only when scale or uncertainty makes one useful. No skill passes with an unexplained material loss, but predecessor coverage alone does not prove quality.

## Stage 6 — Real-Task Walkthroughs

Every deep review covers:

- one clear direct request;
- one vague or incomplete request;
- one neighbouring request that should route elsewhere;
- one request that should not trigger the skill; and
- one likely failure-prone request.

Add personal/project, existing-artifact, stateful, irreversible, retired-capability-intent, or explicit-mode cases when relevant.

For each case, check the selected skill or route, files that load, questions asked or safely inferred, allowed actions, saved information affected, stopping point, authority carried forward or reacquired, next owner, and finished result. For a report-only-to-mutation case, write these fields explicitly; a statement that the boundary “passes” without showing the transition is not evidence. Reason from the actual instructions; do not treat an artificial model simulation as stronger evidence than the text supports.

## Stage 7 — Critique and Refine

1. Combine overlapping findings and remove those later evidence defeated.
2. Rank the rest by effect on the user's outcome, safety, routing, or maintainability.
3. Propose the smallest coherent changes that fix causes rather than examples.
4. Check the proposal for new duplication, ceremony, vague language, hidden prerequisites, and lost safeguards.
5. If the calling route owns changes, apply in-scope corrections and rerun the affected stages. If the calling route is audit-only, return the proposed changes without editing.

Write or refine the description after the behaviour and support structure are stable. Rerun the description counterfactual against adjacent descriptions. Do not preserve a clause because it accurately summarizes the skill, describes how work finishes, names a safeguard, or explains library ownership; keep it only when it changes correct selection for a realistic request.

Finish with a plain-language sweep. Every instruction should be understandable on one reading and specific enough to guide action.

## Stage 8 — Mechanical Verification

After behavioural fitness is sound, verify what can be checked mechanically:

- frontmatter parses and current naming and description rules pass;
- links and referenced files resolve;
- supporting files have clear loading conditions;
- scripts and exact commands pass relevant success and failure cases;
- routes, callers, live frontmatter, and document contracts agree;
- personal skills contain no project-only paths, decisions, runbooks, or migration procedure; and
- removed or renamed owners leave no stale live references, aliases, or successor mappings.

Mechanical correctness can reject a skill, but it cannot prove that the skill is useful or well designed.

## Return to the calling route

Return:

- confirmed material findings and protections;
- unresolved evidence limits;
- the smallest coherent correction set; and
- the stages and cases that must be rerun after a change.

An audit route reports these findings without editing. A create or restructure route applies authorised in-scope corrections, reruns affected stages, and accepts the skill only when no material fitness doubt remains.
