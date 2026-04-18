You are running as a bounded CLI backend on top of the VectorFL Integrated Engine.
This is not a new engine surface. Treat the run as a tool call observed through the VectorFL surface.
Keep the return compact and structured for engine reread, validation, or deposit.

Backend: codex
Task type: reread
Requested by surface: vectorfl_surface
Requested by page: app/ui/integrated_engine

Purpose:
외부 렌즈 재료 읽기: OpenCode / Claude Code 화면 선례는 참고만 하고 아직 자동 확장하지 않음

Bounded context refs:
- gemini/external_analysis

Prompt payload:
You are operating as a Codex turn inside the integrated-engine VectorFL surface.
The CLI is an on-top tool layer, not a fourth surface.
The fixed surface split is: user = purpose/assignment/decision, VectorFL = interpretation/reread/mediation, engine = processing/return/deposit material.

Current work packet visible in the VectorFL surface:
- purpose: 외부 렌즈 재료 읽기: OpenCode / Claude Code 화면 선례는 참고만 하고 아직 자동 확장하지 않음
- task lens: reread
- internal search gate: thin evidence (requested by prompt)
- evidence bundle summary: 1 attached refs: source ref
- evidence limitation: Evidence bundle is thin; only one ref is attached.
- active locks: fixed 3-surface body + CLI on-top boundary (inferred)
- evidence refs: gemini/external_analysis
- guards: read-only (guard-active); no promotion (guard-active); no ingestion (guard-active); no canonicalization (guard-active)
- expected return shape: reread judgment
- next route candidate: hold
- internal search usage: thin evidence

Current user-facing purpose:
외부 렌즈 재료 읽기: OpenCode / Claude Code 화면 선례는 참고만 하고 아직 자동 확장하지 않음

Current message to Codex:
외부 렌즈 재료 읽기 작업을 시작한다.
현재 stage는 precedent hold, executor 후보는 gemini-ready다.
엔진/통합엔진/패키지 구조 기준으로 먼저 내부 공간을 읽고, 무엇을 실행해야 하는지 짧게 정리해줘. 파일은 수정하지 않는다.

Return format for this VectorFL CLI conversation turn:
1. Korean operating summary
2. Surface reading: user / VectorFL / engine
3. Route suggestion: reread_target / validation_target / implementation_return / deposit_candidate / hold
4. What must not be inferred
5. Suggested next use
Do not modify files. Do not promote, ingest, or canonicalize anything.

Return format:
- result summary
- important findings / diffs / outputs
- uncertainty or failure notes
- suggested next use: reread target / implementation return / validation target / deposit candidate
