# Human Preview

Use this workflow to help a person, especially a non-developer, understand and examine observable differences in a live, preview, staging, or dev environment. It produces decision support, not technical approval or a ship verdict.

## Orient

Resolve the observable environment, natural entry point, comparison baseline, and running candidate. The baseline may be the current live experience, a previous build, or stated expected behaviour. If one environment and candidate are obvious, proceed and state them; ask only when several plausible choices would change the walkthrough.

Use a PR, commit, branch, diff, or implementation artifact only as supporting evidence for what should be observable and which build contains it. Never ask the person to examine source control or code. If no relevant environment is available, name what is missing and do not substitute artifact review for human preview.

Before asking the user to do anything, inspect the environment and current evidence Claude can access and establish claims Claude is better placed to assess at proportionate cost. Explain observable differences even when they need no user action, but do not turn checks Claude would perform more reliably or effectively from rendered surfaces, behaviour, artifacts, logs, or test evidence into unnecessary human homework. Token or time cost may justify delegating an otherwise accessible, human-suitable check when the person's effort is reasonable and the evidence will not be worse; checklist-construction effort or a desire for confirmation alone does not.

Explain in plain language:

- the intended outcome and who experiences it;
- what differs observably from the baseline and what deliberately does not;
- where behaviour, UX, data, trust, cost, or operational work could be affected; and
- which claims come from evidence and which remain inference.

Use environment locations, journeys, states, and build identifiers as the primary anchors. Use files or implementation artifacts only as supporting provenance. Explain necessary technical terms briefly and connect them to observable consequences.

Organise the walkthrough around the route the person can follow with the fewest page changes. Preserve state and dependency order first, group work by app page within each dependency phase second, and use product or design concerns within those constraints. Lead with the natural entry point in the environment and explain the comparison a person can actually experience.

## Build the walkthrough

1. Map the user-visible journeys and affected states in the running candidate, including the baseline difference and any setup or permissions needed to observe it.
2. Separate what current evidence establishes from what still needs direct human observation. A user test is justified when the result could change acceptance and either requires the person's judgement, perception, accessibility experience, physical device, app login, account state, or access to an environment Claude lacks, or is a human-suitable check whose Claude execution cost would be disproportionate. Do not delegate a check Claude would perform better or where delegation would produce weaker evidence or unreasonable user effort.
3. Build the minimum required user checklist from those remaining observations. Keep a step only when its result could change acceptance and it meets the human-only or proportionate-delegation rule above. Remove duplicate observations, routine confirmations unrelated to the change, and checks included merely for completeness. For each retained step, give the starting state, action, expected observation, why it matters, what a failure would suggest, and why the person rather than Claude is checking it. If no material uncertainty requires a person, say that no user test is needed.
4. Identify the state-changing setup actions and their dependencies. Use each setup action as the start of a phase: create or place something, complete all checks that depend on that state grouped by page, then perform the next setup action such as deleting or interrupting it and group the resulting checks by page again. Never move a later setup action earlier merely to reduce navigation.
5. Within each phase, finish every relevant check available on the current page before sending the person elsewhere. Revisit a page only when a later setup action creates a genuinely new state to observe. If a section would make the person move back and forth, split or reorder it unless the interaction itself must cross pages in that order.
6. Keep explanations, optional things the person may notice, and specialist or unavailable-environment evidence outside the required checklist. A delegated check must remain an observable, human-suitable action; never ask the user to inspect source control, code, logs, or automated checks.
7. Include negative, interruption, recovery, accessibility, permission, and data-preservation steps only when the changed surface exposes them, their result could change acceptance, and they require human observation.
8. Name unavailable environments, hidden backend behaviour, automated evidence not inspected, and any other limitation. Translate skipped checks into residual exposure rather than implying success.

Call out the few highest-blast-radius areas, such as access, public contracts, data or migrations, money, infrastructure, security, configuration, or privacy. Explain them plainly without scoring or inventing risks.

Present the explanation and complete minimum checklist coherently rather than drip-feeding steps. When the person will work through the checklist away from this conversation — over a sitting or several, on another device, or on paper — publish it as a working document following [Preview checklist artifact](../references/preview-artifact.md). Keep a short check in the reply.

If the user reports results, distinguish observed PASS, observed problem, not run, and unclear; do not manufacture approval from partial results. When fixes produce a new candidate, rebuild the active checklist from those results and the impact of the fixes. Keep only unresolved, not-run, or unclear observations and earlier passes that the changes could have invalidated. Remove still-valid passes from the active checklist; if their history is useful, summarise them compactly at the bottom rather than leaving completed steps mixed among current work. Reset only an invalidated step that genuinely needs repeating.

## Wrap up

Summarise the outcome, material observations, unresolved questions, and next decision: accept the experience, request changes, discuss a concern, or seek a specialist check. When acceptance is material, wait for the user's decision and record it as human evidence; it is not technical or release approval. Preview the affected running candidate again after changes, and revise a published checklist in place rather than issuing a second one. Treat the revised page as the current worklist, not a cumulative record of old and new checks.
