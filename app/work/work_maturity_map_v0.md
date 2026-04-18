# work maturity map v0

## purpose

이 문서는 `app/work/`를
한 덩어리 실험장으로 읽지 않도록
상위 maturity map을 제공하는 entrypoint다.

목표는 두 가지다.

1. 새 agent가 `app/work/`를 어디서부터 읽어야 하는지 빠르게 알게 하기
2. baseline-memory, staged-probe, utility-sidecar를 같은 위상으로 혼동하지 않게 하기

## 1. reading rule

`app/work/`는
core 승격 전 자산이 모인 곳이지만,
모든 하위 폴더가 같은 성격은 아니다.

이 폴더는 아래 세 층으로 읽는 것이 맞다.

## 2. baseline-memory

### primary folder

- `current_layer_baseline`

### why first

- 현재 엔진 철학과 운영 계약을 잠그는 work-contract memory다
- 일반 probe가 아니라 현재 baseline root에 가장 가까운 work lane이다

### reading order

1. `current_layer_baseline/engine_philosophy_declaration_v1.md`
2. `current_layer_baseline/current_layer_baseline_contract_v1.md`
3. `current_layer_baseline/reference_sheet_officeout_v1.md`

### interpretation

- 새 작업이 들어오면 이 층을 먼저 읽고
- 그 다음 probe/utility로 내려가는 것이 맞다

## 3. staged-probe corridor

### representative folders

- `mixed_reentry_probe_stage1`
- `mixed_reentry_observer_stage2`
- `mixed_corridor_boundary_probe_stage3`
- `mixed_corridor_format_disentangle_stage4`
- `technical_business_corridor_decompose_stage5`

### shared traits

- stage 번호가 명시돼 있다
- spec와 runner가 짝을 이룬다
- 하나의 corridor나 boundary를 단계적으로 좁혀 간다

### reading order

아래 순서로 읽는 것이 자연스럽다.

1. stage1
2. stage2
3. stage3
4. stage4
5. stage5

### interpretation

- 이 층은 단발 실험보다 lineage가 중요하다
- 한 stage만 떼어 읽기보다 이전 stage summary와 함께 봐야 한다

## 4. utility-sidecar work

### representative folders

- `observer_ingest_min`
- `operating_ui`
- `operating_ui/fixtures`
- `processor_compare`
- `archive_review/transition_support/workbench_stage1`
- `archive_review/transition_support/result_value_bundle_stage1`
- `archive_review/probe_support/future_segment_probe`
- `archive_review/probe_support/concept_segment_probe`
- `archive_review/external_case_support/external_case_flowline_sweep`
- `archive_review/external_case_support/external_case_folder_sweep`
- `archive_review/interview_support/middle_layer_experiments`
- `archive_review/transition_support/youtube_transcript_probe_0322`
- `archive_review/transition_support/youtube_transcript_probe_0322_b`

### shared traits

- bounded helper 또는 sidecar 실험이다
- 특정 operator surface, ingestion slice, compare loop, topic probe를 다룬다
- useful하지만 work 전체의 기준선은 아니다

### interpretation

- 필요할 때 선택적으로 들어가면 된다
- baseline root나 staged lineage처럼 전부 순차 독해할 필요는 없다

## 5. reading priority by situation

### when understanding current philosophy

먼저 읽을 곳:

- `current_layer_baseline`

### when tracing corridor evolution

먼저 읽을 곳:

- `mixed_reentry_probe_stage1` 부터 `technical_business_corridor_decompose_stage5`까지

### when checking helper surfaces

먼저 읽을 곳:

- `observer_ingest_min`
- `processor_compare`
- `operating_ui`

## 6. current caution

아래 혼동을 피해야 한다.

1. baseline-memory를 일반 실험 폴더처럼 취급하지 않는다
2. stage corridor를 단발 utility와 같은 위상으로 읽지 않는다
3. utility-sidecar 결과를 바로 core maturity처럼 읽지 않는다

## 7. one-line lock

`app/work/`는 단순 실험장 하나가 아니라
baseline-memory, staged-probe, utility-sidecar가 함께 있는 pre-promotion workspace다.
