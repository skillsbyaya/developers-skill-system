# Developers Skill System

An integrated, self-improving skill system for one person building software with AI. It adapts agile product and engineering practices and draws inspiration from the [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD), while reshaping the workflow for a single user working directly with AI.

The system covers discovery, product planning, architecture, UX and UI design, implementation, testing, assurance, compliance, research, writing, project continuity, and maintenance. Its skills are designed to work together: one owner handles the current job, loads only the workflow needed, passes bounded context when specialist help is required, and preserves one source of truth for durable state.

The system improves through use. Demonstrated failures and corrections feed into lessons, skill audit, repair, restructuring, pressure testing, and verification rather than accumulating as unstructured instructions.

## How the system works

1. Route a request directly to one clear skill owner.
2. Load one selected workflow when that owner contains several methods.
3. Keep one primary owner until its work reaches a real stopping point.
4. Use specialist consultation, assurance, or an isolated subagent only when the unresolved decision requires it.
5. Preserve one authoritative source for project state, decisions, lessons, and conventions.
6. Scale planning, evidence, review, and durable records to consequence and reversibility.

```text
work
  -> owner skill
  -> selected workflow
  -> evidence and assurance
  -> completion or demonstrated failure
  -> lessons
  -> skill audit, repair, or restructure
  -> pressure test and verification
  -> improved system
```

## Skills and subagents

Skills and subagents are separate concepts and separate installation surfaces.

- `skills/` contains reusable skill owners, workflows, references, scripts, and assets.
- `subagents/` contains actual isolated worker definitions. These are installed separately and may be platform-specific.

### Terminology

- **Skill:** reusable instructions and supporting resources for a recurring outcome.
- **Area-owner skill:** an approachable skill that owns one domain and selects one workflow at a time. Some current names use the `agent-` prefix for these persona-led owners.
- **Workflow:** a directly selectable method inside an owner skill.
- **Subagent:** an isolated worker with its own context, tools, and permission boundary.

Area-owner skills are not Claude Code subagents. Actual Claude Code subagents live under `subagents/`.

## Installation model

The initial release is one integrated system rather than several independent topical packs.

| Component | Claude Code destination | Codex destination |
| --- | --- | --- |
| Skills | `~/.claude/skills/` | `~/.agents/skills/` |
| Subagents | `~/.claude/agents/` | Platform-specific support to be assessed |

Clone the repository first:

```sh
git clone https://github.com/skillsbyaya/developers-skill-system.git
cd developers-skill-system
```

For Claude Code:

```sh
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R skills/. ~/.claude/skills/
cp subagents/claude-code/*.md ~/.claude/agents/
```

For Codex, install the shared skills but omit the Claude-only `use-codex` skill:

```sh
mkdir -p ~/.agents/skills
for skill in skills/*; do
  [ "$(basename "$skill")" = "use-codex" ] || cp -R "$skill" ~/.agents/skills/
done
```

These commands update matching files but do not remove obsolete files from an earlier release. If replacing an existing installation, back it up and remove the old matching skill directories first when a clean replacement matters.

Claude Code subagents are not installed into Codex. Codex can use the shared skills, but it has a different agent model and no equivalent subagent package is claimed here.

## Project status

This is the first public release of the system. The repository is the distribution source of truth; installed copies are deployments for a specific AI coding environment.

## Maintenance

`main` is the current public distribution. This is a one-maintainer project: changes may land directly on `main` after the affected skill checks and the complete diff pass. Use a short-lived branch when a change needs experimentation, independent review, or several commits before it is release-ready.

## Inspiration and independence

This is an independent project. It is inspired by the BMad Method and broader agile practice, but it is not affiliated with, endorsed by, or an official distribution of BMad Code, LLC.

BMad, BMad Method, and related names are trademarks of BMad Code, LLC. No affiliation or endorsement is implied.

## Licence

Released under the [MIT License](LICENSE).
