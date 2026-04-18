# VectorFL Paper Issue-Run-Result-Governance Intake Mapping v0

## Purpose
This document defines the first thin intake grammar for the selected weekend target:

`Paperclip issue / heartbeat run / result / governance event -> VectorFL intake grammar`

The point is not full integration.
The point is to prove that one external control-plane cycle can be translated into:
- line-bound work packet
- execution trace
- residue note
- governance gate
- advisory return hint

## Core Rule
Do not copy Paperclip ontology into VectorFL as the new center.
Translate external operating events into line-centered internal objects.

That means:
- issue is not the final object
- run is not just a log row
- result is not just a comment
- governance is not just approval state

Each must be translated into a VectorFL reading / action object.

## Mapping Table

### 1. Issue Surface

#### External Inputs
- issue id
- title
- description
- assignee
- project / goal / parent
- issue status

#### VectorFL Translation
- `source_assignment`
- `line_translation`
- `context_refs`
- `execution_guidance`

#### Primary Internal Object
- `line_guided_work_packet`

#### Why
The issue is the bounded work atom, but VectorFL should act on a line-aware packet rather than the external issue row directly.

## 2. Heartbeat Run Surface

### External Inputs
- run id
- started_at / ended_at
- status
- adapter / runtime
- session continuity
- usage / error

### VectorFL Translation
- `execution_trace`
- `reentry_hint`
- `residue_capture_candidate`
- `run_state`

### Primary Internal Object
- `append_only_trace_row`

### Why
The run matters because it reveals execution path, continuity, and reentry pressure, not because it is merely a timestamped event.

## 3. Result Surface

### External Inputs
- result summary
- comment
- produced artifact
- patch / file / url / log
- completion claim

### VectorFL Translation
- `observed_line_candidate`
- `residue_note`
- `operator_summary`
- `advisory_return_hint`

### Primary Internal Objects
- `result_readout_note`
- `reinjection_stub`

### Why
The result should become something rereadable inside VectorFL rather than a terminal output blob.

## 4. Governance Event Surface

### External Inputs
- approval requested / approved / rejected
- budget stop / warning
- reassignment
- pause / board intervention

### VectorFL Translation
- `route_gate`
- `hold_trace`
- `promotion_gate`
- `caution_note`

### Primary Internal Objects
- `governance_gate_note`
- `route_hold_trace`

### Why
Governance is part of the meaning of work progression.
It should affect route selection, hold posture, and future loop bias.

## Target Internal Object Set

### A. `line_guided_work_packet`
- translated issue object

### B. `append_only_trace_row`
- translated run object

### C. `result_reinjection_stub`
- translated result object

### D. `governance_gate_note`
- translated approval / hold object

### E. `advisory_return_hint`
- minimum useful result returned to the operating surface

## Weekend v0 Translation Priority
For the first live pass, translate in this order:

1. issue -> line-guided work packet
2. run -> append-only trace row
3. result -> reinjection stub
4. governance event -> route / hold gate

## Minimum Acceptance
The mapping succeeds if:
- one issue can be explained as a line-aware work packet
- one run can be stored as a trace row with reentry meaning
- one result can be turned into a reinjection stub
- one governance event can be read as a route or hold gate

## Failure Signs
- issue remains only a copied ticket
- run remains only a timestamp list
- result remains only a prose summary
- governance remains only a yes/no approval flag

## One-Line Lock
The first overlay must prove that external control-plane events can be translated into VectorFL line, trace, residue, and gate objects without replacing VectorFL's center of gravity.
