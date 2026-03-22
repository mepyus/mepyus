# promotion review control compare

## 1. current diagnosis
- `doc_006`은 live-imported mixed path에서 translation convergence는 충분하지만 processing residual이 약해서 review lane에 머무는 후보다
- `doc_005`는 processing refinement 이후에도 translation convergence 자체가 없어서 review lane에 못 오른다
- `doc_004`도 weak processing adjacency는 있지만 translation convergence가 없어서 control로 유지된다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가: `promotion_review.translation_coverage_class`
- 추가: `promotion_review.processing_residual_class`
- 추가: `promotion_review.next_review_blocker`
- 유지: canonical lane
- 유지: possibility lane
- 유지: local_ref-scoped translation
- 유지: bridge opening threshold

## 3. verification
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - mode=`none`
  - promotion_review.review_state=`translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - mode=`none`
  - promotion_review.review_state=`translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - mode=`possibility_candidate`
  - promotion_review.review_kind=`translation_led_processing_weak`
  - translation_coverage_class=`broad_local_ref_hit`
  - processing_residual_class=`weak`
  - next_review_blocker=`processing_residual_too_weak`
  - best_local_ref=`processor_compare/doc_006.txt::dst_src_2fd2c39f0fd7_003`
  - matched_handles=`rag`

## 4. current reading
- `doc_006`은 이제 왜 promotion review 대상인지가 더 선명하다
  - local_ref translation hit는 넓게 생김
  - 하지만 processing residual은 아직 weak라서 canonical 승격 근거는 아님
- `doc_005`는 processing residual이 조금 살아나도 translation convergence가 없으면 review lane에도 못 오른다는 control로 기능한다
- 따라서 다음 병목은 translation 확대가 아니라 `processing residual을 review candidate local_ref에서 얼마나 더 국소적으로 끌어올릴 수 있느냐`다

## 5. next recommendation
- 다음 축은 `doc_006` review candidate local_ref 주변의 processing residual 보강이다
- `doc_005`는 계속 translation-missing control로 유지하면서 비교군으로 쓰는 게 맞다
- translation 범위를 넓히는 것보다, review candidate의 `best_local_ref` 주변 processing projection을 더 세밀하게 읽는 쪽이 우선이다
