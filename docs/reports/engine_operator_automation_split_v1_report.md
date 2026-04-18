# engine_operator_automation_split_v1_report.md

## 1. why now

현재 엔진은 이미 다음을 가진다.

- canonical state core
- update/store/history/latest
- process console surface
- diff/badge/attention/memory derived layer
- freeze된 core/derived/surface/experimental 경계

따라서 지금부터는 같은 패턴의 실행을 계속 수동으로 반복하기보다,
자동화 가능한 부분은 파이프라인화하고
메인 테크니션 판단은 경계/교정/검토에 집중시키는 운영 방식이 맞다.

## 2. split summary

### automation으로 돌릴 것

- probe 실행
- state append/update 루프
- latest/history refresh
- diff/badge/queue/memory refresh
- process console payload build
- fixture/consistency rerun
- receipt/log/report skeleton 작성

### 직접 판단으로 남길 것

- canonical enum final choice
- compare verdict
- blocker/attention 의미 분리
- false improvement 방지
- layer freeze policing
- experimental leakage 차단

## 3. practical read

앞으로 내 토큰은 아래에 더 써야 한다.

- 애매한 state 경계 판정
- compare 결과 해석
- derived layer가 truth처럼 오해되는 지점 교정
- update 결과가 과장되지 않았는지 검토

반대로 아래는 가능하면 스크립트화해야 한다.

- run orchestration
- full refresh
- queue/memory rebuild
- bundle receipt/log generation

## 4. current recommendation

다음 우선 자동화 대상은 이 다섯 개다.

1. live run bundle command
2. compare run bundle command
3. canonical state candidate builder
4. derived surface full refresh command
5. process console verification command

## 5. final judgment

지금 엔진은 이미 단순 실험 묶음이 아니라 운영 가능한 프로그램 상태다.
따라서 이제부터의 효율화 방향은 기능 확장보다,
반복 루프를 자동화하고 메인 테크니션 판단을 더 고밀도로 쓰는 쪽이 맞다.
