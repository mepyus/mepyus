# Integrated Engine CLI Deposit Candidate

- source_session_id: `cli_20260418T100549Z_b6ef0965`
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
외부 렌즈 재료 읽기: OpenCode / Claude Code 화면 선례는 참고만 하고 아직 자동 확장하지 않음

## Used Context Refs
- `docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md`

## Result Summary
ss/ui/react_launcher.py)는 React terminal frontend를 띄우고, 별도 backend-only 명령을 프론트 설정으로 넘긴다. 즉 UI가 엔진을 직접 품기보다 백엔드 세션 명령을 호출하는 구조다.
    - 브리지/세션: [session_runner.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/openharness-main/src/openharness/bridge/session_runner.py)는 bridge-managed child session을 spawn/kill하는 얇은 세션 핸들 구조다.
    - 확장 재료: `tools`, `skills`, `plugins`, `hooks`, `mcp`, `permissions`, `memory`, `swarm`, `tasks`, `sandbox`가 독립 폴더로 분리되어 있다.
    - 상위 앱: [ohmo](/Users/sungsookim/universe/vectorfl_replica/references/git_search/openharness-main/ohmo)는 OpenHarness 위에 올라가는 개인 에이전트/게이트웨이 앱이다. VectorFL 기준으로는 core engine이 아니라 “패키지 위 응용층”에 가깝다.
  - VectorFL 대비:
    - 우리 안정 UI는 [app/ui/integrated_engine](/Users/sungsookim/universe/vectorfl_replica/app/ui/integrated_engine)이며, 기준 노트상 `gemini/mock_test`는 참고/제안 clay다.
    - 우리 [runtime](/Users/sungsookim/universe/vectorfl_replica/runtime)은 세션 산출물/manifest/state/return 보관 성격이고, OpenHarness의 프론트 소스처럼 취급하면 안 된다.
    - OpenHarness의 `frontend -> backend-only -> engine/tool loop` 패턴은 참고 가능하지만, VectorFL의 고정 3-surface body와 CLI-on-top boundary를 대체하거나 자동 확장하는 근거는 아니다.

- uncertainty or failure notes
  - evidence bundle은 여전히 thin evidence다. 실제로 읽은 것은 첨부 노트 1개와 OpenHarness 로컬 참조 폴더의 구조/주요 파일 일부다.
  - 테스트 실행, 동작 검증, 외부 웹 확인, 파일 수정은 하지 않았다.
  - OpenHarness의 전체 내부 흐름을 완전 역추적한 것은 아니며, 이번 산출은 큰 틀의 구조 분해용 operating summary다.

- suggested next use
  - reread target: `OpenHarness external lens reread - engine / integrated engine / package split`
  - deposit candidate: `docs/reports` 계열에 “외부 렌즈 자료”로 둘 수 있으나, 현재 턴에서는 no promotion / no ingestion / no canonicalization 유지.
  - validation target: 아직 아님. 먼저 VectorFL이 위 분해를 재읽고 “참고만 할 항목”과 “우리 구조에 비교 가능한 항목”을 분리하는 단계가 필요하다.
  - implementation return: 아님. 구현 변경이나 자동 확장으로 연결하지 말 것.


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

