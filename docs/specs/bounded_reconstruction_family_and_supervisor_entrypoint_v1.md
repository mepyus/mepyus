# bounded_reconstruction_family_and_supervisor_entrypoint_v1

## 1. purpose

- 이 문서는 `structured doc routing`, `engine state bridge`, `observer sidecar`를 하나의 `bounded reconstruction family`로 잠그기 위한 spec이다.
- 이 family의 목적은 흩어진 runtime artifact를 supervisor가 다시 읽을 수 있는 surfaced entrypoint로 묶는 것이다.
- 이 family는 새로운 governance organ이나 session product를 만드는 문서가 아니다.

## 2. family verdict

- `structured doc routing`은 reconstruction family의 intake and routing connector다.
- `engine state bridge`는 reconstruction family의 canonical state connector다.
- `observer sidecar`는 reconstruction family의 bounded observation connector다.
- 셋을 함께 읽으면 우리 repo의 `bounded reconstruction family`가 된다.

정리:

- routing은 source와 artifact를 열고
- bridge는 runtime evidence를 canonical latest로 연결하고
- sidecar는 adopt 이전의 observation hold를 남긴다

즉 이 family는
`scattered runtime evidence -> bounded surfaced reconstruction`
을 담당한다.

## 3. why this is one family

이 셋은 서로 다른 산출물을 만들지만, 같은 reconstruction 문제를 푼다.

### structured doc routing

- source doc를 받아
- receipt, board, commands, multi-lens surfaced view 같은 runtime pointer/output을 만든다
- 실제로 `runtime/receipts`, `runtime/views`, `runtime/commands`, `runtime/manifests`를 동시에 건드린다

### engine state bridge

- runtime evidence를 canonical state patch/proposal로 normalize한다
- history append와 latest regeneration으로 연결한다
- `runtime/views/engine_state_latest/`와 `runtime/views/engine_state_update_events/`를 surfaced state plane으로 유지한다

### observer sidecar

- exploration observation을 `json + md`로 남긴다
- keep / outer / defer를 bounded holding pattern으로 유지한다
- adoption 이전의 읽기 결과를 과장하지 않고 보존한다

세 connector 모두
raw trace를 그대로 던지지 않고,
operator/supervisor가 reread 가능한 surfaced artifact로 바꾼다.

## 4. family boundary

### this family owns

- runtime evidence 재구성
- source-to-artifact lineage visibility
- receipt / view / sidecar pointer bundling
- supervisor-first surfaced readout
- bounded next attention hint

### this family does not own

- governance decision
- maturity verdict
- promotion signal
- reopen trigger
- repo-wide identity/session productization
- execution authority expansion

핵심:

- 이 family는 reconstruction family다
- decision family가 아니다

## 5. current family members and their live surfaces

### routing connector

