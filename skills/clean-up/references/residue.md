# Residue check

Residue is text that says how the system got here instead of how it is. It builds up when a change is patched on top of the text it made wrong. Remove it, and leave no note that you did.

**Test each sentence:** would a session that never knew the earlier state act differently without it? If not, it goes.

## What to remove

| Kind | Looks like | Do |
| --- | --- | --- |
| Tombstone | "retired on…", "no longer", "formerly", "replaces the old…", a table row marked "not used" | Delete. Keep only a current fact the text would lack without it. |
| Ghost rule | A prohibition, exception, pointer or reassurance that only makes sense against something now gone | Confirm the thing is gone, then delete. |
| Fixed-problem note | "Fixed in…", "landed as…", the incident that led to a rule | Delete. A note that holds nothing else goes whole, with its index line. |
| Stacked amendment | A rule followed by "since…", "also…", "except…", "correction:" | Rewrite as one current rule that behaves the same. |
| Change narrative | "now", "new", "as of", "going forward", or a name-and-date stamp on a current rule | Rewrite in plain present tense, unstamped. |
| Patch for another source | A note or paragraph correcting a stale claim that still stands elsewhere | Correct the source and delete the patch. |
| Standing workaround | Steps for getting round a defect in something the user owns: a script, hook, configuration, skill or check | Fix the defect and delete the steps. When the fix is more than this sweep can verify, pass it to the backlog owner and leave the steps beside that item's ID. |

Keep the current rule and the one clause of reason a session needs to apply it to a case it does not list. Keep the same words where they are the subject matter: a retired product, a legacy system being migrated. Leave archives, applied migrations and finished delivery records alone; they are history by design.

## Where to look

1. **Everything loaded at session start**, read in full: each instruction file in the chain (global, parent and project), and the runtime's memory index and notes. A memory index line is a short pointer; trim one that carries the note's content.
2. **The documents those files name as authorities for how work is done**: workflow, conventions, script and test guides, the queue, the backlog. Rank them with `sh scripts/residue-scan.sh <path>…` from this skill's folder and read the highest in full. The scan finds marker words only. Ghost rules and workarounds carry none, so a file read in full is the only complete check.
3. **A skill library**, when the project is one or the user includes it.
4. **Product and design documents** only when the user includes them. Ask first when a sweep would touch files that open branches are editing.

## Clean and report

Edit directly. This removal changes no live rule, so it needs no confirmation. When unsure whether a sentence is a live rule, leave it and list it. The reason for each removal goes in the commit message.

Then find the producer. When several instances share a kind, find the instruction, template or step that told a session to write them, such as one asking for a record of why something changed, and change it through its owner (`upskill` for a skill). Cleaning without this refills.

Report words before and after for each surface, each workaround passed on with its ID, the producer changed, and the unsure list.
