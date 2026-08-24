---
name: close-session
description: "Closes working sessions cleanly and produces fresh-session continuation when needed. Use when agent-dev finishes an implementation packet, or when the user says to wrap up, close or end the session, stop for today, or otherwise signals that the current session is ending."
---

# Close Session

Select one workflow and read only that workflow.

| Need | Read |
| --- | --- |
| Agent Dev finished or stopped one coordinated or staged implementation packet and must preserve continuation for a fresh session | [Packet close](workflows/packet-close.md) |
| The user signals that the current working session is ending, including “stop for today” | [Full close](workflows/full-close.md) |

A natural session-end signal always selects full close, even when the session also ended at a packet boundary. Agent Dev invokes packet close automatically at an internal packet boundary when the user has not requested the broader full close; no additional prompt is required.

Do not preload or combine the workflows. Both routes end the current session and prepare any continuation for a new one. Neither route continues active work after closing.
