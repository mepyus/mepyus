You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: inspect
Requested by surface: vectorfl_surface
Requested by page: package3_step_a_real_openharness_structure_profile

Purpose:
Package 3 Step A: real bounded OpenHarness structure profiling for existing continuity package.

Bounded context refs:
- references/git_search/openharness-main
- references/git_search/openharness-main/README.md
- references/git_search/openharness-main/pyproject.toml
- docs/reports/integrated_engine_real_worker_boundary_audit_v0.md
- docs/specs/integrated_engine_worker_adapter_prompt_contract_v0.md

Prompt payload:
Perform a real bounded structural profile of references/git_search/openharness-main for our integrated-engine package notebook. Do not modify files. Focus only on: 1) what this repo appears to be, 2) top-level areas worth treating as internal lens material, 3) concrete files/dirs that should be inspected next, 4) one specific next_continue_hint for continuing this same package. Include the required WORKER_RETURN_JSON block on its own delimiter lines.

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
  "run_kind": "inspect",
  "answer": "<direct answer or main response>",
  "findings": ["<key observation>"],
  "files_artifacts": ["<path or artifact ref>"],
  "next_continue_hint": "<specific next step for this same package>",
  "open_questions": ["<unresolved blocker>"],
  "risks_or_limits": ["<uncertainty or limit>"],
  "source_refs": ["<bounded context ref actually used>"]
}
END_WORKER_RETURN_JSON
