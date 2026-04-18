[[A]] [[OBJ:graphrag_enterprise_next_loop_gate_validation_v1]] [[SEM:comparison_validation_of_next_loop_entry_gate_on_second_and_third_candidate_assets]]

# graphrag / enterprise next loop gate validation v1

## 1. purpose

- 이번 문서의 목적은 앞서 2순위 / 3순위 비교 예제로 뽑았던
  - `inputs/external_cases/graphrag_neosh.txt`
  - `inputs/external_cases/enterprise.txt`
  를 현재 잠근 3축 구조와 `second_order_next_loop_entry_gate_v1` 기준 위에서 검증하는 것이다.
- 핵심은 새 실험을 여는 것이 아니라, 이 자산들이 현재 gate를 통과하는지 아니면 hold 근거를 더 강화하는지 판정하는 것이다.

## 2. baseline structural read

### 2-1. graphrag_neosh

- baseline probe:
  - `w3/s1`: window `1`
  - `w6/s3`: window `1`
- read:
  - segmentation support 없이는 즉시 single block collapse

### 2-2. enterprise

- baseline probe:
  - `w3/s1`: window `1`
  - `w6/s3`: window `1`
- read:
  - dialogue-like transcript이지만 baseline에선 역시 single block collapse

### 2-3. shared implication

- 두 자산 모두 `openai_02_11`와 달리,
  baseline 자체로는 next-loop validation 대상이 아니라
  **segmentation support가 먼저 필요한 자산**이다.

## 3. after segmentation support

### 3-1. graphrag_neosh

- segmentation support 후:
  - `w3/s1`: window `200`
  - `w6/s3`: window `67`

### 3-2. enterprise

- segmentation support 후:
  - `w3/s1`: window `334`
  - `w6/s3`: window `111`

### 3-3. structural verdict

- 두 자산 모두 `segmentation = 필요조건 복구축`이라는 현재 판정과 일치한다.
- 즉 2차 태도를 시험할 최소 기반은 회복되었다.

## 4. what survived after current second-order stack

### 4-1. graphrag_neosh

- purpose layer에서 살아난 것:
  - objects:
    - `모델 work`
    - `생산성/코딩`
    - `에이전트 애플리케이션`
  - relations:
    - `reinforcement_hint`
    - `transition_hint`
    - `execution_shift_hint`
    - `question_generation_hint`
    - `contrast_hint`
- meaning:
  - question opening / relation movement 태도는 유지된다.

### 4-2. enterprise

- purpose layer에서 살아난 것:
  - objects:
    - `모델 work`
    - `생산성/코딩`
    - `에이전트 애플리케이션`
    - `일의 미래`
    - `전략/방향성`
  - relations:
    - `transition_hint`
    - `reinforcement_hint`
    - `question_generation_hint`
    - `specification_hint`
    - `execution_shift_hint`
- meaning:
  - dialogue-like structure 덕분에 user-layer opening은 더 풍부하지만,
  현재 판독은 여전히 reusable attitude 수준에서만 살아난다.

## 5. what still did not recover

### 5-1. question-inducing candidates

- graphrag_neosh:
  - `0`
- enterprise:
  - `0`

shared read:
- relation movement와 question-opening 태도는 살아나도,
  gate가 요구하는 `question-inducing block candidate` emergence는 여전히 없다.

### 5-2. context unit grounding

- graphrag_neosh:
  - context units `3`
  - 전부 `fallback_grounded`
  - pointer source는 `purpose_top_windows`
- enterprise:
  - context units `3`
  - 전부 `fallback_grounded`
  - pointer source는 `purpose_top_windows`

shared read:
- context unit institution은 아직 direct grounding을 얻지 못했다.

### 5-3. role-like reading

- graphrag_neosh:
  - paragraph role analyses `3`
  - 모두 `role_like_reading_observed`
  - `weak_medium + fallback_grounded`
- enterprise:
  - paragraph role analyses `3`
  - 모두 `role_like_reading_observed`
  - `weak_medium + fallback_grounded`

### 5-4. suspicious scaffold carryover

- 두 자산 모두 아래 context scaffold를 거의 동일하게 재생산했다.
  - `agent_interface_transition_unit`
  - `future_of_work_supervisor_unit`
  - `model_eval_shift_unit`

shared read:
- 이것은 role-like reading이 generalized institution으로 회복됐다는 증거가 아니라,
  **기존 scaffold naming carryover가 여전히 강하다는 증거**다.

## 6. gate verdict

### 6-1. what is confirmed again

- reusable attitude는 여러 자산에서 살아남는다.
- segmentation support는 collapse를 실제로 완화한다.
- pointer + heading probe는 fallback-grounded role-like reading까지는 만든다.

### 6-2. what still blocks the gate

- direct grounded recovery 없음
- question-inducing candidate가 두 자산 모두 `0`
- context unit은 fallback grounding에 머묾
- role-like reading은 weak_medium only
- naming / context scaffold carryover 위험 지속

## 7. final judgment

- `graphrag_neosh`: `ENTRY_GATE_NOT_PASSED`
- `enterprise`: `ENTRY_GATE_NOT_PASSED`

### why

- 두 자산 모두 current second-order stack이 완전히 무너지지는 않는다는 점은 보여준다.
- 그러나 현재 gate가 요구하는:
  - direct grounding
  - candidate emergence
  - repeated evidence-linked role recovery without carryover
  를 보여주지 못한다.

즉 이 두 자산은 gate reopening 근거가 아니라,
**현재 hold basis를 cross-asset 쪽에서 더 두껍게 만드는 검증 자산**이다.

## 8. one-line summary

> `graphrag_neosh.txt`와 `enterprise.txt`는 segmentation support 후에도 reusable attitude만 부분적으로 회복될 뿐, direct grounding / question-inducing candidate / scaffold-independent role recovery를 보여주지 못했으므로 next loop entry gate를 통과하지 못한다.
