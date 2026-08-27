---
name: close-session
description: "Closes working sessions cleanly and produces fresh-session continuation when needed. Use after agent-dev completes or stops delivery work, or when the user says to wrap up, close or end the session, stop for today, or otherwise signals that the current session is ending."
---

# Close Session

Select one workflow and read only that workflow.

| Need | Read |
| --- | --- |
| Agent Dev finished or stopped a named implementation packet or slice, through any delivery route, and must preserve continuation for a fresh session | [Packet close](workflows/packet-close.md) |
| Agent Dev finished or stopped another delivery unit, or the user signals that the current working session is ending, including “stop for today” | [Full close](workflows/full-close.md) |

A natural session-end signal always selects full close, even when the session also ended at a packet boundary. Agent Dev invokes the matching close automatically after every delivery boundary; no additional prompt is required.

Do not preload or combine the workflows. Both routes end the current session and prepare any continuation for a new one. Neither route continues active work after closing.
