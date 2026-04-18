You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: summarize
Requested by surface: vectorfl_surface
Requested by page: gemini/mock_test

Purpose:
Gemini mock main surface proxy validation: summarize package 1.1 closeout note.

Bounded context refs:
- docs/reports/integrated_engine_cli_on_top_package1_1_closeout_note_v0.md

Prompt payload:
Read the bounded context and return two short bullets: usable path and remaining deferral. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
