# Session Data

Load this reference only for a system-wide or recent-session token audit. Session transcripts may contain sensitive prompts, paths, and outputs: aggregate the minimum fields needed and do not reproduce prompt content in the report.

## Locate a bounded window

Claude Code session history is normally stored as JSONL under:

```text
~/.claude/projects/<encoded-project>/<session-id>.jsonl
```

Subagent transcripts may appear below a session's `subagents/` folder. For a recent audit, begin with primary session files modified during an agreed window such as seven days. Inspect subagent files only when worker cost or timing is a live hypothesis.

The format is platform-owned and may change. Parse defensively, skip malformed records, and inspect keys on a small current sample before relying on a field.

## Current useful fields

As observed on 2026-07-16, assistant records store usage under `message.usage`:

| Field | Use |
| --- | --- |
| `input_tokens` | Fresh uncached input for the message |
| `cache_creation_input_tokens` | Input written to cache |
| `cache_read_input_tokens` | Input served from cache |
| `output_tokens` | Generated output |

Useful derived measures:

- **Approximate context at a message:** input + cache creation + cache read.
- **Peak context:** maximum approximate context in one session.
- **Non-cached work proxy:** input + cache creation + output. This is not a price calculation.
- **Cache-read ratio:** cache read divided by total input-side tokens. Interpret with the surface's caching behaviour and task shape; a low ratio is a lead, not a defect.

Other current evidence:

- top-level `timestamp` gives event timing, though first-to-last duration can include idle time;
- `attachment.type == "skill_listing"` may expose available skill names and count;
- `assistant.message.content[]` items with `type == "tool_use"` identify tool calls;
- a `Skill` tool call records the selected skill in `input.skill`;
- an `Agent` tool call records a worker spawn and its position in the session; and
- file paths, branch, permission mode, model, and other metadata may appear in top-level records but should be read only when they can change the diagnosis.

## Aggregate without retaining prompts

For each primary session, collect only what the audit needs:

- path or anonymised identifier;
- first and last timestamp;
- peak context and the message position where it occurred;
- summed input, cache creation, cache read, and output tokens;
- skill invocations;
- worker count and timing relative to context growth;
- major tool-call counts when repeated broad reads or command output are relevant; and
- parse failures or missing fields.

Rank sessions by peak context and non-cached work proxy, then inspect a small representative set: the largest sessions, repeated patterns, and a lower-cost comparison. Co-occurrence points to a question; the event sequence and loading path support or reject a cause.

Do not save a raw transcript-derived report unless it will improve a current decision. If a durable aggregate is justified, exclude prompts and sensitive content, record the time window and schema assumptions, and remove the report when it no longer supports an active optimisation decision.

