# doc_004 Analysis

## 적합성 판단

- 비교 실험용 입력으로 적절하다.
- 시스템 설명, 기능 정의, 예시, 권한/사이드 이펙트, 데이터 반영 구조가 순차적으로 나온다.
- 처리자마다 `action`, `action_type`, `side_effect`, `writeback_dataset`을 어떻게 anchor로 잡는지 차이를 보기 좋다.

## Codex 기준선 절단 판단

### fragment 1
- 범위: Foundry 온톨로지에서 액션이 무엇이고 왜 쓰는지 설명
- 중심 움직임: `action transaction definition`

### fragment 2
- 범위: 액션 유형 정의와 사이드 이펙트 포함 설명
- 중심 움직임: `action_type definition`

### fragment 3
- 범위: Assign Employee 예시와 role 변경, 링크 생성 설명
- 중심 움직임: `assign_employee example`

### fragment 4
- 범위: 알림, 권한, HR 수행 예시
- 중심 움직임: `side_effect and permission controls`

### fragment 5
- 범위: Foundry 온톨로지의 실제 데이터 매핑과 데이터 자산 가치 설명
- 중심 움직임: `ontology data mapping`

### fragment 6
- 범위: 액션 커밋, 애플리케이션 반영, 일관된 편집, writeback 데이터셋 설명
- 중심 움직임: `writeback consistency flow`

## 관찰 포인트

- `action`과 `action_type`을 분리하는지 묶는지 차이가 날 수 있다.
- `Assign Employee` 예시를 `example`로 읽는지 `instruction`이나 `support`로 읽는지 갈릴 수 있다.
- `side_effect`, `permission`, `writeback_dataset` 같은 운영 개념을 object/process/structural 중 무엇으로 anchor화하는지 흔들릴 수 있다.
