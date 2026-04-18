# Integrated Engine Process Validation Gate v0

## 1. Purpose

This spec defines validation gates for the candidate handling process camera.

It separates:

- process-level gates
- target-level gates

It does not promote any target.
It does not authorize rollout.

## 2. Result Scale

Use:

- `directly`: concrete bounded support from the current evidence
- `weakly`: visible but dependent on inference or surrounding context
- `not yet`: not meaningfully supported
- `blocked`: action must stop because boundary or authority would drift

## 3. Process-Level Gates

| gate | question | pass condition | fail / hold signal |
|---|---|---|---|
| grounding sufficiency | Is there enough evidence for the selected target and lens? | evidence bundle names sources and support reason | source-level only may be `weakly`; missing trace is hold |
| lens-explicitness | Is the reading angle explicit? | primary lens and supporting lenses are named with purpose | vague "review" or name-only lens |
| principle-bearing structure | Is there a shaping principle? | rule explains why judgment follows | retrospective summary only |
| boundary clarity | Are forbidden inferences explicit? | promotion, rollout, canonicalization, and invalid reuse are blocked where relevant | authority boundary vague |
| rollback visibility | Are rollback cues and destinations visible? | invalid shapes, forcing, hidden partial/missing, and authority drift have stop/hold destinations | rollback cues scattered or absent |
| action readiness | Can a bounded packet be formed? | allowed actions, forbidden actions, expected return are explicit | worker would need full chat reread |
| authority drift prevention | Does the gate prevent candidate becoming canonical? | status and not-promoted boundary explicit | candidate read as completion |
| rollout drift prevention | Does the gate prevent automatic reuse? | reuse requires separate validation | adjacency treated as proof |

## 4. Target-Level Gates

| gate | question | examples |
|---|---|---|
| target type fit | Is this target compatible with the selected process lens? | camera candidate vs lens candidate vs rollback rule asset |
| target shape | Is there enough content-bearing material? | report body, transcript body, review note |
| target status | Is target candidate / hold / rollback-only / usable? | `eligible`, `not promoted`, `weakly`, `directly` |
| target stop rule | What stops the run? | invalid target shape, weak evidence, authority drift |

## 5. Gate Outcome

Allowed outcomes:

- usable for bounded action
- usable for inspection only
- weak fit, hold
- supplement needed
- insufficient
- rollback-only
- blocked

Forbidden outcomes:

- automatic promotion
- automatic rollout
- canonical ingestion without separate gate
- multi-agent execution without execution packet

## 6. Phase 2 Validation

Inspectable language check:

- gates are phrased as questions and pass/hold conditions

Process vs target check:

- process-level and target-level gates are separated

Overclaim check:

- no gate creates promotion or rollout authority

