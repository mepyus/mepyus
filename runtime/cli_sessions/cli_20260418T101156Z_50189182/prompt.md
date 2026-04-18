You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: reread
Requested by surface: vectorfl_surface
Requested by page: /vectorfl-engine/vectorfl

Purpose:
외부 렌즈 재료 읽기 dry run 검증

Bounded context refs:
- gemini/external_analysis

Prompt payload:
외부 렌즈 재료를 읽고 패키지 공정 이벤트가 남는지만 dry run으로 확인한다.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
