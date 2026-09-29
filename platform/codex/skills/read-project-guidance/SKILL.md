---
name: read-project-guidance
description: Loads a project's CLAUDE.md and project-context.md so Codex shares Claude's project instructions and durable implementation context. Use before substantive work in an existing project that contains either file, and when work moves into a differently scoped project area.
---

# Read Project Guidance

Before substantive project work, load the following once per conversation context. Reuse sources already read and still available; invoking another skill is not a reason to reload them. After compaction or an external edit, retrieve the missing or changed guidance before relying on it.

1. Resolve the project or repository root from the current workspace.
2. Read the root `CLAUDE.md` when present. If the work is inside a directory governed by a closer `CLAUDE.md`, read that file too and apply it within its scope.
3. Read the root `project-context.md` when present, or the project-context file explicitly named by `CLAUDE.md`.
4. Treat those files as the authoritative sources for current project directives, state, constraints, and durable implementation patterns. Read only the linked material relevant to the task.
5. If either file is absent, continue with the available project instructions. Do not create, reconstruct, or copy a missing source unless the user asks.

When the task changes area or a consequential action depends on project policy, re-read the relevant source section before acting. Surface material conflicts or ambiguity instead of silently combining incompatible rules.

Keep this skill as a pointer. Do not copy project rules, state, or context into this skill or another Codex-only instruction file. When an authorised change is needed, update the authoritative project source.

## Hard limits

- **Anything real users or real data depend on:** Never deploy or push changes to a live system that real users or real data rely on without confirming first and surfacing risks. Before a project has real users, working directly in live is fine.
- **Database schema changes:** Never run migrations or alter schemas without explicit confirmation.
- **File deletions and restructuring:** Removing dead code just replaced is fine. Deleting, renaming, or moving files not created in the current piece of work needs a quick confirmation first.
