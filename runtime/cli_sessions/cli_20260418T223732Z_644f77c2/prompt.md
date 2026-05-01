You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: summarize
Requested by surface: vectorfl_surface
Requested by page: package2_worker_adapter_contract_validation_escalated

Purpose:
Actual worker contract smoke: return only a minimal bounded structured worker return for package continuity validation.

Bounded context refs:
- docs/specs/integrated_engine_worker_return_contract_v0.md
- docs/reports/integrated_engine_real_worker_boundary_audit_v0.md

Prompt payload:
Read the bounded contract refs if available. Keep the prose short. The most important requirement is to include the WORKER_RETURN_JSON block exactly as requested by the adapter prompt. Do not modify files.

Return format:
- result summary
- answer: direct answer or main response body
- findings: key observations as bullets
- files_artifacts: concrete file paths or generated outputs
- next_continue_hint: specific next step for this same package
- open_questions: unresolved blockers
- risks_or_limits: uncertainty, weak spots, dry-run limits, or blocked areas
- source_refs: bounded context refs actually used
- suggested next use: reread target / implementation return / validation target / deposit candidate

You must also include one machine-readable block near the end of the answer.
Use exactly this delimiter format and valid JSON. Keep arrays as arrays of strings.
WORKER_RETURN_JSON
{
  "schema_version": "integrated_engine_worker_return_v0",
  "worker_id": "codex",
  "package_id": "<package id if known>",
  "run_kind": "summarize",
  "answer": "<direct answer or main response>",
  "findings": ["<key observation>"],
  "files_artifacts": ["<path or artifact ref>"],
  "next_continue_hint": "<specific next step for this same package>",
  "open_questions": ["<unresolved blocker>"],
  "risks_or_limits": ["<uncertainty or limit>"],
  "source_refs": ["<bounded context ref actually used>"]
}
END_WORKER_RETURN_JSON
