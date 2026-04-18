[[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]
[[A]] [[OBJ:external_case_first_pass]] [[SEM:thin_operation_rules_live_validation]]

# CODEx 지시서 — External Case First Pass v1
# 목적: 방금 잠근 thin operation rules가 실제 외부 사례 1건에서 살아 움직이는지 검증한다.
# 이번 턴 범위: 외부 사례 1건 선택 -> exploration observation 기록 1회 -> core/outer/defer/observer_only 판독 1세트 생성
# 금지: 코어 수정, trigger 자동화 확장, 번역층 구축, 예시문 대량 생성

## 0. 이번 턴의 성격
이번 턴은 새 철학을 쓰는 턴이 아니다.
문서를 더 늘리는 턴도 아니다.

이번 턴은 오직 하나를 확인하는 턴이다.

방금 잠근 3개 운영 슬롯이 실제 사례 1건에서 반복 가능한 방식으로 작동하는가.

## 1. 입력 사례 선택 기준
- 외부 기술 / 외부 회사 사례 / 외부 운영 방식 / 외부 구조 아이디어 중 1건
- 한 번에 읽고 핵심 차이를 잡을 수 있는 크기
- 우리 엔진에 바로 채택/보류/관측 판단을 해볼 수 있는 사례
- 너무 장황한 원문보다 핵심 설명이 비교적 선명한 사례

## 2. 이번 턴 목표 산출물
- `docs/examples/external_case_first_pass_<case_name>_v1.md`
- `runtime/observer/exploration/json/external_case_first_pass_<case_name>_v1.json`
- `runtime/observer/exploration/md/external_case_first_pass_<case_name>_v1.md`
- `runtime/contracts/core_promotion_reading_<case_name>_v1.json`
- 필요 시 `runtime/contracts/refinement_trigger_reading_<case_name>_v1.json`

## 3. 작업 A — 외부 사례 1건을 observation layer에 기록
중요한 건 멋진 해석이 아니라 반복 가능한 기록이다.

즉 아래를 구분해서 남긴다.
- 이 사례에서 실제로 눈에 띈 구조
- 우리 엔진에 바로 가져올 수 있는 것
- 아직 바로 가져오면 과한 것
- 나중 참고용으로만 남겨둘 것

## 4. 작업 B — core promotion checklist로 1차 판독
사례 전체를 한 덩어리로 판단하지 말고,
핵심 운영 원리 / 기록 구조 / 위험 일반화 요소 / observer 전용 요소 정도로 나눠 판독한다.

## 5. 작업 C — refinement trigger 관점에서 현재 상태 읽기
이번 단일 사례가 지금 당장 refinement를 여는 수준인지,
아직 watch 수준인지,
아예 no_trigger인지 읽는다.

## 6. 문서 작성 방식
외부 사례 소개문이 아니라 운영면 검증 기록으로 쓴다.

## 7. 일부러 하지 말 것
- 사례를 코어에 실제 편입하지 말 것
- translation layer를 새로 만들지 말 것
- trigger 자동 판정기를 무겁게 만들지 말 것
- 새로운 observer 타입을 우후죽순 늘리지 말 것
- 사례 1건을 계기로 전체 설계를 다시 흔들지 말 것

## 8. 완료 기준
- observation json/md 가 남는다
- 후보 2~4개가 core_candidate / outer_candidate / defer / observer_only 로 나뉜다
- refinement 상태가 읽힌다
- 문서가 운영면 검증 기록으로 남는다

## 9. 한 줄 요약
이번 턴은 외부 사례 1건을 실제로 넣어
exploration observation 기록 + core/outer/defer 판독 + refinement 상태 읽기
가 반복 가능한 운영 슬롯으로 작동하는지 검증하는 턴이다.
