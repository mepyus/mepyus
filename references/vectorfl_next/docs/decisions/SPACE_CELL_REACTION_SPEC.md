# Space Cell Reaction Spec

## Decision

`space_cell`의 살아 있음은 반응 이벤트로 남겨야 한다.
이번 단계에서는 `thickening`, `split`, `relocation`을 append-only reaction event로 기록한다.

## Reaction meanings

- `thickening`
  - recurrence와 결속이 두꺼워지는 반응
  - 기본 cell state는 `held`로 이동한다
- `split`
  - 내부 긴장과 경계 증폭으로 하나의 cell 유지가 흔들리는 반응
  - 기본 cell state는 `unstable`로 이동한다
- `relocation`
  - 기존 cell의 주 결속에서 실질적으로 이탈하는 반응
  - 기본 cell state는 `reentering`으로 이동한다

## Event rule

- 반응은 `space_cell_reacted` 이벤트로 남긴다.
- payload에는 `reaction_kind`, `pressure_profile_id`, `triggered_by_seed_ids`, `note`를 남긴다.
- 반응은 reader 해석이 아니라 코어 내부 구조 변화 흔적이다.

## Local space implication

- `relocation` 반응이 포함된 cell 조합은 `bridge_exposed`로 본다.
- `split` 반응이 포함된 cell 조합은 `boundary_heavy`로 본다.
- shared boundary tendency와 반응 이력이 함께 있을 때 `stable_local`까지 갈 수 있다.

## Follow-up risk

- 현재 local space 판정은 반응 종류 우선 규칙이라 단순하다.
- 다음 단계에서 recurrence density와 bridge exposure intensity를 함께 봐야 한다.
