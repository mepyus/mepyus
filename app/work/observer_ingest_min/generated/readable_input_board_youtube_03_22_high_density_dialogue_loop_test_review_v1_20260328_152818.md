# readable input board / youtube_03_22_high_density_dialogue_loop_test_review_v1_20260328_152818

## 1. 입력 정보
- input_id: `youtube_03_22_high_density_dialogue_loop_test_review_v1`
- label: `youtube_03_22_high_density_dialogue_loop_test_review_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/youtube_03_22_high_density_dialogue_loop_test_review_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `461`
- unit_count: `52`

## 3. unit 목록 요약
- unit_001 — heading_block / preamble ~ preamble — "[[A]] [[OBJ:youtube_03_22_high_density_dialogue_loop_test_review_v1]] [[SEM:review_report_for_repeated_dialogue_asset_te..."
- unit_002 — heading_block / 리뷰 리포트 — youtube_03_22 고밀도 대화 자산 반복 테스트 결과 정리 ~ 리뷰 리포트 — youtube_03_22 고밀도 대화 자산 반복 테스트 결과 정리 — "# 리뷰 리포트 — youtube_03_22 고밀도 대화 자산 반복 테스트 결과 정리..."
- unit_003 — heading_block / 1. 기본 정보 ~ 1. 기본 정보 — "## 1. 기본 정보 - test_name: - `youtube_03_22_high_density_dialogue_loop_test_review_v1` - created_at: - `2026-03-28` - inpu..."
- unit_004 — heading_block / 2. 이번 테스트의 목적 ~ 2. 이번 테스트의 목적 — "## 2. 이번 테스트의 목적 이번 테스트는 아래를 보기 위해 수행했다. - 이전 loop run에서 보인 객체 후보가 다시 살아나는지 - 다층 판독이 반복 실행에서도 유지되는지 - 관계 운동 힌트가 재현되는지 - ..."
- unit_005 — heading_block / 3. loop 조건 요약 ~ 3. loop 조건 요약 — "## 3. loop 조건 요약..."
- unit_006 — heading_block / 3-1. 분절 조건 ~ 3-1. 분절 조건 — "### 3-1. 분절 조건 - segment_mode: - heading + paragraph block split - window_mode: - sliding multi-window test - overlap: -..."
- unit_007 — heading_block / 3-2. 판독 출력 조건 ~ 3-2. 판독 출력 조건 — "### 3-2. 판독 출력 조건 - layer_reading: - YES - relation_hint: - YES - question_intent_fit: - YES - residue_review: - YES - u..."
- unit_008 — heading_block / 3-3. 비교 조건 ~ 3-3. 비교 조건 — "### 3-3. 비교 조건 - baseline_compare_used: - YES - prior_result_compare_used: - YES - cross-run_compare_used: - YES ---..."
- unit_009 — heading_block / 4. top-level 판정 ~ 4. top-level 판정 — "## 4. top-level 판정 - status: - `PASS_WITH_NOTE`..."
- unit_010 — heading_block / 한 줄 판정 ~ 한 줄 판정 — "### 한 줄 판정 - `같은 loop를 다시 돌려도 객체 후보, 층위, 관계 힌트, 질문 의도 적합 window가 거의 같은 모양으로 재현되어 반복 학습 자산으로는 충분히 안정적이지만, residue는 여전히 su..."
- unit_011 — heading_block / 왜 그렇게 판정했는가 ~ 왜 그렇게 판정했는가 — "### 왜 그렇게 판정했는가 - 동일한 4개 window/stride 조건에서 상위 객체 후보 순서와 관계 힌트 순서가 사실상 그대로 유지됐다. - `RLVR/CUA`, `bundle-unbundle/OpenClaw..."
- unit_012 — heading_block / 5. 객체 후보 판독 ~ 5. 객체 후보 판독 — "## 5. 객체 후보 판독..."
- unit_013 — heading_block / 5-1. 반복적으로 살아난 객체 후보 ~ 5-1. 반복적으로 살아난 객체 후보 — "## 5-1. 반복적으로 살아난 객체 후보 - object_candidate_1: - `에이전트 애플리케이션` - strength: - strongest repeated - why: - 모든 run에서 최상위 객체로..."
- unit_014 — heading_block / 5-2. 객체 성장성 해석 ~ 5-2. 객체 성장성 해석 — "## 5-2. 객체 성장성 해석 - 이미 두꺼운 층: - `에이전트 애플리케이션`, `모델 work`, `전략/방향성` - 새로 붙은 층: - `AI의 미래`는 `모델 work`와의 연결층에서, `일의 미래`는 `에..."
- unit_015 — heading_block / 6. 층위 판독 결과 ~ 6. 층위 판독 결과 — "## 6. 층위 판독 결과..."
- unit_016 — heading_block / 6-1. 반복적으로 보인 층위 ~ 6-1. 반복적으로 보인 층위 — "### 6-1. 반복적으로 보인 층위 - 설명/해석 층: - strongest repeated layer - 구현/실행 층: - present - 구조/연결 층: - present - 전략/방향 층: - strong..."
- unit_017 — heading_block / 6-2. 층위 강도 해석 ~ 6-2. 층위 강도 해석 — "### 6-2. 층위 강도 해석 - 가장 두꺼운 층: - `설명/해석 층` - 예상보다 강했던 층: - `전략/방향 층` - `질문 유도 층` - 예상보다 약했던 층: - `검증/근거 층` - 아직 거의 안 보이는 ..."
- unit_018 — heading_block / 6-3. user-facing opening 관점 해석 ~ 6-3. user-facing opening 관점 해석 — "### 6-3. user-facing opening 관점 해석 - 사용자가 바로 읽기 쉬운 층: - `전략/방향 층` - `구현/실행 층` - gloss가 붙어도 아직 흐린 층: - `검증/근거 층` 일부 - `구조..."
- unit_019 — heading_block / 7. 관계 힌트 판독 ~ 7. 관계 힌트 판독 — "## 7. 관계 힌트 판독..."
- unit_020 — heading_block / 7-1. 반복적으로 보인 관계 운동 ~ 7-1. 반복적으로 보인 관계 운동 — "### 7-1. 반복적으로 보인 관계 운동 - reinforcement_hint: - strongest repeated - contrast_hint: - stable repeated - transition_hint:..."
- unit_021 — heading_block / 7-2. 관계 힌트 예시 ~ 7-2. 관계 힌트 예시 — "### 7-2. 관계 힌트 예시 - sample_1: - source_segment: - `32_39` cluster - relation_hint: - `reinforcement_hint`, `contrast_hin..."
- unit_022 — heading_block / 7-3. 현재 한계 ~ 7-3. 현재 한계 — "### 7-3. 현재 한계 - 단순 공출현처럼만 보이는 부분: - broad strategic language가 많은 구간 - 아직 관계 운동으로 읽기 어려운 부분: - generic capability overha..."
- unit_023 — heading_block / 8. 질문 의도 적합 문단 ~ 8. 질문 의도 적합 문단 — "## 8. 질문 의도 적합 문단..."
- unit_024 — heading_block / 8-1. 가장 강하게 닿는 문단 후보 ~ 8-1. 가장 강하게 닿는 문단 후보 — "### 8-1. 가장 강하게 닿는 문단 후보 - candidate_1: - segment_ref: - `32_34`, `32_35`, `32_39` - why_it_matches_user_intent: - `AI의 ..."
- unit_025 — heading_block / 8-2. 이 문단들이 중요한 이유 ~ 8-2. 이 문단들이 중요한 이유 — "### 8-2. 이 문단들이 중요한 이유 - 객체를 두껍게 한다 / 질문을 연다 / 관계를 만든다 / 층위를 번역한다 중 무엇인가: - `이 문단들은 네 가지를 거의 동시에 수행한다. 객체를 두껍게 하고, 사용자 질..."
- unit_026 — heading_block / 8-3. 아직 질문 의도와 잘 안 붙는 문단 ~ 8-3. 아직 질문 의도와 잘 안 붙는 문단 — "### 8-3. 아직 질문 의도와 잘 안 붙는 문단 - segment_ref: - capability-overhang explanatory windows 일부 - why_not: - 설명은 풍부하지만 다음 탐색 질문..."
- unit_027 — heading_block / 9. residue 간섭 리뷰 ~ 9. residue 간섭 리뷰 — "## 9. residue 간섭 리뷰..."
- unit_028 — heading_block / 9-1. 반복적으로 보인 residue 유형 ~ 9-1. 반복적으로 보인 residue 유형 — "### 9-1. 반복적으로 보인 residue 유형 - discourse_connective_residue: - strong repeated - speaker_or_source_residue: - strong rep..."
- unit_029 — heading_block / 9-2. 실제 방해가 된 residue ~ 9-2. 실제 방해가 된 residue — "### 9-2. 실제 방해가 된 residue - 어떤 residue가 opening summary를 흐렸는가: - `generic_abstraction_residue` - `conversational_filler_..."
- unit_030 — heading_block / 9-3. 이번 턴의 해석 ~ 9-3. 이번 턴의 해석 — "### 9-3. 이번 턴의 해석 - hard suppression 대상 아님: - YES - summary-stage deprioritization 후보: - YES - 유지해야 하는 residue: - 일부 spe..."
- unit_031 — heading_block / 10. broad reading vs interview/dialogue reading ~ 10. broad reading vs interview/dialogue reading — "## 10. broad reading vs interview/dialogue reading..."
- unit_032 — heading_block / 10-1. broad concept처럼 읽힌 부분 ~ 10-1. broad concept처럼 읽힌 부분 — "### 10-1. broad concept처럼 읽힌 부분 - `AI의 미래`, `모델 work`, `전략/방향성`은 broad concept side로도 읽힌다...."
- unit_033 — heading_block / 10-2. interview/dialogue residue가 강하게 낀 부분 ~ 10-2. interview/dialogue residue가 강하게 낀 부분 — "### 10-2. interview/dialogue residue가 강하게 낀 부분 - capability-overhang 설명 구간 - 적응 경쟁 / 10x 전환 구간..."
- unit_034 — heading_block / 10-3. 이번 자료가 어디에 더 가까운가 ~ 10-3. 이번 자료가 어디에 더 가까운가 — "### 10-3. 이번 자료가 어디에 더 가까운가 - `mixed` - why: - `broad concept처럼 자라는 객체와 interview/dialogue residue가 동시에 강하다. 그래서 concept..."
- unit_035 — heading_block / 11. 엔진 관점 해석 ~ 11. 엔진 관점 해석 — "## 11. 엔진 관점 해석 이번 결과를 공간 운영 엔진 관점에서 읽으면:..."
- unit_036 — heading_block / 11-1. 입력은 어떤 객체 성장 이벤트였는가 ~ 11-1. 입력은 어떤 객체 성장 이벤트였는가 — "### 11-1. 입력은 어떤 객체 성장 이벤트였는가 - `AI의 미래 / 일의 미래 / 에이전트 애플리케이션 / 모델 work / 전략/방향성` 객체군을 동시에 두껍게 한 성장 이벤트였다...."
- unit_037 — heading_block / 11-2. 어떤 객체가 실제로 두꺼워졌는가 ~ 11-2. 어떤 객체가 실제로 두꺼워졌는가 — "### 11-2. 어떤 객체가 실제로 두꺼워졌는가 - `에이전트 애플리케이션` - `모델 work` - `전략/방향성`..."
- unit_038 — heading_block / 11-3. 어떤 층이 보강되었는가 ~ 11-3. 어떤 층이 보강되었는가 — "### 11-3. 어떤 층이 보강되었는가 - 설명/해석 위에 전략/방향, 구현/실행, 질문 유도 층이 반복적으로 보강됐다...."
- unit_039 — heading_block / 11-4. 어떤 관계가 새로 보였는가 ~ 11-4. 어떤 관계가 새로 보였는가 — "### 11-4. 어떤 관계가 새로 보였는가 - 모델 capability ↔ search problem ↔ agent execution - bundle-unbundle ↔ app replacement ↔ strate..."
- unit_040 — heading_block / 11-5. 아직 비어 있는 층은 무엇인가 ~ 11-5. 아직 비어 있는 층은 무엇인가 — "### 11-5. 아직 비어 있는 층은 무엇인가 - relation typing의 더 선명한 분해 - residue-aware summary stabilization ---..."
- unit_041 — heading_block / 12. 이번 테스트의 진짜 의미 ~ 12. 이번 테스트의 진짜 의미 — "## 12. 이번 테스트의 진짜 의미 이번 테스트는 단순히 이 문서를 읽었다는 뜻이 아니라, 아래 중 무엇을 증명했는지로 적는다. - 객체 판독 가능성 - 층위 판독 가능성 - 관계 운동 판독 가능성 - 질문 의도 ..."
- unit_042 — heading_block / 13. 다음 bounded step 추천 ~ 13. 다음 bounded step 추천 — "## 13. 다음 bounded step 추천..."
- unit_043 — heading_block / 추천 1 ~ 추천 1 — "### 추천 1 - next_step_name: - summary-stage deprioritization candidate review - why: - residue는 남겨 두되, opening summary에서 ..."
- unit_044 — heading_block / 추천 2 ~ 추천 2 — "### 추천 2 - next_step_name: - question-intent fit refinement - why: - 이미 잘 뜨는 window cluster를 더 선명하게 묶어 주면 객체 성장과 사용자 질문 ..."
- unit_045 — heading_block / 추천 3 ~ 추천 3 — "### 추천 3 - next_step_name: - object growth candidate accumulation review - why: - repeated objects를 이후 다른 youtube dialog..."
- unit_046 — heading_block / 14. 지금 하지 말아야 할 것 ~ 14. 지금 하지 말아야 할 것 — "## 14. 지금 하지 말아야 할 것 - 일반화 잠금 - axis refactor - 사전류/백과사전류 투입 ---..."
- unit_047 — heading_block / 15. 재사용 가치 판정 ~ 15. 재사용 가치 판정 — "## 15. 재사용 가치 판정..."
- unit_048 — heading_block / 이 자료는 앞으로 어떤 용도로 재사용 가능한가 ~ 이 자료는 앞으로 어떤 용도로 재사용 가능한가 — "### 이 자료는 앞으로 어떤 용도로 재사용 가능한가 - 반복 테스트 자산: - YES - 객체 성장 재료: - YES - residue 훈련 재료: - YES - user-layer translation 훈련 재료..."
- unit_049 — heading_block / 재사용 난이도 ~ 재사용 난이도 — "### 재사용 난이도 - 낮음..."
- unit_050 — heading_block / 다시 돌릴 때 조정할 것 ~ 다시 돌릴 때 조정할 것 — "### 다시 돌릴 때 조정할 것 - `window/stride는 그대로 유지하고, 다음에는 summary-stage priority 조정 여부만 얇게 비교하면 된다.` ---..."
- unit_051 — heading_block / 16. 운영 반영 ~ 16. 운영 반영 — "## 16. 운영 반영 - delta reflected: - `runtime/views/repo_delta_log_latest_v1.md` - raw log appended: - `runtime/logs/repo_d..."
- unit_052 — heading_block / 17. 진짜 한 줄 요약 ~ 17. 진짜 한 줄 요약 — "## 17. 진짜 한 줄 요약 > `youtube_03_22.md`는 같은 loop를 다시 돌려도 객체·층위·관계·질문 의도 구조가 거의 같은 모양으로 반복되어, 반복 학습형 고밀도 대화 테스트 자산으로는 충분히 안..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

