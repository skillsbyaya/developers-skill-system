# Area Context Review

Build a current cross-artifact map for one canonical project area before product shaping, bundling, prioritisation, or a user decision. This workflow is read-only. It uses identifiers as routing aids and does not create an item index, rewrite source artifacts, allocate IDs, or decide another owner's question.

## Establish the area and scope

1. Resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) and the project's registered `identifier-areas` file, normally `reference/identifier-areas.yaml`.
2. Resolve the user's term to one canonical area, including a declared alias. If no registry exists or no area fits, inspect only enough current product language to recommend a canonical area; do not silently create it during this read-only workflow. When the project has not adopted routed IDs yet, continue from explicitly supplied and clearly current sources, use a bounded text search for the proposed area and genuine alternate terms, and report reduced retrieval confidence.
3. Establish the decision this review must support: an area overview, backlog shaping, epic/story bundling, priority choice, conflict resolution, or another bounded planning question.

For a simple request about one known item, read that item directly instead of running an area review. For a project-wide implementation-readiness verdict, use `check-work` after the planning set is known.

## Route, triage, and deepen

Search current authoritative project documentation for the exact dotted area segment, whether primary or secondary. For example, route `Invoicing` with a complete-segment search such as:

```sh
rg -n '\.Invoicing([.]|[^[:alnum:]_]|$)' <current-documentation-paths>
```

Exclude archive folders, superseded whole documents, generated output, and history by default. Include current candidates across relevant types: backlog items (`B`), requirements (`FR`), architecture decisions (`A`), general decisions (`D`), epics and stories (`E`, `S`), review findings (`RV`), obligations (`OB`), risks (`RK`), controls (`CT`), evidence (`EV`), and preserved legacy IDs with canonical area suffixes.

Then:

1. Group matches by item type, source authority, and current lifecycle.
2. Read each matched section before loading a whole document. Discard stale, retired, completed-as-history, or false-positive matches.
3. Follow explicit dependencies, superseding links, requirement coverage, and lineage even when the related item has another area.
4. Broaden beyond identifier matches when the source shows a material cross-cutting dependency, conflict, risk, or missing routing suffix. Treat a missing suffix as a discoverability finding, not proof the substance is absent.
5. When adoption is partial or a material omission is plausible, run a bounded secondary search for the canonical area and declared aliases in current headings, filenames, and likely authoritative sources. Triage these results separately; do not turn every prose mention into an area item.
6. For money movement, authentication, authorisation, security, destructive behaviour, privacy, safety, or compliance, read the fuller relevant authoritative source and obtain the appropriate specialist judgement before relying on a section-level summary.

Do not read every matching document end to end merely because it contains the area. Do not treat an ID match as proof that an item is current, relevant, or authoritative.

## Build the map

Return only categories supported by current evidence:

- area boundary and the planning question;
- accepted product requirements and unresolved requirement choices;
- accepted, proposed, deferred, or superseded decisions;
- architecture constraints and open technical choices;
- committed delivery and its current owner;
- backlog candidates and future plans;
- obligations, risks, controls, and material evidence gaps;
- dependencies, overlaps, contradictions, and missing coverage; and
- source-quality or routing gaps that could have hidden relevant work.

Pair every ID with its human title and source. Distinguish authoritative facts, user decisions, inference, and unresolved questions. Ask the user only the material questions whose answers could change scope, priority, bundling, acceptance, or risk. When the review precedes epics and stories, finish with the coherent candidate work set and excluded items with reasons; move to decomposition only after material user decisions are resolved or explicitly deferred.

## Finish

Report the canonical area and any alias used, sources and lifecycle boundary searched, the decision-ready area map, important omissions or confidence limits, material user questions, and the recommended next PM or specialist workflow. Create no durable review artifact unless the user separately asks for one and its purpose and home are agreed.
