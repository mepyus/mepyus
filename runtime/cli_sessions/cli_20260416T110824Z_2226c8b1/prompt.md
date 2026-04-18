You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: reread
Requested by surface: vectorfl_surface
Requested by page: app/ui/integrated_engine

Purpose:
Operator report loop smoke test: read the CLI-on-top grammar note and return a compact route-status summary.

Bounded context refs:
- docs/reports/integrated_engine_cli_on_top_shared_language_grammar_reread_v0.md

Prompt payload:
Read the bounded context and return a compact status note. End with: suggested next use: validation target. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
