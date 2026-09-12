# Organisation and Pruning

Use this workflow for a documentation sweep, a bounded archive, an identifier-vocabulary change, or migration to agreed document conventions.

## Choose the operation

- **Sweep:** documents are messy, stale, duplicated, bloated, misfiled, or inconsistent. Inspect the relevant tree and propose a coherent target.
- **Convention migration:** the user wants existing documents brought into an agreed structure or naming system. Establish the adopted target in project context, then plan the bounded migration. Route unresolved project-rule design to `manage-project-context`, or global preference changes to `personalise-working-system`, before migrating files.
- **Archive:** a known set of documents is superseded and needs removal from the live set without deletion.
- **Identifier vocabulary:** the user wants to create, inspect, rename, merge, or prune the project's canonical identifier areas. Read [identifier conventions](../references/identifier-conventions.md) and the current project area registry at the path recorded in context, normally `reference/identifier-areas.yaml`.

Start from supplied paths and current artifacts. Read other project-context sections only when they contain decisions needed to judge the documents. For a small or moderate set, inspect every document in scope. For a large set, inventory paths and metadata first, state a meaningful boundary, then read by likely issue cluster instead of loading the whole tree.

Exclude tool-managed memory, hidden system state, generated or build output, and vendored dependencies unless the user explicitly includes them.

## Apply the conventions with judgement

Read only the relevant Documentation conventions section of the project's context. Follow explicit user requirements and binding project instructions first. If the section is missing, preserve explicit existing conventions and stable paths; report the context gap and use `manage-project-context` when establishing rules is in scope. Do not use the global template as a live rule source for a cleanup. Judge each document by what it is for and who needs it.

- **Placement and naming:** classify by purpose and lifecycle rather than title keywords, then identify the document type, folder, area, and durable distinguishing detail. When no convention fits, record a convention gap instead of forcing a match. Preserve stable paths or identifiers when churn would cost more than the inconsistency.
- **Duplication:** two documents may duplicate wholly, or share only a restated argument while both stay live. Archive a wholly superseded copy once still-useful unique content is merged; where only an argument is shared both documents usually survive, so one owner carries the reasoning and every other site keeps the conclusion and a pointer. **The owner is the document whose stated purpose is incomplete without the content** — where a record of work and a durable reference both hold it, the reference owns it and the record cites. **Check the copies still agree before choosing:** a pair that has drifted apart identifies which side is stale, and that correction is worth more than the tidy-up, but resolve it against an explicit current authority as concept staleness requires below — never by preferring the better-written copy or the more recently changed file. **Lifecycle decides whether there is anything to fix:** a live delivery record legitimately carries its own argument, while a retired or archived one is frozen history and is never edited to remove a repetition.
- **Hygiene staleness:** remove finished-work-as-current, dated session framing, obsolete navigation, duplicated history, and next-action sections that contain anything other than the actual next direction.
- **Concept staleness:** remove a reversed decision, abandoned approach, or invalid claim only from an explicit current decision or stale-concepts list. Never infer a pivot from tidy but older prose.
- **Size and structure:** split only when parts have distinct lasting purposes or readers. Keep one source intact when the real need is a shorter derivative and route that need to the `agent-writer` distillation workflow.
- **Discoverability:** repair broken inbound links and navigation. Do not reject an intentionally standalone document merely because nothing links to it.
- **Identifier routing:** keep the project's area registry to the smallest useful canonical vocabulary. Resolve genuine alternate terms through aliases, not duplicate areas. Never turn it into an item index, counter, priority list, or `next` register.

Prune always-read control and context files hardest because their cost recurs. Keep them to instructions and facts that are almost always needed; leave task history, backlog state, review logs, and detailed source material in their owners.

When the sweep finds a consequential documentation gap, report the intended reader, decision it blocks, and evidence for the gap. Do not inspect code or author domain content merely to fill it.

## Preserve evidence from preventable documentation residue

When pruning finds supported evidence that an item remained in the live set because the responsible producing or closing workflow did not clean it up at the right time, or that it should never have been recorded durably, capture one compact learning candidate instead of invoking `learn-lessons`. Record only the affected artifact, the expected lifecycle or recording boundary, how it entered or remained in the live set when known, and the consequence. Put the candidate in the current owning story or package when one exists so packet close can preserve it; otherwise include it in the current work outcome for full close. Do not create a standalone lesson note or queue entry.

