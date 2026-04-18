# Route Registry v0

## 목적

이 문서는 [route_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/route_registry_v0.json)
을 현재 family 기반 route의 첫 registry로 고정한다.

이 registry는 scheduler가 아니라
현재 어떤 route가 존재하고,
어느 family에 속하며,
무슨 조건에서 열리고 닫히는지 적는 canonical 목록이다.

## 현재 포함된 route

### fam_input_to_reading

- `route_input_direct_ingest`
- `route_preprocess_compare_first`

### fam_transition_thickening

- `route_preflight_reread`
- `route_stage_corridor_probe`

### fam_operator_readout

- `route_readonly_board`
- `route_internal_search`

## registry 의미

이 registry가 생기면서
route는 더 이상 문장 안에 흩어진 설명이 아니라,
최소 아래를 갖는 객체가 된다.

- 어느 family에 속하는가
- 언제 열리는가
- 언제 닫히는가
- 현재 위치를 무엇으로 읽는가
- 다음 분기점이 무엇인가
- 어떤 output과 residue를 남기는가

## 아직 남은 약점

### 1. activation/exclusion이 여전히 해석 문장 중심이다

다음 버전에서는 일부를 신호/필드 기반으로 더 압축할 필요가 있다.

### 2. route 간 우선순위는 아직 없다

현재는 fallback만 일부 적혀 있고,
selection policy는 별도 문서가 필요하다.

### 3. projection_line과 직접 연결되진 않는다

지금은 family 기준 registry이고,
projection registry는 다음 단계다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `projection_line_schema_v0` 와 `projection_registry_v0`를 만들어 route와 projection을 연결
2. 또는 `route_selection_policy_v0`를 만들어 현재 route 중 무엇을 우선 고를지 규정

현재로서는 2번이 더 실용적이다.
