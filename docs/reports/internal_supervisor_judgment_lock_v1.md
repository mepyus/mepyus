# internal supervisor judgment lock v1

## 1. 목적

이 문서는 오늘의 최종 판단을 내부 감독 기준으로 잠그기 위한 기록이다.

핵심은 단순 요약이 아니라, 앞으로 무엇을 먼저 하고 무엇을 아직 열지 말아야 하는지를 명확히 남기는 것이다.

## 2. 잠근 판단

현재까지 만든 공간은 맞는 방향으로 가고 있다.

잠긴 축은 다음과 같다.

- control plane
- breadcrumbs
- latent line first
- candidate / boundary / watch rule
- phase transition + hold
- tension / rejection / external intake awareness

이들은 모두 읽기, 재독해, 판단 흔적화, 성급한 승격 방지를 다루는 장치들이다.

즉 지금의 중심은 `읽기 질서 / 재독해 질서 / 판단 흔적화 구조`다.

## 3. 아직 자동으로 열리지 않는 것

읽기 공간이 성숙했다고 해서 곧바로 Claude Code 구현 단계가 열리지는 않는다.

구현 단계에서는 질문이 바뀐다.

- 무엇을 먼저 읽을 것인가
- 어떤 선이 짙어졌는가
- 무엇을 후보로 볼 것인가

에서

- 이 개념을 코드에서는 어떤 구조로 내릴 것인가
- 구현 drift를 어떻게 막을 것인가
- 의도대로 구현됐는지를 무엇으로 판정할 것인가

로 바뀐다.

따라서 별도의 구현 하강층이 필요하다.

## 4. 지금 추가로 필요한 3축

### 4.1 concept_to_implementation_map_v0

필요한 이유:

- latent line, breadcrumb, candidate, phase, watch rule 같은 개념 언어를
  데이터 모델, 함수, 상태머신, 이벤트 로그, 트리거, 서비스, UI surface 같은 구현 언어로 내려야 한다.
- 이 매핑이 없으면 구현은 자기식 해석으로 drift하기 쉽다.

역할:

- 공간 언어를 구현 언어로 투영하는 공식 사상표

### 4.2 build_drift_anchor_v0

필요한 이유:

- 구현 작업은 긴 턴으로 흐르기 쉽고, 의도 drift가 쉽게 생긴다.
- 시작 전에 핵심 목적, 하지 않을 것, 중간 점검 질문을 고정해야 한다.

역할:

- 구현용 pre-read eye
- build 전에 방향을 먼저 고정하는 장치

### 4.3 implementation_eval_criteria_v0

필요한 이유:

- 코드가 동작하는 것과 의도대로 구현된 것은 다르다.
- phase transition, hold, boundary, watch rule 같은 규칙은 의도 적합성까지 판정해야 한다.

역할:

- 구현이 “돌아간다”를 넘어 “의도대로 구현됐다”를 판정하는 기준

## 5. 현재 우선순위

1. `concept_to_implementation_map_v0`
2. `build_drift_anchor_v0`
3. `implementation_eval_criteria_v0`

이 순서가 필요한 이유:

- 먼저 개념을 어떤 코드 단위로 내릴지 정해야 drift anchor와 evaluation이 정확해진다.
- 구현 하강층은 읽기 공간의 연장이 아니라 별도 층이다.

## 6. 최종 판단

- 외부 평가는 참고와 교차 검증에 좋다.
- 하지만 최종 경로 판정은 이 공간의 누적 맥락을 아는 내부 감독 판단이 맡아야 한다.

즉:

**외부 평가는 재료이고, 최종 운용 판단은 내부 감독 기준이 잡아야 한다.**

## 7. 한 줄 결론

> 지금까지의 공간은 읽기와 재독해의 공간으로는 맞게 성숙하고 있지만, Claude Code 구현을 열기 위해서는 concept_to_implementation_map, build_drift_anchor, implementation_eval_criteria라는 별도 구현 하강층이 필요하다.

