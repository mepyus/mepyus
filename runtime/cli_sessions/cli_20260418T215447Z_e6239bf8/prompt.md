You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: inspect
Requested by surface: vectorfl_surface
Requested by page: runrecord_contract_validation

Purpose:
Validate structured worker return contract on the existing OpenHarness package continuity path.

Bounded context refs:
- references/git_search/openharness-main

Prompt payload:
Dry-run contract validation: profile the source, return structured worker_return fields, and keep route as reread_target.

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
