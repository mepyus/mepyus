You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: validate
Requested by surface: vectorfl_surface
Requested by page: app/ui/integrated_engine

Purpose:
Suggested-next-use inference smoke test for validation target.

Bounded context refs:
- runtime/cli_sessions/cli_20260416T102612Z_277b5388/session.json
- runtime/cli_sessions/cli_20260416T102612Z_277b5388/structured_return.json

Prompt payload:
Read the bounded context. Return that the suggested next use should be validation target because the remaining uncertainty is browser validation. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
