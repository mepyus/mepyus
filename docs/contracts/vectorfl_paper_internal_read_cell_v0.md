# VectorFL Paper Internal Read Cell Contract v0

## Role
Reread internal materials deeply enough to produce evidence-backed line seeds instead of generic summaries.

## Why This Cell Exists
External comparison quality depends on internal reading depth.
If internal reread is thin, every later expansion becomes thin.

## Managed By
- Primary CLI: `gemini-cli`
- Secondary CLI: `codex-cli`

## Reads First
- user / assistant conversation flows
- prior close-out notes
- internal reading casebook
- internal reading limits
- evidence bundles
- failure traces
- md declarations or locked direction notes

## Core Questions
- What pressure keeps repeating?
- What misunderstanding kept getting corrected?
- What question actually opened the structure?
- What is stable already?
- What is still unclear?
- What should not be flattened into TODO language?

## Allowed Actions
- reread dialogue and internal materials
- extract repeated pressures
- extract misunderstanding corrections
- form line seeds
- separate stable vs unclear vs next probe

## Disallowed Actions
- finalize external direction without evidence
- rewrite everything into summary-only prose
- turn line candidates into implementation tasks too early
- claim closure because wording sounds good

## Required Evidence
- at least 3 repeated pressures
- at least 2 misunderstanding corrections
- at least 3 question structures worth keeping
- at least 3 line seeds with evidence backing

## Output Format

### `stable`
- What already appears reusable or locked

### `unclear`
- What remains structurally unresolved

### `next_questions`
- Questions that should drive the next loop

### `line_seeds`
Each seed should include:
- `line_name`
- `core_claim`
- `repeated_evidence`
- `what_it_resists`
- `what_it_enables`

## Human Report
Use `supervisor_report_v0`.
The report must say:
- what was reread
- why this reread mattered
- what became more stable
- what is still not ready
- whether external lookup should proceed now

## Handoff Targets
- `external_resource_cell`
  Why: turn internal gaps into selective external comparison tasks
- `synthesis_cell`
  Why: convert reread results into a supervisor-readable next-step report

## Reopen Conditions
- outputs collapse into vague summaries
- no stable / unclear split exists
- line seeds cannot be tied to repeated evidence
- external lookup is requested without internal question shaping

## Return Slot
- `line_candidates_latest`
- `internal_read_report_latest`
