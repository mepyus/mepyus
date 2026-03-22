# review output surface stabilization round1

## 1. current diagnosis
- policy 분리가 round4까지 진행되면서 핵심 판정 축은 대부분 외부 callable policy로 빠졌다
- 이제 다음 병목은 giant review dict 를 한 함수에서 전부 조립하는 output surface 쪽이었다
- 이번 round1의 목적은 output behavior 를 바꾸지 않고, surface 조립을 sub-assembler 들로 나누어 안정화하는 것이다

## 2. exact changes

### 변경 파일
- [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)

### 새 surface sub-assembler
- `_assemble_anchor_review_surface(...)`
- `_assemble_threshold_review_surface(...)`
- `_assemble_live_side_review_surface(...)`
- `_assemble_cross_path_review_payload(...)`
- `_assemble_canonicalization_review_surface(...)`
- `_assemble_direct_overlap_review_surface(...)`
- `_assemble_space_entry_review_surface(...)`

### 결과
- `assemble_promotion_review_surface(...)` 는 이제 giant inline dict 대신
  - base payload
  - anchor surface
  - threshold surface
  - live-side surface
  - cross-path surface
  - canonicalization surface
  - direct overlap surface
  - space entry surface
를 합성하는 형태가 되었다

즉 output surface 자체도 레이어별로 읽히기 시작했다.

## 3. verification

### compile
- `python3 -m py_compile` 통과

### canonical fixture
- `doc_004 -> doc_005`
  - `canonical`
  - `review_state = not_applicable`

### review candidate
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode = possibility_candidate`
  - `review_state = candidate`
  - `space_entry_state = structural_led_space_pre_entry`
  - `cross_path_canonicalization_proposal_state = token_supported_candidates_present`

### control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`

## 4. current reading
- `policy boundary exists`
- `fixture boundary exists`
- `output surface is now internally layered instead of one giant dict`

## 5. what not changed
- canonical 기준 안 바꿈
- review field 명 안 바꿈
- viewer 수정 안 함
- lifecycle tag 안 붙임
- fixture runner 안 만듦

## 6. next recommendation
1. 다음은 `lifecycle tag` 를 붙이는 것이 자연스럽다
2. 그 다음 `fixture runner`
3. output surface 는 지금 단계에서 충분히 안정적이다

## 7. final sentence
- 이번 round1로 output surface 도 policy와 비슷하게 레이어 단위로 읽히기 시작했다
- 즉 지금 엔진은
  - policy boundary
  - fixture boundary
  - surface boundary
를 모두 갖추기 시작했다
