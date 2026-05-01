# Integrated Engine CLI Deposit Candidate

- source_session_id: `cli_20260418T233627Z_91e863f5`
- backend_kind: `codex`
- task_type: `reread`
- requested_by_surface: `vectorfl_surface`
- requested_by_page: `app/ui/integrated_engine`
- status: `done`

- route_label: `engine_request_candidate`
- current_marks: `none`
- user_decision_state: `pending_candidate_review`
- canonical_deposition_state: `not_ingested`

## Task Purpose
내부 설계 증명: 신규 패키지. 중앙 setup에서 목적/렌즈/근거를 잡은 뒤 CLI 실행으로 보낼 수 있음

## Used Context Refs
- `gemini/external_analysis`

## Result Summary
reread_target: `app/ui/integrated_engine/folder_status.md`
  - reread_target: `runtime/contracts/integrated_engine_single_handler_package_instance_v0.json`
  - validation_target: 이후에 `PackageStack -> central setup -> CliHostControlPanel -> readable return/deposit candidate`가 실제 한 패킷으로 이어지는지 화면/상태 기준 검증.
  - implementation_return: 아직 아님.
  - deposit_candidate: 아직 아님.
  - hold: 외부 분석 ref를 설계 근거로 과확장하는 해석은 hold.

- What must not be inferred
  - 신규 패키지 구조가 final schema로 확정되었다고 보면 안 된다.
  - CLI를 네 번째 surface로 보면 안 된다.
  - User surface에서 Engine surface로 직접 우회한다고 보면 안 된다.
  - `packageStackSeed`나 현재 TSX type을 canonical package DB / enum / state machine으로 보면 안 된다.
  - `gemini/external_analysis`를 canonical source나 ingest된 내부 지식으로 보면 안 된다.
  - deposit candidate가 실제 ingest/deposit 완료를 뜻한다고 보면 안 된다.

- uncertainty or failure notes
  - 문서 기준은 일부 시차가 있다. 04-14 문서들은 `runtime/views/vectorfl_dual_surface_app`를 current React surface로 말하고, 04-16/04-17 `app/ui/integrated_engine/folder_status.md`는 `app/ui/integrated_engine`를 현재 main implementation area로 재지정한다. 최신 폴더 상태 기준으로는 `app/ui/integrated_engine`를 우선 읽는 것이 타당하다.
  - attached evidence ref는 thin evidence다. 내부 구조 판단은 repo 내부 문서와 코드 읽기에서 보강했지만, promotion / ingestion / canonicalization은 수행하지 않았다.

- suggested next use: reread target / implementation return / validation target / deposit candidate
  - suggested next use: reread target
  - next reread packet:
    - target: `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
    - lens: “신규 package intake가 central setup을 거쳐 CLI host turn payload로 변환되는가”
    - evidence: `WorkPacketDraft`, `PackageStack`, `CliHostControlPanel` props/state 연결부, contract imports
    - expected return: “구조 연결 판정 + 빠진 연결부 목록”
  - 그 다음 단계는 validation target이 적절하다. Implementation return이나 deposit candidate는 아직 이르다.


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

