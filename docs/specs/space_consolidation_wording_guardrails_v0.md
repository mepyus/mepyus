# space consolidation wording guardrails v0

## purpose

이 문서는 space consolidation 계열 문서가 `관찰 압축`을 넘어서 `완결 아키텍처 선언`처럼 과장되지 않도록 wording 규칙을 잠그기 위한 것이다.

## approved wording

- `현재 잠금 가능한 관찰면`
- `distributed organ`
- `중첩 boundary`
- `append-only 우선`
- `mixed hold 보호`
- `active surface 보호`
- `reference native reading first`
- `line과 non-line unit이 함께 작동한다`

## avoid wording

- `완결된 구조`
- `최종 아키텍처`
- `중앙 통제 모듈`
- `명확히 분리된 층`
- `이미 고정된 기관 체계`
- `flow line으로 확정되었다`
- `line만이 중심 단위다`

## status wording rules

- `explicit strong`
  - 여러 문서와 runtime surface에서 반복적으로 드러나고, 실제 ledger/profile/summary layer까지 갖춘 경우에만 쓴다.
  - 현재는 `기록기억기` 같은 축에만 조심스럽게 사용한다.
- `distributed strong`
  - 단일 파일/모듈은 없지만, 여러 문서/스크립트/surface에 걸쳐 역할이 일관되게 관찰될 때 쓴다.
  - strong이지만 `single organ`처럼 말하지 않는다.
- `partial candidate`
  - 존재 흔적은 분명하지만 아직 상시 기관처럼 잠그기 이른 경우에 쓴다.
  - `emerging`, `보이기 시작함`, `후보` 같은 표현과 함께 쓴다.
- `weak cue`
  - 개념적 신호는 있으나 역할 단위로 말하기 아직 약할 때 쓴다.
- `absent`
  - 다른 가능성(`distributed`, `partial`, `weak`)을 먼저 검토한 뒤 마지막에만 쓴다.

## boundary wording rules

- boundary는 `완전 분리`보다 `중첩된 경계 읽기`로 쓴다.
- `baseline / operating / ledger / active surface / reference`는 층이지만, 실제 구현에서는 겹친다는 점을 함께 적는다.
- `active surface`는 현재 읽기면이자 보호 대상이라고 쓴다.
- `ledger`는 overwrite 금지보다 `append-only 우선`으로 쓴다.
- `reference layer`는 `외부를 내부로 평탄화하지 않음`을 같이 적는다.

## governance wording rules

- governance는 `중앙 규율 시스템`보다 `분산된 stop points`로 쓴다.
- 반드시 다음 어휘를 우선한다:
  - `mixed hold`
  - `observer-only`
  - `promotion 금지`
  - `next check trigger`
  - `append guard`
- `멈춘다`고 쓸 때는 가능한 한 `무엇이 / 어디서 / 왜` 멈추는지 함께 적는다.
- governance를 line 승격만의 문제로 축소하지 말고, event/hint/phase/surface/residue/trace까지 포함하는 리듬으로 쓴다.

## line vs non-line wording rules

- `line 중심`은 유지하되 `line only`처럼 쓰지 않는다.
- 가능하면 다음 표현을 같이 둔다:
  - `fragment`
  - `event`
  - `hint`
  - `phase`
  - `surface`
  - `residue`
  - `trace`
- line을 설명할 때 다른 first-class unit을 지우지 않는다.
- `line family / projection / route`를 말할 때도, 그것이 artifact/hint/phase/surface를 통해 작동한다는 문장을 함께 둔다.

## final rule

이 계열 문서는 `설계 확장`이 아니라 `관찰 압축`으로 쓴다.  
따라서 가장 안전한 문장 규칙은 다음이다.

- `이미 존재하는 것을 짧게 잠근다`
- `강한 것과 약한 것을 섞어 과장하지 않는다`
- `분산된 것을 분산된 채로 적는다`
- `완결 구조처럼 쓰지 않는다`
