# Integrated Engine Common Language Extraction Round2 Synthesis v1

Date: 2026-04-14

## scope

This is `harvest_round_2`, using `Integrated Engine Exploration Question Set v1.1` as the reusable protocol and `docs/reports/integrated_engine_common_language_extraction_v1.md` as `harvest_round_1`.

This report is not a final schema, enum, DB model, canonical state machine, or workflow-hub lock.

## repeated expressions across round_1 and round_2

- `goal / scope / material context`  
  Still stable as user-surface body language.

- `intermediate formation reading / line / relation / gap / pending / reflux`  
  Still stable as VectorFL-surface body language. Round_2 strengthens it with the current shell wording `line-first surface` and `not team board`.

- `ingest / process / validate / trace-memory / return`  
  Still stable as engine-surface body language.

- `return is not only result text`  
  Still stable. Round_2 strengthens it with `report return is not product completion` and `must write a return artifact, not chat-only notes`.

- `final schema 아님 / language material / future layer / unresolved`  
  Still stable as assistant judgment grammar.

- `body vs optional tool layer`  
  Still stable. Round_2 adds more concrete action-strength grammar: `records_dialogue_only`, `draft_only`, `does_not_run_cli`, and `does_not_declare_gate_close`.

## stronger rewrites found in round_2

- Round_1: 벡터플면은 중간 형성체 판독면이다.  
  Round_2 stronger rewrite: 벡터플면은 `line-first surface`이며 `not team board`다. 즉 팀/worker보다 공간 표면의 line/relation/gap/export/reflux 반응을 먼저 읽는다.

- Round_1: 반환은 단순 결과가 아니라 trace/memory와 함께 돌아온다.  
  Round_2 stronger rewrite: `report return is not product completion`; completed는 보고가 돌아왔다는 뜻이지 제품 작업이 끝났다는 뜻이 아니다.

- Round_1: trace/memory를 다음 재료로 남긴다.  
  Round_2 stronger rewrite: `must write a return artifact, not chat-only notes`; chat-only note는 다음 순환 재료로 충분하지 않다.

- Round_1: latest runtime records should not be treated as permanent truth.  
  Round_2 stronger rewrite: latest completed execution도 current object / draft fingerprint / worker가 맞아야 current-run proof다.

- Round_1: stage와 maturity는 다르다.  
  Round_2 stronger rewrite: TSX의 `LineHealth`와 `VectorLineStage`는 current surface language이지만 final enum이나 maturity substitute가 아니다.

## immediately usable setup language

- 사용자면은 목적, 범위, 재료 문맥을 세우는 시작면이다.
- 벡터플면은 요청이 바로 실행으로 떨어지기 전 line, relation, gap, pending, reflux를 읽고 번역하는 중간 형성체 판독면이다.
- 엔진면은 ingest, process, validate를 수행하고 trace/memory와 함께 return을 남기는 처리/환류면이다.
- React/Vite 앱은 현재 사용자면/벡터플면 shell이고, Python `/vectorfl-engine/operate`는 engine-facing surface다.
- 실제 실행 증거는 화면 상태나 latest 이름만으로 확정하지 않고 freshness gate로 current object / draft / worker 연결을 확인한다.
- worker/CLI completed는 report return을 뜻할 수 있으며, product completion이나 gate close로 읽지 않는다.
- 내부 읽기 결과는 stable / unclear / next questions / line seeds로 분리해 report artifact로 남긴다.

## assistant grammar worth keeping

- 이 표현은 사용자면 / 벡터플면 / 엔진면 / 도구층 중 어디에 속하는가?
- 이 표현은 body-language / assistant-grammar / shared-language / future-layer 중 무엇인가?
- 이 산출은 language material인가, final schema인가, current lock인가, unresolved인가?
- 이 latest 실행은 current object / draft fingerprint / worker가 맞는가?
- 이 CLI/worker 상태는 `records only`, `draft only`, `read-only report return`, `execution`, `gate close` 중 무엇인가?
- 이 line 상태는 health/stage인가, maturity 판단인가?
- external search 전에 internal line이 shaped 되었는가?
- completed라는 말이 report returned인지 product completed인지 구분되어 있는가?

## expressions that should still not be locked

- `VectorFL surface as final workflow manager`
- `Team Relay Board` as body skeleton
- `automatic routing / queue distribution`
- TSX `LineHealth` and `VectorLineStage` as final enums
- `stable / unclear / next_questions / line_seeds` as final return schema
- `persistent_assignment_gate_inspector` as body skeleton
- Paperclip `IssueProperties` lineage as current integrated-engine body language
- latest manifest field names as permanent API schema

## open gaps for round_3

- How to display `maturity_level` separately from TSX `LineHealth` and `VectorLineStage`.
- How to define the minimum return artifact fields without turning them into final schema too early.
- How to keep VectorFL surface as operating waist candidate without promoting it into a workflow hub.
- Where handoff/waiting/report should live during low-intensity operation.
- Whether freshness gate needs a small regression fixture for stale completed false positives.
- How much of `persistent_assignment_gate_inspector` is reusable shared language and how much is Paperclip lineage/future UI work.
