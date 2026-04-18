# multi lens document reading v0 strength patch note

## Purpose

이 note는 stable/thick 두 lens에 한해서
keyword seed와 `reading_basis` 문장을 bounded refinement 한 범위를 기록한다.

## What changed

- `line_input_to_reading_organ`
  - 단독 `입력`, 단독 `읽기`만으로 바로 `strong`이 되지 않도록
    strong seed를 더 조합형 표현으로 좁혔다
  - 일반 표현은 partial match로만 남겨 `weak` 쪽으로 내릴 수 있게 했다

- `line_transition_over_surface`
  - 너무 좁던 starter seed를 조금 넓혀
    `표면 전환`, `surface transition`, `transition over surface` 같은 설명 가능한 조합을 받게 했다
  - `전환`과 `표면`이 함께 있는 조합도 strong 후보로 열었다
  - 단독 `표면`만으로 strong을 주지는 않는다

- `reading_basis`
  - `strong`: `matched seed: ...; primary stable/thick lens basis`
  - `weak`: partial match 또는 low-confidence downgrade를 직접 적는다
  - `absent`: `no relevant seed / no basis`를 직접 적는다

## Why

- `input_to_reading_organ`의 over-trigger 가능성을 줄이기 위해
  일반 표현을 partial 쪽으로 이동시켰다
- `transition_over_surface`의 under-reading 상태를 줄이기 위해
  설명 가능한 조합형 seed를 조금 넓혔다

## What did not change

- scoring formula 추가 없음
- aggregation 구현 없음
- candidate/thin lens actual application 확대 없음
- line registry 수정 없음

## Next step

다음 단계는 validation 결과를 보고 stable/thick 두 lens의 partial match 경계만 더 좁게 읽는 것이다.
