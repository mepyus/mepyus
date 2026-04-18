# Dialogue Loop Test Generated Index

이 폴더는 단일 산출물 묶음이 아니라 여러 validation family가 겹친 belt다.

주요 family:

- `youtube_03_22_dialogue_loop_test_*`
  - high-density dialogue loop baseline
- `context_unit_candidates_*`
  - context unit 후보 추출면
- `dialogue_asset_purpose_synthesis_*`
  - asset purpose synthesis 면
- `question_inducing_block_candidates_*`
  - question-inducing block 후보면
- `multi_pass_interpretation_training_*`
  - multi-pass reread/training 면
- `paragraph_role_interpretation_*`
  - paragraph role 해석면
- `*_engine_purpose_validation_*`
  - asset별 purpose validation 면
- `*_multi_pass_validation_*`
  - asset별 multi-pass validation 면
- `*_paragraph_role_validation_*`
  - asset별 paragraph role validation 면

읽기 원칙:

- 이 generated belt는 단순 부산물이 아니라 여러 report가 직접 참조하는 현재 validation surface다.
- 그래서 파일별 삭제보다 family 단위 reread가 먼저다.
