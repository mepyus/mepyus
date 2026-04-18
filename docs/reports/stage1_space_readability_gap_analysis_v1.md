# stage1_space_readability_gap_analysis_v1

## 목적
현재 엔진 구조를 탐색/응결핵/관계 판독 관점에서 읽고
이미 되는 것과 아직 비어 있는 것을 bounded하게 구분한다.

## ALREADY_AVAILABLE

### 1. input_ref / write_trace / evidence_refs
- source:
  - receipts
  - per-run boards
  - per-run commands
  - provenance link index
  - origin maps
- reading:
  - 새 입력이 어떤 산출을 만들었는지 다시 내려가는 경로는 이미 충분히 있다.

### 2. related_run_ids
- source:
  - receipt
  - operation_board_latest
  - per-run board
  - commands artifacts
- reading:
  - run-level identity는 이미 강하다.

### 3. related_session_ids
- source:
  - Gemini observer logs
  - session baseline docs
- reading:
  - 세션 레벨 묶음도 observer 레인에서는 이미 가능하다.

### 4. user-language translation seed
- source:
  - Gemini observer logs
  - external case relation reading example
- reading:
  - 내부 상태를 사용자 언어로 풀어쓰는 seed는 이미 있다.

## PARTIALLY_AVAILABLE

### 5. focus_labels / focus_anchor / focus_object
- source:
  - label packet
  - observer_ingest_min outputs
  - external case relation example
- reading:
  - 형성용 값은 있지만 탐색 판독용 focus object로 정규화되지는 않았다.

### 6. relation_kind
- source:
  - external_case_relation_reading_contract
  - observation probe contract
- reading:
  - 문서 문법으로는 있지만 runtime return contract로는 아직 약하다.

### 7. relation_reason / hold_reason / separation_reason
- source:
  - external case example
  - Gemini summary
  - various reports
- reading:
  - 이유를 적는 관습은 있으나 표준 슬롯은 아직 없다.

### 8. future_use_hint / borrowable_structure / not_adopted_reason
- source:
  - external case example
  - planning docs
- reading:
  - 개념은 이미 있으나 탐색 결과의 필수 산출로 잠겨 있지는 않다.

## MISSING_BUT_ATTACHABLE

### 9. exploration observation artifact
- why missing:
  - 현재 observer는 session summary와 generic observation 위주다.
- why attachable:
  - `runtime/observer/` 아래에 exploration-specific note 또는 sidecar json을 붙이면 코어를 안 흔들고 수용 가능하다.

### 10. standardized relation output bundle
- why missing:
  - 현재는 relation kind와 reason이 문서 예시 안에만 있고 run output contract에는 없다.
- why attachable:
  - `docs/templates/` + `runtime/observer/exploration/` 조합으로 보조 기록층 추가 가능.

### 11. record_target normalization
- why missing:
  - 결과를 어디에 남길지 사람이 문맥으로 판단한다.
- why attachable:
  - `observer`, `reports`, `receipts appendix`, `sidecar json` 중 표준 후보를 문서 계약으로 추가 가능.

## MISSING_AND_NOT_NEEDED_NOW

### 12. global relation engine
- reading:
  - 지금은 필요 없다. 현재 단계는 bounded review와 sidecar observation이면 충분하다.

### 13. ontology-like hard schema
- reading:
  - 지금 단계에선 과하다. 현재 엔진 방향과도 어긋난다.

### 14. full exploration UI
- reading:
  - 지금은 관찰 워크벤치 정의까지만 가면 된다.

## 총평
- 현재 엔진은 `근거 회수`와 `기록 추적`에는 강하다.
- 현재 엔진은 `탐색 의미 판독 반환`에서는 아직 보조층이 필요하다.
- 따라서 이번 단계의 정답은 코어 대수술이 아니라
  `exploration observation sidecar` 와 `relation note template` 을 붙이는 것이다.
