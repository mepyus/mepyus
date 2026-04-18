# first_live_run_turboquant_youtube_v1.md

## 1. input identification

- asset_name: `turboquant_youtube`
- source_file: `inputs/external_cases/TurboQuant_youtube.txt`
- source_type: `dialogue_asset`
- live_run_label: `turboquant_youtube_live_run_v1`
- probe_output: `app/work/dialogue_loop_test/generated/turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z.json`

### input character

- transcript형 기술 설명 입력이다.
- 개념어와 구조 설명이 강하고, 사례/비유가 중간중간 섞인다.
- `KV cache`, `quantization`, `polar/QJL`, 대형 모델 적용 가능성 같은 naming-heavy technical framing이 강하다.

## 2. first-pass result

- `window_count=1`이라 first-pass가 사실상 single mega-window로 수렴했다.
- object candidate는 `에이전트 애플리케이션`, `모델 work` 정도만 얇게 잡혔다.
- layer hint는 `설명/해석 층` 우세, 그 다음 `구현/실행 층`, `검증/근거 층` 순이다.
- segmentation summary 자체는 별도 요약값이 비어 있었고, 실제 read는 `untitled` mega block에 가까웠다.
- residue는 conversational filler보다 discourse/technical connective 쪽이 더 두드러진다.

### read

- 1차는 trace를 남기긴 했지만, packet 형성 전부터 이미 압축 압력이 강했다.
- 따라서 naming-heavy 상위 해석은 canonical로 올리지 않고 experimental namespace에만 남겼다.

## 3. packet result

- packet_texture: `overcompressed_closure_heavy`
- packet formation note: `window_count=1 and untitled mega-block suggest compressed packet`

### why

- probe가 단일 window로 수렴했다.
- source는 길고 내용 밀도가 높은데, bridge packet은 아직 breathing room을 거의 만들지 못했다.
- question-intent score는 일부 있지만, window granularity가 너무 납작해서 structured-open 쪽으로 올리기엔 근거가 약했다.

## 4. canonical state result

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

### why

- `packet_texture`: single-window packet이라 과압축 판정이 보수적으로 맞다.
- `grounding_status`: source/probe ref는 분명하지만 direct grounding까지는 아니다.
- `emergence_status`: 완전 무출현보다는 약한 opening sign이 있으나, 과대승격은 금지해 `low_emergence`로 두었다.
- `carryover_risk`: technical naming pressure가 강하지만, prepared scaffold 확증까지는 아니어서 `high`로 두었다.
- `maturation_state`: 완전 blocked보다 `fallback`이 더 맞다. trace는 살아 있고 bridge도 성립했지만 packet quality가 약하다.
- `traceability_status`: source -> probe -> state -> process console 경로가 실제로 확인됐다.

## 5. canonical vs experimental separation

### canonical로 들어간 것

- packet texture
- grounding / emergence / carryover / maturation / traceability
- compressed-family / carryover-pattern 비교 기억
- fallback-grounding / scaffold-carryover blocker

### experimental로 남긴 것

- input character 요약
- first-pass object candidates
- first-pass layer hints
- packet formation note

### read

- transcript 안의 high-level technical naming은 이번 run에서 canonical truth가 아니라 operator aid로만 취급했다.

## 6. derived layer result

- history: 첫 record 1건 append
- latest: 생성 완료
- diff: `no_previous_state`
- interpretation badge: `no_previous_state`
- attention:
  - `priority_level`: `medium`
  - `attention_reason`: `no_previous_state_anchor`
  - `queue_status`: `new`
- attention memory:
  - `attention_pattern_summary`: `insufficient_attention_history`

### read

- 이번 run은 provenance-only가 아니다.
- 새 asset의 첫 canonical anchor라서 active attention으로 읽힌다.
- 다만 attention memory는 아직 이벤트가 1건뿐이라 과잉 요약 없이 중립 상태로 남는다.

## 7. process console read result

- latest read: 확인됨
- lineage history read: 확인됨
- adjacent diff read: `no_previous_state`
- attention read: active item 확인됨
- attention memory read: 확인됨
- asset rail inclusion: 확인됨

## 8. final judgment

- `TurboQuant_youtube.txt`는 freeze된 state-first engine에 실제로 무리 없이 들어왔다.
- 이번 입력은 naming-heavy technical transcript라 packet 압축 압력이 강했고, 그래서 canonical state는 보수적으로 잡았다.
- 핵심은 과잉 해석 없이 `source -> first-pass -> packet -> canonical state -> latest/history -> diff/attention/memory -> process console`이 실제로 한 번 끝까지 관통했다는 점이다.

### next read

- 다음 실운용에서 더 볼 것은 object promotion이 아니라, 이 자산이 이후 runtime evidence에서 `overcompressed_closure_heavy`를 유지하는지, 아니면 `overcompressed_breathing` 쪽으로 재판정될 만큼 packet granularity가 살아나는지다.
