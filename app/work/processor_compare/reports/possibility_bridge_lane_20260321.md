# Possibility Bridge Lane 2026-03-21

## 1. current diagnosis
- current runtime-common baseline:
  - live / imported / legacy material 모두 최소 `observer_or_ambiguity_trace` baseline을 가짐
  - canonical bridge enrichment와 local space exposure baseline도 공통으로 읽힘
- current mixed-path bottleneck:
  - `live-imported`, `live-legacy` 경로에서 canonical opening은 여전히 드묾
  - baseline 부재가 아니라 opening semantics 병목으로 읽힘
- canonical lane preservation:
  - 고정 canonical 사례는 그대로 canonical 유지
  - 이번 턴은 canonical rule을 완화하지 않았음

## 2. exact changes
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - canonical bridge opening rule 유지
  - possibility lane 추가:
    - `bridge_mode`
    - `cross_path_type`
    - `possibility_basis`
    - `promotion_blockers`
    - `blocked_reason`
  - `trace.note == "weak"` 이면서 mixed path인 경우만 possibility 평가
  - canonical pair가 이미 있으면 possibility 생성 안 함
- [runtime_space_anchor_sync.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/runtime_space_anchor_sync.py)
  - local space에 아래 baseline 추가/유지:
    - `canonical_bridge_exposure_count`
    - `possibility_bridge_exposure_count`
    - `possibility_bridge_refs`
    - `state_transition_summary`
- [backfill_possibility_bridges.py](/Users/sungsookim/universe/vectorfl_replica/scripts/backfill_possibility_bridges.py)
  - selective backfill 경로 추가
  - mixed path possibility evaluation만 수행
  - full rebuild 없음

## 3. verification
### fixed canonical cases
- `doc_004 <-> doc_005`
  - canonical 유지
  - local spaces:
    - `lsp_00018441d497`: canonical `6`, possibility `0`
    - `lsp_2dde7aef787a`: canonical `9`, possibility `0`
- `doc_005 <-> doc_006`
  - canonical 유지
  - local space `lsp_4eadb2fe7a96`: canonical `10`, possibility `0`
- `test_live_space_sync_20260321 <-> test_canonical_ingest_20260321`
  - canonical 유지
  - local space `lsp_3630ca5d8a22`: canonical `3`, possibility `0`

### mixed-path results
- `engine_phase1_imported_doc_probe_20260321 <-> test_live_space_sync_20260321`
  - possibility candidate 생성
  - possibility bridge:
    - `pbg_lsp_327fa516bc6c__lsp_3eaef4e0c6dc`
    - `bridge_mode = possibility_candidate`
    - `cross_path_type = live-legacy`
  - local spaces:
    - `lsp_327fa516bc6c`: canonical `1`, possibility `1`
    - `lsp_3eaef4e0c6dc`: canonical `2`, possibility `2`
- `engine_phase1_imported_doc_probe2_20260321 <-> test_live_space_sync_20260321`
  - possibility candidate 생성
  - possibility bridge:
    - `pbg_lsp_3eaef4e0c6dc__lsp_fca5c1cfe512`
    - `bridge_mode = possibility_candidate`
    - `cross_path_type = live-legacy`
  - local space `lsp_fca5c1cfe512`: canonical `1`, possibility `1`

### possibility basis / blockers
- common possibility basis keys:
  - `partial_anchor_alignment`
  - `weak_processing_overlap`
  - `observer_affinity`
  - `structural_echo`
  - `partial_handle_overlap`
  - `shared_scene_or_flow_hint`
- common promotion blockers:
  - `missing_canonical_anchor_alignment`
  - `processing_overlap_below_canonical`
  - `cross_path_translation_gap`

### distribution
- canonical:
  - fixed cases 유지
- possibility_candidate:
  - `2`
- none:
  - mixed imported-doc opening에서는 여전히 다수

## 4. current reading
- current reading:
  - `bridge-common runtime with possibility lane introduced`
  - `mixed-path possibility semantics active, canonical lane preserved`
- not yet reached:
  - stable `live-imported` possibility opening
  - possibility-aware local-space state transition beyond inferred summary

## 5. next recommendation
- next patch priority:
  - `live-imported` opening semantics 재검토
  - imported doc 쪽 `cross_path_translation_gap`을 더 구체적으로 분해
- likely next comparison:
  - `live-imported none` vs `live-legacy possibility_candidate`
  - `partial_anchor_alignment`가 어떤 경우 possibility까지 못 올라가는지 비교
- not yet ready:
  - region/viewer로 다시 올라가는 것
  - canonical threshold 완화

## final line
이번 턴의 결과는 `mixed path를 억지 canonical로 만들지 않고`, 약한 흔적을 `possibility_candidate` lane으로 따로 보존하는 데 성공한 것이다. 다만 현재 lane은 `live-legacy`에서만 실제로 열렸고, `live-imported` opening semantics는 아직 다음 엔진 과제로 남아 있다.
