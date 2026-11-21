# Subagents

This folder is for actual isolated worker definitions, separate from reusable skills.

The current Claude Code system uses two bounded subagents, stored under `claude-code/`:

- `evidence-reader`
- `skill-scout-quarantine`

These definitions have restricted tools and specific safety or independence roles. The `developer-skills` plugin serves them as subagents, not skills: `.claude-plugin/plugin.json` lists them under `agents`.
