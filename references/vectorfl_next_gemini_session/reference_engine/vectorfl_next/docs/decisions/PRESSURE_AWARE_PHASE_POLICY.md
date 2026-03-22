# Pressure-Aware Phase Policy

## Decision

phase compression은 reaction kind뿐 아니라 pressure signature 변화도 phase 경계로 본다.

## Current rule

- 연속된 event라도 pressure signature가 달라지면 새 phase를 연다.
- 따라서 같은 `thickening`이라도 압력장이 달라지면 다른 국면으로 읽는다.

## Why

- 공간 국면은 반응 종류만으로는 충분히 읽히지 않는다.
- 압력장이 달라지면 같은 반응도 다른 phase일 수 있다.

## Follow-up risk

- 현재는 signature bucket이 거칠다.
- 다음 단계에서 duration-based recent window를 추가하면 phase 변화 읽기가 더 자연스러워질 수 있다.
