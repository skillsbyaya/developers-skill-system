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
7. Commit and push a safe non-live checkpoint at every session boundary so work can continue locally or in the cloud.

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
| Subagents | `~/.claude/agents/` | Platform-specific support to be assessed |

Clone the repository first:

```sh
git clone https://github.com/skillsbyaya/developers-skill-system.git
cd developers-skill-system
```

Install or refresh both local runtimes:

```sh
./scripts/install.sh all
```

Install only one runtime when needed:

```sh
./scripts/install.sh claude
./scripts/install.sh codex
```

The installer replaces repository-managed skill directories exactly, removes skills retired by a later repository version, and preserves unrelated runtime, plugin, system, and personal skills. Claude receives `use-codex`; Codex omits it and receives the Codex-only `read-project-guidance` bridge. Claude Code subagents remain a separate installation surface.

### Cloud sessions

The repository is public, so a cloud environment can load a reviewed release without copying skills into every application repository. Pin the setup to a trusted commit or immutable release tag; do not fetch and execute a moving branch on every session start:

```sh
git clone https://github.com/skillsbyaya/developers-skill-system.git /tmp/developers-skill-system
git -C /tmp/developers-skill-system checkout --detach <trusted-commit>
/tmp/developers-skill-system/scripts/install.sh codex
```

Use `claude` instead of `codex` for a Claude Code cloud environment. A project may keep a small bootstrap script containing the reviewed commit; it should not vendor the whole skill library. Update that pin deliberately after reviewing a new skill-system commit. For an Agents API sandbox, the pinned repository's `skills/` directory may instead be registered as a capability directory, with platform-specific skills added separately.

Claude Code subagents are not installed into Codex. Codex can use the shared skills, but it has a different agent model and no equivalent subagent package is claimed here.

### Upgrading documentation conventions

After updating the integrated skills, remove these obsolete resources from each installed skill root (`~/.claude/skills/` or `~/.agents/skills/`), preserving any personal customisations first:

- `organise-docs/doc-conventions.csv`
- `organise-docs/references/convention-resolution.md`
- `organise-docs/templates/project-conventions.md`

Global document defaults now live in [`manage-project-context/templates/documentation-conventions.md`](skills/manage-project-context/templates/documentation-conventions.md). Use `manage-project-context` to adopt the relevant rules into each project's existing context. If a project has a separate convention record, consolidate its valid local rules and update its pointers before retiring it. Established project rules and document paths are preserved unless an explicit adoption task changes them.

## Project status

The repository is the distribution source of truth; installed copies are deployments for a specific AI coding environment. Make changes here, validate them, commit and push them, then run the installer to refresh local Claude and Codex copies.

Material changes are recorded in the [change log](CHANGELOG.md).

## Maintenance

`main` is the current public distribution. This is a one-maintainer project: changes may land directly on `main` after the affected skill checks and the complete diff pass. Use a short-lived branch when a change needs experimentation, independent review, or several commits before it is release-ready.

Every working session commits and pushes a safe checkpoint to a non-live branch so another local or cloud session can continue. A checkpoint with failing or incomplete work must be labelled and must not be merged. This standing preservation rule never authorises a force-push, a direct push to a live or protected branch, a release, or a deployment.

## Inspiration and independence

This is an independent project. It is inspired by the BMad Method and broader agile practice, but it is not affiliated with, endorsed by, or an official distribution of BMad Code, LLC.

BMad, BMad Method, and related names are trademarks of BMad Code, LLC. No affiliation or endorsement is implied.

## Licence

Released under the [MIT License](LICENSE).
