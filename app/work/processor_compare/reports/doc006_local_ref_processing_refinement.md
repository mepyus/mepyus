# doc006 local_ref processing refinement

## 1. current diagnosis
- 요약: `doc_006`의 translation-hit local_ref 주변 processing profile을 `review/compare` 쪽으로 국소 보정하자, possibility candidate가 이제 `translation-led / processing-weak`가 아니라 `translation-assisted local candidate + strong processing residual`로 읽히게 됐다
- control: `doc_005`는 processing 보정 이후에도 translation convergence가 없어 여전히 `translation_missing`
- canonical lane: 변화 없음

## 2. exact changes
- 변경 파일: `app/core/runtime/labeler.py`
- 적용: processor_compare doc 전용 `relational review` cue 추가
  - `graph rag`
  - `vector rag`
  - `기존 rag`
  - `반면`
  - `복잡 질의`
  - `multi-hop`
  - `관계`
  - `질의`
  - `추론`
- 적용: `Object Type / Property / Graph DB / Relationship / Node / 온톨로지`류 entity cue를 spec/run derivation에 반영
- 실행: `scripts/refine_imported_processing_profiles.py runtime processor_compare/doc_005.txt processor_compare/doc_006.txt`
- 유지: translation scope
- 유지: canonical/possibility evaluator thresholds
- 유지: bridge opening rules

## 3. verification
- selective re-label:
  - updated_material_count=`48`
  - synced_local_spaces=`lsp_2dde7aef787a`, `lsp_4eadb2fe7a96`
- `doc_006` mixed pair
  - before: `best_processing_score=0.483`, `processing_convergence_level=weak`, `review_kind=translation_led_processing_weak`
  - after: `best_processing_score=0.936`, `processing_convergence_level=strong`, `review_kind=translation_assisted_local_candidate`
  - after best_local_ref=`processor_compare/doc_006.txt::dst_src_2fd2c39f0fd7_016`
  - after next_review_blocker=`missing_canonical_anchor_alignment`
- `doc_005` mixed pair
  - mode=`none`
  - promotion_review.review_state=`translation_missing`
- canonical 사례 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `doc_006`은 이제 review candidate로서 충분히 읽힌다
  - local_ref translation hit가 넓게 있고
  - 그 local_ref 주변 processing residual도 strong 으로 회복됐다
  - 남은 blocker는 더 이상 pure processing flatness가 아니라 canonical anchor alignment 쪽이다
- `doc_005`는 translation convergence가 없어서 여전히 control case로 남는다

## 5. next recommendation
- 다음 축은 processing refinement를 더 넓히는 게 아니라 `doc_006` review candidate의 canonical promotion review 기준을 분리해서 보는 것이다
- 즉 이제 엔진 질문은
  - strong local translation + strong processing residual 이 있어도
  - 왜 canonical anchor alignment가 부족한지
  - 어떤 review threshold를 두고 possibility에서 승격 검토할지
  쪽으로 넘어가는 게 맞다
