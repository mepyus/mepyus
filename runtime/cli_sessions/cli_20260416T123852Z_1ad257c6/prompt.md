You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: reread
Requested by surface: vectorfl_surface
Requested by page: app/ui/integrated_engine

Purpose:
Step 3 smoke: route label dry-run target for engine request candidate.

Bounded context refs:
- docs/reports/integrated_engine_next_operating_checklist_v0.md

Prompt payload:
Dry-run route label smoke. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
