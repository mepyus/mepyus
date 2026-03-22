# current

## 목적

이 문서는 `vectorfl_replica/references/md_maker`에서
현재까지 무엇을 했는지 빠르게 다시 확인하기 위한 작업 기준선 문서다.

즉 길게 다시 읽기 전에,

- 오늘 무엇을 만들었는가
- 어떤 기준으로 만들었는가
- 지금 문서 묶음이 어떤 상태인가

를 한 번에 확인하기 위한 현재 상태 메모다.

## 현재 작업 목적

이번 작업의 목적은 `WashTank` 코드를 바로 수정하는 것이 아니라,
`WashTank`를 다시 읽고 그 프로그램을 만들던 과정과 의도를
md로 복원하는 것이다.

핵심 의도는 다음과 같다.

1. 탱크 프로그램을 만들던 과정을 다시 기록하고 싶다
2. 웹 ChatGPT와 함께 만들며 흩어진 이유와 맥락을 다시 남기고 싶다
3. 나중에 다른 프로그램이나 다른 공정을 만들 때 재사용 가능한 해석 레이어를 만들고 싶다
4. 여러 프로그램의 md 파일을 모아, 코드와 과정 문서를 함께 읽는 실험을 하고 싶다

즉 이 작업은 `WashTank` 정리이면서 동시에
앞으로 다른 공정 프로그램을 만들 때 가져갈 설계 언어를 남기는 작업이다.

## 이번에 한 일

`WashTank` 참조 폴더를 읽고,
그 내용을 코드 설명이 아니라 "과정과 의도" 기준으로 다시 풀어쓴 md 문서들을 만들었다.

현재 생성된 문서는 다음과 같다.

- `reader_guide.md`
- `index.md`
- `WashTank_overview.md`
- `WashTank_process_flow.md`
- `WashTank_screen_roles.md`
- `WashTank_engine_and_data.md`
- `WashTank_build_traces.md`
- `WashTank_screen_creation_reasons.md`
- `WashTank_jms_screen_connection.md`
- `WashTank_glossary.md`
- `WashTank_timeline_guess.md`
- `WashTank_screen_process_engine_map.md`

## 문서 묶음의 현재 성격

지금 `md_maker`는 단순 요약 폴더가 아니라,
아래 층을 가진 `WashTank` 해석 레이어가 되기 시작했다.

### 1. 개요 층

- `WashTank_overview.md`

### 2. 공정 흐름 층

- `WashTank_process_flow.md`

### 3. 화면 해석 층

- `WashTank_screen_roles.md`
- `WashTank_screen_creation_reasons.md`
- `WashTank_screen_process_engine_map.md`

### 4. 엔진 / 데이터 층

- `WashTank_engine_and_data.md`
- `WashTank_jms_screen_connection.md`
- `WashTank_glossary.md`

### 5. 과정 흔적 층

- `WashTank_build_traces.md`
- `WashTank_timeline_guess.md`

### 6. 읽기 가이드 층

- `reader_guide.md`
- `index.md`

## 지금까지 합의한 중요한 해석

현재까지 읽은 기준으로 `WashTank`는 다음처럼 해석하고 있다.

1. 단순 탱크 관리 앱이 아니라, 탱크를 공정 흐름 안에서 움직이는 운영 프로그램이다
2. 공정 분리뿐 아니라 사무실 / 현장 / 장비기사 / 셔틀 / 부지 차이까지 화면에 반영하려 했다
3. 화면은 많지만 그 밑에는 `JMS`와 상태 전이 구조를 하나의 질서로 묶으려는 생각이 있다
4. 이 폴더는 완성 제품보다 "만들어지던 흔적"이 남은 아카이브로 보는 편이 더 맞다
5. md로 다시 풀어두면, 나중에 다른 공정 프로그램을 만들 때 속도와 일관성이 올라간다

## 현재 판단

이번 작업은 성공적으로 시작되었다.

이유:

- `WashTank`를 다시 읽을 기준 문서가 생겼다
- 코드와 md를 섞어 읽는 기반이 생겼다
- 이후 다른 프로그램도 같은 방식으로 문서화할 수 있는 템플릿 감각이 생겼다

즉 지금 상태만으로도 `WashTank`는
단순 참조 코드 폴더가 아니라,
재구성 가능한 공정 기록 자료가 되기 시작했다.

## 다음에 이어서 하기 좋은 일

다음 작업 후보는 아래와 같다.

1. `md_maker` 문서 간 링크를 더 촘촘히 연결하기
2. `WashTank`의 특정 화면 하나를 깊게 읽어 별도 집중 문서 만들기
3. `db.md`, `tms.md`를 더 세밀하게 풀어 별도 문서 만들기
4. 다른 프로그램도 같은 방식으로 md 레이어 만들기
5. 여러 프로그램 md를 모아 비교 가능한 기록 폴더로 키우기

## 한 줄 정리

현재 `md_maker`는 `WashTank`를 다시 배우기 위한 해설 모음이 아니라,
나중에 다른 공정 프로그램을 만들 때도 재사용할 수 있는
"공정 해석 언어 저장소"의 시작점이다.
