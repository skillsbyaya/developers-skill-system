# Story Preparation

Read this reference only from the prepare-story workflow, when staged delivery starts from one approved epic or backlog story that has no implementation-ready story record, or when the user asks to refresh a not-yet-started story.

Resolve an exact stable key and the project's registered story location. If tracking is absent, use the bounded tracker bootstrap in staged delivery only when one authoritative epics document and the PM structural convention make every key and order unambiguous. Otherwise stop for the target or structural owner.

When resolution or source discovery uses a project ID or dotted area suffix, resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project `identifier-areas` registry. Match the exact base key and pair it with its title. Use each canonical area segment to find candidate current requirements, architecture decisions, risks, controls, and related delivery items; triage matched sections before reading broader sources, follow explicit dependencies, and exclude archives and superseded whole documents. For money, authentication, authorisation, security, destructive behaviour, privacy, safety, or compliance, read the fuller relevant authority rather than relying on a routed section alone.

Read the complete authoritative outcome and acceptance plus only the relevant requirements, architecture, UX, project constraints, current code, tests, prior story evidence, and recent change history needed to implement without guessing. Check external guidance only when volatile versions, APIs, or security facts could change correctness. Preserve source locations and expose unresolved conflicts; do not copy source prose into the story.

## Use specialists only for readiness-changing uncertainty

Consult a specialist only when an unresolved question is material, is not settled by authoritative sources or established project conventions, falls outside routine engineering mechanics or needs genuinely fresh expertise, and its answer could change acceptance, constraints, change boundaries, packets, verification, or whether the story is ready. Do not consult for a fixed choice, a familiar local and reversible implementation detail, an existing pattern that already answers the question, taste-only feedback, or generic reassurance.

Route the unresolved question to its actual owner:

- product outcome, acceptance, scope, priority, or business rules → PM owner or user;
- durable cross-system boundaries, data ownership, public contracts, migration strategy, platform or dependency commitments, or similarly consequential structural choices → `agent-architect`;
- user journeys, interaction behaviour, state meaning, information hierarchy, interface copy, usability, or experience-accessibility → `agent-ux-designer`;
- visual hierarchy, component appearance or placement, new shared primitives, tokens, themes, responsive presentation, or brand expression → `agent-ui-designer`;
- test-system, suite, CI, cross-system evidence, or critical failure-path strategy → `agent-test-architect`, while Dev retains routine affected-test design; and
- authentication, authorisation, sensitive data, money, destructive behaviour, privacy, safety, legal, compliance, database integrity, or similarly critical domain exposure → the direct relevant specialist.

Give one specialist the approved outcome, the exact unresolved question, the minimum relevant sources, and a read-only boundary. Ask for one compact decision or evidence result with assumptions and implications for the story; the specialist does not write the story or tracker. Dev checks the result against current sources, integrates only supported findings, and retains story ownership and user decisions. Use another specialist only for a second distinct uncertainty. Do not duplicate the same question with a generic validator unless critical consequence or conflicting evidence requires independent assurance.

Do not run a general UX or UI sweep after every story. Request a bounded review of the prepared draft only when a new or shared pattern, several consequential states or layouts, or unresolved experiential acceptance could materially change the story, and resolve it before `ready-for-dev`. If a defect's cause or required fix is not sufficiently established, stop and route to investigation instead of inventing an implementation plan.

Create or update one semantically complete story containing:

- the authoritative outcome, observable acceptance, constraints, and non-goals;
- current-code reuse points, likely change surfaces, contracts, and behaviour to preserve;
- consequential security, performance, data, compatibility, deployment, and test requirements;
- bounded implementation packets with dependencies and verification; and
- an execution area for decisions, evidence, files, review findings, status, exact continuation, and one current completion-assurance note. Initialise that note with the expected consequence floor, any known completion attention, and the likely completion condition; state explicitly when the plan is routine and no independent assurance is expected unless implementation changes the risk.

Resolve genuine design decisions here, not at build time, and record each supported decision in the story. A new interaction pattern or shared primitive is a prep-time decision — not a build-time "try it on the sandbox and see."

Do not regenerate a story already in progress, review, or done. Refresh a ready story only when asked and preserve its execution and review history. Set `ready-for-dev` only when material behaviour can be implemented without guessing.

Validate the prepared story back against its sources before implementation: acceptance completeness, correct reuse points and layer, versions and contracts, permissions and risk controls, error and edge paths, dependencies, and verification. Use one fresh read-only validator when the source breadth or consequence makes independent coverage material and the boundary can be enforced; otherwise validate inline and state any consequential limitation. The main owner resolves findings, writes the story, and retains user decisions.
