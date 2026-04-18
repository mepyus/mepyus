# Dialogue Loop Test Family

이 폴더는 지금 시점에서 `archive_review` 로 내리지 않는 살아있는 emergent line belt다.

핵심 의미:

- dialogue asset을 여러 단계로 reread 하면서
  - `context_unit_candidates`
  - `dialogue_asset_purpose_synthesis`
  - `question_inducing_block_candidates`
  - `multi_pass_interpretation_training`
  - `paragraph_role_interpretation`
  로 이어지는 반복 검증 선을 남긴다.

왜 남기나:

- 많은 report가 이 generated 결과를 직접 참조한다.
- `engine_purpose_validation`, `multi_pass_validation`, `question_inducing_block`, `process_trace_validation` 계열이 여기에 직접 기대고 있다.
- 그래서 지금은 support archive가 아니라 살아있는 validation belt로 읽는 편이 맞다.

읽기 순서:

1. `generated/context_unit_candidates*`
2. `generated/dialogue_asset_purpose_synthesis*`
3. `generated/question_inducing_block_candidates*`
4. `generated/multi_pass_interpretation_training*`
5. `generated/paragraph_role_interpretation*`

대표 cohort:

- `youtube_03_22_dialogue_loop_test_*`
- `claude_code_index_*`
- `openai_02_11_*`
- `enterprise_*`
- `graphrag_neosh_*`
- `knowledge_editing_youtube_*`
- `gary_tan_brain_*`
