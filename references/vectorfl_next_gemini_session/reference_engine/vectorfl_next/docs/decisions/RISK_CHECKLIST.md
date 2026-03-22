# Risk Checklist

새 코드를 넣기 전 아래를 먼저 본다.

## Collapse risk

- `material`이 너무 빨리 point처럼 다뤄지고 있지 않은가
- `point_seed`가 사실상 final point처럼 무거워지지 않았는가
- `space_cell`이 cluster candidate처럼 읽히지 않는가
- `bridge_trace`가 merge trigger처럼 작동하지 않는가

## Vocabulary risk

- spine / basin / leak / return 같은 reader 단어가 core field로 들어오지 않았는가
- observer language가 ontology처럼 굳지 않았는가
- source_type taxonomy가 formation role보다 앞서지 않았는가

## Runtime risk

- 상태 전이가 append-only event로 남는가
- 현재 상태와 이력 저장이 분리되는가
- lineage와 reentry 자리가 남아 있는가

## Reference misuse risk

- `vectorfl`의 stage 구조를 이름만 바꿔 가져오지 않았는가
- candidate/point/cluster semantics를 그대로 옮기지 않았는가

## Decision rule

하나라도 애매하면 바로 구현하지 말고 decision 문서를 추가한다.
