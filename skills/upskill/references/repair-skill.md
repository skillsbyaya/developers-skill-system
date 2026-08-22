# Repair a Skill

Use this route when a skill has a demonstrated or clearly modelled failure and the goal is a durable correction.

## Find the failure class

Reproduce the reported case when practical or model it precisely from the available evidence. Define expected behavior, observed behavior, entry state, relevant environment, and impact. Locate the cause in triggering, intent capture, judgement, procedure, conditional loading, resources, state, mutation boundaries, output checks, compatibility, or ownership.

Do not patch only the reported phrase or example when the same cause would fail elsewhere. Identify the smallest adjacent cases that distinguish a durable class fix from overfitting, including a should-still-pass case and a should-not-trigger or should-not-change case where relevant.

Read [platform compatibility](platform-compatibility.md) only when current Claude Code behavior may cause the failure. Read [registration and consumers](registration-and-consumers.md) only when the repair changes metadata, a route, resource relationship, document contract, or consumer. Read [worker use](worker-use.md) only when worker behavior caused or is proposed to fix the failure.

## Correct and verify

Change the earliest reliable cause while preserving the owner's intended boundary. Update dependent resources or consumers required for the fix; avoid unrelated cleanup.

Replay the reported case and the adjacent cases. Validate affected metadata, links, resources, and deterministic helpers. Finish when the failure class is corrected without creating neighbour collisions, hidden prerequisites, broader mutation, or extra ceremony.

If the skill's ownership or purpose is the cause, stop treating the work as a contained repair and use the restructure route when authorised.
