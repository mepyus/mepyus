# Dialogue Loop Generated Condensation Candidates v1

## 목적

이 문서는 [app/work/dialogue_loop_test/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/dialogue_loop_test/generated)
안의 반복 family를

- `keep all`
- `keep exemplar + latest`
- `condensation candidate`

로 나눠 다음 감량 배치의 기준을 만든다.

전제:

- 이 폴더는 여전히 `active surface` 다.
- 그래서 이번 단계에서는 파일 삭제를 바로 하지 않고 family 단위 판정만 잠근다.

## 1. keep all

아래는 현재 report가 직접 기대고 있고, family 내부 중복도 낮아서 아직 전부 유지한다.

- `context_unit_candidates_*`
- `dialogue_asset_purpose_synthesis_*`
- `question_inducing_block_candidates_*`
- `multi_pass_interpretation_training_*`
- `paragraph_role_interpretation_*`
- `*_engine_purpose_validation_*`
- `*_multi_pass_validation_*`
- `*_paragraph_role_validation_*`

이유:

- validation chain의 각 단계 결과라 서로 역할이 다르다.
- 지금 줄이면 report link와 reread 맥락이 먼저 깨진다.

## 2. keep exemplar + latest

아래는 반복 window/step 출력이 많아 family별 대표본과 최신본만 남기는 쪽이 가능하다.

### A. youtube baseline family

- family: `youtube_03_22_dialogue_loop_test_*`
- 현재 반복:
  - `w3_s1`, `w4_s2`, `w6_s3`, `w8_s4`
  - 세 timestamp 세트가 겹쳐 총 12개
- 권장 보존:
  - exemplar:
    - `youtube_03_22_dialogue_loop_test_w6_s3_20260328T062625Z.json`
  - latest set:
    - `youtube_03_22_dialogue_loop_test_w3_s1_20260328T064937Z.json`
    - `youtube_03_22_dialogue_loop_test_w4_s2_20260328T064937Z.json`
    - `youtube_03_22_dialogue_loop_test_w6_s3_20260328T064938Z.json`
    - `youtube_03_22_dialogue_loop_test_w8_s4_20260328T064938Z.json`
- condensation candidate:
  - 초기 `062008/062009` 세트
  - 중간 `062624/062625` 세트 중 exemplar 제외분

### B. claude code index dialogue loop family

- family: `claude_code_index_dialogue_loop_test_*`
- 현재 반복:
  - `w3_s1`, `w4_s2`, `w6_s3`, `w8_s4`
- 권장 보존:
  - latest set 전체 유지
- condensation candidate:
  - 없음

판단:

- 이 family는 한 번의 세트만 있으므로 아직 감량보다 유지가 우선이다.

### C. segmentation probe families

- `claude_code_index_segmentation_probe_v1_*`
- `enterprise_segmentation_probe_v1_*`
- `graphrag_neosh_segmentation_probe_v1_*`

권장 보존:

- exemplar 1개:
  - 보통 `w3_s1`
- latest / stronger pass 1개:
  - 보통 `w6_s3`

판단:

- 동일 family 안에서 window 규모 비교 목적이 명확하다.
- 장기적으로는 각 family당 `초기 비교본 + 최신 비교본`만 남겨도 line reread는 가능하다.

### D. baseline probe families

- `openai_02_11_baseline_probe_v1_*`
- `enterprise_baseline_probe_v1_*`
- `graphrag_neosh_baseline_probe_v1_*`
- `knowledge_editing_youtube_probe_v1_*`
- `gary_tan_brain_probe_v1_*`

권장 보존:

- exemplar 1개:
  - earliest or `w3_s1`
- latest 1개:
  - `w6_s3` 또는 family latest

판단:

- 목적은 breadth가 아니라 compare trace다.
- family당 2개면 reading 기억은 대체로 유지된다.

## 3. singleton keep

아래는 지금 파일 수가 적거나 역할이 분명해서 단건 유지가 맞다.

- `claude_code_index_probe_preview_*`
- `claude_code_index_segcheck_base_*`
- `claude_code_index_segcheck_support_*`
- `turboquant_youtube_live_run_v1_*`
- `turboquant_youtube_reseg_b_v1_*`
- `turboquant_youtube_reseg_c_v1_*`
- `choi_ai_classroom_*_cohort_live_run_v1_*`

## 4. immediate next batch

다음 실제 감량 배치는 아래 순서가 안전하다.

1. `youtube_03_22_dialogue_loop_test_*` 12개 중 exemplar/latest 표를 먼저 확정
2. `*_baseline_probe_*` 와 `*_segmentation_probe_*` 를 family당 2개 보존 규칙으로 줄일지 검토
3. report link가 직접 물고 있는 파일은 latest 쪽으로 우선 재지정

## 5. do-not-condense-yet

아래는 지금 줄이면 안 된다.

- `context_unit_candidates_*`
- `dialogue_asset_purpose_synthesis_*`
- `question_inducing_block_candidates_*`
- `multi_pass_interpretation_training_*`
- `paragraph_role_interpretation_*`

이유:

- 이 다섯 축이 현재 dialogue reread line의 실제 읽기 뼈대다.
