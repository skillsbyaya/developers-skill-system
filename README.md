# Developers Skill System

An integrated, self-improving skill system for one person building software with AI. It adapts agile product and engineering practices and draws inspiration from the [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD), while reshaping the workflow for a single user working directly with AI.

The system covers discovery, product planning, architecture, UX and UI design, implementation, testing, assurance, compliance, research, writing, project continuity, and maintenance. Its skills are designed to work together: one owner handles the current job, loads only the workflow needed, passes bounded context when specialist help is required, and preserves one source of truth for durable state.

The system improves through use. Demonstrated failures and corrections feed into lessons and skill changes that replace or remove the instruction at fault, rather than accumulating as extra rules. Ceremony, repetition, and unclear output count as defects.

## How the system works

1. Route a request directly to one clear skill owner.
2. Load one selected workflow when that owner contains several methods.
3. Keep one primary owner until its work reaches a real stopping point.
4. Use specialist consultation, assurance, or an isolated subagent only when the unresolved decision requires it.
5. Preserve one authoritative source for project state, decisions, lessons, and conventions.
6. Scale planning, evidence, review, and durable records to consequence and reversibility.
7. Keep one delivery batch across short chats: checkpoint remotely at handoff and publish once its agreed outcome and assurance are complete (`close-session`).

```text
work
  -> owner skill
  -> selected workflow
  -> evidence and assurance
  -> completion or demonstrated failure
  -> lessons
  -> skill review and change
  -> improved system
```

## Skills and subagents

Skills and subagents are separate concepts and separate installation surfaces.

- `skills/` contains reusable skill owners, workflows, references, scripts, and assets shared across Claude Code and Codex, except the documented Claude-only `use-codex` skill.
- `platform/` contains the small number of runtime-specific additions that should not be mirrored to the other platform.
- `subagents/` contains actual isolated worker definitions. These are installed separately and may be platform-specific.

### Terminology

- **Skill:** reusable instructions and supporting resources for a recurring outcome.
- **Area-owner skill:** an approachable skill that owns one domain and selects one workflow at a time. Some current names use the `agent-` prefix for these persona-led owners.
- **Workflow:** a directly selectable method inside an owner skill.
- **Subagent:** an isolated worker with its own context, tools, and permission boundary.

Area-owner skills are not Claude Code subagents. Actual Claude Code subagents live under `subagents/`.

## Installation model

This repository is the canonical distribution. Installed copies under a runtime's home directory are generated deployments, not editing sources.

| Component | Claude Code destination | Codex destination |
| --- | --- | --- |
| Shared skills | `~/.claude/skills/` | `~/.agents/skills/` |
| Platform-specific skills | `platform/claude/skills/` when present | `platform/codex/skills/` |
| Subagents | `~/.claude/agents/` | None |

Clone the repository first:

```sh
git clone https://github.com/skillsbyaya/developers-skill-system.git
cd developers-skill-system
```

On the machine where you edit the skills, link both runtimes to the clone so there is one local copy:

```sh
./scripts/install.sh --link all
```

Claude Code and Codex then read the clone directly: an edit made from either is live at once and is the same edit you commit and push. Rerun the command only when a skill is added, renamed, or removed. Without `--link`, the installer copies instead (`./scripts/install.sh all`, or `claude` / `codex` for one runtime); use copies on machines where you do not edit the skills.

The installer replaces repository-managed skill directories exactly, removes skills retired by a later repository version, preserves unrelated runtime, plugin, system, and personal skills, and installs the Claude Code subagents into `~/.claude/agents/`. Claude receives `use-codex`; Codex omits it and receives the Codex-only `read-project-guidance` bridge.

### Cloud sessions

The repository is public, so a cloud environment can install the current release at session start without copying skills into every application repository. A project keeps a small bootstrap script, run during environment setup:

```sh
git clone --depth 1 https://github.com/skillsbyaya/developers-skill-system.git /tmp/developers-skill-system
/tmp/developers-skill-system/scripts/install.sh claude
```

Use `codex` instead of `claude` for a Codex cloud environment. This tracks `main`, so cloud sessions match local ones with no per-project updates; it relies on only trusted maintainers pushing to `main`. If that ever stops being true, check out a reviewed commit or release tag after cloning instead.

Claude Code subagents are not installed into Codex. Codex can use the shared skills, but it has a different agent model and no equivalent subagent package is claimed here.

## Project status

The repository is the distribution source of truth; installed copies are deployments for a specific AI coding environment. Make changes here (directly, or through linked runtimes), validate them, and commit and push them; cloud sessions pick them up at their next start.

## Maintenance

`main` is the current public distribution. This is a one-maintainer project: changes may land directly on `main` after the affected skill checks and the complete diff pass. Use a short-lived branch when a change needs experimentation, independent review, or several commits before it is release-ready.

When work remains unfinished at a session boundary, commit and push a safe checkpoint to a non-live branch so another local or cloud session can continue. Label incomplete or failing checkpoints and do not merge until the work is complete and its required checks pass. Completed changes may follow the direct-to-`main` route above without an intermediate checkpoint branch or pull request. This preservation rule does not authorise force-pushes, bypassing branch protection, live-system changes, releases or deployments.

## Inspiration and independence

This is an independent project. It is inspired by the BMad Method and broader agile practice, but it is not affiliated with, endorsed by, or an official distribution of BMad Code, LLC.

BMad, BMad Method, and related names are trademarks of BMad Code, LLC. No affiliation or endorsement is implied.

## Licence

Released under the [MIT License](LICENSE).
