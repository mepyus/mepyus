# Duration Window Policy

## Decision

recent observation은 event count뿐 아니라 duration 기준으로도 잘라 읽을 수 있어야 한다.

## Current rule

- `recent_seconds`를 주면 현재 시각 기준 최근 N초 안의 reaction event만 읽는다.
- 이 필터는 count-based recent limit과 함께 사용할 수 있다.

## Why

- 최근 10개 반응보다 최근 10분의 반응이 더 자연스러운 시간 감각을 줄 수 있다.
- 시간성은 필드보다 관찰 창으로 먼저 다루는 편이 공간 기준에 맞다.

## Follow-up risk

- 현재는 seconds 단위만 있다.
- 다음 단계에서 분/시간 단위 shortcut이나 richer time windows를 추가할 수 있다.