- code:
  - [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py#L34)
- main outputs:
  - `runtime/receipts/*.md`
  - `runtime/views/operation_board_latest.md`
  - `runtime/views/multi_lens_document_reading/*.json`
  - `runtime/commands/*.md`

### state bridge connector

- spec:
  - [engine_state_runtime_update_bridge_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/engine_state_runtime_update_bridge_v1.md#L1)
- main surfaced outputs:
  - `runtime/views/engine_state_latest/*.json`
  - `runtime/views/engine_state_update_events/*.json`

### observer sidecar connector

- spec:
  - [exploration_observation_sidecar_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/exploration_observation_sidecar_contract_v1.md#L1)
- main surfaced outputs:
  - `runtime/observer/exploration/json/*.json`
  - `runtime/observer/exploration/md/*.md`

## 6. supervisor-facing reconstruction problem

현재 supervisor는 아래 표면을 각각 따로 읽어야 한다.

- routing receipt
- latest operation board
- multi-lens supervisor surface
- engine state latest
- engine state update events
- exploration sidecar

이 구조는 artifact는 충분히 남기지만,
supervisor first reconstruction entrypoint는 아직 얇다.

현재 강한 점:

- receipt는 lineage와 generated file를 잘 남긴다
- views는 surfaced output을 잘 남긴다
- sidecar는 bounded exploration hold를 잘 남긴다

현재 약한 점:

- supervisor가 한 번에 읽는 recomposed primary view가 없다
- receipt/view/sidecar 사이의 current reconstruction bundle이 분산돼 있다
- run 단위와 topic 단위가 섞여 보여도 그걸 다시 묶는 supervisor contract가 없다

## 7. entrypoint verdict

필요한 것은 새 runtime decision organ이 아니라
`supervisor-facing bounded reconstruction entrypoint`다.

이 entrypoint는 아래 성격을 가져야 한다.

- supervisor first
- surfaced first
- pointer backed
- bounded and non-governing
- latest plus per-reconstruction pair

## 8. canonical placement

권장 canonical path는 아래다.

- per-reconstruction json:
  - `runtime/views/reconstruction_supervisor/<reconstruction_id>.json`
- per-reconstruction md:
  - `runtime/views/reconstruction_supervisor/<reconstruction_id>.md`
- latest pointer md:
  - `runtime/views/reconstruction_supervisor_latest.md`
- latest pointer json:
  - `runtime/views/reconstruction_supervisor_latest.json`

원칙:

- `views` 아래에 둔다. primary consumer가 supervisor이기 때문이다.
- `json + md` 쌍을 같이 둔다. machine/operator read를 둘 다 허용하기 때문이다.
- `latest`는 pointer이고, authoritative bundle은 per-reconstruction artifact다.

## 9. reconstruction id rule

권장 id 규칙:

- `reconstruction_<topic_or_doc_slug>_<run_or_window_id>`
- `reconstruction_<asset_id>_<timestamp>`

원칙:

- 하나의 reconstruction artifact는 하나의 bounded reading window만 대표한다
- repo 전체를 한 장으로 접으려 하지 않는다
- `latest`는 가장 최근 primary pointer일 뿐이다

## 10. input contract of the entrypoint

entrypoint는 최소 아래 입력군을 읽을 수 있어야 한다.

### required input families

- `runtime/receipts/*`
- `runtime/views/operation_board_latest.md` 또는 per-run board
- `runtime/views/multi_lens_document_reading/*_supervisor_surface_*.json` 또는 동급 surfaced view
- `runtime/observer/exploration/json/*.json`

### optional input families

- `runtime/views/engine_state_latest/*.json`
- `runtime/views/engine_state_update_events/*.json`
- `runtime/commands/*.md`
- `runtime/manifests/origin_maps/*.json`

중요:

- entrypoint는 raw source를 처음부터 재해석하는 자리가 아니다
- 이미 생성된 surfaced artifact를 bounded recomposition 하는 자리다

## 11. minimum json shape

json entrypoint는 최소 아래 필드를 가진다.

- `kind`
- `reconstruction_id`
- `constructed_at`
- `scope_ref`
- `supervisor_surface_kind`
- `lineage`
- `routing_context`
- `observer_context`
- `state_context`
- `primary_readout`
- `linked_receipts`
- `linked_views`
- `linked_sidecars`
- `handoff_boundary`
- `bounded_next_attention`
- `guards`

## 12. field meaning

### kind

- 값은 `bounded_reconstruction_supervisor_surface_v1`로 고정한다

### scope_ref

- 이번 reconstruction이 무엇을 묶는지 가리킨다
- 예:
  - 특정 문서
  - 특정 asset
  - 특정 bounded run window

### lineage

- source doc ref
- observer run id
- routing run id
- related asset id
- constructed_from families

### routing_context

- latest receipt ref
- operation board ref
- routing mode summary
- generated artifact summary

### observer_context

- selected exploration sidecar refs
- observation type summary
- keep / outer / defer compressed summary

### state_context

- latest engine state ref if present
- latest update event ref if present
- changed canonical field summary if present

### primary_readout

- supervisor가 먼저 읽는 surfaced explanation이다
- 길게 raw artifact를 복붙하지 않는다
- 아래 4가지를 최소로 가진다
  - `current_surface_summary`
  - `what_is_stable_now`
  - `what_is_only_observed`
  - `what_needs_next_attention`

### handoff_boundary

- reconstruction이 멈추는 지점을 명시한다
- 반드시 아래 성격을 유지한다
  - observation handoff
  - not decision
  - not promotion

### guards

- overclaim prohibition을 명시한다
- 최소 guard:
  - `not_decision_surface`
  - `not_maturity_surface`
  - `not_promotion_signal`
  - `not_session_authority_surface`

## 13. markdown companion shape

md entrypoint는 아래 section을 기본으로 가진다.

1. `context`
2. `primary readout`
3. `linked surfaces`
4. `handoff boundary`
5. `next attention`

### context

- reconstruction_id
- scope_ref
- constructed_at
- routing run / observer run / asset summary

### primary readout

- current surfaced summary
- current stable surface
- current observed-only surface

### linked surfaces

- receipt
- operation board
- supervisor view
- engine state latest if present
- exploration sidecar

### handoff boundary

- why this stops here
- what this surface does not decide

### next attention

- bounded reread hint
- bounded comparison hint
- bounded state-check hint

## 14. composition rules

### receipt is lineage spine

- receipt는 source, markers, run id, generated files를 갖는다
- reconstruction entrypoint는 receipt를 lineage spine으로 삼는다
- receipt를 버리고 새 설명을 만들면 안 된다

### views are supervisor surface spine

- multi-lens supervisor surface, operation board, engine state latest는 surfaced view spine이다
- reconstruction entrypoint는 views를 우선 읽는다
- raw trace나 deep manifest는 secondary reference다

### sidecar is bounded observation supplement

- exploration sidecar는 현재 core adoption 전의 observation hold를 제공한다
- reconstruction entrypoint는 sidecar를 보조 readout으로 붙인다
- sidecar를 decision 근거처럼 승격하면 안 된다

## 15. explicit anti-drift rules

- receipt와 view가 충돌하면 receipt의 lineage와 view의 surfaced readout을 분리해서 적는다
- sidecar observation을 engine state latest와 같은 권한층으로 취급하지 않는다
- latest pointer는 authoritative record가 아니다
- reconstruction entrypoint는 new canonical state를 쓰지 않는다
- reconstruction entrypoint는 새로운 session/store/lock layer를 만들지 않는다

## 16. relationship to existing supervisor surfaces

이 entrypoint는 [multi_lens_document_reading_v0_supervisor_reading_surface_spec.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/multi_lens_document_reading_v0_supervisor_reading_surface_spec.md#L1)
의 확장 재사용으로 읽어야 한다.

차이:

- multi-lens supervisor surface는 한 reading organ의 surfaced output이다
- reconstruction entrypoint는 여러 surfaced artifact를 다시 묶는 family-level surface다

즉:

- multi-lens surface는 one output supervisor view
- reconstruction entrypoint는 multi-surface supervisor bundle

## 17. implementation shape recommendation

실제 구현을 열면 얇은 composer 하나면 충분하다.

권장 형태:

- entry script 또는 module:
  - `app/runtime/reconstruction_supervisor_surface.py`
  - 또는 `scripts/build_reconstruction_supervisor_surface.py`
- 역할:
  - 입력 ref 수집
  - bounded family recomposition
  - `json + md + latest pointer` write

주의:

- 여기서 state patch를 만들지 않는다
- 여기서 receipt를 대체하지 않는다
- 여기서 exploration을 governance verdict로 바꾸지 않는다

## 18. one-line lock

> `bounded_reconstruction_family_and_supervisor_entrypoint_v1`는 `structured doc routing`, `engine state bridge`, `observer sidecar`를 하나의 bounded reconstruction family로 묶고, `runtime/observer/exploration + receipts + views`를 supervisor가 한 번에 읽는 surfaced-first, pointer-backed, non-governing reconstruction entrypoint로 다시 조합하는 규정이다.
