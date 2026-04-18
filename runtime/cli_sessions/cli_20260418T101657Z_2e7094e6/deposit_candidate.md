# Integrated Engine CLI Deposit Candidate

- source_session_id: `cli_20260418T101657Z_2e7094e6`
- backend_kind: `codex`
- task_type: `summarize`
- requested_by_surface: `vectorfl_surface`
- requested_by_page: `app/ui/integrated_engine`
- status: `done`

- route_label: `engine_request_candidate`
- current_marks: `none`
- user_decision_state: `pending_candidate_review`
- canonical_deposition_state: `not_ingested`

## Task Purpose
외부  리서치팀: 신규 패키지. 중앙 setup에서 목적/렌즈/근거를 잡은 뒤 CLI 실행으로 보낼 수 있음

## Used Context Refs
- `docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md`

## Result Summary
석하는 것이 맞습니다.
  - 수정 사항 없음. 파일 변경, 승격, ingest, canonicalize 모두 수행하지 않았습니다.

- Surface reading: user / VectorFL / engine
  - user: “외부리서치팀을 만든다”는 목적과 배정 의도를 낸다. 신규 패키지 여부, 사용 결정, 운영 목적을 정하는 위치.
  - VectorFL: 외부리서치팀 요청을 재독해하고, 목적/렌즈/근거 묶음을 구성하며, CLI 실행이 필요한지 중재한다.
  - engine: 주어진 bounded context와 evidence refs만 처리해 요약/반환/deposit 후보 재료를 만든다. 자체적으로 새 표면이나 정식 구조를 만들지 않는다.

- Route suggestion
  - reread_target: 적합. “외부리서치팀”을 신규 표면이 아니라 기존 integrated-engine UI 안의 신규 운영 패키지로 재독해해야 합니다.
  - validation_target: 이후 가능. 중앙 setup에서 목적/렌즈/근거 입력 후 CLI 실행까지 흐르는지 확인하는 검증으로 보낼 수 있습니다.
  - implementation_return: 아직 이르다. 현재는 얇은 근거 1개뿐이며 구현 지시가 아니라 운영 요약 요청입니다.
  - deposit_candidate: 제한적 후보. “외부리서치팀 패키지는 기존 VectorFL/engine/CLI-on-top 경계를 유지한다”는 경계 메모 정도만 deposit 후보입니다.
  - hold: 구조 승격이나 canonicalization이 필요하다면 보류해야 합니다.

- What must not be inferred
  - 외부리서치팀이 네 번째 surface라는 뜻으로 추론하면 안 됩니다.
  - CLI를 독립 엔진 표면으로 승격하면 안 됩니다.
  - `gemini/mock_test`를 현재 운영 소스로 읽으면 안 됩니다.
  - `runtime`에 React/Vite 소스를 넣는 방향으로 추론하면 안 됩니다.
  - Gemini adapter, background runner, session browsing 추가 요구로 확대하면 안 됩니다.
  - 이 단일 근거 문서를 canonical source로 승격하거나 ingest한 것으로 간주하면 안 됩니다.

- uncertainty or failure notes
  - 근거가 `docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md` 하나뿐이라 얇습니다.
  - 외부리서치팀 패키지의 입력 스키마, 권한 범위, 결과 deposit 규칙은 아직 근거에서 확정되지 않았습니다.
  - 실제 브라우저 hand-check 여부는 근거 문서상 다음 단계로 남아 있습니다.

- suggested next use: reread target / implementation return / validation target / deposit candidate
  - suggested next use: `reread_target`
  - reread target: “외부리서치팀 신규 패키지”를 기존 `app/ui/integrated_engine` 안에서 목적/렌즈/근거를 구성해 CLI 실행으로 넘기는 운영 패키지로 재독해.
  - validation target: 이후 stable UI에서 중앙 setup → CLI 실행 → engine return 흐름을 한 번 검증.
  - deposit candidate: “외부리서치팀은 새 surface가 아니며 CLI는 on-top layer”라는 경계 메모만 후보.


## Important Diffs / Findings / Outputs
- not separated in package 1 return


## Uncertainty / Failure Notes
- none recorded


## Suggested Next Use
validation_target

## Validation / Decision Boundary
- This file is a deposition candidate only.
- It is not canonical memory, not an approved record, and not automatic ingestion.
- User decision or a later explicit deposition package is still required.

