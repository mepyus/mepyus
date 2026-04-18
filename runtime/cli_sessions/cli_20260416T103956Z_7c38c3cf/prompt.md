You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: validate
Requested by surface: vectorfl_surface
Requested by page: app/ui/integrated_engine

Purpose:
Suggested-next-use explicit tail inference retest.

Bounded context refs:
- docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md

Prompt payload:
Return a compact validation note. Mention deposit candidate as a deferred area in the body, but end exactly with: suggested next use: validation target. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
