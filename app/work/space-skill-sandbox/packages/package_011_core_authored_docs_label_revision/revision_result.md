# Package 011 Revision Result

## Script Updated

- `scripts/sandbox/package_metadata_scan.sh`

## Change Summary

Added a small package-local metadata classification:

- standard package records are excluded
- package-root markdown files outside the standard record list are listed as `Core Authored Doc Candidates`
- candidate status remains `reviewed_by: pending`
- `Deep-Read Candidates` now includes core authored doc candidates before standard review records

## Standard Package Records

- `package_brief.md`
- `user_summary.md`
- `package_closeout.md`
- `codex_review_bundle.md`
- `codex_validation.md`
- `handoff_log.md`
- `gemini_packet.md`
- `metadata_scan_report.md`

## What The Script Still Does Not Do

- decide correctness
- decide importance
- rank candidates
- validate package success
- promote any signal
- write outside the target package
- scan the whole md space

## Smoke Results

### Package 006

- report regenerated: true
- core authored doc candidates:
  - `priority_note_v0.md`
  - `small_execution_unit_registry_candidate_v0.md`
- reviewed_by_pending: true
- whole_md_scan: false

### Package 003

- report regenerated: true
- core authored doc candidates:
  - `analysis_result.md`
- reviewed_by_pending: true
- whole_md_scan: false

## Safety Checks

- syntax_check: PASS
- overwrite_refusal: PASS
- invalid_path_rejection: PASS
- package_local_output_only: true
- graph_created: false
- index_created: false
- ontology_created: false
- router_created: false
- controller_created: false
- automation_created: false

