You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: reread
Requested by surface: vectorfl_surface
Requested by page: scripts/run_integrated_engine_language_loop.py

Purpose:
Internal language translation data loop 2: collect line / connection / axis material from bounded context.

Bounded context refs:
- docs/reports/integrated_engine_cli_on_top_current_operating_state_v0.md
- docs/reports/integrated_engine_surface_exposure_and_shared_language_boundary_v0.md

Prompt payload:
Read the bounded context as an internal-language translation data collection loop.

Do not modify files.
Do not propose UI copy.
Do not create a final glossary.
Do not promote features.

Return compact data in this shape:
- internal phrase or signal observed
- human-readable line, not final wording
- repeated connection it belongs to
- emerging axis candidate
- surface exposure note: user / vectorfl / engine
- what must not be flattened
- next reread question
- suggested next use: validation target

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
