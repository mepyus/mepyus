# doc_002 Analysis

## 적합성 판단

- 비교 실험용 입력으로 적절하다.
- 설명형 문서라서 `scene`, `role`, `anchor`의 수렴/분기를 보기 쉽다.
- 정의 -> 프레임워크별 SDK 방식 -> 통합 비용 문제 -> MCP 해법 으로 흐름이 분명하다.

## Codex 기준선 절단 판단

### fragment 1
- 범위: Agent 구현에 프레임워크가 필요한 이유와 대표 프레임워크 소개
- 중심 움직임: `agent framework 필요성 설명`

### fragment 2
- 범위: 각 프레임워크가 자체 Tool SDK를 제공하는 방식 설명
- 중심 움직임: `framework-specific sdk 구조 설명`

### fragment 3
- 범위: 개별 SDK 연동 방식의 운영 부담 설명
- 중심 움직임: `integration burden 문제 제기`

### fragment 4
- 범위: MCP를 표준 프로토콜 해법으로 제시
- 중심 움직임: `mcp standardization solution 제시`

## 관찰 포인트

- 처리자마다 `SDK`, `Tool`, `Integration`, `Protocol`을 anchor로 어떻게 잡는지 차이가 날 가능성이 높다.
- `scene`은 대체로 `explanation`에 수렴하겠지만, 마지막 단락은 `comparison`이나 `instruction` 쪽으로 갈릴 수 있다.
- `role`은 앞단은 `definition` 또는 `support`, 후반 문제 단락은 `problem`, 마지막 단락은 `bridge`나 `expansion`으로 갈릴 가능성이 있다.
