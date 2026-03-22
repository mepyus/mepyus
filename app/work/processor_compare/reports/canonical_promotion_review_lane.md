# canonical promotion review lane

## 1. current diagnosis
- `doc_006`은 이제 mixed live-imported 경로에서 `possibility_candidate`를 넘어서, canonical 승격 심사 기준으로 보면 `anchor_alignment_pending` 상태다
- 즉 translation / processing / observer 게이트는 통과했지만 canonical anchor alignment 게이트가 아직 닫혀 있다
- `doc_004`, `doc_005`는 여전히 translation 자체가 없어서 review lane 밖 control 로 유지된다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가: `promotion_review.gate_vector`
- 추가: `promotion_review.promotion_readiness_class`
- 추가: `promotion_review.promotion_decision`
- 유지: canonical 판정 기준
- 유지: possibility 판정 기준
- 유지: local_ref-scoped translation
- 유지: bridge opening thresholds

## 3. verification
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - mode=`none`
  - review_state=`translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - mode=`none`
  - review_state=`translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - mode=`possibility_candidate`
  - review_kind=`translation_assisted_local_candidate`
  - translation_coverage_class=`broad_local_ref_hit`
  - processing_residual_class=`strong`
  - gate_vector.translation_gate=`true`
  - gate_vector.processing_gate=`true`
  - gate_vector.observer_gate=`true`
  - gate_vector.canonical_anchor_gate=`false`
  - promotion_readiness_class=`anchor_alignment_pending`
  - promotion_decision=`review_canonical_anchor_alignment`
  - next_review_blocker=`missing_canonical_anchor_alignment`

## 4. current reading
- `doc_006`은 이제 “번역도 맞고 processing도 충분하지만 canonical anchor alignment가 아직 부족한 승격 검토 후보”로 읽힌다
- 즉 다음 병목은 translation도 processing도 아니고, canonical anchor alignment review 그 자체다
- `doc_005`는 계속 translation-missing control 로 유지되므로, doc_006 승격 검토를 비교할 때 기준점으로 쓸 수 있다

## 5. next recommendation
- 다음 축은 bridge threshold 완화가 아니라 `doc_006` 후보에 대해 canonical anchor alignment review 기준을 별도로 정의하는 것이다
- 즉 엔진 질문은 “translation+processing이 strong일 때 어떤 anchor alignment가 더 있어야 canonical review를 통과시키는가” 쪽으로 넘어가야 한다
