You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: inspect
Requested by surface: vectorfl_surface
Requested by page: /vectorfl-engine/vectorfl

Purpose:
Stop-and-use run 2: inspect one small runtime/view source region conceptually.

Bounded context refs:
- app/runtime/vectorfl_integrated_engine_shell.py

Prompt payload:
Inspect app/runtime/vectorfl_integrated_engine_shell.py only enough to identify the CLI Host / Control panel role. Return three short bullets: where it appears, what it renders, and whether it reads as on-top rather than a new surface. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
