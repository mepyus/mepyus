# VectorFL Paper Weekend Pilot Scenario v0

## Purpose
This document defines the first weekend target for `VectorFL Paper`.
The goal is not full autonomous orchestration.
The goal is to close one real loop with scenario-bearing material.

## First Target
The first target is:

`scenario-included material -> internal read -> line seeds -> selective external comparison -> synthesis report -> supervisor decision -> internal return`

This means the pilot input should already contain:
- a scenario
- reasoning pressure
- conversation flow
- internal reading implications

## Recommended Input Package
- the four scenario-bearing documents from the current conversation bundle
- prior close-out notes relevant to `VectorFL Paper`
- current evidence bundle set
- current operable surface outputs

## Minimum Cell Set
- `internal_read_cell`
- `external_resource_cell`
- `synthesis_cell`

## Minimum CLI Assignment
- `gemini-cli` for internal reread pressure extraction
- `codex-cli` for structured synthesis, payload shaping, and report writing

## Minimum Deliverables

### 1. Internal Read Output
- stable
- unclear
- next questions
- 3 to 5 line seeds

### 2. External Resource Output
- candidate references
- why each reference matters
- what should not be imported
- what is ready for injection

### 3. Synthesis Output
- confirmed lines
- unresolved tensions
- supervisor report
- next loop proposal

## Success Criteria
- the scenario is not flattened into TODOs
- internal reading produces reusable line seeds
- external comparison is selective rather than broad
- a human supervisor can decide `go / hold / reopen / redirect`
- the loop returns artifacts into internal memory

## Failure Signs
- summary replaces line formation
- external references are gathered without changing judgment
- the supervisor report reads like a progress note only
- no next-loop proposal exists

## Weekend Definition Of Done
- the 3-cell loop runs once on real scenario-bearing material
- outputs exist in both internal language and human supervision language
- at least one follow-up loop is clearly proposed
