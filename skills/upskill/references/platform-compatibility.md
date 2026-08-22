# Claude Code Skill Compatibility

Read this reference only when current Claude Code behavior affects naming, metadata, discovery, invocation, execution context, permissions, or file structure. Verify volatile details against the current [official Claude Code skills documentation](https://code.claude.com/docs/en/skills) before relying on them; update this reference when the platform changes.

## Current contract

- A skill is a directory containing `SKILL.md`. Personal skills live under `~/.claude/skills/`; project skills live under `.claude/skills/` and depend on repository trust and context.
- Frontmatter is YAML between `---` delimiters.
- A supplied `name` may use only lowercase letters, numbers, and hyphens and is limited to 64 characters. If it is omitted, the directory name supplies it. Choose a specific name that reflects the skill's job. Avoid vague names such as `helper` or `utils`; use a vendor name only when the skill is genuinely vendor-specific.
- Give every installed skill a specific, non-empty, third-person description. Put the key use case first and say what the skill does and when to use it through positive natural-request cues. Follow the core description-minimality rule; use the smallest exclusion only for a demonstrated cue collision that would otherwise select the wrong skill.
- `when_to_use` may add trigger context. The combined `description` and `when_to_use` listing text is subject to the current configured per-skill limit, whose documented default is 1,536 characters. Treat that as a volatile listing behavior, not a writing target, and verify the installed configuration when the limit matters.
- By default, both the user and Claude may invoke a skill. `disable-model-invocation: true` makes it user-only and removes its description from Claude's automatic skill context. `user-invocable: false` hides it from the menu while retaining model invocation. Choose these controls from the intended entry and side-effect boundary.
- `allowed-tools` pre-approves matching tools while the skill is active; it does not remove other tools or create a safety sandbox. Enforce denied capabilities through actual permission or execution controls.
- `context: fork` runs the skill in a subagent context without conversation history and requires an actionable task, not reference-only guidance. Choose an `agent` only when that execution context is necessary.
- Other supported fields include argument hints and mappings, model and effort overrides, hooks, path-scoped activation, and shell selection. Add them only when their documented behavior is needed.

Keep supporting files close to the skill, link them with stable relative paths, and state exactly when each should load. Validate frontmatter parsing, name and directory agreement, links, and invocation behavior in the installed environment. Do not copy platform field lists or limits into unrelated route files.
