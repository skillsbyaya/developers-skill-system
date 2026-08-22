# Organisation and Pruning

Use this workflow for a placement or naming answer, a documentation sweep, a bounded archive, or a deliberate change to the document system.

## Choose the operation

- **Lookup:** the user asks where one document belongs or what to call it. Resolve the matching rows and notes through [the convention-resolution rules](../references/convention-resolution.md), answer with the purpose match, path, and filename, then stop. Do not inventory the project.
- **Sweep:** documents are messy, stale, duplicated, bloated, misfiled, or inconsistent. Inspect the relevant tree and propose a coherent target.
- **Convention redesign:** the user wants different placement, naming, lifecycle, identifier, or format rules. Judge whether each durable change is a global default or a project-specific divergence, then design the convention and its migration together.
- **Archive:** a known set of documents is superseded and needs removal from the live set without deletion.
- **Identifier vocabulary:** the user wants to create, inspect, rename, merge, or prune the project's canonical identifier areas. Read [the convention-resolution rules](../references/convention-resolution.md) and the current `reference/identifier-areas.yaml` when it exists.

Start from supplied paths and current artifacts. Read project context only when it contains decisions needed to judge the documents. For a small or moderate set, inspect every document in scope. For a large set, inventory paths and metadata first, state a meaningful boundary, then read by likely issue cluster instead of loading the whole tree.

Exclude tool-managed memory, hidden system state, generated or build output, and vendored dependencies unless the user explicitly includes them.

## Apply the conventions with judgement

Read the relevant convention rows and notes; do not restate the registry as prose. Judge each document by what it is for and who needs it.

- **Placement and naming:** classify by purpose and lifecycle rather than title keywords, then identify the document type, folder, area, and durable distinguishing detail. When no convention fits, record a convention gap instead of forcing a match. Preserve stable paths or identifiers when churn would cost more than the inconsistency.
- **Duplication:** choose the living authority, merge only still-useful unique content, and archive the superseded copy.
- **Hygiene staleness:** remove finished-work-as-current, dated session framing, obsolete navigation, duplicated history, and next-action sections that contain anything other than the actual next direction.
- **Concept staleness:** remove a reversed decision, abandoned approach, or invalid claim only from an explicit current decision or stale-concepts list. Never infer a pivot from tidy but older prose.
- **Size and structure:** split only when parts have distinct lasting purposes or readers. Keep one source intact when the real need is a shorter derivative and route that need to the `agent-writer` distillation workflow.
- **Discoverability:** repair broken inbound links and navigation. Do not reject an intentionally standalone document merely because nothing links to it.
- **Identifier routing:** keep `reference/identifier-areas.yaml` to the smallest useful canonical vocabulary. Resolve genuine alternate terms through aliases, not duplicate areas. Never turn it into an item index, counter, priority list, or `next` register.

Prune always-read control and context files hardest because their cost recurs. Keep them to instructions and facts that are almost always needed; leave task history, backlog state, review logs, and detailed source material in their owners.

When the sweep finds a consequential documentation gap, report the intended reader, decision it blocks, and evidence for the gap. Do not inspect code or author domain content merely to fill it.

## Learn from preventable documentation residue

When pruning finds evidence that an item remained in the live set because the responsible producing or closing workflow did not clean it up at the right time, or that it should never have been recorded durably, invoke `learn-lessons` with its current-correction workflow before that evidence is lost. Supply the affected artifact, the expected lifecycle or recording boundary, how the item entered or remained in the live set when known, and the consequence. Ask it to separate evidence from inference, identify the cause, and propose the smallest durable prevention through the correct owner, such as a producing skill, closeout instruction, convention, template, or deterministic check.

Do not invoke it for ordinary ageing, valid history, intentional archive material, forward-only convention adoption, or clutter with no supported preventable behaviour. Keep the documentation cleanup moving, but do not expand it into protected skill, instruction, configuration, tool, or project changes without the authority those targets require.

## Assess convention mismatches

Treat a difference from the resolved convention as a decision to assess, not an automatic defect to normalise. For each mismatch:

1. State the resolved rule and whether it comes from an explicit project instruction, `reference/project-conventions.md`, or the global convention.
2. Describe the smallest adjustment that would conform and the practical payoff, such as clearer discovery, lower ambiguity, repaired automation, reduced recurring maintenance, or consistency that helps real readers.
3. Assess migration cost and safety: stable-path or identifier churn, inbound references, external links, hardcoded consumers, producing skills, tooling, collisions, concurrent work, archive or history value, reversibility, and risk of losing unique content.
4. Give one verdict:
   - **Adjust now:** the ongoing payoff is material and the migration is bounded and acceptably safe.
   - **Adopt forward-only:** the convention is useful for new work, but retrospective migration has little practical payoff.
   - **Retain as a project exception:** a durable local need justifies the difference; propose a delta-only project override if one does not already exist.
   - **Change the convention:** the mismatch exposes a weak global rule or project override; route the convention decision before migrating artifacts.
   - **Investigate further:** references, ownership, consumers, concurrency, or content consequences are too uncertain for a safe recommendation.

Do not recommend migration for cosmetic consistency alone. Group mismatches only when the same rule, adjustment, payoff, and risks genuinely apply; separate any item with a distinct consumer, collision, authority, or loss risk.

## Redesign a convention

1. Resolve the affected global rules and any project overrides, then read representative artifacts and any producing skills that hardcode the current rule.
2. Design one unambiguous home and naming rule for each recurring document type. Prefer Markdown for human-readable working documents; use another format only for a real machine, interactivity, compact-registry, or external-contract need.
3. Propose the global-source or project-overlay edits, file migrations, inbound-reference repairs, affected consumers, collisions, exceptions, and whether adoption is forward-only or retrospective. A project override contains only durable differences and their reasons; it never copies the global source wholesale.
4. After approval, update the relevant convention source first, creating `reference/project-conventions.md` from [the template](../templates/project-conventions.md) on the first confirmed project divergence. Migrate only the approved scope, repair affected links, and use `upskill` for any producing-skill change.
5. Verify each changed row against representative existing artifacts and one future path derived from the new rule. Report anything deliberately left on the former convention.

For an identifier-vocabulary change, preserve stable base IDs and archives. Update current suffixes and affected current references only after the vocabulary change is approved. Remove an unused area only when no current ID uses it, no current document declares it, no alias or current product language needs it, and no active near-term work needs it.

## Propose, apply, and verify

Return the mismatch assessment before the target structure. Then provide an itemised list of approved candidate moves, renames, merges, splits, prunes, convention edits, and archives. Tie each candidate to its verdict and include references that must change. Include meaningful no-change decisions where forward-only adoption, a justified project exception, uncertainty, stable paths, or existing authority outweigh migration.

Show that plan before moving, renaming, merging, splitting, pruning, or archiving existing material. After approval, apply only its scope; preserve unrelated content and stop on a collision, ambiguous merge, concurrent edit, or broader consequence. Archive superseded material when it retains recovery value; delete only with explicit approval.

Then verify:

- every changed path exists once and every archived item left the live set;
- inbound relative links and explicit path references resolve;
- current facts have one authority and no approved unique content was lost;
- resolved global and project convention rows describe the resulting and future placement; and
- no backlog ordering, domain decision, progressed state, or unrelated file changed.

Finish with the resulting structure, convention changes, archived material, repaired references, unresolved gaps, and any skipped item with its reason.
