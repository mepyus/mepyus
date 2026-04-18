# core_promotion_checklist_v1

## purpose
외부 사례 / 예시문 / 관측 결과 / 탐색 판독이 쌓일 때
무엇을 코어 후보로 읽고,
무엇을 외곽 후보로 남기며,
무엇을 보류해야 하는지
반복 가능한 체크리스트로 고정한다.

## reading rule
- 이 문서는 자동 승격 규칙이 아니다.
- 현재 목적은 코어 후보 판독 기준을 observer/readout에서 반복 가능하게 만드는 것이다.
- 승격 보류 이유를 반드시 남긴다.

## checklist

### 1. repeat_frequency
- 동일하거나 매우 유사한 판단 슬롯이 반복해서 등장하는가

### 2. cross_context_reappearance
- 서로 다른 문맥 / 주제 / 입력 유형에서도 재등장하는가

### 3. cross_session_or_run_presence
- session 또는 run 을 넘어 반복되는가

### 4. actual_reuse_evidence
- 후속 설계 / 기능 판단 / 문서 작성에서 실제 다시 참조되었는가

### 5. outer_only_sufficiency
- observer / guide / outer layer 에만 남겨도 충분한가

### 6. explanatory_axis_role
- 다른 요소를 설명하는 축인가
- 아니면 독립 중심축 후보인가

### 7. premature_generalization_risk
- 지금 코어로 올리면 과도하게 일반화될 위험이 있는가

## status values
- `core_candidate`
- `outer_candidate`
- `defer`
- `observer_only`

## minimum reasoning fields
- `status`
- `reason`
- `repeat_frequency`
- `cross_context_reappearance`
- `cross_session_or_run_presence`
- `actual_reuse_evidence`
- `outer_only_sufficiency`
- `explanatory_axis_role`
- `premature_generalization_risk`
- `next_review_hint`

## reading guidance

### core_candidate
- 반복 출현이 있고
- 다른 문맥에서도 다시 나타나며
- 후속 작업에서 실제 재사용되고
- outer layer 에만 남기기엔 부족한 경우

### outer_candidate
- 설명력은 있지만
- 코어 축으로 고정하기엔 아직 이르고
- observer / report / guide 에 두는 편이 적절한 경우

### defer
- 가능성은 보이나
- 반복성과 재사용 근거가 아직 부족하거나
- 일반화 위험이 큰 경우

### observer_only
- 현재는 관찰 기록으로만 남기는 것이 맞는 경우
- 코어 후보 판단 자체가 아직 시기상조인 경우

## note
- 코어 승격은 빠를수록 좋은 것이 아니다.
- 반복성과 재사용 근거 없이 올리면 코어 비대화만 생긴다.
