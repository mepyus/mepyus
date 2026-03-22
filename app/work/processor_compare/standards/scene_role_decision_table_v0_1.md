# Scene Role Decision Table v0.1

빠른 판정을 위한 축약 표다.
애매하면 이 표를 먼저 보고, 그래도 애매하면 `calibration_guardrails_v0_1.md`를 본다.

## 기본 매핑

| 문단 성격 | scene | role | 비고 |
| --- | --- | --- | --- |
| 개념 직접 정의 | explanation | definition | `scene=definition` 금지 |
| 사례 소개 | explanation | example | `scene=example` 금지 |
| 문제 진단 | explanation | problem | 한계/부담/실패 |
| 핵심 주장 | explanation | thesis | 결론/중심 메시지 |
| 비교 전환 | comparison 또는 explanation | bridge | 비교 도입이면 comparison 우선 |
| 비교 본문 | comparison | support 또는 contrast | 직접 대비 구조 |
| 절차 설명 | explanation | support 또는 expansion | `scene=process` 금지 |
| 활용 확장 | explanation | expansion | 응용/전망 |
| 메타 총평 | reflection | meta | 진짜 메타일 때만 |
| 실험/사례 근거 | evidence | support 또는 example | 실제 결과/근거 제시 |

## 금지 매핑

- `scene=definition`
- `scene=example`
- `scene=process`
- `scene=thesis`
- `scene=support`

## 빠른 예시

- `Object Type은 ... 비즈니스의 최소 단위다`
  - `scene=explanation`
  - `role=definition`

- `NASA 사례에서는 ... 추천이 가능하다`
  - `scene=explanation`
  - `role=example`

- `기존 시스템은 사일로라 수작업이 필요하다`
  - `scene=explanation`
  - `role=problem`

- `Graph RAG는 이런 한계를 보완한다`
  - `scene=explanation`
  - `role=thesis` 또는 `role=bridge`

- `이제 Vector RAG와 Graph RAG를 비교해보자`
  - `scene=comparison`
  - `role=bridge`

- `링크는 AI reasoning의 의미 연결선이다`
  - 기본은 `scene=explanation`, `role=expansion`
  - 정말 한 단계 위 총평이면만 `scene=reflection`, `role=meta`
