# Integrated Engine Surface Object Contracts v0

## 1. Purpose

이 문서는 통합엔진 surface object contract의 첫 얇은 잠금이다.

이 문서는 DB 설계서가 아니고, 엔진 내부 canonical model 문서도 아니다. 지금 단계의 성격은 아래와 같다.

- final schema 아님
- surface contract 후보 문서
- mock -> actual state 연결을 위한 중간 계약 문서
- 역할, 경계, 금지선을 먼저 잠그는 문서

목표는 각 surface가 자기 역할을 하려면 어떤 상태 종류를 받아야 하는지 의미 경계를 고정하는 것이다.

## 2. Shared Contract Template

각 contract는 아래 순서를 따른다.

1. Contract Name
2. Role
3. Owning Surface
4. Why This Surface Needs It
5. Minimal Fields
6. Optional Fields
7. Explicitly Excluded For Now
8. Mock Attachment Point
9. Actual Attachment Point
10. Transition Rule
11. Open Questions

작성 원칙:

- 최종 스키마처럼 쓰지 않는다.
- 필드보다 역할과 경계를 먼저 쓴다.
- optional과 excluded를 반드시 분리한다.
- mock attachment point와 actual attachment point를 같이 적는다.
- open questions를 남기고 억지로 수렴하지 않는다.

## 3. UserGoalState

### Contract Name

UserGoalState

### Role

사용자면이 현재 목적 선언을 읽고 운영 중심축으로 삼기 위한 객체.

### Owning Surface

- owning surface: user surface
- secondary surface: engine surface summary, only if needed

### Why This Surface Needs It

사용자면이 단순 task board가 아니라 목적 선언, 범위 지정, 운영 기준 표면이 되기 위해 필요하다.

### Minimal Fields

- `goal_id`: 현재 목표를 식별하기 위한 최소 id.
- `title`: 목표 이름. 사용자면의 중심 제목.
- `purpose`: 왜 이 목표를 하는지 설명.
- `scope`: 이번 턴 또는 현재 흐름의 범위.
- `status`: 현재 목표 상태를 화면에 드러내기 위한 상태값.

### Optional Fields

- `constraints`
- `expected_outputs`
- `linked_ingest_ids`

### Explicitly Excluded For Now

- `execute_now`
- `auto_assign`
- `cli_operator_id`
- `repo_change_request`
- `autonomous_control_policy`

### Mock Attachment Point

- `runtime/views/vectorfl_dual_surface.tsx`의 goal / mission section
- `runtime/views/vectorfl_dual_surface_app/src/main.tsx`에서 주입 상태로 넘길 수 있는 boundary

### Actual Attachment Point

- 향후 user surface injected state layer
- `app/runtime/vectorfl_integrated_engine_api.py`의 `build_vectorfl_integrated_engine_state`에서 user-facing summary로 안정 공급될 수 있는 위치

### Transition Rule

목표 입력이 local `useState`를 넘어 injected state로 공급되어도 사용자면이 목적 선언면으로서 의미를 유지할 때 actual contract 후보로 승격한다.

### Open Questions

- `scope`를 문자열로 둘지 구조화할지.
- `constraints`를 지금 바로 surface에 노출할지.
- `linked_ingest_ids`가 1차 사용자면에서 필요한지, 엔진면 요약에서만 필요한지.

## 4. TeamFlowState

### Contract Name

TeamFlowState

### Role

사용자면이 팀 구성, 담당 배치, 팀 간 relay 흐름을 읽기 위한 객체.

### Owning Surface

- owning surface: user surface
- secondary surface: engine surface summary, only if needed

### Why This Surface Needs It

사용자면의 팀 보드가 단순 카드 목록이나 칸반 보드로 납작해지지 않고, 목적을 팀과 담당에게 배치하는 운영 표면이 되기 위해 필요하다.

### Minimal Fields

- `flow_id`: 팀 흐름 단위를 식별하기 위한 id.
- `goal_id`: 어느 목적에 연결된 팀 흐름인지 연결.
- `teams`: 팀 단위 상태 목록.
- `current_team_id`: 현재 relay 상에서 중심이 되는 팀.
- `status`: 전체 팀 흐름의 현재 상태.

`teams` 최소 필드:

- `team_id`: 팀 식별자.
- `team_name`: 화면에 표시할 팀 이름.
- `role`: 팀의 의미 역할.
- `status`: 팀의 현재 진행 상태.
- `instruction`: 이 팀에게 주어진 현재 지시.

### Optional Fields

- `handoff_order`
- `input_refs`
- `output_refs`
- `assignee_refs`
- `hold_reason`

### Explicitly Excluded For Now

- `auto_route`
- `auto_assign`
- `execute_team_now`
- `worker_spawn_payload`
- `repo_mutation_payload`

### Mock Attachment Point

- `runtime/views/vectorfl_dual_surface.tsx`의 Team Routing Board
- `runtime/views/vectorfl_dual_surface.tsx`의 Execution Route Board / Report Log Center

