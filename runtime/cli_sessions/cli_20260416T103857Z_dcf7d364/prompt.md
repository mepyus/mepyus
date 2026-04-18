You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: validate
Requested by surface: vectorfl_surface
Requested by page: app/ui/integrated_engine

Purpose:
Cross-surface reflection smoke test: verify CLI return can be read as user assignment signal and engine return material.

Bounded context refs:
- docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md
- app/ui/integrated_engine/VectorFLIntegrationShell.tsx

Prompt payload:
Read the bounded context. Return three short sections: user surface assignment signal, VectorFL operating signal, engine return/validation signal. End with suggested next use: validation target. Do not modify files.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
