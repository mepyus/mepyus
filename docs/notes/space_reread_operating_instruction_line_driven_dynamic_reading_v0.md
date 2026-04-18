# space reread operating instruction / line-driven dynamic reading v0

## purpose

이번 노트는 현재 explicit line들을 동적 판독면으로 다루며
공간 전체를 다시 읽기 위한 실전 작전서다.

line을 taxonomy 항목으로 고정하지 않는다.
각 line을 들고 공간을 훑으면서
새로운 면, 연결, hub 후보를 드러내는 것이 목적이다.

## explicit line sources

- `runtime/manifests/line_registry.json`
- `runtime/manifests/latent_line_registry_v1.json`

## active lines

### registry lines

- `pre_read_eye`
- `raw_return_preservation`
- `input_to_reading_organ`
- `transition_over_surface`

### latent registry lines

- `alignment_before_autonomy`
- `harness_over_model`
- `work_absorption_harness`

### reread-added lines

- `late-condensation instead of concept-first fixation`
- `preservation before closure`
- `reread as the real operating motion`
- `human-language surface is not decoration`
- `user thought itself is already source material`
- `inspection against premature naming`

## common operating rules

1. line을 정의하지 않는다. 재료를 가리킨다.
2. 각 line은 공간 전체를 다시 읽는 렌즈다.
3. reread 결과는 provenance와 함께 기록한다.
4. local pattern과 thick line을 구분한다.
5. hub는 두 개 이상의 독립 경로에서 교차가 확인된 뒤에만 후보로 올린다.
6. premature naming을 경계한다.

## reread order

1. registry lines 먼저
2. latent registry lines 다음
3. reread-added lines 마지막
4. 각 line reread 후 hub candidate 교차 확인
5. 전체 결과를 line별 operating report로 남길 것

## line-by-line entry points

### `pre_read_eye`

- 먼저 읽을 곳
  - `runtime/manifests/line_registry.json`
  - `app/core/runtime/post_preprocess_first_pass.py`
  - `app/core/runtime/external_input_gate.py`
  - `runtime/breadcrumbs.jsonl`
- human-language surface
  - 이 자료를 읽기 전에 나는 이미 무엇을 기대하고 있었는가?
  - 공간이 새 인풋을 어떤 눈으로 먼저 보는가?

### `raw_return_preservation`

- 먼저 읽을 곳
  - `app/core/runtime/file_store.py`
  - `app/core/registry/provenance_hygiene.py`
  - `app/fragment/store.py`
  - `app/core/state_store/history_compaction_policy.py`
- human-language surface
  - 이 판단은 원본에서 온 것인가, 가공 이후에서 온 것인가?
  - 나중에 되돌아볼 때 원형 재료가 남아 있는가?

### `input_to_reading_organ`

- 먼저 읽을 곳
  - `app/core/runtime/inputter.py`
  - `app/core/runtime/external_input_gate.py`
  - `app/core/runtime/external_transcript_preprocess.py`
  - `app/input_layer/*`
  - `app/core/runtime/observer.py`
- human-language surface
  - 이 자료가 어떻게 공간 안으로 들어오는가?
  - 들어오는 과정에서 무엇이 바뀌고 무엇이 유지되는가?

### `transition_over_surface`

- 먼저 읽을 곳
  - `runtime/manifests/line_registry.json`
  - `app/core/runtime/line_thickening.py`
  - `runtime/logs/line_promotion_log.jsonl`
  - `app/work/observer_ingest_min/generated/*`
- human-language surface
  - 이 기능/문서/코드는 어떤 표면을 넘어서 작동하는가?
  - 전환이 일어날 때 무엇이 손실되고 무엇이 보존되는가?

### `alignment_before_autonomy`

- 먼저 읽을 곳
  - `runtime/manifests/latent_line_registry_v1.json`
  - `docs/contracts/*`
  - `docs/baselines/*`
  - `app/core/runtime/approval_policies.py`
  - `app/core/runtime/review_policies.py`
- human-language surface
  - 이 작업을 agent에게 넘기기 전에 방향이 맞춰졌는가?
  - 정렬 없는 자율화가 어떤 비용을 만드는가?

### `harness_over_model`

