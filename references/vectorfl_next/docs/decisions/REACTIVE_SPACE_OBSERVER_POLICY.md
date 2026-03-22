# Reactive Space Observer Policy

## Decision

reactive space observer는 코어를 바꾸지 않고 현재 반응 분포를 읽는 읽기 전용 관찰 계층으로 둔다.

## Current rule

- `thickening`, `split`, `relocation` event 수를 요약한다.
- local space state 분포를 보여준다.
- bridge state 분포를 보여준다.
- 반응한 cell id들을 reaction kind별로 묶어 보여준다.

## Why

- 현재 엔진이 어떤 반응장을 만들고 있는지 빠르게 봐야 한다.
- observer는 reader와 비슷하지만 ontology를 바꾸지 않아야 한다.

## Follow-up risk

- 아직 시간 흐름이나 pressure signature 분포는 보여주지 않는다.
- 다음 단계에서 temporal observation을 추가할 수 있다.
