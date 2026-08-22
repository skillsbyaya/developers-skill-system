# Technical Research

Resolve a technical question with current primary evidence, explicit trade-offs, and project-fit reasoning.

## Frame the decision

Establish the technical question, candidate options, current system and constraints, required capabilities, decision criteria, operational horizon, and acceptable evidence age. Inspect repository or architecture evidence only when project fit is part of the question.

Scale the work to a focused answer, comparative decision, project-fit assessment, supplied-source synthesis, or reusable landscape report.

## Research by decision criteria

Select only dimensions that matter:

- capability and constraint fit;
- compatibility, interoperability, standards, and migration path;
- maturity, maintenance, release cadence, ecosystem, and support horizon;
- performance and scalability under a defined workload;
- security properties and operational burden;
- licensing, portability, cost drivers, and lock-in;
- developer experience, observability, testing, deployment, and failure recovery.

Do not force every technical concern into every comparison.

## Evidence and comparison

- Prefer official documentation, specifications, standards, release notes, repositories and issue trackers, maintainer statements, original research papers, and reproducible benchmarks.
- Record the applicable version and date for consequential claims. Compare equivalent versions, configurations, workloads, and definitions.
- Distinguish documented capability, observed benchmark, vendor claim, inference, and assumption.
- Treat benchmarks as workload-specific evidence, not universal rankings.
- Check deprecation, support, licensing, and compatibility against current authoritative sources.
- Compare fair alternatives, including the status quo when credible.

When external evidence cannot resolve a project-specific uncertainty, recommend the smallest useful spike, benchmark, proof of concept, or measurement plan. Do not present an unrun experiment as evidence.

## Ownership boundaries

Research may compare architecture approaches, but `agent-architect` owns the resulting design decision and durable architecture record. `agent-dev investigation` owns forensic work on an existing defect or incident; `agent-dev` owns implementation. Security, privacy, database, legal, and compliance constraints may be identified and sourced here, but substantive judgement remains with their specialists.

## Decide and finish

Lead with the current best answer or recommendation and strongest credible alternative. State criteria, project-fit implications, confidence, risks, reversibility, validation path, and unresolved evidence that could change the choice.

When a reusable report is warranted, use [the general research template](../templates/research.md) as an optional structure.