Invoke `learn-lessons` with its current-correction workflow during pruning only for a serious preventable failure when delaying would genuinely lose important causal evidence, such as when cleanup must remove the only source from which the cause can be established and compact capture cannot preserve it. The urgency must come from the evidence-loss risk, not merely from the fact that the residue was preventable.

Keep the documentation cleanup moving, but do not expand it into protected skill, instruction, configuration, tool, or project changes without the authority those targets require.

## Assess convention mismatches

Treat a difference from the resolved convention as a decision to assess, not an automatic defect to normalise. For each mismatch:

1. State the adopted rule and its source in project context or an explicit binding instruction. A difference from a global template is not a project defect.
2. Describe the smallest adjustment that would conform and the practical payoff, such as clearer discovery, lower ambiguity, repaired automation, reduced recurring maintenance, or consistency that helps real readers.
3. Assess migration cost and safety: stable-path or identifier churn, inbound references, external links, hardcoded consumers, producing skills, tooling, collisions, concurrent work, archive or history value, reversibility, and risk of losing unique content.
4. Give one verdict:
   - **Adjust now:** the ongoing payoff is material and the migration is bounded and acceptably safe.
   - **Adopt forward-only:** the convention is useful for new work, but retrospective migration has little practical payoff.
   - **Retain as a project exception:** a durable local need justifies the difference; record the complete affected rule and its reason in project context when that update is authorised.
   - **Change the convention:** the mismatch exposes an unsuitable project rule or a global preference worth reconsidering; route the convention decision before migrating artifacts.
   - **Investigate further:** references, ownership, consumers, concurrency, or content consequences are too uncertain for a safe recommendation.

Do not recommend migration for cosmetic consistency alone. Group mismatches only when the same rule, adjustment, payoff, and risks genuinely apply; separate any item with a distinct consumer, collision, authority, or loss risk.

## Migrate an agreed convention

1. Read the adopted project rule and representative artifacts, including consumers that hardcode affected paths. If the target is unresolved, return the concrete mismatch and required decision to the convention owner; do not infer approval for a redesign from a cleanup request.
2. Propose file migrations, inbound-reference repairs, affected consumers, collisions, exceptions, and whether adoption is forward-only or retrospective. Preserve useful fixed-name contracts, unique content, and stable identifiers.
3. When authorised, update the affected project-context rule with its complete adopted form and any deliberate exception. Global preference changes belong to `personalise-working-system`; producing-skill changes belong to `upskill`.
4. Migrate only the approved scope and repair affected references. Do not move files merely because the global template changed.
5. Verify representative existing paths and one future path against the adopted rule. Record any forward-only boundary in context so later cleanup does not undo it.

For an identifier-vocabulary change, preserve stable base IDs and archives. Update current suffixes and affected current references only after the vocabulary change is approved. Remove an unused area only when no current ID uses it, no current document declares it, no alias or current product language needs it, and no active near-term work needs it.

## Propose, apply, and verify

Return the mismatch assessment before the target structure. Then provide an itemised list of approved candidate moves, renames, merges, splits, prunes, convention edits, and archives. Tie each candidate to its verdict and include references that must change. Include meaningful no-change decisions where forward-only adoption, a justified project exception, uncertainty, stable paths, or existing authority outweigh migration.

Show that plan before moving, renaming, merging, splitting, pruning, or archiving existing material. After approval, apply only its scope; preserve unrelated content and stop on a collision, ambiguous merge, concurrent edit, or broader consequence. Archive superseded material when it retains recovery value; delete only with explicit approval.

Then verify:

- every changed path exists once and every archived item left the live set;
- inbound relative links and explicit path references resolve;
- current facts have one authority and no approved unique content was lost;
- adopted rules in project context describe the resulting and future placement, including deliberate exceptions; and
- no backlog ordering, domain decision, progressed state, or unrelated file changed.

Finish with the resulting structure, convention changes, archived material, repaired references, unresolved gaps, and any skipped item with its reason.
