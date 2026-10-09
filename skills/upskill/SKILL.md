---
name: upskill
description: Creates, changes, simplifies, reviews, or removes reusable Claude Code skills, and finds external skills worth adopting. Use when the user wants a new skill, a skill fixed or made lighter, a skill's triggering or output changed, a review of one skill or the whole library, or outside skills compared with theirs. Not for ordinary project work that merely involves skills.
---

# Upskill

A skill earns its place only when sessions that use it finish faster or better than sessions without it. Every loaded instruction costs context and is followed literally, so a needless step is not harmless: it slows every run, and a wrong one does damage every run. Treat ceremony, repetition and unclear output as defects, as serious as a missing capability.

## Where changes go

Edit the canonical source, never an installed copy. When the library is a cloned repository with an install script, the clone is the source and `~/.claude/skills/` (Claude Code) and `~/.agents/skills/` (Codex) are deployments: edit the clone, run its installer, commit and push, then tell the user which projects pin an older commit of the library. Without a repository, personal skills live in `~/.claude/skills/` and project skills in the project's `.claude/skills/`.

## Choose the job

| The user wants | Do |
| --- | --- |
| A skill fixed, simplified, retargeted, merged, split or removed | [Change a skill](#change-a-skill) below |
| A new skill | [Create a skill](references/create-skill.md) |
| A judgement on one skill or the whole library | [Review skills](references/review.md) |
| External skills or patterns worth adopting | [External discovery](references/external-evidence.md) |

When asked to review and fix, review and then change without asking again. Ask first only when a fix changes what a skill is for or removes something the user may rely on.

Read [platform compatibility](references/platform-compatibility.md) when changing frontmatter, invocation or file structure, and [worker use](references/worker-use.md) when adding or changing subagent use.

## Writing standard

Apply this to every line written or changed, and use it as the review checklist.

1. **Write only what changes behaviour.** Delete what a capable model does anyway ("be thorough", "check your work", "consider edge cases"), restated principles, rationale, history, and prohibitions against things nobody would do.
2. **Say it once.** Each rule lives in the one file that loads when it is needed. A rule repeated in the core and a workflow is applied twice and drifts. Do not repeat the user's global instructions inside skills.
3. **Plain and concrete.** Short sentences, everyday words, an example rather than an abstract category. If a sentence needs a second reading, rewrite it. Avoid invented vocabulary unless the skill defines it once and uses it often.
4. **Lightest process by default.** A review, confirmation, walkthrough, record, worker, handoff or extra session is mandatory only when the instruction names the risk it prevents and that risk is likely enough to justify the cost on every run. Put heavier process behind an explicit condition, never a default. Each split into smaller units or sessions costs a handoff and a re-read; split only where one unit cannot be finished and verified in one go.
5. **Specify the output.** Where a skill reports to the user, say what the report contains and how long it is: normally the outcome first, then anything the user must do or decide, then nothing else. Do not repeat what is already on screen, restate one fact in several sections, list checks that passed, or narrate the process.
6. **Prevent before instructing.** Prefer a script, template or removed step over an instruction to remember something. A repair that only adds text is suspect: find the text that caused the failure and change or delete it.
7. **Load only what is needed.** The core holds what every run needs; anything else loads on a stated condition. Do not split a short skill into files, and do not make a model open a file only to learn it was not needed.
8. **Keep personal skills portable.** No project names, paths, decisions or history in a personal skill.

## Change a skill

1. **Find the cause.** For a reported behaviour, look for it in a real transcript (Claude Code: `~/.claude/projects/<project>/*.jsonl`; Codex: `~/.codex/sessions/`), reading only what the question needs, and locate the instruction that produced it. The cause is usually an instruction that over-asks, repeats or is vague, not a missing one.
2. **Fix the class.** Correct every occurrence of the same pattern in the skills in scope, and name other skills that share it so the user can widen the work.
3. **Replace or delete before adding.** Apply the writing standard to the text you touch. For a merge or split, decide which jobs land in which skill first, then move only content that passes the standard.
4. **Keep references whole.** When renaming, moving or removing a file or skill, search the library for references and update them in the same change. Remove a capability only once its genuine uses have somewhere to go.
5. **Check in proportion.** Parse changed frontmatter, resolve changed links and run changed scripts. Then read the changed skill as the model that will execute it, against the reported case and one ordinary request: it should do the right thing with no extra steps. When the description changed, compare it with neighbouring descriptions.
6. **Ship and report.** Ship as described in [Where changes go](#where-changes-go). Report what changed and why, the size of each changed file before and after, and anything the user should try. A net size increase needs a stated reason.
