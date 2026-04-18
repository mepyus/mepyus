# multi_lens_input_to_reading_organ_basis_quality_refinement_spec_v0

## verdict

- `input_to_reading_organ` basis quality refinement target is locked as a bounded spec asset
- this refinement path is limited to basis quality only
- this turn does not change runtime code, operating state, or heuristic scope

## current weakness summary

현재 `line_input_to_reading_organ` 축의 약점은 basis quality 쪽에 있다.

관찰된 상태:

- `reading_basis`가 partial match 설명에 자주 머문다
- `low linkage_confidence` downgrade 설명이 반복적으로 나온다
- basis 문장이 왜 해당 결과가 나왔는지 최소 설명은 하지만, operator가 evidence density를 빠르게 판독하기에는 아직 얇다
- active axis이긴 하지만 current basis quality만으로 richer interpretation을 열 수는 없다

정리:

- 현재 문제는 maturity 부족을 판정하는 것이 아니다
- 현재 문제는 basis wording과 evidence description clarity가 아직 제한적이라는 것이다

## allowed refinement target

이번 refinement branch에서 허용되는 대상은 아래로 한정한다.

### basis wording quality

- `reading_basis` 문장을 더 직접적이고 읽기 쉽게 만드는 것
- partial match / no relevant seed / low-confidence downgrade의 이유를 더 분명히 쓰는 것
- operator가 current output의 explanation quality를 더 빨리 판독할 수 있게 만드는 것

### evidence description clarity

- 어떤 seed, phrase, or basis cue가 실제로 걸렸는지 더 명확히 드러내는 것
- 무엇이 있었고 무엇이 부족했는지 설명을 더 선명하게 만드는 것
- current explanation을 observation quality 수준에서만 다듬는 것

### confidence guard tightening

- low-confidence downgrade 설명이 더 보수적이고 명확하게 보이도록 wording을 다듬는 것
- weak 판정을 strong처럼 오해하지 않도록 basis 문장 경계를 더 분명히 하는 것
- confidence handling의 설명 강도를 조정하는 것

주의:

- 여기서 말하는 confidence guard는 scoring layer가 아니다
- basis wording과 explanation clarity를 더 보수적으로 만드는 범위만 허용한다

## prohibited interpretations

아래 해석은 금지다.

- `active != maturity`
- `weak != promotion evidence`
- refined basis `!=` state promotion
- clearer basis `!=` line thickness increase
- basis refinement `!=` operating anchor readiness

정리:

- 이번 branch는 readout explanation quality branch다
- governance, maturity, promotion branch가 아니다

## bounded refinement scope

범위는 아래로 고정한다.

- `input_to_reading_organ` only
- `reading_basis` wording quality
- evidence description clarity
- low-confidence explanation guard

범위 밖:

- `transition_over_surface` reopening 금지
- 다른 line으로의 refinement 확장 금지
- artifact contract 변경 금지
- active / parked / candidate state 변경 금지

## explicit non-goals

- no scoring
- no candidate promotion
- no auto state transition
- no maturity judgment
- no parked-axis reopening
- no transition_over_surface refinement in this branch
- no hidden decision logic

## patch reopen condition

actual runtime patch는 아래 조건이 충족된 뒤에만 연다.

- this spec is locked
- proposed change가 `input_to_reading_organ` basis quality improvement로만 설명 가능하다
- proposed change가 maturity, promotion, parked-axis governance를 건드리지 않는다
- proposed change가 wording/evidence explanation scope를 넘지 않는다

reopen rule:

- 위 조건을 만족하지 못하면 runtime patch를 열지 않는다
- patch proposal이 basis quality branch인지 먼저 판정한 뒤에만 진행한다

## technical summary

- `input_to_reading_organ` current weakness is basis thinness, not maturity uncertainty
- allowed refinement target is limited to explanation quality, evidence clarity, and low-confidence wording guard
- active axis라는 이유로 promotion/maturity branch를 열면 안 된다
- runtime patch는 이 spec lock 이후에만, 그리고 basis quality 범위 안에서만 열 수 있다

## user-language summary

- 지금 손볼 수 있는 건 `input_to_reading_organ`의 "설명 문장 품질"뿐이다
- 이 line이 active라고 해서 더 성숙했다거나 올려도 된다는 뜻은 아니다
- `weak`가 많이 보인다고 promotion 근거가 되는 것도 아니다
- 다음 patch를 열더라도, 이번에는 basis를 더 읽기 좋게 만드는 정도까지만 허용된다

## close-out

- future supervisor는 이제 proposed change가 genuinely basis quality improvement인지 판정할 수 있다
- architecture debate, promotion debate, parked-axis debate는 이 branch에서 다시 열지 않는다
- `input_to_reading_organ` basis quality refinement는 여기서 bounded branch로만 연다