- 먼저 읽을 곳
  - `runtime/manifests/latent_line_registry_v1.json`
  - `app/core/runtime/approval_policies.py`
  - `app/core/runtime/review_policies.py`
  - `app/core/runtime/external_input_gate.py`
- human-language surface
  - 모델이 좋아서 결과가 좋은가, 운영 구조가 좋아서 결과가 좋은가?
  - harness 없는 모델 호출이 어떤 결과를 만드는가?

### `work_absorption_harness`

- 먼저 읽을 곳
  - `runtime/manifests/latent_line_registry_v1.json`
  - `app/core/runtime/observer.py`
  - `app/core/runtime/workspace_manifest.py`
  - `app/core/runtime/workspace_report.py`
  - `app/core/runtime/reactive_space_report.py`
- human-language surface
  - 이 작업은 공간에 흔적을 남기는가?
  - 작업이 끝난 뒤 공간이 달라졌는가?

### `late-condensation instead of concept-first fixation`

- 먼저 읽을 곳
  - `docs/reports/internal_space_line_drawing_practice_v0.md`
  - `docs/reports/interpretive_line_thickening_practice_v0.md`
  - `app/core/runtime/line_thickening.py`
- human-language surface
  - 이 개념을 지금 이름 붙여야 하는가, 아직인가?
  - 빠른 개념화가 이후 읽기를 막고 있는가?

### `preservation before closure`

- 먼저 읽을 곳
  - `docs/reports/internal_space_line_drawing_practice_v0.md`
  - `app/core/registry/provenance_hygiene.py`
  - `app/core/state_store/history_compaction_policy.py`
  - `app/core/runtime/review_state_ledger.py`
- human-language surface
  - 이걸 지금 닫아야 하는가?
  - 닫기 전에 아직 드러나지 않은 것이 있는가?

### `reread as the real operating motion`

- 먼저 읽을 곳
  - `docs/reports/interpretive_line_thickening_practice_v0.md`
  - `app/core/runtime/reread_audit.py`
  - `app/core/runtime/runtime_view_refresh.py`
  - `app/core/runtime/observer.py`
- human-language surface
  - 이 판단은 한 번 읽고 내린 것인가, 다시 읽고 내린 것인가?
  - 다시 읽으면 달라지는 것이 있는가?

### `human-language surface is not decoration`

- 먼저 읽을 곳
  - `docs/reports/internal_space_line_drawing_practice_v0.md`
  - `docs/reports/interpretive_line_thickening_practice_v0.md`
  - 현재 명령/지시 자산들
- human-language surface
  - 이 문서는 읽고 끝나는가, 읽고 판단하게 만드는가?
  - 기술 설명이 행동을 만드는가?

### `user thought itself is already source material`

- 먼저 읽을 곳
  - `docs/reports/internal_space_line_drawing_practice_v0.md`
  - 현재 대화 흐름
  - `inputs/*`
  - `app/core/runtime/inputter.py`
- human-language surface
  - 내 생각이 공간에 들어갔는가?
  - 공간이 내 생각을 재료로 쓰고 있는가, 아니면 소비하고 있는가?

### `inspection against premature naming`

- 먼저 읽을 곳
  - `docs/reports/internal_space_line_drawing_practice_v0.md`
  - `runtime/manifests/line_registry.json`
  - `runtime/logs/line_promotion_log.jsonl`
  - `app/core/runtime/line_thickening.py`
- human-language surface
  - 이 이름이 지금 붙여도 되는 이름인가?
  - 이름을 붙인 뒤 재료 읽기가 줄었는가?

## current hub candidates — do not declare yet

### reading-discipline hub

- `late-condensation instead of concept-first fixation`
- `preservation before closure`
- `inspection against premature naming`

### operating-structure hub

- `alignment_before_autonomy`
- `harness_over_model`
- `work_absorption_harness`

### space-motion hub

- `reread as the real operating motion`
- `input_to_reading_organ`
- `transition_over_surface`

### origin-preservation hub

- `raw_return_preservation`
- `user thought itself is already source material`
- `human-language surface is not decoration`

## output rule

결과는 정의집이 아니다.

각 line별로 아래만 짧게 남긴다.

- 살아난 곳
- 살아나지 않은 곳
- local / thick 판단
- hub 교차 조짐
- human-language one-liner
