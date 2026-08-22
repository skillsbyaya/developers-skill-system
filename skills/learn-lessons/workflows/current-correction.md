# Current Correction

Use the live triggering exchange. Read only enough surrounding context to identify the intended outcome, produced outcome, correction, and consequence. Check `~/.claude/LESSONS.md` only for a matching unresolved pattern. Treat an absent file as an empty queue.

## Diagnose

1. Separate observation from inference.
2. Identify project truth or corrective work that must be routed now.
3. Identify the preventable agent mechanism, if supported:
   - missing, ambiguous, misplaced, or conflicting instructions;
   - wrong routing or split ownership;
   - context retrieval or conditional-loading failure;
   - an adequate rule that lacks enforcement or verification;
   - a tool, hook, script, configuration, permission, or platform limitation; or
   - a one-off execution or knowledge error with no useful durable prevention.
4. State confidence and the strongest plausible alternative.

Do not manufacture a global lesson when evidence supports only a project consequence or one-off mistake.

## Choose the destination

Prefer the existing owner that can prevent the root cause. Do not duplicate the same content across queue, project context, backlog, instructions, and skills.

For an instruction or skill change, use `upskill` to inspect the current owner and make the smallest coherent correction. Prefer replacing or consolidating existing wording over appending another rule. Prefer an enforceable mechanism over prose when the failure is mechanical and the mechanism has the facts needed to decide safely.

Test the proposed prevention counterfactually:

- Would it have changed the triggering outcome?
- Could it misroute or burden a neighbouring case?
- Does an adequate rule already exist?
- Is the proposed owner able to observe and enforce the condition?

## Maintain the queue and apply

If the pattern remains unresolved, create the queue when absent and add one compact `×1` entry, or increment a genuinely matching unresolved entry. When creating it, use a `# Lessons` heading and one sentence stating that it contains unresolved agent-behaviour improvements only. Merge only the same root cause.

Use one compact line per unresolved root cause:

```markdown
- [YYYY-MM-DD ×N] <behavioural failure class in goal terms> — <current evidence or context needed to resolve it>
```

Do not add status fields, completed entries, project-specific task detail, transcripts, or facts that native memory already owns.

Before changing a protected target without specific prior authority, present the evidence, inferred mechanism, target, exact change, expected counterfactual benefit, and material trade-off, then ask. Preserve the unresolved queue entry if the change is deferred or declined.

After an authorised change, run the smallest finished-behaviour check that could disprove the fix. Remove the queue entry only when the prevention is installed and that check passes. If verification fails, keep the entry and report why.
