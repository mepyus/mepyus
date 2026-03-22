# translation processing interplay probe

## 1. current diagnosis
- 요약: translation+processing interplay shows that doc_006 possibility is translation-led with weak processing convergence, while doc_005/doc_004 remain translation-missing and only weakly processing-adjacent
- strongest reading: processing refinement improved residual variation, but translation-assisted handle convergence remains the actual gate for live-imported lift

## 2. verification
- `doc_004`: mode=`none`, none_reason=`anchor_vocabulary_translation_gap`, translation_available=False, matched_handles=[], processing_best_score=0.6, convergence_level=`weak`
- `doc_005`: mode=`none`, none_reason=`anchor_vocabulary_translation_gap`, translation_available=False, matched_handles=[], processing_best_score=0.6, convergence_level=`weak`
- `doc_006`: mode=`possibility_candidate`, none_reason=``, translation_available=True, matched_handles=['rag'], processing_best_score=0.483, convergence_level=`weak`

## 3. current reading
- doc_004: weak processing adjacency exists, but no translation-assisted handle convergence, so none remains stable
- doc_005: processing is less flat than before, but still no translated-handle match to the live probe, so none remains stable
- doc_006: possibility is preserved by local_ref rag translation, but the best processing interplay score is only 0.483, so promotion is not processing-backed yet

## 4. next recommendation
- primary: do not widen translation; use doc_006 as the first promotion-review case with explicit translation-led / processing-weak labeling
- secondary: keep doc_005 as control case for translation-missing none
