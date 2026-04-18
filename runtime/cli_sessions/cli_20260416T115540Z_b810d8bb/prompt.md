You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: reread
Requested by surface: user_surface
Requested by page: scripts/run_integrated_engine_language_loop.py

Purpose:
Internal language Koreanization data loop 1: collect Korean operating-language data from bounded context.

Bounded context refs:
- docs/reports/integrated_engine_cli_on_top_shared_language_grammar_reread_v0.md
- docs/reports/integrated_engine_cli_on_top_operator_report_grammar_trial_v0.md

Prompt payload:
Read the bounded context as a Koreanization data collection loop for integrated-engine internal language.

Do not modify files.
Do not propose UI copy.
Do not create a final glossary.
Do not promote features.

Return compact data in this shape:
- internal phrase or signal observed
- source context where it appeared
- internal meaning / operational role
- Koreanization candidate, not final UI copy
- Korean preservation requirement
- risky Korean flattening to avoid
- why this helps the user operate
- what meaning gets lost if shortened
- repeated connection it belongs to
- emerging axis candidate
- surface exposure note: user / vectorfl / engine
- external expression support needed, if any
- next reread question
- suggested next use: validation target

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
