# Subagents

This folder is for actual isolated worker definitions, separate from reusable skills.

The current Claude Code system uses four bounded subagents, stored under `claude-code/`:

- `evidence-reader`
- `persona-panelist`
- `skill-scout-quarantine`
- `untrusted-content-reader`

These definitions have restricted tools and specific safety or independence roles. They must be installed into the platform's subagent location rather than its skills location. The first release will document Claude Code installation explicitly and will claim Codex support only where an equivalent, enforceable worker boundary has been verified.
