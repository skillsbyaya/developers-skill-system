---
name: learn-lessons
description: "Prevents recurrence after a correction or delivery mistake, reviews and resolves unresolved agent-behaviour lessons, and runs retrospectives across completed epics, releases, milestones, or chosen work blocks. Use when the user explicitly asks to learn from a current failure, work through the lessons queue, find cross-work patterns, or check whether earlier improvements held."
---

# Learn Lessons

Turn supported evidence from a current correction or completed body of work into the smallest durable improvements, while keeping project consequences and global agent-behaviour prevention with their proper owners.

## Select one workflow

Read exactly one workflow:

| Request | Read |
| --- | --- |
| Learn from the current correction, mistake, or confirmed close-session lesson | [Current correction](workflows/current-correction.md) |
| Review, implement, accept, merge, or clear existing unresolved lessons | [Review queue](workflows/review-queue.md) |
| Review a completed epic, release, milestone, or chosen work block for cross-work patterns and improvements | [Completed-work retrospective](workflows/completed-work-retrospective.md) |

An explicit workflow request selects it directly without consultation or sibling loading. Use current correction for one triggering exchange, queue review for existing unresolved entries, and completed-work retrospective for synthesis across several completed items or one consequential completed event. A `close-session` handoff may select only current correction.

Do not auto-trigger from frustration, generic criticism, a factual correction, cleanup alone, a simple status question, or a request whose primary job is editing a skill. Follow an `organise-docs` handoff during pruning only when it states that a serious preventable documentation-practice failure would lose important causal evidence if current correction were delayed. Routine preventable residue is captured compactly for packet or full close and does not trigger this skill.

## Ownership

`~/.claude/LESSONS.md` is the single queue for unresolved agent-behaviour improvements. This skill alone creates, merges, increments, or removes its entries.

The queue is not history, native memory, project context, or a defect backlog. Route:

- durable project facts and constraints to the project-context owner;
- corrective delivery work to the active story, change package, or backlog owner;
- skill creation or change to `upskill`;
- instruction, configuration, tool, hook, or deterministic-check changes to their canonical owner; and
- only an unresolved preventable behaviour pattern to `LESSONS.md`.

A completed-work retrospective does not write to `LESSONS.md`. When it identifies a supported agent-behaviour correction, finish the retrospective with the exact evidence and select current correction only if the user asks to continue; do not preload both workflows.

A single incident may justify a durable fix when the cause and prevention are clear. Recurrence strengthens only an entry that is still unresolved. Once the fix is applied and verified, remove the entry; a later recurrence starts new evidence at `×1`.

## Protected changes

Queue maintenance is part of this skill. Changes to skills, instruction files, skill metadata, hooks, scripts, configuration, tools, or project artifacts require the authority appropriate to that target. An explicit request to apply a specific correction supplies that authority; a general request to “learn lessons” does not.

Finish with the selected scope, evidence and limitations, conclusions, destinations used, changes and verification completed, and anything that remains unresolved.
