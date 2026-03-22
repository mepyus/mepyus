# Local Space Stability Spec

## Decision

`stable_local`은 cell 수가 아니라 boundary durability와 숙성된 경계 연속성으로 판정한다.

## Current rule

- 최소 두 개 이상의 cell이 있어야 한다.
- cell들은 shared boundary tendency를 가져야 한다.
- cell들은 모두 `held` 상태여야 한다.
- pressure signature가 동일해야 한다.
- boundary durability score가 cell 수 이상이어야 한다.
- thickening 반응은 최소 한 번 이상 있어야 한다.
- constituent cell들에 active mismatch branch가 없어야 한다.

이 조건을 만족하지 않으면:

- split 반응이 있으면 `boundary_heavy`
- relocation 반응이 있으면 `bridge_exposed`
- shared boundary만 있으면 `forming`
- 그것도 없으면 `sparse`

## Why

- 단순 count 기반 local space는 저장 묶음으로 다시 퇴행한다.
- 살아 있는 local space는 경계 유지 경도와 반응 연속성이 함께 있어야 한다.
- mismatch branch가 섞인 묶음은 아직 숙성 중인 공간이지 안정 장으로 바로 읽으면 안 된다.

## Follow-up risk

- 현재 boundary durability는 shared boundary strength와 held cell 수의 곱으로 단순 계산한다.
- 이후에는 temporal spacing과 boundary persistence decay도 함께 봐야 한다.
