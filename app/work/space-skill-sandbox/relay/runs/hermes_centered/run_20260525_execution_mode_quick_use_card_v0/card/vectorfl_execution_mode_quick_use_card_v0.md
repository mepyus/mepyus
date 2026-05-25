# VectorFL 실행모드 quick use card v0

상태: candidate / NOT_AUTHORITY
작성일: 2026-05-25T20:57:52.666307+09:00

## 한 줄 규칙

사용자가 `실행모드`라고 명시하면 Hermes는 VectorFL 공간을 읽고 활용만 한다. 공간을 수정, 구조화, 연결, 승격하지 않는다.

## 왜 필요한가

실행모드는 스킬처럼 짧게 붙여 쓰는 모드다.

예:

```text
실행모드: 이 자료 바탕으로 답해줘
실행모드로 처리해줘
실행모드. 공간은 참고만 하고 실행해
```

이렇게 하면 Hermes는 이미 만들어 둔 map, card, guide, closeout을 참고만 하고, 새 공간 산출물을 만들지 않는다.

## 속도가 빨라지는 이유

- 새 pointer/map/view를 매번 만들지 않는다.
- workspace validation/receipt를 매번 생성하지 않는다.
- 공간 설계와 실제 실행을 섞지 않는다.
- 이미 만든 read-first surface만 골라 빠르게 활용한다.

## 허용

- 기존 VectorFL 자산 읽기
- 기존 map/card/receipt를 판단 근거로 활용
- 사용자가 요청한 실제 작업 수행
- 명시된 output만 작성
- 필요하면 어떤 공간을 참고했는지 짧게 언급

## 금지

- workspace/space asset 수정
- 새 pointer/map/schema/card 생성
- VectorFL 공간 재구조화
- candidate/matured/authority 승격
- registry/current-position mutation
- move/archive/delete/source edit
- 별도 scope 없는 live external call

## 멈춤 규칙

실행 중 공간을 수정해야 할 필요가 생기면 자동으로 진행하지 않는다.

그때는:

```text
이 작업은 실행모드 밖의 공간 설계/수정 작업입니다. HOLD.
```

라고 표시하고 멈춘다.

## 현재 상태

이 카드는 아직 Hermes skill이 아니다.
workspace-internal candidate다.
나중에 사용자가 원하면 skill/prompt snippet으로 승격할 수 있다.
