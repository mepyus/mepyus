# refinement_trigger_rules_v1

## purpose
정련(refinement)을
언젠가 필요하면이 아니라
개시 조건이 명시된 운영 트리거로 고정한다.

## status values
- `no_trigger`
- `watch`
- `refinement_candidate`
- `refinement_recommended`

## trigger rules

### 1. external_case_accumulated_ge_5
- 새 외부 사례가 5건 이상 누적되면
- 비교축 / 차용 구조 / 분리 유지 기준이 중복되는지 점검한다.

### 2. repeated_relation_slot_ge_3
- 같은 relation slot 또는 핵심 패턴이 3회 이상 반복되면
- 코어 후보 / outer 유지 / defer 재검토를 연다.

### 3. observer_readout_confusion
- observer readout 이 길어져
- core / outer / defer 혼선이 커지면
- 정련 후보로 본다.

### 4. guide_contract_index_relayout_needed
- guide / contract / example 이 늘어나
- 인덱스 재배치가 필요하면
- 구조 정리용 refinement 를 연다.

### 5. repeated_defer_candidate
- 같은 후보가 2회 이상 defer 로 남으면
- 재판정 필요 상태로 본다.

## operating rule
- trigger 는 자동 실행기가 아니다.
- trigger hit 시 사람이 refinement 개시 여부를 판단할 수 있게 만든다.
- 너무 잦은 정련을 피하기 위해 소수의 trigger 만 유지한다.

## recommended reading

### no_trigger
- 지금은 정련을 열 필요가 없음

### watch
- 신호는 있으나 아직 정련 개시 전

### refinement_candidate
- 정련 후보로 공식 표기할 수준

### refinement_recommended
- 이번 운영 묶음 안에서 정련 패스를 여는 것이 유익한 수준

## note
- 정련은 삭제가 아니라 재배치와 경량화다.
- trigger 의 목적은 과잉 확장과 코어 비대화를 늦추는 것이다.
