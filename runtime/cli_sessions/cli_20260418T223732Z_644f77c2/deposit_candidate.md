# Integrated Engine CLI Deposit Candidate

- source_session_id: `cli_20260418T223732Z_644f77c2`
- backend_kind: `codex`
- task_type: `summarize`
- requested_by_surface: `vectorfl_surface`
- requested_by_page: `package2_worker_adapter_contract_validation_escalated`
- status: `done`

- route_label: `engine_request_candidate`
- current_marks: `none`
- user_decision_state: `pending_candidate_review`
- canonical_deposition_state: `not_ingested`

## Task Purpose
Actual worker contract smoke: return only a minimal bounded structured worker return for package continuity validation.

## Used Context Refs
- `docs/specs/integrated_engine_worker_return_contract_v0.md`
- `docs/reports/integrated_engine_real_worker_boundary_audit_v0.md`

## Result Summary
orker_return_contract_v0.md`
- `docs/reports/integrated_engine_real_worker_boundary_audit_v0.md`

suggested next use:
validation target

WORKER_RETURN_JSON
{
  "schema_version": "integrated_engine_worker_return_v0",
  "worker_id": "codex",
  "package_id": "unknown",
  "run_kind": "summarize",
  "answer": "Actual worker contract smoke completed. Use the worker-emitted block as the primary adapter validation target for projecting structured_return.worker_return.",
  "findings": [
    "Worker return schema version is integrated_engine_worker_return_v0.",
    "Runtime should prefer structured_return.worker_return before fallback parsing.",
    "Actual worker output enters through CodexCliAdapter.start_run(...) stdout/stderr/returncode.",
    "Package 2 should validate a parseable worker-emitted block, not only runtime-synthesized normalization."
  ],
  "files_artifacts": [
    "docs/specs/integrated_engine_worker_return_contract_v0.md",
    "docs/reports/integrated_engine_real_worker_boundary_audit_v0.md"
  ],
  "next_continue_hint": "Validate that the adapter can extract this WORKER_RETURN_JSON block from actual worker stdout and project it into structured_return.worker_return.",
  "open_questions": [
    "Package id was not provided in the prompt.",
    "Whether validation should require strict JSON parse success or allow markdown fallback remains a package decision."
  ],
  "risks_or_limits": [
    "This was a read-only smoke response; no files were modified.",
    "Actual external worker compliance is only validated if the adapter parses the emitted block, not by this response alone."
  ],
  "source_refs": [
    "docs/specs/integrated_engine_worker_return_contract_v0.md",
    "docs/reports/integrated_engine_real_worker_boundary_audit_v0.md"
  ]
}
END_WORKER_RETURN_JSON


## Important Diffs / Findings / Outputs
- not separated in package 1 return


## Uncertainty / Failure Notes
- none recorded


## Suggested Next Use
validation_target

## Validation / Decision Boundary
- This file is a deposition candidate only.
- It is not canonical memory, not an approved record, and not automatic ingestion.
- User decision or a later explicit deposition package is still required.

