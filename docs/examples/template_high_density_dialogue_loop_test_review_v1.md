[[A]] [[OBJ:template_high_density_dialogue_loop_test_review_v1]] [[SEM:review_report_template_for_repeated_dialogue_asset_testing]]

# 리뷰 리포트 템플릿 — 고밀도 대화 자산 반복 테스트 결과 정리

## 0. 문서 목적

이 문서는 고밀도 대화 자산 반복 테스트 결과를
일회성 요약이 아니라
다음 refinement / 확장 / 반복 학습에 다시 참조할 수 있는
리뷰 리포트로 남기기 위한 템플릿이다.

핵심은 아래를 함께 남기는 것이다.

- 객체 후보
- 층위 판독 결과
- 관계 힌트
- 질문 의도 적합도
- residue 간섭
- 다음 bounded step

---

## 1. 기본 정보

- test_name:
- created_at:
- input_asset:
- source_scope:
- loop_script:
- generated_output_dir:
- report_author:
- run_purpose:

예시:
- test_name: `youtube_03_22_high_density_dialogue_loop_test_v1`
- input_asset: `inputs/external_cases/youtube_03_22.md`

---

## 2. 이번 테스트의 목적

이번 테스트는 아래를 보기 위해 수행했다.

- 엔진이 이 대화를 단순 설명형 review로만 읽는지
- 객체 후보가 반복적으로 살아나는지
- 다층 판독이 실제로 보이는지
- 관계 운동 힌트가 잡히는지
- 사용자의 질문 의도와 강하게 닿는 문단이 존재하는지
- residue가 어느 단계에서 번역을 방해하는지

한 줄 목적:
- `______________________________________________`

---

## 3. loop 조건 요약

### 3-1. 분절 조건
- segment_mode:
- window_mode:
- overlap:
- chunk_length_policy:
- repeat_count:

### 3-2. 판독 출력 조건
- layer_reading: YES / NO
- relation_hint: YES / NO
- question_intent_fit: YES / NO
- residue_review: YES / NO
- user_facing_gloss: YES / NO

### 3-3. 비교 조건
- baseline_compare_used:
- prior_result_compare_used:
- cross-run_compare_used:

---

## 4. top-level 판정

- status:
  - `PASS`
  - `PASS_WITH_NOTE`
  - `HOLD`

### 한 줄 판정
- `______________________________________________`

### 왜 그렇게 판정했는가
- `______________________________________________`
- `______________________________________________`
- `______________________________________________`

---

## 5. 객체 후보 판독

## 5-1. 반복적으로 살아난 객체 후보
- object_candidate_1:
  - strength:
  - why:
- object_candidate_2:
  - strength:
  - why:
- object_candidate_3:
  - strength:
  - why:

예시 형식:
- `AI의 미래`
- `일의 미래`
- `에이전트 애플리케이션`
- `생산성/코딩`
- `모델 work`

## 5-2. 객체 성장성 해석
각 객체에 대해 아래를 적는다.

- 이미 두꺼운 층:
- 새로 붙은 층:
- 아직 빈 층:
- 강화 필요 여부:
- 영속 객체 후보 여부:

---

## 6. 층위 판독 결과

### 6-1. 반복적으로 보인 층위
- 설명/해석 층:
- 구현/실행 층:
- 구조/연결 층:
- 전략/방향 층:
- 검증/근거 층:
- 질문 유도 층:

### 6-2. 층위 강도 해석
- 가장 두꺼운 층:
- 예상보다 강했던 층:
- 예상보다 약했던 층:
- 아직 거의 안 보이는 층:

### 6-3. user-facing opening 관점 해석
- 사용자가 바로 읽기 쉬운 층:
- gloss가 붙어도 아직 흐린 층:
- 다음 질문을 유도하는 층:
- 단순 정보층에 머무는 층:

---

## 7. 관계 힌트 판독

### 7-1. 반복적으로 보인 관계 운동
- reinforcement_hint:
- contrast_hint:
- transition_hint:
- execution_shift_hint:
- specification_hint:
- question_generation_hint:

### 7-2. 관계 힌트 예시
- sample_1:
  - source_segment:
  - relation_hint:
  - why:
- sample_2:
  - source_segment:
  - relation_hint:
  - why:
- sample_3:
  - source_segment:
  - relation_hint:
  - why:

