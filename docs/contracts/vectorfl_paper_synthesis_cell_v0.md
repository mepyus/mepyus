# VectorFL Paper Synthesis Cell Contract v0

## Role
Bind internal reread and external comparison into confirmed lines, a supervisor-readable report, and the next loop proposal.

## Why This Cell Exists
Without synthesis, the system accumulates reading fragments.
This cell is where the loop becomes decision-ready rather than merely information-rich.

## Managed By
- Primary CLI: `codex-cli`
- Secondary CLI: `gemini-cli`

## Required Inputs
- internal read outputs
- external resource outputs
- current governance or hold state
- current evidence bundle set
- current task seed or scenario scope

## Core Questions
- Which line seeds are now strong enough to confirm?
- Which tensions remain unresolved?
- What actually changed after external comparison?
- What should the supervisor decide next?

## Allowed Actions
- confirm or reject line candidates
- merge internal and external evidence
- write human-readable supervision reports
- propose next loop actions
- prepare return artifacts for internal memory

## Disallowed Actions
- hide unresolved tensions to make the report look clean
- claim confirmation without evidence
- skip the human decision layer
- collapse the loop into “done” too early

## Required Evidence
- every confirmed line must cite internal and/or external evidence
- every unresolved tension must be named plainly
- a `go / hold / reopen / redirect` recommendation must be present
- next loop proposal must be concrete enough for the next cell activation

## Output Format

### `confirmed_lines`
Each confirmed line should include:
- `line_name`
- `core_claim`
- `evidence_basis`
- `human_translation`
- `next_use`

### `unresolved_tensions`
- what still resists closure

### `supervisor_report`
- formatted with `supervisor_report_v0`

### `next_loop_proposal`
- which cell moves next
- why
- with which inputs

## Human Report
Use `supervisor_report_v0`.
The report must say:
- what was done this loop
- what changed materially
- what is now usable
- what is still unclear
- what the supervisor should decide now

## Handoff Targets
- `supervisor`
  Why: final decision point for the current loop
- `internal_read_cell`
  Why: reopen reread if tensions remain
- `external_resource_cell`
  Why: re-run comparison if the supervisor chooses expansion

## Reopen Conditions
- confirmed lines still depend on impressionistic language
- unresolved tensions were hidden or omitted
- no next-loop proposal exists
- supervisor recommendation is not actionable

## Return Slot
- `supervisor_report_latest`
- `loop_closeout_notes_latest`
- `confirmed_lines_latest`
