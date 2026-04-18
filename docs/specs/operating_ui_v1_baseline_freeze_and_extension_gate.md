# operating ui v1 baseline freeze and extension gate

## 1. purpose

이 문서는 현재까지 닫힌 operating UI를
**배포 가능한 read-only baseline v1**으로 고정하고,
이후 어떤 변경이 safe refinement이고,
어떤 변경이 guarded extension이며,
어떤 변경이 baseline-changing work인지 경계를 잠그는 문서다.

이 문서는 새 기능 제안 문서가 아니라
기준선 보호 문서다.

## 2. canonical references

이 freeze 문서는 아래 canonical reference 위에서만 해석한다.

1. [operating_ui_vocabulary_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_ui_vocabulary_lock_v1.md)
2. [operating_ui_state_axis_stabilization_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_state_axis_stabilization_v1.md)
3. [operating_ui_legacy_wording_reconciliation_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_legacy_wording_reconciliation_v1.md)
4. [operating_ui_canonical_reading_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_canonical_reading_note_v1.md)

## 3. freeze summary

### current baseline identity

현재 baseline은:
- `viewer_server` 위에 올라간
- `runtime process-console payload -> adapter -> read-only components`
흐름의
- **3영역 read-only operating shell**
이다.

즉 이 baseline은:
- page shell 완성본이 아니다
- modal/action workflow가 아니다
- write-capable operating console이 아니다

현재 고정된 baseline 정의:
- `Live Control Bar`
- `Derived State Strip`
- `Asset State Board`
- `Selected Detail Summary`
- `Activity Panel`
- controlled unavailable path

### current scope

현재 scope는 아래까지만 포함한다.

- selected asset query navigation
- runtime live read-only composition
- invalid query fallback-selected handling
- controlled `live_unavailable` path
- vocabulary/state-axis stabilized helper text
- SSR 기반 lightweight layout

### in-scope surfaces

- `/operating-ui-live`
- `/api/operating-ui-live`
- query param:
  - `asset_id`
  - `sort_by`
  - `live_mode=unavailable` (controlled validation path)

### explicitly out of scope

- modal
- feedback input
- write/action capability
- realtime/websocket
- search/filter semantics 확장
- deep routing
- client-heavy interaction
- drag/drop
- React/SPA migration
- raw payload direct read by components

## 4. locked semantics

다음 semantics는 baseline에서 고정한다.

### state axes

#### selection_query_state
- `default_selected`
- `valid_asset_id`
- `invalid_selected_asset_query`
- `no_selected_asset`
- `empty_assets`

#### live_availability
- `live_ready`
- `no_selected_asset`
- `empty_board`
- `state_unavailable`
- `live_unavailable`

원칙:
- `selection_query_state`는 query 해석 결과만 의미한다
- `live_availability`는 live source/readiness 상태만 의미한다
- 두 축은 가능하면 orthogonal하게 유지한다

### surface responsibility

- `Live Control Bar`
  - query 해석
  - requested/current shown/fallback 관계
  - live source 상태
- `Derived State Strip`
  - selected asset 핵심 상태 요약
- `Selected Detail Summary`
  - selected asset richer summary
  - `fallback-selected asset` badge 허용
- `Activity Panel`
  - activity/history fallback만 담당

원칙:
- strip/detail/activity는 query 오류의 주 설명면이 아니다
- query/live 오류 의미를 분산시키지 않는다

### controlled unavailable path position

`live_mode=unavailable`는:
- 일반 live route를 대체하지 않는다
- 실제 runtime failure injection이 아니다
- baseline의 unavailable fallback을 검증 가능한 경로로 재현하는
  **controlled validation path**다

validation-only controlled path 원칙:
- `live_mode`
- `compare_mode`
는 일반 운용 기능이 아니라 validation-only override다
- unknown 값은 baseline 동작으로 안전하게 내려와야 한다

## 5. locked vocabulary

다음 vocabulary는 baseline에서 고정한다.

- `requested asset`
- `current shown asset`
- `fallback-selected asset`
- `selected asset`
- `live source unavailable`
- `selected asset has no canonical state yet`
- `history unavailable`
- `empty board`

원칙:
- 새 문서는 [operating_ui_vocabulary_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_ui_vocabulary_lock_v1.md) 기준을 따른다
- historical wording은 reference-only다

## 6. what counts as baseline change

### safe refinement

아래는 baseline을 바꾸지 않는 refinement다.

- helper/notice wording polish
- quiet badge wording polish
- fallback copy consistency 정리
- report/spec reconciliation
- layout spacing/read order 수준의 lightweight refinement
- controlled validation note 추가

조건:
- semantics unchanged
- vocabulary unchanged
- state axes unchanged
- route/query contract unchanged

### guarded extension

아래는 baseline을 직접 깨지는 않지만,
review 없이 붙이면 baseline 의미를 흔들 수 있는 작업이다.

- 새 read-only panel 추가
- live route/query contract touch
- builder/adapter contract touch
- selected asset source rule 조정
- board/detail/activity 정보 범위 확장
- controlled unavailable path의 의미 확장

조건:
- 별도 review가 필요하다
- baseline을 유지할지, v1.1 refinement인지, baseline change인지 먼저 판정해야 한다

### baseline-changing work

아래는 baseline 변경으로 본다.

- write/action capability
- feedback persistence
- realtime/websocket
- search/filter semantics 확장
- client-heavy interaction
- React/SPA migration
- modal을 primary reading surface로 승격
- raw payload direct read by components
- state axis / vocabulary 재정의
- query selection semantics 변경

원칙:
- 이 계열은 safe refinement로 포장하지 않는다
- 별도 baseline revision 또는 v2 proposal로 다룬다

## 7. extension gate summary

### gate A. safe refinement

허용:
- wording polish
- helper/badge quiet polish
- docs/reports reconciliation

기준:
- same behavior
- same semantics
- same contracts

### gate B. guarded extension

허용 가능하나 사전 판정 필요:
- new read-only panel
- route/query contract touch
- builder/adapter contract touch

질문:
- 기존 3영역 shell을 흐리게 하는가
- raw payload와 component 경계를 흔드는가
- current shown asset / selected asset 책임을 섞는가

### gate C. baseline-changing work

즉시 baseline 밖으로 분류:
- write/action
- realtime
- search/filter semantics
- client-heavy interaction
- raw payload direct read

## 8. backlog summary

### small refinements available now

1. control bar/status line의 소음 줄이기
2. legacy docs reconciliation note 보강
3. unavailable path wording consistency 재점검

### guarded review candidates

1. read-only compare candidate panel 추가
2. minimal selected detail meta refinement
3. adapter/model contract의 작은 field normalization 확장

### hold outside baseline

1. modal/detail explorer
2. feedback/write flow
3. live search/filter interaction

## 9. reading rule

제3자가 operating UI를 읽을 때는 아래 순서를 따른다.

1. current baseline freeze 문서
2. vocabulary lock
3. state axis stabilization
4. legacy wording reconciliation
5. historical reports

즉:
- 이 문서는 현재 baseline의 가장 바깥 경계다
- historical report보다 우선한다

## 10. limitations

- 이 freeze는 v1 read-only baseline을 고정하는 문서다
- future extension의 세부 설계 문서는 아니다
- guarded extension이 실제로 들어갈 때는 별도 proposal이 필요하다
