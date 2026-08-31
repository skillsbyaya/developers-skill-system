# Review Queue

Read the complete current `~/.claude/LESSONS.md`, then inspect only the present owner files directly relevant to each entry. If the queue is absent or empty, report that no unresolved lessons exist and do not create it. Do not search old session transcripts to reconstruct missing context.

For each entry, recommend one outcome:

- **Implement** — current evidence supports a durable prevention and its owner.
- **Accept as-is** — the user consciously accepts the behaviour or trade-off; remove the entry only after that explicit choice.
- **Keep unresolved** — evidence, intended behaviour, ownership, or a safe prevention remains unclear. Not available to an entry at `×3` or beyond whose recorded resolution is an application gap against rules that already exist: recurrence at that count is evidence the rule cannot be applied as written, so recommend Implement instead.
- **Merge** — two entries describe the same unresolved root cause; show the proposed combined wording and recurrence count before changing them.

Return a compact list or table with the entry, recommendation, reason, likely owner, and evidence limitation. Let the user choose which protected changes or accepted trade-offs to apply. A queue-review request authorises queue maintenance needed for approved merges or removals, but does not by itself authorise edits to other protected files.

For each selected Implement item:

1. Treat the entry and current owner evidence as the starting observation; separate the inferred root cause and strongest plausible alternative.
2. Prefer the existing owner that can prevent the cause. Name the actor that runs at the moment the failure occurs and the artefact it reads then; the owner must be that artefact, established by naming rather than by judging a candidate adequate. Test whether the exact prevention would have changed the recorded failure without burdening a neighbouring case.
3. Present the target, exact change, expected benefit, and material trade-off before changing a protected target unless that specific change was already authorised.
4. Process one coherent owner change at a time and run the smallest finished-behaviour check that could disprove it.
5. Remove the entry only after the prevention is installed and the check passes. Keep it unresolved when authority is declined, evidence remains weak, or verification fails.

Keep one compact line per unresolved root cause:

```markdown
- [YYYY-MM-DD ×N] <behavioural failure class in goal terms> — <current evidence or context needed to resolve it>
```

Do not add status fields, completed entries, project-specific task detail, transcripts, or facts that native memory already owns.

Leave the queue with unresolved entries only, no duplicate root causes, and no accepted or implemented history.
