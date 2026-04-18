# VectorFL Paper Weekend Pilot Execution Order v0

## Purpose
This note defines the order in which the first weekend pilot loop should actually run.

## Order

### 1. Load Material Bundle
- Load the scenario-bearing material bundle.
- Confirm that the current conversation bundle remains included.

### 2. Activate `internal_read_cell`
- Produce:
  - stable points
  - unclear points
  - next questions
  - line seeds

### 3. Activate `external_resource_cell`
- Use only shaped questions from internal output.
- Produce:
  - candidate references
  - rejection rules
  - injection candidates

### 4. Activate `synthesis_cell`
- Bind internal and external outputs.
- Produce:
  - confirmed lines
  - unresolved tensions
  - supervisor report
  - next loop proposal

### 5. Supervisor Decision
- Decide:
  - go
  - hold
  - reopen
  - redirect

### 6. Internal Return
- Return approved results into Paper memory slots.
- Minimum return artifacts:
  - confirmed lines
  - injected reference proposal
  - next probe
  - loop closeout note

## Weekend Definition Of Done
The loop is only considered closed if all 6 steps have explicit artifacts.
