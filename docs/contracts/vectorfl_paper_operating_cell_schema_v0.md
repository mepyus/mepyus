# VectorFL Paper Operating Cell Schema v0

## Purpose
This schema defines the minimum structure of an operating cell inside `VectorFL Paper`.
A cell is not a label or dashboard tab.
A cell is a working unit that combines:
- a lens
- managed internal functions
- a managing CLI
- an md contract
- outputs
- handoff behavior
- a human-readable supervision surface

## Core Rule
Every cell must help close the loop:

`input -> internal reread -> line formation -> selective external lookup -> internal return -> next judgment`

If a proposed cell does not help this loop, it is not an operating cell yet.

## Required Fields

### `cell_id`
- Stable unique identifier.
- Example: `internal_read_cell`

### `label`
- Human-readable name for the cell.
- Example: `Internal Read Cell`

### `purpose`
- One sentence explaining why this cell exists.
- It must describe a function, not a department identity.

### `lens`
- What this cell is optimized to notice first.
- Example:
  - repeated pressure
  - unclear structure
  - reusable line seed
  - external comparison target

### `managed_internal_functions`
- Concrete internal functions, scripts, records, or reading assets this cell is allowed to touch.
- These should be expressed as actual managed materials, not vague intentions.

### `managing_cli`
- The CLI primarily responsible for managing this cell.
- Initial allowed values:
  - `codex-cli`
  - `gemini-cli`
  - `hybrid`

### `md_contract`
- Path to the md contract this cell must read before acting.
- This is the behavioral contract, not a note.

### `inputs`
- Inputs this cell expects to receive.
- Examples:
  - current task seed
  - prior line candidates
  - recall bundles
  - unresolved tensions
  - external candidate references

### `outputs`
- Outputs this cell is expected to emit.
- Examples:
  - stable / unclear split
  - line seed set
  - candidate reference set
  - human report
  - next loop proposal

### `required_evidence`
- Minimum evidence required before this cell can claim completion.
- Example:
  - at least 3 repeated pressures
  - at least 2 explicit misunderstandings corrected
  - at least 1 internal-to-external bridge question

### `handoff_targets`
- Which cells can receive this cell's output.
- Each target should also say why the handoff exists.

### `human_report_format`
- The supervision format this cell must produce for a human decision-maker.
- This should point to a named report format rather than ad hoc prose.

### `external_pair_team`
- External-facing paired cell or `null`.
- Internal cells that affect expansion should usually have an external pair.

### `governance`
- Constraints and escalation rules.
- Minimum fields:
  - `allowed_actions`
  - `disallowed_actions`
  - `needs_human_gate`
  - `reopen_conditions`

### `return_slot`
- Where the result returns to inside `VectorFL Paper`.
- Example:
  - `line_candidates_latest`
  - `external_candidates_latest`
  - `supervisor_report_latest`

## Optional Fields

### `scenario_scope`
- Which scenario or pilot this cell currently serves.

### `run_notes`
- Temporary runtime notes for the current loop only.

### `quality_checks`
- Lightweight completion checks that can be machine-checked or reviewer-checked.

## Minimum Example

```yaml
cell_id: internal_read_cell
label: Internal Read Cell
purpose: Reread internal materials deeply enough to separate stable signals from unclear pressure.
lens:
  - repeated pressure
  - misunderstanding correction
  - reusable line seed
managed_internal_functions:
  - dialogue reread
  - casebook reread
  - evidence bundle attachment review
managing_cli: gemini-cli
md_contract: docs/contracts/vectorfl_paper_internal_read_cell_v0.md
inputs:
  - task_seed
  - prior_dialogue_material
  - internal_casebook
outputs:
  - stable_points
  - unclear_points
  - next_questions
  - line_seeds
required_evidence:
  - 3 repeated pressures
  - 2 corrected misunderstandings
handoff_targets:
  - cell_id: external_resource_cell
    why: Convert internal gaps into selective external lookup tasks.
  - cell_id: synthesis_cell
    why: Turn internal reread into a supervision-ready interim summary.
human_report_format: supervisor_report_v0
external_pair_team: external_resource_cell
governance:
  allowed_actions:
    - reread internal materials
    - extract line seeds
  disallowed_actions:
    - finalize product direction without synthesis
  needs_human_gate: false
  reopen_conditions:
    - line seeds collapse into generic TODOs
return_slot: line_candidates_latest
```

## Validation Questions
- Does this cell describe a working function rather than a role label?
- Can a CLI manage it without fresh human re-instruction each time?
- Does it emit evidence-backed outputs rather than summaries only?
- Is the handoff explicit?
- Can a human supervisor understand what happened from its report?

## v0 Initial Cells
- `internal_read_cell`
- `external_resource_cell`
- `synthesis_cell`

These three are the minimum 1st-loop cell set.
