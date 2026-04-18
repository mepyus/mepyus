# turboquant_youtube_resegmentation_rewindow_compare_v1.md

## 1. baseline recap

- asset_name: `turboquant_youtube`
- source_file: `inputs/external_cases/TurboQuant_youtube.txt`
- baseline probe: `turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z.json`

### baseline canonical state

- `packet_texture`: `overcompressed_closure_heavy`
- `grounding_status`: `fallback_grounded`
- `emergence_status`: `low_emergence`
- `carryover_risk`: `high`
- `maturation_state`: `fallback`
- `traceability_status`: `traceable`

### why compare was needed

- baseline first-pass가 사실상 single mega-window로 수렴했다.
- 따라서 window/stride/segment assist를 더 촘촘하게 주면 packet이 `overcompressed_breathing` 쪽으로라도 움직일지 확인할 필요가 있었다.

## 2. run parameter table

| run | label | segment_assist | window_size | stride | note |
|---|---|---:|---:|---:|---|
| A | `baseline` | `none` | 6 | 3 | first live run reference |
| B | `finer segmentation` | `index_support` | 3 | 1 | 분절 극대화 시도 |
| C | `finer segmentation + overlap` | `index_support` | 4 | 2 | overlap 보강 시도 |

## 3. result comparison table

| run | block_count | window_count | packet_texture | grounding | emergence | carryover | maturation | traceability |
|---|---:|---:|---|---|---|---|---|---|
| A | 1 | 1 | `overcompressed_closure_heavy` | `fallback_grounded` | `low_emergence` | `high` | `fallback` | `traceable` |
| B | 1 | 1 | `overcompressed_closure_heavy` | `fallback_grounded` | `low_emergence` | `high` | `fallback` | `traceable` |
| C | 1 | 1 | `overcompressed_closure_heavy` | `fallback_grounded` | `low_emergence` | `high` | `fallback` | `traceable` |

## 4. probe comparison read

### shared probe character across all runs

- `block_count=1`
- `window_count=1`
- heading은 계속 `untitled`
- object candidate는 계속 `에이전트 애플리케이션`, `모델 work`
- relation hint, question-intent score, residue total도 사실상 동일
- `opening_summary`도 baseline과 compare runs가 동일

### interpretation

- 이번 범위의 segmentation/windowing 변경은 실제 packet granularity를 살리지 못했다.
- `index_support`를 켜고 window를 줄여도 source 자체가 여전히 single mega-block로 들어왔다.
- 따라서 packet은 `closure-heavy`에서 `breathing`으로 이동하지 않았다.

## 5. canonical compare candidate result

이번 compare run들은 baseline latest를 overwrite하지 않고 compare-only 판단으로만 기록한다.

### run B candidate

- `packet_texture`: `overcompressed_closure_heavy`
- `grounding_status`: `fallback_grounded`
- `emergence_status`: `low_emergence`
- `carryover_risk`: `high`
- `maturation_state`: `fallback`
- `traceability_status`: `traceable`
- `comparison_memory_reason`:
  - `same_compressed_family`
  - `similar_carryover_pattern`
- `gate_blocker_summary`:
  - `fallback_grounding_dominance`
  - `scaffold_carryover_risk`

### run C candidate

- `packet_texture`: `overcompressed_closure_heavy`
- `grounding_status`: `fallback_grounded`
- `emergence_status`: `low_emergence`
- `carryover_risk`: `high`
- `maturation_state`: `fallback`
- `traceability_status`: `traceable`
- `comparison_memory_reason`:
  - `same_compressed_family`
  - `similar_carryover_pattern`
- `gate_blocker_summary`:
  - `fallback_grounding_dominance`
  - `scaffold_carryover_risk`

## 6. interpretation by axis

### packet texture

- 이동 없음
- `overcompressed_closure_heavy` 유지

### grounding / traceability

- source-return 경로 자체는 여전히 있다.
- 하지만 granularity가 늘었다고 볼 만큼 ref coverage가 살아나지 않아 `fallback_grounded`에서 움직이지 않았다.
- `traceability`는 계속 `traceable` 유지다.

### emergence

- `low_emergence` 유지
- finer segmentation만으로 `minimal_emergence`까지의 이동 증거는 없다.

### carryover risk

- `high` 유지
- transcript의 technical naming pressure가 강하고, granularity 확보 자체가 실패했기 때문에 risk 완화 근거가 없었다.

### maturation

- `fallback` 유지
- trace는 있으나 packet breathing recovery가 없어 state 이동이 생기지 않았다.

## 7. final judgment

- final_judgment: `compression-dominant intrinsic`

### why

- baseline, run B, run C 모두 `block_count=1`, `window_count=1`이었다.
- packet texture, grounding, emergence, carryover, maturation, traceability가 전부 동일했다.
- 즉 이번 범위에서 문제는 단순 window size/stride tuning보다 source의 single mega-block intake character가 더 지배적이었다.

## 8. next recommendation

- baseline latest는 그대로 유지한다.
- 이번 compare runs는 overwrite가 아니라 compare memory로만 둔다.
- 다음 evidence는 단순 rewindow보다 source intake/segmentation stage에서 mega-block 자체를 더 직접적으로 깨는 방향이 아니면 상태 이동이 작을 가능성이 높다.
