# canonical anchor review split

## 1. current diagnosis
- `doc_006`은 이제 단순 possibility가 아니라 typed canonical review candidate 로 읽힌다
- translation / processing / observer 게이트는 통과했지만, canonical anchor 쪽은 `semantic`만 부분적으로 맞고 `structural / process / object` corroboration 이 부족하다
- 따라서 현재 가장 강한 canonical anchor 부족 유형은 `single_anchor_supported_but_not_compounded` 이다
- control cases:
  - `doc_004`, `doc_005`는 여전히 `translation_missing`

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `review_anchor_gap_class`
  - `review_anchor_support_class`
  - `anchor_alignment_evidence`
  - `anchor_alignment_missing_types`
  - `anchor_alignment_subcritical_types`
  - `anchor_alignment_compound_state`
- 적용: translation hit와 canonical anchor support를 분리 기록
- 적용: 양쪽 material에서 실제 겹치는 anchor type만 canonical review support로 간주
- 유지: canonical 기준
- 유지: possibility 기준
- 유지: translation scope
- 유지: control case state

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `translation_gate=true`
  - `processing_gate=true`
  - `observer_gate=true`
  - `canonical_anchor_gate=false`
  - `review_anchor_gap_class=anchor_alignment_present_but_subcritical`
  - `review_anchor_support_class=semantic_anchor_present_but_subcritical`
  - `anchor_alignment_compound_state=single_family_only`
  - `anchor_alignment_missing_types=[structural_anchor_alignment_missing, process_anchor_alignment_missing, object_anchor_alignment_missing]`
  - `anchor_alignment_evidence.semantic_overlap=[graph, rag]`
  - `anchor_alignment_evidence.structural_overlap=[]`
  - `anchor_alignment_evidence.process_overlap=[]`
  - `anchor_alignment_evidence.object_overlap=[]`
  - `next_review_blocker=single_anchor_supported_but_not_compounded`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_004`
    - `review_state=translation_missing`
  - `engine_phase1_observer_probe_20260321 -> doc_005`
    - `review_state=translation_missing`
- canonical 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `doc_006`은 canonical review candidate 이지만, 현재는 `semantic overlap`만 있는 상태다
- 즉 `graph / rag` 수준의 의미 anchor는 맞지만, 그것이 structural/process/object 쪽 corroboration 으로 compound 되지 않았다
- 그래서 translation + processing + observer가 강해도 canonical anchor review는 아직 통과하지 못한다
- `doc_005`는 translation 자체가 없으므로 review lane에 진입하지 못하는 control 로 계속 유효하다

## 5. next recommendation
- 다음 축은 translation이나 processing이 아니라 `anchor derivation / anchor support accumulation` 쪽이다
- 특히 `doc_006` 후보에서
  - structural anchor를 더 명시적으로 남길지
  - process/object anchor corroboration 을 어떻게 축적할지
  - semantic 단일 지지를 compound 지지로 올릴 review 기준을 어떻게 둘지
  를 보는 게 맞다
