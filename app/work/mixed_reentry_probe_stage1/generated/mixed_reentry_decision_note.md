# mixed reentry decision note

## A. hold는 생산적인가
- 예. round 간 재등장으로 같은 corridor가 다시 붙는 경우가 반복적으로 보인다.

## B. 어떤 mixed가 가장 재진입 가치가 큰가
- `round1::win_02` -> `round2::win_05` / `meaningful`
- `round1::win_05` -> `round2::win_05` / `strong`
- `round1::win_06` -> `round2::win_05` / `strong`

## C. 지금 단계에서 승격 규칙을 만들면 안 되는 이유
- re-entry는 support 강화이지 stable closure reached가 아니다
- 지금은 hold 가치 확인 단계이지 승격 규칙 제정 단계가 아니다

## D. 다음 턴이 observer 확장인지, 더 많은 input 검증인지
- 다음은 더 많은 input 검증 쪽이 먼저다. 같은 corridor가 세 번째 입력에서도 다시 붙는지 봐야 한다.
