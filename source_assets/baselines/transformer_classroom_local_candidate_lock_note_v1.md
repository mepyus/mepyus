[[A]] [[OBJ:lock_note]] [[SEM:transformer_classroom_local_candidate_lock]]

# transformer_classroom_local_candidate_lock_note_v1

## lock
- transformer classroom same-topic pass에서 확인된 3단 설명 frame
  - 제약/문제 배경 제시
  - transformer 기본 구조 진입
  - 주요 작동 메커니즘 설명
  는 local explanatory candidate로 유지한다.

- graphrag_neosh negative control 결과,
  exact same frame은 반복되지 않았고
  broader technical-explanatory overlap만 부분적으로 확인되었다.

## current judgment
- same-topic transformer classroom frame = `VALID_LOCAL_CANDIDATE`
- broader general technical frame = `NOT_YET_CONFIRMED`
- promotion = `HOLD`
- overgeneralization risk = `YES_IF_PROMOTED_NOW`

## operating note
- 다음 단계에서는 이 frame을 baseline/general law로 승격하지 않는다.
- 현재 상태에서는 후보로 보관하고, current surface는 확장하지 않는다.
- delta latest 수준의 짧은 흔적만 유지한다.