### Actual Attachment Point

- `app/runtime/vectorfl_integrated_engine_api.py`의 `team_registry`
- `app/runtime/vectorfl_integrated_engine_api.py`의 latest assignment / latest supervisor route readout

### Transition Rule

mock의 `teams`와 실제 `team_registry`, latest assignment, supervisor route가 2회 이상 같은 의미로 대응될 때 actual contract 후보로 승격한다.

### Open Questions

- `role`을 단일 문자열로 둘지 `primary_cell` 같은 내부 필드와 분리할지.
- `handoff_order`를 1차부터 노출할지.
- `TeamFlowState`가 report/log까지 포함할지, `WorkMemoryRecord`로 분리할지.

## 5. EngineIngestState

### Contract Name

EngineIngestState

### Role

엔진면이 외부 자료 입력 상태를 읽고 어떤 재료가 현재 엔진으로 들어오고 있는지 보여주기 위한 객체.

### Owning Surface

- owning surface: engine surface
- secondary surface: user surface material summary, only if needed

### Why This Surface Needs It

엔진면이 단순 inventory viewer가 아니라 공간 입력 입구를 가진 컨트롤면이 되기 위해 필요하다.

### Minimal Fields

- `ingest_id`: 입력 단위를 식별하는 id.
- `source_label`: 어떤 자료인지 보여주는 이름.
- `source_path`: 입력 위치.
- `source_type`: 입력 종류.
- `status`: 입력 처리 상태.

### Optional Fields

- `linked_goal_ids`
- `requested_by`
- `created_at`
- `updated_at`

### Explicitly Excluded For Now

- `direct_execute_command`
- `file_mutation_payload`
- `autonomous_retry_policy`
- `script_generation_instruction`
- `repo_write_request`

### Mock Attachment Point

- `gemini/mock_test/vectorfl_engine_surface_mock.tsx`의 ingest entry panel 후보 영역
- 현재는 명시 ingest panel이 약하므로 `SpaceHealthPanel` 또는 상단 summary와 분리될 새 입력 상태 영역 후보

### Actual Attachment Point

- `app/runtime/vectorfl_integrated_engine_api.py`의 `build_vectorfl_integrated_engine_state`
- 향후 `/api/vectorfl-engine/state`의 engine-facing ingest summary

### Transition Rule

실제 ingest 상태가 Python API 쪽에서 안정적으로 노출되고, 엔진면에서 mock seed가 아닌 actual state로 렌더링될 수 있을 때 연결한다.

### Open Questions

- `source_type` enum을 지금 어디까지 둘 것인지.
- `linked_goal_ids`가 engine surface에 즉시 필요한지.
- `requested_by`를 지금 surface에 보여줄 필요가 있는지.

## 6. EnginePipelineState

### Contract Name

EnginePipelineState

### Role

엔진면이 외부 자료 또는 작업 재료의 처리 파이프라인 상태를 읽기 위한 객체.

### Owning Surface

- owning surface: engine surface

### Why This Surface Needs It

엔진면이 admin dashboard나 단순 asset inventory가 아니라 원본 번역, 입력기, 라인 생성, 추출, 공간 분석, 검증 흐름을 보는 컨트롤면이 되기 위해 필요하다.

### Minimal Fields

- `pipeline_id`: 파이프라인 상태 단위를 식별하는 id.
- `current_step`: 현재 중심 단계.
- `steps`: 단계별 상태 목록.
- `status`: 전체 파이프라인 상태.

`steps` 최소 필드:

- `step_id`: 단계 식별자.
- `name`: 단계 이름.
- `status`: 단계 상태.
- `note`: 단계별 짧은 상태 메모.

### Optional Fields

- `ingest_id`
- `started_at`
- `finished_at`
- `output_refs`
- `error_summary`

### Explicitly Excluded For Now

- `run_step_now`
- `retry_command`
- `script_body`
- `scheduler_policy`
- `autonomous_recovery_plan`

### Mock Attachment Point

- `gemini/mock_test/vectorfl_engine_surface_mock.tsx`의 engine summary / supervisor queue 주변
- 명시 pipeline panel은 아직 약하므로 향후 `EnginePipelineState`용 panel 후보가 필요

### Actual Attachment Point

- `app/runtime/vectorfl_integrated_engine_api.py`의 `engine_loop`
- `app/runtime/vectorfl_integrated_engine_shell.py`의 `page-engine-only` 또는 future injected engine state

### Transition Rule

`engine_loop`의 stage 상태가 실제 runtime manifest와 일관되게 대응되고, 화면이 그 상태를 실행 버튼이 아니라 처리 흐름으로 읽을 수 있을 때 actual contract 후보로 승격한다.

### Open Questions

- `current_step`이 `engine_loop.stage_id`와 바로 대응되는지.
- ingest pipeline과 worker pipeline을 같은 객체로 볼지 분리할지.
- `status` enum을 surface 전용으로 둘지 runtime 상태값을 그대로 받을지.

## 7. VectorFlowState

