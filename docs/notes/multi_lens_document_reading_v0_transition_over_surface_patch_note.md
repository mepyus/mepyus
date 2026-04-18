# multi lens document reading v0 transition over surface patch note

## Purpose

이 note는 `line_transition_over_surface` 한정 partial-match minimal patch 범위를 기록한다.

## Why only this lens

- 최근 patch 이후 `input_to_reading_organ`은 보수화됐지만
  `transition_over_surface`는 fixture 기준으로 여전히 mostly `absent/weak`였다
- 그래서 이번 턴은 다른 lens를 다시 흔들지 않고
  `transition_over_surface` 한 축만 따로 조정했다

## Boundary changes

- `strong`
  - 조합형 seed가 분명할 때만 유지
- `weak`
  - 조합형 seed + low-confidence
  - `transition/surface` token 조합은 있으나 clear seed가 아닐 때
  - surface phrase + weak transition context가 있을 때
- `absent`
  - 단독 token
  - 설명 불가능한 약한 단일 반응

## reading_basis changes

- `strong`
  - `matched combination: ...; primary stable/thick lens basis`
- `weak`
  - partial combination 또는 low-confidence downgrade를 직접 적는다
- `absent`
  - `no relevant transition-over-surface combination seed`를 직접 적는다

## Still not done

- scoring formula 추가 없음
- aggregation 구현 없음
- candidate/thin lens actual application 확대 없음
- input_to_reading_organ 재조정 없음

## Next step

다음 단계는 validation 결과를 보고 `transition_over_surface` weak partial-match가 과한지 부족한지만 다시 좁게 보는 것이다.
