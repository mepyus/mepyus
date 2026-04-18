# lecture_transcript_cohort_batch_test_v1.md

## 1. input cohort identification

### cohort_name

- `lecture_transcript_cohort_v1`

### selected assets

- `choi_ai_classroom_cnn`
  - `inputs/external_cases/choi_ai_classroom_cnn.txt`
- `choi_ai_classroom_neural_networks`
  - `inputs/external_cases/choi_ai_classroom_neural_networks.txt`
- `choi_ai_classroom_transformer1`
  - `inputs/external_cases/choi_ai_classroom_transformer1.txt`
- `choi_ai_classroom_vlm`
  - `inputs/external_cases/choi_ai_classroom_vlm.txt`

### why these four were treated as one cohort

- 모두 `choi_ai_classroom_*` 계열이다.
- 도입부부터 강의/수업형 발화가 명확하다.
- 시간축이 붙은 transcript이며, 정의 -> 설명 -> 예시 -> 세부 전개가 반복된다.
- 주제는 다르지만 교수형 설명 구조가 공통적으로 선명하다.

## 2. pipeline

모든 자산은 같은 파이프라인을 탔다.

- source intake
- probe
  - `window_size=6`
  - `stride=3`
  - `segment_assist=index_support`
- canonical state append
- latest/history refresh
- diff/attention/memory refresh
- process console read verification

## 3. per-asset summary

| asset_id | window_count | packet_texture | grounding | emergence | carryover | maturation | traceability | attention | memory |
|---|---:|---|---|---|---|---|---|---|---|
| `choi_ai_classroom_cnn` | 165 | `structured_open_low_emergence` | `partially_grounded` | `low_emergence` | `medium` | `weak` | `traceable` | `no_previous_state_anchor` | `insufficient_attention_history` |
| `choi_ai_classroom_neural_networks` | 167 | `structured_open_low_emergence` | `partially_grounded` | `low_emergence` | `medium` | `weak` | `traceable` | `no_previous_state_anchor` | `insufficient_attention_history` |
| `choi_ai_classroom_transformer1` | 169 | `structured_open_low_emergence` | `partially_grounded` | `low_emergence` | `medium` | `weak` | `traceable` | `no_previous_state_anchor` | `insufficient_attention_history` |
| `choi_ai_classroom_vlm` | 163 | `structured_open_low_emergence` | `partially_grounded` | `low_emergence` | `medium` | `weak` | `traceable` | `no_previous_state_anchor` | `insufficient_attention_history` |

## 4. cohort-wide pattern

### packet texture

- 공통 texture는 `structured_open_low_emergence`다.
- `window_count`가 모두 160개 이상으로, turboquant의 single mega-window와 명확히 다르다.
- 즉 이 cohort는 transcript이지만 packet granularity가 실제로 살아 있다.

### grounding / traceability

- 네 자산 모두 `partially_grounded`
- 네 자산 모두 `traceable`
- 강의형 설명 구조와 heading/segment 흐름이 source-return을 안정화시켰다.

### emergence

- 네 자산 모두 `low_emergence`
- 구조적 opening sign은 있으나, `question_opening_present`나 `minimal_emergence`로 올릴 만큼 강하지는 않다.

### carryover

- 네 자산 모두 `medium`
- 기술 용어와 강의 scaffold는 있지만, turboquant처럼 naming-heavy technical pressure가 packet 전체를 closure-heavy로 누르진 않았다.

### maturation

- 네 자산 모두 `weak`
- `fallback`보다 한 단계 위에서 머문다.
- trace와 packet structure는 살아 있지만 emergence는 아직 약하다.

### attention / memory

- 네 자산 모두 첫 canonical anchor라 `no_previous_state_anchor`
- memory는 모두 `insufficient_attention_history`
- 이것은 초기 cohort anchor 생성으로 읽는 것이 맞고, 문제 신호로 과장하면 안 된다.

## 5. canonical vs experimental separation

### canonical로 넣은 것

- packet texture
- grounding / emergence / carryover / maturation / traceability
- `breathing_contrast` 비교 기억

### experimental로 남긴 것

- cohort_name
- input character
- window_count / block_count
- packet formation note
- top object candidates
- top layer hints

### read

- 강의 주제명 자체나 교수 스타일 naming은 canonical로 승격하지 않았다.
- 강의 transcript의 구조적 장점만 state로 보존하고, naming-heavy 해석은 experimental에 남겼다.

## 6. turboquant comparison

### turboquant baseline

- `packet_texture`: `overcompressed_closure_heavy`
- `grounding_status`: `fallback_grounded`
- `emergence_status`: `low_emergence`
- `carryover_risk`: `high`
- `maturation_state`: `fallback`
- `traceability_status`: `traceable`

### relative position of this cohort

- packet texture는 turboquant보다 분명히 더 recoverable하다.
- grounding도 `fallback_grounded`보다 `partially_grounded` 쪽으로 안정적이다.
- carryover도 `high`보다 `medium`으로 낮다.
- maturation도 `fallback`보다 `weak`로 올라와 있다.

### read

- 이 cohort는 turboquant와 같은 compressed family가 아니다.
- lecture structure가 실제로 packet breathing room과 source-return을 만든다.

## 7. final judgment

- final_judgment: `lecture-structured recoverable cohort`

### why

- 네 자산 모두 multi-window packet을 만들었다.
- 네 자산 모두 `structured_open_low_emergence`로 수렴했다.
- grounding / carryover / maturation도 turboquant보다 한 단계 더 안정적이다.
- 같은 결의 입력군으로서 공통 반응이 충분히 반복됐다.

## 8. next recommendation

- 이 cohort는 compare-only memory가 아니라 **반복 실운용용 입력군**으로 채택할 가치가 있다.
- 특히 future batch에서는 이 cohort 내부에서
  - `low_emergence -> minimal_emergence`
  - `weak -> residue`
  이동이 생기는지를 추적하기 좋다.
- 다음 재실행 우선순위는 `transformer1`과 `vlm`이다.
  - 이유: 구조적 열림은 살아 있는데 기술 개념 밀도가 높아, 이후 packet/state 이동을 보기 좋다.