### Contract Name

VectorFlowState

### Role

벡터플면이 현재 목적의 중간 흐름을 line, relation, gap, genealogy, ingress, export, reflux 상태로 읽기 위한 객체.

### Owning Surface

- owning surface: vectorfl surface
- secondary surface: user surface summary, only if needed

### Why This Surface Needs It

벡터플면이 단순 line viewer가 아니라 사용자면과 엔진면 사이에서 현재 흐름이 어떻게 표면화되는지 보여주는 중간 통로가 되기 위해 필요하다.

### Minimal Fields

- `flow_id`: 중간 흐름 단위를 식별하는 id.
- `goal_id`: 어느 목적과 연결되는지 표시.
- `summary`: 현재 흐름에 대한 짧은 요약.
- `active_lines`: 현재 표면에 드러난 line 목록.
- `gaps`: 보강이 필요한 결핍 목록.
- `lineage_events`: line 변화의 시간축 이벤트.

`active_lines` 최소 필드:

- `line_id`: line 식별자.
- `title`: line 이름.
- `health`: line 두께나 건강 상태.
- `current_stage`: ingress / processing / export / reflux / validation 대기 같은 흐름 단계.

### Optional Fields

- `source_refs`
- `connected_to`
- `export_refs`
- `reflux_refs`
- `relation_summary`

### Explicitly Excluded For Now

- `operate_line_now`
- `auto_strengthen_line`
- `external_search_command`
- `implementation_handoff_command`
- `repo_mutation_payload`

### Mock Attachment Point

- `runtime/views/vectorfl_dual_surface.tsx`의 Line Atlas
- `runtime/views/vectorfl_dual_surface.tsx`의 Line Genealogy / Relation Web / Line Event Stream

### Actual Attachment Point

- `app/runtime/vectorfl_integrated_engine_api.py`의 latest internal read report / latest synthesis report readout
- `app/runtime/vectorfl_integrated_engine_shell.py`의 `/vectorfl-engine/vectorfl` 렌더 경로

### Transition Rule

mock의 `Line` / `LineEvent`가 실제 `latest_internal_read_report.line_seeds` 또는 `latest_synthesis_report.confirmed_lines`에서 안정적으로 공급될 때 actual contract 후보로 승격한다.

### Open Questions

- `current_stage`를 실제 runtime 단계와 어떻게 맞출지.
- `health`를 surface 전용 값으로 둘지 내부 점수와 연결할지.
- relation과 gap을 `active_lines` 안에 둘지 별도 배열로 둘지.

## 8. ValidationReturnPacket

### Contract Name

ValidationReturnPacket

### Role

엔진면이 검증 결과와 과정 잔여물을 다시 공간 재료로 환류하기 위해 읽는 객체.

### Owning Surface

- owning surface: engine surface
- secondary surface: user surface report summary, only if needed

### Why This Surface Needs It

검증이 단순 pass/fail 판정으로 끝나지 않고, 어떤 판단과 잔여물이 다시 공간에 들어갈 가치가 있는지 드러내기 위해 필요하다.

### Minimal Fields

- `packet_id`: 검증 환류 패킷 식별자.
- `goal_id`: 어느 목적 흐름에서 나온 검증인지 연결.
- `summary`: 검증 환류 요약.
- `accepted_refs`: 다시 공간 재료로 받아들일 참조.
- `hold_refs`: 보류하거나 재검토할 참조.
- `status`: 환류 패킷 상태.

### Optional Fields

- `reasoning_notes`
- `next_reingest_requested`
- `validator_ref`
- `created_at`
- `related_pipeline_id`

### Explicitly Excluded For Now

- `auto_reingest_now`
- `gate_close_command`
- `repo_patch_payload`
- `script_execution_command`
- `autonomous_fix_request`

### Mock Attachment Point

- `gemini/mock_test/vectorfl_engine_surface_mock.tsx`의 supervisor queue / bridge panel 주변
- 향후 engine surface의 validation return / reflux panel 후보

### Actual Attachment Point

- `app/runtime/vectorfl_integrated_engine_api.py`의 latest supervisor gate / gemini review / worker execution readout
- `app/runtime/vectorfl_integrated_engine_shell.py`의 `page-engine-only` 또는 synthesis/verification return readout

### Transition Rule

검증 결과가 실제 manifest에서 `accepted`, `hold`, `next reingest` 의미로 안정적으로 분리되어 공급될 때 actual contract 후보로 승격한다.

### Open Questions

- `accepted_refs`와 `hold_refs`를 단순 string 배열로 둘지 ref object로 둘지.
- Gemini review와 Codex verification을 같은 packet으로 합칠지.
- `next_reingest_requested`를 boolean으로 둘지 별도 request object로 둘지.

## 9. One-Line Lock

이 문서의 contract들은 구현체나 최종 스키마가 아니라, 각 surface가 자기 역할을 하려면 어떤 상태 종류를 받아야 하는지 의미 경계와 금지선을 먼저 잠그는 중간 계약이다.
