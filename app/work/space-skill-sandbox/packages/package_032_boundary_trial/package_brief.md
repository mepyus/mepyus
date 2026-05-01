# Package Brief

## Current Operating Note

Package 032 is in hold closeout. The next allowed step is not artifact analysis; it is Run 114 user confirmation preflight.

## Required Preflight Rule

If candidate selection produces `selection_allowed: needs_user_confirmation`, stop immediately before file reading, signal extraction, or analysis. Request explicit user approval for the named candidate.

If the candidate category is unclear, mixed, or mismatched, do not reinterpret it into scope. Request user category reclassification.

## Package 032 Boundary

- current_status: hold_closeout
- next_run: `run_114_package_032_user_confirmation_preflight`
- allowed_next_action: candidate selection metadata preflight only
- target_artifact_analysis_allowed_without_user_approval: false

## Stop Block

```text
SELECTION_CONFIRMATION_REQUIRED
candidate_path:
claimed_category:
category_confidence:
selection_allowed: needs_user_confirmation
reason:
requested_user_action: approve this candidate, reject it, or reclassify the category
```
