---
name: close-session
description: "Closes working sessions cleanly and produces fresh-session continuation when needed. Use after agent-dev completes or stops delivery work, or when the user says to wrap up, close or end the session, stop for today, or otherwise signals that the current session is ending."
---

# Close Session

Triage the close before reading a workflow. Choose the boundary and preservation depth independently; implementation mechanics must not force either too much or too little knowledge capture.

## 1. Choose the boundary

| Boundary | Read |
| --- | --- |
| Agent Dev finished or stopped a named implementation packet or slice, through any delivery route | [Packet close](workflows/packet-close.md) |
| Agent Dev finished or stopped another delivery unit, or the user signals that the current working session is ending, including “stop for today” | [Full close](workflows/full-close.md) |

A natural session-end signal always selects full close, even when the session also ended at a packet boundary. Agent Dev invokes the matching close automatically after every delivery boundary; no additional prompt is required.

## 2. Choose the preservation depth

- **Routine:** Current status, one exact continuation boundary, and isolated durable facts are already written or can be repaired directly from session evidence.
- **Knowledge-rich:** Several material decisions, ideas, new constraints, rejected approaches, or corrections remain unwritten; one interconnected decision set would lose its relationships if reduced to isolated facts; or a confirmed mistake has a cause, consequence, or prevention that would otherwise be lost.

Message count, elapsed time, packet size, and ordinary implementation detail do not justify knowledge-rich capture. Consequence, unwritten durable knowledge, and recurrence risk do.

Read only the selected boundary workflow. It applies the triaged depth and conditionally loads shared knowledge capture when needed. Knowledge-rich depth does not turn packet close into full close or widen its lifecycle, Git, review, or deployment authority. Both workflows end the current session and prepare continuation for a new one; neither continues active work after closing.
