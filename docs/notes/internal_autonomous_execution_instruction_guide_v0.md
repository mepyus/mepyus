# internal autonomous execution instruction guide v0

## Purpose

이 문서는 내부 자율 실행 지시서를 설계할 때
어떤 경계와 실행 규율을 먼저 잠가야 하는지 정리한다.

핵심은 모델이 똑똑한가보다,
턴 경계, 금지 범위, 검증 게이트, 정지 조건이
시스템적으로 잠겨 있는가다.

## Core stance

- 자율 실행은 자유 실행이 아니다
- 각 턴은 명시된 범위 안에서만 움직여야 한다
- 다음 턴 진입은 성공 조건을 통과했을 때만 허용한다
- 관찰 턴과 구현 턴은 반드시 분리한다

## Required control points

### 1. turn boundary enforcement

- `Turn 1만`, `Turn 2까지만`, `Turn 2 이후 정지` 같은 규칙을 명시한다
- 각 턴의 시작 조건과 종료 조건을 분리해서 적는다
- 최종 정지 조건은 자연어 권고가 아니라 강한 실행 규칙처럼 적는다

### 2. do not do isolation

- 금지 항목은 별도 블록으로 분리한다
- 파일 수정 금지, runtime 오염 금지, broad refactor 금지처럼
  금지 범위를 구체적으로 적는다
- 금지 범위는 목표보다 먼저 읽혀도 될 정도로 앞에 두는 편이 안전하다

### 3. artifact-scoped execution

- 각 턴에서 수정 가능한 파일과 생성 가능한 파일을 명시한다
- 가능하면 file placement를 따로 둔다
- 이렇게 해야 skeleton 턴이 validation 턴으로 번지는 것을 막을 수 있다

### 4. deliverable-driven stopping

- 멈춤 조건은 deliverable 단위로 적는다
- 예:
  - 파일 생성
  - 검증 실행
  - 요약 보고
- deliverable 보고가 끝나면 반드시 멈춘다고 명시한다

### 5. validation gate before continuation

- 다음 턴 진입 전에 통과해야 할 명령을 적는다
- 예:
  - `py_compile`
  - probe script
  - validation script
- 실패 시 다음 턴으로 가지 말라고 명시한다

### 6. spec-to-code traceability

- 어떤 spec을 참조해 구현하는지 SSOT를 먼저 적는다
- patch 턴이라면 참조 spec 문서를 명시한다
- 그래야 patch가 임의 확장으로 흐르지 않는다

### 7. observation vs implementation separation

- validation 턴은 관찰만 한다고 분리한다
- 이 턴에서 코드 수정 금지라고 명확히 적는다
- 반대로 patch 턴은 수정 범위를 좁게 적는다

### 8. regression guard anchoring

- 현재 통과 fixture와 expected를 별도 문서나 스크립트로 고정한다
- 이후 patch는 그 regression guard를 먼저 통과해야 한다
- 기준 자체를 바꾸는 패치는 별도 턴으로 분리한다

### 9. output contract normalization

- 최종 보고 형식을 고정한다
- 예:
  - `Turn 1 summary`
  - `Turn 2 summary`
- 보고 형식이 고정돼야 실행자가 범위를 넘지 않는다

## Recommended instruction structure

아래 순서를 권장한다.

1. overall goal
2. fixed baseline
3. turn scope
4. implement exactly
5. do not do
6. validation
7. deliverables
8. definition of done
9. stop rule
10. final output format

## Common failure modes

- stop rule이 약해서 다음 턴으로 넘어감
- validation 턴에서 patch를 시작함
- 금지 파일을 건드림
- spec 없이 구현을 추측으로 확장함
- regression 기준이 없어 새 patch가 이전 품질을 깨뜨림
- output format이 느슨해서 보고가 장황해지고 범위가 넓어짐

## Writing rules

- 각 턴은 하나의 목적만 갖게 쓴다
- 구현 턴과 관찰 턴을 섞지 않는다
- `TBD`는 명시적으로 남긴다
- broad, global, fully 같은 표현은 피한다
- 과장보다 경계가 먼저 보이게 쓴다

## Minimal checklist

- 턴 경계가 명시됐는가
- 금지 범위가 분리됐는가
- 수정 파일 범위가 명시됐는가
- 검증 명령이 있는가
- 실패 시 정지 규칙이 있는가
- 다음 턴 자동 진입 금지 여부가 명시됐는가
- 최종 보고 형식이 고정됐는가

## Next use

다음부터 내부 자율 실행 지시서를 쓸 때는
이 문서를 템플릿 체크리스트처럼 먼저 참조한다.
