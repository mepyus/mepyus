# operation_surface_pointer_spec_v1

## 1. Purpose
This contract defines how latest operation surfaces should behave as pointer surfaces instead of content-heavy summary copies.

## 2. Role Split

### Latest Surface
- role:
  - quick current-state pointer
- must include:
  - latest run id
  - timestamp
  - receipt pointer
  - per-run board pointer
  - per-run commands pointer
  - compacted provenance pointer when available
  - short routing summary
- must not include:
  - large copied output lists
  - repeated event history blocks
  - duplicated per-run content

### Per-Run Surface
- role:
  - evidence-bearing run artifact
- should preserve:
  - detailed output list
  - event history
  - command details
  - run-specific trace context

## 3. Latest Board Minimum Shape
- latest run
- pointers
- summary
- note

## 4. Latest Commands Minimum Shape
- latest run
- document processing command
- pointers to receipt / latest board / per-run board / per-run commands
- note that per-run artifact is the detailed command record

## 5. Lock
- latest is representative
- per-run is evidentiary
- latest must remain thin even as trace volume grows
