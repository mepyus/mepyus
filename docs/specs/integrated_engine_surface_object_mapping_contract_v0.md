# Integrated Engine Surface Object Mapping Contract v0

## 1. Purpose

이 문서는 통합엔진 3면이 앞으로 어떤 구조 객체를 받아야 살아나는지 잠그기 위한 매핑 계약이다.

현재 목표는 기능 구현이 아니다. 화면을 mock로 보지 않고, 앞으로 공간 상태를 받을 수 있는 슬롯으로 읽기 위해 최소 객체 경계를 먼저 고정한다.

이 문서는 `docs/specs/integrated_engine_operating_methodology_direction_v0.md`의 방향지시서 위에 얹히는 객체 매핑 문서다.

## 2. Surface Role Lock

### 2-1. User Surface

역할:

- 목적 선언
- 팀 운영
- 담당 배치
- 진행 관찰

핵심 객체:

- `UserGoalState`
- `TeamFlowState`

보강 객체:

- `WorkMemoryRecord`

금지 오해:

- 단순 task board로 축소하지 않는다.
- 엔진 내부 inventory를 사용자면의 주된 데이터 구조로 삼지 않는다.

### 2-2. VectorFL Surface

역할:

- 사용자면과 엔진면 사이의 중간 통로
- line, relation, gap, genealogy, ingress, reflux 상태 표면화

핵심 객체:

- `VectorFlowState`

금지 오해:

- line viewer로만 축소하지 않는다.
- 팀 운영면이나 엔진 조작면으로 바꾸지 않는다.

### 2-3. Engine Surface

역할:

- 외부 자료 입력
- 파이프라인 처리
- 자산 감시
- 검증 환류와 재투입 감독
- 정비 상태 관찰

핵심 객체:

- `EngineIngestState`
- `EnginePipelineState`
- `ValidationReturnPacket`

보강 객체:

- `EngineAssetRegistry`
- `WatchpointRegistry`
- `EventTraceState`
- `WorkMemoryRecord`

금지 오해:

- 일반 admin dashboard로 만들지 않는다.
- 지금 없는 자율 실행 능력을 UI가 이미 가진 것처럼 고정하지 않는다.

## 3. Object Contracts

이 절의 필드는 최종 스키마가 아니라 최소 surface contract다. 실제 런타임 상태와 맞추는 과정에서 필드는 확장될 수 있다.

### 3-1. UserGoalState

소유 표면:

- 사용자면

목적:

- 사용자의 운영 선언을 단순 문자열이 아니라 목적 상태 객체로 받는다.

최소 필드 후보:

- `goal_id`
- `title`
- `purpose`
- `scope`
- `constraints`
- `expected_outputs`
- `status`
- `linked_ingest_ids`

주요 연결 패널:

- 목적 선언 헤더
- 현재 목적과 연결된 재료 요약

주의:

- `title`은 기존 goal input의 중심 문자열이 될 수 있지만, 사용자면은 `title`만 보지 않고 목적의 범위와 제약, 연결 재료까지 함께 읽어야 한다.

### 3-2. TeamFlowState

소유 표면:

- 사용자면

목적:

- 팀 배치, 팀 간 relay, handoff 흐름을 상태 객체로 받는다.

최소 필드 후보:

- `flow_id`
- `goal_id`
- `teams`
- `current_team_id`
- `handoff_order`
- `input_refs`
- `output_refs`
- `status`

`teams` 최소 필드 후보:

- `team_id`
- `team_name`
- `role`
- `status`
- `instruction`
- `input_refs`
- `output_refs`

주요 연결 패널:

- 팀 라우팅 보드
- 실행 흐름 보드
- handoff 보드
- 보고 / 로그 센터

주의:

- backlog, active, handoff, review는 단순 칸반 상태가 아니라 팀 간 relay 흐름으로 읽어야 한다.

### 3-3. VectorFlowState

소유 표면:

- 벡터플면

목적:

- 현재 목적이 공간 안에서 line, relation, gap, genealogy, ingress, reflux로 어떻게 드러나는지 받는다.

최소 필드 후보:

- `flow_id`
- `goal_id`
- `summary`
- `active_lines`
- `gaps`
- `lineage_events`

`active_lines` 최소 필드 후보:

- `line_id`
- `title`
- `health`
- `current_stage`
- `source_refs`
- `connected_to`

`gaps` 최소 필드 후보:

- `gap_id`
- `title`
- `why`
- `linked_line_ids`

`lineage_events` 최소 필드 후보:

- `event_id`
- `line_id`
- `type`
- `title`
- `time`
- `detail`

주요 연결 패널:

- 상단 요약 영역
- Line Atlas
- Genealogy 패널
- Relation / Gap 패널
- ingress / export / reflux strip

주의:

- `current_stage`는 ingress, processing, export_waiting, reflux, pending_validation 같은 흐름 strip의 기준이 된다.

### 3-4. EngineIngestState

소유 표면:

- 엔진면

목적:

- 외부 자료가 무엇이고, 어떤 목적과 연결되었으며, 지금 어디까지 공간 재료로 처리되었는지 받는다.

최소 필드 후보:

- `ingest_id`
- `source_label`
- `source_path`
- `source_type`
- `status`
- `linked_goal_ids`
- `created_at`
- `updated_at`

