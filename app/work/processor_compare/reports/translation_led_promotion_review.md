# translation-led promotion review

## 1. current diagnosis
- 요약: mixed live-imported 경로에서 `doc_006`만 translation-assisted local ref convergence가 실제로 생기고, processing은 여전히 weak라서 canonical 승격이 아니라 promotion review lane에 남겨야 한다
- control cases: `doc_004`, `doc_005`는 여전히 `translation_missing` 상태라 promotion review 대상이 아님
- canonical lane: `doc_004 <-> doc_005`, `doc_005 <-> doc_006`, `test_live_space_sync_20260321 <-> test_canonical_ingest_20260321` 모두 그대로 유지

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가: mixed evaluator payload에 `promotion_review` 필드 추가
- 추가: persisted possibility payload/evaluation에도 `promotion_review` 포함
- 유지: canonical 판정 기준
- 유지: possibility 판정 기준
- 유지: translation scope = `local_ref`
- 유지: viewer / region / translation broadcast

## 3. verification
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - mode=`none`
  - review.available=`false`
  - review_state=`translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - mode=`none`
  - review.available=`false`
  - review_state=`translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - mode=`possibility_candidate`
  - review.available=`true`
  - review_kind=`translation_led_processing_weak`
  - recommendation=`keep_in_possibility_review_lane`
  - matched_local_ref_count=`26`
  - matched_handles=`rag`
  - best_processing_score=`0.483`
  - processing_convergence_level=`weak`
- live-legacy possibility:
  - review_state=`not_applicable`
- canonical pairs:
  - review_state=`not_applicable`

## 4. current reading
- `doc_006`은 이제 단순 possibility가 아니라 `translation-led / processing-weak` review candidate 로 읽힌다
- 즉 가능성은 분명히 있지만, processing residual이 아직 승격을 지지하지 않는다
- `doc_004`, `doc_005`는 같은 live probe 대비 local processing adjacency는 있어도 translation convergence가 없어 review candidate 단계에도 못 오른다

## 5. next recommendation
- 다음 축은 promotion review lane 확대가 아니라 `translation+processing interplay`를 더 정밀하게 읽는 것이다
- 특히 `doc_006`의 review candidate를 control case `doc_005`와 비교하면서
  - processing residual이 얼마나 더 필요했는지
  - translation hit local_ref가 어떤 processing profile 위에서만 의미가 있었는지
  를 엔진에서 더 분해하는 쪽이 맞다