### 7-3. 현재 한계
- 단순 공출현처럼만 보이는 부분:
- 아직 관계 운동으로 읽기 어려운 부분:
- 관계가 보이지만 유형 구분은 애매한 부분:

---

## 8. 질문 의도 적합 문단

### 8-1. 가장 강하게 닿는 문단 후보
- candidate_1:
  - segment_ref:
  - why_it_matches_user_intent:
- candidate_2:
  - segment_ref:
  - why_it_matches_user_intent:
- candidate_3:
  - segment_ref:
  - why_it_matches_user_intent:

### 8-2. 이 문단들이 중요한 이유
- 객체를 두껍게 한다 / 질문을 연다 / 관계를 만든다 / 층위를 번역한다 중 무엇인가:
- `______________________________________________`

### 8-3. 아직 질문 의도와 잘 안 붙는 문단
- segment_ref:
- why_not:
- residue_or_gap_reason:

---

## 9. residue 간섭 리뷰

### 9-1. 반복적으로 보인 residue 유형
- discourse_connective_residue:
- speaker_or_source_residue:
- conversational_filler_residue:
- generic_abstraction_residue:
- quasi_topic_residue:
- observer_transition_residue:

### 9-2. 실제 방해가 된 residue
- 어떤 residue가 opening summary를 흐렸는가:
- 어떤 residue가 topic-bearing anchor와 경쟁했는가:
- 어떤 residue는 있어도 큰 문제는 없었는가:

### 9-3. 이번 턴의 해석
- hard suppression 대상 아님:
- summary-stage deprioritization 후보:
- 유지해야 하는 residue:
- borderline residue:

---

## 10. broad reading vs interview/dialogue reading

### 10-1. broad concept처럼 읽힌 부분
- `______________________________________________`

### 10-2. interview/dialogue residue가 강하게 낀 부분
- `______________________________________________`

### 10-3. 이번 자료가 어디에 더 가까운가
- broad concept side / dialogue side / mixed
- why:
  - `______________________________________________`

---

## 11. 엔진 관점 해석

이번 결과를 공간 운영 엔진 관점에서 읽으면:

### 11-1. 입력은 어떤 객체 성장 이벤트였는가
- `______________________________________________`

### 11-2. 어떤 객체가 실제로 두꺼워졌는가
- `______________________________________________`

### 11-3. 어떤 층이 보강되었는가
- `______________________________________________`

### 11-4. 어떤 관계가 새로 보였는가
- `______________________________________________`

### 11-5. 아직 비어 있는 층은 무엇인가
- `______________________________________________`

---

## 12. 이번 테스트의 진짜 의미

이번 테스트는 단순히 이 문서를 읽었다는 뜻이 아니라,
아래 중 무엇을 증명했는지로 적는다.

- 객체 판독 가능성
- 층위 판독 가능성
- 관계 운동 판독 가능성
- 질문 의도 적합 문단 식별 가능성
- residue 간섭 위치 식별 가능성
- 고밀도 대화 자산의 테스트 재료 가치

한 줄 의미:
- `______________________________________________`

---

## 13. 다음 bounded step 추천

### 추천 1
- next_step_name:
- why:
- scope_limit:

### 추천 2
- next_step_name:
- why:
- scope_limit:

### 추천 3
- next_step_name:
- why:
- scope_limit:

예시:
- residue interference reduction review
- summary-stage deprioritization candidate review
- object growth candidate accumulation review
- question-intent fit refinement
- relation hint vocabulary tightening

---

## 14. 지금 하지 말아야 할 것

- `______________________________________________`
- `______________________________________________`
- `______________________________________________`

예시:
- 일반화 잠금
- axis refactor
- 사전류/백과사전류 투입
- hard suppression
- 전체 자료군 일괄 투입

---

## 15. 재사용 가치 판정

### 이 자료는 앞으로 어떤 용도로 재사용 가능한가
- 반복 테스트 자산:
- 객체 성장 재료:
- residue 훈련 재료:
- user-layer translation 훈련 재료:
- example asset 후보:

### 재사용 난이도
- 낮음 / 중간 / 높음

### 다시 돌릴 때 조정할 것
- `______________________________________________`

---

## 16. 운영 반영

- delta reflected:
- raw log appended:
- receipt created:
- related directive/baseline/example references:

예시:
- `runtime/views/repo_delta_log_latest_v1.md`
- `runtime/logs/repo_delta_log.jsonl`

---

## 17. 진짜 한 줄 요약

> `______________________________________________`