주요 연결 패널:

- 외부 자료 입력 입구
- 현재 입력 재료 상태 요약

주의:

- 엔진면의 입력 입구는 단순 파일 목록이 아니라 공간 재료화 상태를 보여줘야 한다.

### 3-5. EnginePipelineState

소유 표면:

- 엔진면

목적:

- 원본 번역, 입력기, 라인 생성, 라인 번역, 추출, 공간 분석, 검증으로 이어지는 처리 흐름을 받는다.

최소 필드 후보:

- `pipeline_id`
- `ingest_id`
- `current_step`
- `steps`
- `status`

`steps` 최소 필드 후보:

- `step_id`
- `name`
- `status`
- `started_at`
- `finished_at`
- `note`

주요 연결 패널:

- 파이프라인 상태 패널

주의:

- 엔진면은 inventory만 보여주는 면이 아니다. 처리 흐름과 각 단계의 상태를 함께 드러내야 한다.

### 3-6. ValidationReturnPacket

소유 표면:

- 엔진면

목적:

- 검증팀이 읽은 결과와 과정 잔여물을 다시 공간 재료로 환류할 수 있게 받는다.

최소 필드 후보:

- `packet_id`
- `goal_id`
- `summary`
- `accepted_refs`
- `hold_refs`
- `reasoning_notes`
- `next_reingest_requested`
- `status`

주요 연결 패널:

- 환류 패널
- 검증 재투입 패널
- supervisor queue

주의:

- 검증은 판정 결과가 아니라 다시 넣을 재료로 읽어야 한다.

### 3-7. EngineAssetRegistry

소유 표면:

- 엔진면

목적:

- 엔진이 다루는 자산 목록과 상태를 registry로 받는다.

최소 필드 후보:

- `assets`

`assets` 최소 필드 후보:

- `asset_id`
- `kind`
- `title`
- `path`
- `health`
- `updated_at`
- `summary`

주요 연결 패널:

- Asset Inventory Tree
- Selected Asset Inspector

### 3-8. WatchpointRegistry

소유 표면:

- 엔진면

목적:

- 자산, 처리 흐름, 환류 과정에서 봐야 할 watchpoint를 받는다.

최소 필드 후보:

- `items`

`items` 최소 필드 후보:

- `watchpoint_id`
- `title`
- `severity`
- `status`
- `why`
- `next_action`
- `asset_id`

주요 연결 패널:

- Watchpoint Registry
- Selected Asset Inspector
- supervisor queue

### 3-9. EventTraceState

소유 표면:

- 엔진면

목적:

- 처리와 상태 변화의 event trace를 받는다.

최소 필드 후보:

- `events`

`events` 최소 필드 후보:

- `event_id`
- `type`
- `title`
- `detail`
- `time`
- `asset_id`

주요 연결 패널:

- Event Console
- Selected Asset Inspector

### 3-10. WorkMemoryRecord

소유 표면:

- 사용자면
- 엔진면
- 전체 보강층

목적:

- 이번 턴의 판단, hold 이유, close-out, 다음 작업 방향을 과정 기억으로 남긴다.

최소 필드 후보:

- `record_id`
- `goal_id`
- `summary`
- `decision`
- `hold_reason`
- `closeout_note`
- `next_direction`
- `refs`
- `created_at`

주요 연결 패널:

- 보고 / 로그 센터
- operating rules / 기록 영역
- supervisor queue

주의:

- `WorkMemoryRecord`는 결과 로그가 아니라 환류 가능한 운영 기억이다.

## 4. Attachment Priority

### 4-1. Priority 1

먼저 붙일 객체:

- 사용자면 ↔ `UserGoalState`
- 사용자면 ↔ `TeamFlowState`
- 엔진면 ↔ `EngineIngestState`
- 엔진면 ↔ `EnginePipelineState`

이 4개가 붙으면 사용자면과 엔진면은 최소한 선언과 처리를 받는 표면이 된다.

### 4-2. Priority 2

다음에 붙일 객체:

- 벡터플면 ↔ `VectorFlowState`
- 엔진면 ↔ `ValidationReturnPacket`

이 2개가 붙으면 중간 통로와 검증 환류 구조가 살아난다.

### 4-3. Priority 3

보강층 객체:

- 엔진면 ↔ `EngineAssetRegistry`
- 엔진면 ↔ `WatchpointRegistry`
- 엔진면 ↔ `EventTraceState`
- 전체 ↔ `WorkMemoryRecord`

이 층은 감독, 기록, 세부 운영을 두껍게 만든다.

## 5. Current Non-Goals

이 객체 매핑을 잠근다고 해서 아래를 구현하지 않는다.

- 화면에서 직접 repo 수정
- 화면에서 직접 스크립트 생성/수정 실행
- CLI 자동 운영
- 사용자면/엔진면에서 자율 실행 주체 부착
- 벡터플면을 운영면으로 변경
- mock 화면에 기능을 계속 덧붙이는 방식의 확장

현재 목표는 상태와 흐름을 받을 구조 슬롯을 잠그는 것이다.

## 6. One-Line Lock

다음 단계는 mock에 기능을 더 얹는 것이 아니라, 사용자면, 벡터플면, 엔진면이 각각 어떤 구조 객체를 받아야 자기 역할을 하는지 먼저 고정하는 것이다.
