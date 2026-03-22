# mixed reentry compare board

## 1. 어떤 mixed들이 재진입 신호를 받았는가
- total candidates: `6`
- matched candidates: `6`
- strength counts: `{'meaningful': 1, 'strong': 4, 'weak': 1}`

## 2. 어떤 transition corridor가 반복적으로 다시 붙는가
- `technical->organization`: `5`
- `technical->business`: `1`

## 3. 어떤 mixed는 재등장해도 거의 강화되지 않는가
- `weak` reentry는 anchor family는 비슷하지만 arrival axis 보강이 부족한 경우다.

## 4. good_hold의 실제 증거
- reentry strength가 `meaningful` 또는 `strong` 이면 hold 가치가 사후적으로 확인된 것으로 본다.

## 5. 보류의 가치가 증명된 경우 / 아직 보류만 된 경우
- retention confirmed yes: `5`
- retention confirmed partial: `1`

## 6. canonical 승격 후보가 있는가
- 이번 stage1에서는 `stable_closure_reached` 는 없음
- 일부 corridor는 `closure_partially_strengthened` 까지는 갔지만 여전히 hold가 맞다

## 7. 아직 승격하면 안 되는 이유
- re-entry는 보였지만 stable closure reached 증거는 없다
- 강화와 승격을 구분해야 한다
