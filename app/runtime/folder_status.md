# folder_status / runtime

## 1. Folder Identity
- path: `runtime`
- role_guess: Runtime execution and view layer for input, reporting, space view, measurement view, and operator-facing state.
- one_line_definition: `app/runtime` is the engine's active execution and projection layer.
- engine_position: body_runtime_layer
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `6`
- immediate_child_files: `24`
- file_types: `.py` x 24

## 3. Child Folders
- `bridge_layer`
- `ingest`
- `measurement_view`
- `reporting`
- `source_view`
- `space_view`

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `__init__.py`, `bootstrap.py`, `connection_engine.py`, `dust_field.py`, `file_store.py`, `graph_view.py`, `inputter.py`, `labeler.py`, `live_input.py`, `observer.py`, `operator_ui_state.py`, `reactive_space_report.py`, `region_atlas.py`, `reporting.py`, `reread_audit.py`, `scale_review.py`, `semantic_terrain_fields.py`, `semantic_terrain_geometry.py`, `sparse_presence_review.py`, `stage0_handoff.py`

## 6. Quick Reading
- 이 폴더는 immediate child folder 중심으로 읽는 것이 맞다.
- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.

## 7. Folder-Level Summary
- 이 폴더는 입력기에서 넘어온 재료를 실제 동작/관측/표면화 코드로 연결하는 실행층이다.
- `scripts/` 와 직접 연결되며, 산출은 root `runtime/` 에 남는다.
- 현재 중요한 하위 레인은 아래다.
  - `ingest/`
  - `source_view/`
  - `measurement_view/`
  - `space_view/`
  - `reporting/`
  - `bridge_layer/`
- 현재 엔진 전용 코드가 많지만, view/report/ingest 일부는 범용 실행 부품 후보로 읽을 수 있다.

## 8. Important Areas Now

### first priority
- `ingest`
- `source_view`
- `measurement_view`
- `reporting`

### second priority
- `space_view`
- `bridge_layer`
- `observer.py`
- `reporting.py`

### later priority
- `reread_audit.py`
- `scale_review.py`
- `sparse_presence_review.py`
- `semantic_terrain_*`

## 9. Key Files

### `bootstrap.py`
- current role: runtime 진입 보조
- function: runtime 동작 초기화/연결 보조
- input/output: runtime 실행 환경 세팅
- engine position: execution bootstrap
- reuse potential: 중간
- caution: 단독 의미보다 전체 runtime 흐름 안에서 봐야 한다

### `observer.py`
- current role: runtime observer 레이어
- function: observer 적용/관측 보조
- input/output: runtime artifacts <-> observer-enriched state
- engine position: observer-first runtime bridge
- reuse potential: 높음
- caution: `app/measurement/observer.py` 와 역할을 혼동하지 말 것

### `reporting.py`
- current role: runtime report 조립
- function: 결과 표면용 리포트 구성
- input/output: runtime internal state -> report artifacts
- engine position: report assembler
- reuse potential: 중상
- caution: 세부 build는 `scripts/` 와 함께 읽는 편이 정확하다

### `inputter.py`
- current role: 입력 재료를 runtime 흐름으로 넘기는 보조 진입점
- function: 입력 레이어와 runtime 사이 접점 형성
- input/output: input-layer materials -> runtime handling
- engine position: intake bridge
- reuse potential: 중상
- caution: 현재 엔진 전용 연결부가 섞여 있을 가능성이 높다

## 10. Current Reading
- 지금은 `app/runtime` 을 코드 실행면으로 읽는 것이 맞다.
- `scripts/` 가 바깥 실행 팔이라면, 이 폴더는 안쪽 동작 기관이다.
- 먼저 `ingest -> source/measurement/reporting -> space_view` 흐름을 읽고, 그 다음 review/audit 계열을 보면 된다.

## 11. Current Use Hint
- 이 문서는 first-pass runtime code index 이다.
- 다음 탐색에서는 하위 `ingest`, `source_view`, `measurement_view`, `reporting` 의 `folder_status.md` 를 먼저 읽고 필요한 파일만 연다.

## 12. Caution
- root `runtime/` 과 `app/runtime` 을 혼동하면 동작 코드와 산출 표면이 섞인다.
- review/audit 계열 파일은 현재 핵심 흐름보다 후순위다.
- 다음 보강은 하위 폴더별 핵심 `.py` 의 per-file block 확장으로 이어지는 것이 맞다.
