# Pressure Transition Observer Policy

## Decision

observer는 pressure signature의 분포뿐 아니라 signature 사이의 전이 빈도도 읽을 수 있어야 한다.

## Current rule

- reaction sequence에서 연속된 pressure signature 쌍을 센다.
- axis 이름 조합도 함께 모아 반복되는 pressure combination을 보여준다.

## Why

- 공간 변화는 어떤 압력장이 얼마나 많았는지뿐 아니라 어떤 압력장에서 다른 압력장으로 넘어갔는지에도 드러난다.
- axis combination은 signature 한 줄보다 더 빠르게 구조를 읽게 해준다.

## Follow-up risk

- 현재 전이는 단순 연속 쌍 빈도다.
- 다음 단계에서 reaction kind와 pressure transition을 같이 묶어 읽을 수 있다.
