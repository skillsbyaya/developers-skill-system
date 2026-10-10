---
name: close-session
description: "Closes a working session: saves what the next session needs, preserves the work in Git, and gives one clear handoff. It is the only route that lands repository work, so use it whenever finished work is ready to merge or ship, including after a review and its fixes; also use it after agent-dev finishes or stops delivery work, or when the user says to wrap up, close or end the session, stop for today, or otherwise signals that the session is ending."
---

# Close Session

A close does three things: makes sure nothing the next session needs exists only in this conversation, preserves the work in Git, and tells the user in a few lines where things stand and what happens next. It does not continue the work, start new work, run reviews, or complete a story.

- **Packet close:** agent-dev finished or stopped one named packet or slice. The packet's boundary holds: agent-dev's delivery controls decide what a packet may change, and a close never widens it.
- **Full close:** anything else, including any sign from the user that the session is ending.

Work lands only through a close, whatever skill or instruction produced it, so step 2 owns the order of reporting and landing. A project instruction that names a landing command, such as a ship script, describes how step 2 lands, not a separate trigger.

Work from what this session already knows. Do not rerun checks, survey the project, or reread broad sources. If a close already ran in this conversation, cover only what changed since and never repeat a change report already posted.

## 1. Save what exists only in the conversation

The record that owns the work (story, change package or plan) must hold its current state, the exact next step, and any decision, constraint, rejected approach or correction that later work needs and that is written nowhere else. Write what is missing into the document that owns it, replacing outdated text rather than appending a session diary. Update another document only when this session made it wrong.

- A delivery-status or next-steps document is replaced, not appended: writing the new next action removes the one it supersedes, along with any note another document now holds.
- Send a confirmed correction to agent behaviour through `learn-lessons` current correction only when it would otherwise be lost.
- Create no session log, handoff file or summary document.

## 2. Preserve the work in Git

Skip this when the session changed nothing in a repository.

1. Follow the project's declared Git workflow. Stop and name the blocker when the workflow is unclear, the branch is wrong for the work, or session work cannot be separated from unrelated changes, secrets or local environment files.
2. Stage explicit paths. Recheck the branch and every staged path immediately before committing.
3. Commit and push session work to its non-live working branch so a fresh local or cloud session can resume it. Start the message with `checkpoint:` when the work is incomplete or its checks fail; a checkpoint is never landed.
4. Land a completed unit when the project's workflow authorises it, in this order. A packet lands only when the project's workflow lands each packet.
   1. **Change report first,** unless one already posted covers every current change: what changed, grouped by document and by code area, in plain terms, naming each judgement call and any new wording. Write it from what the session already knows. It is not an approval gate; carry straight on unless it contains a decision that is the user's to make.
   2. **Then land, in the same turn:** pull request, gates and merge as one action, run in the background when it waits on remote gates so comments can still arrive. A mergeable pull request left open is unfinished work, not a handoff.
   3. **A comment before the merge** goes into the same pull request: make the accepted change, rerun its affected checks, and make sure only the updated head merges, after its gates pass.

Never report a commit, push or merge that did not happen. If the work cannot reach the remote, say so: the next session cannot resume in the cloud.

## 3. Ask, then choose one next action

Ask every decision this session surfaced that is the user's to make, in one round of questions, before writing the output. Do not invent questions. Carry a decision forward only when something must happen first, and name it.

Choose exactly one next action, taking the first that applies:

1. the same unit, when it is incomplete or its checks failed;
2. a user action or decision that blocks the next step;
3. an independent review the story record requires before the next step;
4. the next ready packet;
5. the next item in the project's ordered backlog or plan, when the order is unambiguous; otherwise the user's answer to where the project goes next, asked in the round above.

## Output

The whole output, with each fact said once:

1. **Status:** one or two plain sentences on what was done, whether checks passed, and where the work is (merged, pushed to a named branch, or the Git blocker). Link a saved document only when the user will want to open it, such as where their decision was recorded.
2. **Problems:** a short list only for failing checks, unsafe or unresolved state, or something the user must do that is not the handoff. Omit it otherwise. Never use it for things already saved in a document.
3. **Handoff,** exactly this shape:

```markdown
### Handoff

> **New session:** <what the next session is about, in plain words> — On `<branch>`, <verb> <unit> with <skill> from `<repository-relative record path>`.
>
> **Model:** <capability class> — <model>.
>
> **Effort:** <level>.
```

For a blocker, the first line is `> **You:** <the one action>` or `> **Waiting for <who>:** <what>`, with Model and Effort `not applicable`.

Naming the skill carries its procedure: do not restate gates, record updates, review steps or when to stop. Use the project's model-routing policy when it has one. Otherwise use High capability for consequential or unsettled judgement and Standard for settled, well-tested work; effort medium for settled implementation, high for consequential work or review, low only for mechanical work. Name a model only when it is known to be available.

No recap, no list of checks that passed, no list of saved files, no empty sections, no second next action. End the session after the output.
