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
7. Keep one delivery batch across short chats: checkpoint remotely at handoff and publish once its agreed outcome and assurance are complete.

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

- `skills/` contains reusable skill owners, workflows, references, scripts, and assets for Claude Code.
- `subagents/` contains actual isolated worker definitions. These are installed separately.

### Terminology

- **Skill:** reusable instructions and supporting resources for a recurring outcome.
- **Area-owner skill:** an approachable skill that owns one domain and selects one workflow at a time. Some current names use the `agent-` prefix for these persona-led owners.
- **Workflow:** a directly selectable method inside an owner skill.
- **Subagent:** an isolated worker with its own context, tools, and permission boundary.

Area-owner skills are not Claude Code subagents. Actual Claude Code subagents live under `subagents/`.

## Installation model

This repository is the one source. It is also a Claude Code plugin marketplace (`.claude-plugin/marketplace.json`) holding one plugin, `devkit`, which serves every skill under `skills/` and the subagents under `subagents/claude-code/`. Installed copies are generated from it; nobody edits them.

Add the marketplace once to the Claude account, at claude.ai → Customize → Plugins → Add, by its URL:

```text
https://github.com/skillsbyaya/developers-skill-system
```

Then install `devkit` from it. Account plugins reach every Claude Code session on that account, cloud and desktop alike, so no project repository copies or installs the skills. In a session they are named `devkit:<skill>`, for example `devkit:agent-dev`.

In a terminal without the account, the same plugin installs with:

```sh
/plugin marketplace add skillsbyaya/developers-skill-system
/plugin install devkit@developers-skill-system
```

Claude Code updates the plugin only when `version` in `.claude-plugin/plugin.json` changes, so every change that lands on `main` raises it: the last number for a wording fix, the middle one for a changed or added skill, the first for a removed or renamed one. Only trusted maintainers push to `main`, because every session runs what it holds.

## Maintenance

`main` is the current public distribution. This is a one-maintainer project: changes may land directly on `main` after the affected skill checks and the complete diff pass. Use a short-lived branch when a change needs experimentation, independent review, or several commits before it is release-ready.

When work remains unfinished at a session boundary, commit and push a safe checkpoint to a non-live branch so another local or cloud session can continue. Label incomplete or failing checkpoints and do not merge until the work is complete and its required checks pass. Completed changes may follow the direct-to-`main` route above without an intermediate checkpoint branch or pull request. This preservation rule does not authorise force-pushes, bypassing branch protection, live-system changes, releases or deployments.

## Inspiration and independence

This is an independent project. It is inspired by the BMad Method and broader agile practice, but it is not affiliated with, endorsed by, or an official distribution of BMad Code, LLC.

BMad, BMad Method, and related names are trademarks of BMad Code, LLC. No affiliation or endorsement is implied.

## Licence

Released under the [MIT License](LICENSE).
