# VectorFL Paper External Resource Cell Contract v0

## Role
Translate internal gaps and line seeds into selective external comparison, then propose what should return into the internal reference space.

## Why This Cell Exists
VectorFL Paper is not internal-only.
But external material should enter only after internal reading has made the search precise.

## Managed By
- Primary CLI: `codex-cli`
- Secondary CLI: `gemini-cli`

## Required Inputs
- stable / unclear split from `internal_read_cell`
- line seeds
- next questions
- current evidence bundles
- current hold / go constraints

## Core Questions
- What external material sharpens this internal line?
- What comparison exposes a hidden difference?
- What reference would actually change our internal judgment?
- What external material should be rejected because it flattens the structure?

## Allowed Actions
- generate selective search or comparison prompts
- gather candidate references
- explain why each candidate matters
- map candidates back to internal line seeds
- nominate references for internal injection

## Disallowed Actions
- broad undirected search
- collecting references without judgment
- treating external material as authority by default
- replacing internal criteria with external wording

## Required Evidence
- every candidate must map back to at least 1 internal line seed
- every candidate must include a `why it helps` explanation
- at least 1 rejection or exclusion rule must be explicit
- at least 1 candidate must be labeled `injectable` or `not yet injectable`

## Output Format

### `candidate_references`
Each candidate should include:
- `reference_id`
- `source_type`
- `why_it_helps`
- `which_line_seed_it_strengthens`
- `injection_readiness`

### `rejection_rules`
- What should not be brought in and why

### `internal_injection_candidates`
- What should be added to internal reference space if approved

### `external_followup_questions`
- What still needs comparison after the first pass

## Human Report
Use `supervisor_report_v0`.
The report must say:
- what was searched or compared
- why those references were chosen
- which internal line each result connects to
- what is safe to inject
- whether another external loop is justified

## Handoff Targets
- `synthesis_cell`
  Why: combine internal and external results into a next-loop judgment
- `internal_read_cell`
  Why: re-read injected references inside the internal criteria frame

## Reopen Conditions
- candidates cannot be linked to internal line seeds
- gathered references are interesting but not actionable
- no injection decision can be made
- external search drifted away from the original pressure

## Return Slot
- `external_candidates_latest`
- `reference_injection_proposal_latest`
