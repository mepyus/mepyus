# stage1_space_readability_bounded_attachment_plan_v1

## 목적
현재 엔진 코어를 흔들지 않고
탐색/응결핵/관계 판독에 필요한 최소 보조 관찰층을 어디에 어떻게 붙일지 제안한다.

## attachment principle
- core rewrite 금지
- existing pointer/evidence/provenance/session 구조 재사용
- observation-like sidecar 우선
- 사용자 언어 설명 포함

## 1. recommended attachment A — exploration observation note
- target:
  - `runtime/observer/exploration/YYYY-MM-DD/`
- shape:
  - md note
- purpose:
  - 새 입력 1건을 기존 자산과 비교한 관계 판독 결과를 사용자 언어로 남김
- why good:
  - observer lane 성격과 맞고, session/run/pointer를 이미 붙일 수 있다.

## 2. recommended attachment B — exploration relation sidecar json
- target:
  - `runtime/observer/exploration/YYYY-MM-DD/`
- shape:
  - `exploration_<input_slug>_<session_or_run>.json`
- purpose:
  - `relation_kind`, `focus_anchor`, `related_assets`, `borrowable_structure` 같은 구조화 필드 저장
- why good:
  - 나중 검색/페이지 구성 시 md보다 재사용성이 높다.

## 3. recommended attachment C — note template
- target:
  - `docs/templates/stage1_exploration_observation_note_template_v1.md`
- purpose:
  - 사람이 exploration note를 쓸 때 빠지기 쉬운 relation reason / future use hint / not adopted reason을 강제

## 4. recommended attachment D — guide-level read contract
- target:
  - `docs/guides/`
- purpose:
  - 나중 page-first로 흐르지 않게 “탐색 결과는 어떤 읽기면이어야 하는가”를 사용자 문체로 고정
- note:
  - 이번 턴에는 template까지만 있어도 충분하다.

## preferred record targets
1. primary:
  - `runtime/observer/exploration/...`
2. secondary:
  - 관련 receipt 또는 per-run board pointer
3. tertiary:
  - reports/guides/contracts에 정리된 long-form reflection

## not recommended now
- receipt 본문에 relation block를 직접 넣기
- provenance index schema에 relation_reason을 바로 넣기
- latest board를 relation dashboard로 확장하기

## one-line plan
현재 단계의 가장 좋은 부착 방식은
**runtime observer 아래 exploration sidecar를 두고, 문서 템플릿으로 relation reasoning을 표준화하는 것**이다.
