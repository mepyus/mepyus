# WashTank Reader Guide

## 목적

이 문서는 `md_maker` 안에 쌓인 `WashTank` 관련 md들을
어떤 목적과 순서로 읽으면 좋은지 안내하기 위한 가이드다.

이 폴더의 문서들은 전부 같은 종류가 아니다.

어떤 문서는 전체 개요를 잡기 좋고,
어떤 문서는 엔진과 데이터 구조를 보기에 좋고,
어떤 문서는 만드는 과정의 흔적을 읽기에 좋다.

그래서 이 가이드는
"지금 무엇을 알고 싶은가"에 따라 읽기 경로를 나눠 주는 역할을 한다.

## 1. 처음 읽는 경우

처음 `WashTank`를 읽는다면 아래 순서가 가장 무난하다.

1. `WashTank_overview.md`
2. `WashTank_process_flow.md`
3. `WashTank_screen_roles.md`
4. `WashTank_screen_process_engine_map.md`

이 순서는:

- 프로그램이 무엇을 하려는지
- 공정이 어떻게 이어지는지
- 화면이 어떤 역할로 나뉘는지
- 한눈에 보는 매핑표

까지 빠르게 잡는 데 좋다.

## 2. 엔진 관점으로 읽고 싶은 경우

`WashTank`를 화면보다 엔진과 상태 전이 중심으로 보고 싶다면 아래 순서가 좋다.

1. `WashTank_engine_and_data.md`
2. `WashTank_jms_screen_connection.md`
3. `WashTank_screen_process_engine_map.md`
4. `WashTank_glossary.md`

이 순서는:

- 탱크 / 상태 / 작업 / 이벤트 / 위치 구조를 먼저 보고
- 화면이 `JMS`와 어떻게 붙는지 본 뒤
- 용어를 다시 고정하는 데 좋다.

## 3. 만드는 과정의 흔적을 읽고 싶은 경우

`WashTank`를 완성품이 아니라
만들어지던 과정의 폴더로 읽고 싶다면 아래 순서가 좋다.

1. `WashTank_build_traces.md`
2. `WashTank_screen_creation_reasons.md`
3. `WashTank_timeline_guess.md`
4. `WashTank_overview.md`

이 순서는:

- 왜 이 폴더가 아카이브처럼 보이는지
- 각 화면이 왜 생겼는지
- 어떤 순서로 분화되었는지

를 읽는 데 맞다.

## 4. 화면만 빠르게 잡고 싶은 경우

실제 JSX 파일을 보기 전에
어느 화면이 무엇인지 빠르게 잡고 싶다면 아래 순서가 좋다.

1. `WashTank_screen_roles.md`
2. `WashTank_screen_creation_reasons.md`
3. `WashTank_screen_process_engine_map.md`

이 순서는 사무실 / 현장 / 장비기사 / 래퍼 화면을 빠르게 구분하는 데 좋다.

## 5. 용어가 헷갈릴 때

중간에 용어가 흔들리면 바로 아래 문서로 돌아오면 된다.

- `WashTank_glossary.md`

이 문서는 정답 사전이 아니라,
현재 `WashTank`를 읽을 때 기준을 잡아주는 해석 틀이다.

## 6. 추천 묶음

### A. 빠른 이해 묶음

- `WashTank_overview.md`
- `WashTank_process_flow.md`
- `WashTank_screen_process_engine_map.md`

### B. 엔진 이해 묶음

- `WashTank_engine_and_data.md`
- `WashTank_jms_screen_connection.md`
- `WashTank_glossary.md`

### C. 과정 복원 묶음

- `WashTank_build_traces.md`
- `WashTank_screen_creation_reasons.md`
- `WashTank_timeline_guess.md`

## 7. 이 가이드의 의미

`WashTank`는 코드와 md가 섞여 있고,
화면도 많고,
엔진과 역할 분해가 함께 들어 있어서
무작정 읽으면 오히려 흐름이 잘 안 잡힌다.

이 가이드는 그걸 막기 위해,
지금 어떤 관점으로 읽을지 먼저 정하게 해주는 문서다.

즉 이 문서는 요약 문서가 아니라
`md_maker` 전체를 읽는 입구 역할을 한다.

## 한 줄 정리

`WashTank`는 한 가지 방식으로만 읽는 폴더가 아니기 때문에,
개요 / 엔진 / 과정 / 화면 중 어떤 관점으로 읽을지 먼저 고르고 들어가는 편이 가장 낫다.
