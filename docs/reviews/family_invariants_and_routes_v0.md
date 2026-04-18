# Family Invariants And Routes v0

## 목적

이 문서는 현재 상위 family 세 개에 대해
`root invariant` 와 `route signature` 를 실제 값으로 채운다.

대상:

- `fam_input_to_reading`
- `fam_transition_thickening`
- `fam_operator_readout`

## 1. fam_input_to_reading

### root invariant

- `family_id`: `fam_input_to_reading`
- `family_name`: `Input To Reading`
- `family_status`: `active`
- `problem_field`: raw input becoming readable operating material
- `core_distinction`: raw input vs readable structured entry
- `transition_logic`: ingest -> split/shape -> readable entry
- `judgment_question`: 이 입력을 어떤 경로로 읽기 가능한 진입면으로 바꿀 것인가
- `completion_criterion`: 입력이 traceable하고 readable하며 downstream handoff 가능한 entry로 전환됨
- `bounded_spaces`:
  - `input_ingest_space`
  - `external_input_preprocess_space`
- `scope_objects`:
  - raw input documents
  - split units
  - preprocess outputs
- `route_modes`:
  - direct ingest
  - registry ingest
  - compare-first preprocess
  - regroup-first preprocess
- `primary_line_types`:
  - `reading_line`
  - `structural_line`
- `primary_facets`:
  - `material_facet`
  - `distinction_facet`
  - `linkage_facet`
  - `direction_facet`
  - `residue_facet`
- `residue_return_mode`: ingest and preprocess residue return to future entry shaping

### representative routes

#### route_input_direct_ingest

- `route_id`: `route_input_direct_ingest`
- `family_id`: `fam_input_to_reading`
- `route_name`: `direct ingest`
- `mode_class`: `ingest`
- `purpose_invariant`: raw input을 최소 trace와 readable split로 빠르게 entry화
- `activation_conditions`:
  - input is readable enough for split-first entry
  - no preprocess-required verdict exists
- `exclusion_conditions`:
  - raw transcript is too noisy
  - preprocess-required verdict already exists
- `current_position_schema`:
  - input_kind detected
  - split_mode resolved
  - readable board available
- `next_decision_points`:
  - downstream reading handoff
  - preprocess shaping escalation

#### route_preprocess_compare_first

- `route_id`: `route_preprocess_compare_first`
- `family_id`: `fam_input_to_reading`
- `route_name`: `compare-first preprocess`
- `mode_class`: `preprocess`
- `purpose_invariant`: raw input을 무작정 정리하지 않고 먼저 preprocess necessity를 비교 판정
- `activation_conditions`:
  - transcript feels too raw for direct ingest
  - uncertain-needs-probe state is detected
- `exclusion_conditions`:
  - input already entered canonical ingest
  - no preprocessing ambiguity remains
- `current_position_schema`:
  - before/after preprocess comparison visible
  - readiness status available
  - regroup or probe branch still open
- `next_decision_points`:
  - regroup-first
  - post-preprocess probe
  - return to direct ingest

## 2. fam_transition_thickening

### root invariant

- `family_id`: `fam_transition_thickening`
- `family_name`: `Transition Thickening`
- `family_status`: `active`
- `problem_field`: transition/reentry blockage and thickening
- `core_distinction`: simple pass/fail vs active transition condition
- `transition_logic`: observed blockage -> reread -> thickening or closure decision
- `judgment_question`: 이 전환은 왜 막혔고 지금 thickening/closure 중 어디에 있는가
- `completion_criterion`: active transition line의 상태, blockage 이유, next decision point가 설명 가능함
- `bounded_spaces`:
  - `transition_validation_space`
  - `operating_readout_space`
- `scope_objects`:
  - transition_over_surface lines
  - latent lines
  - reread decisions
  - corridor validation outputs
- `route_modes`:
  - preflight reread
  - stage corridor probe
  - residue robustness validation
  - reconstruction supervisor readout
- `primary_line_types`:
  - `decision_line`
  - `residue_line`
- `primary_facets`:
  - `distinction_facet`
  - `linkage_facet`
  - `direction_facet`
  - `operation_facet`
  - `residue_facet`
- `residue_return_mode`: unresolved transition edges return as thickening residue or branching cues

### representative routes

#### route_preflight_reread

- `route_id`: `route_preflight_reread`
- `family_id`: `fam_transition_thickening`
- `route_name`: `preflight reread`
- `mode_class`: `reread`
- `purpose_invariant`: active latent line를 현재 phase와 함께 다시 읽어 thickening/closure 상태를 점검
- `activation_conditions`:
  - active latent line exists
  - preflight or same-line recurrence occurs
- `exclusion_conditions`:
  - no active line is selected
  - closure already frozen for this family slice
- `current_position_schema`:
  - active_latent_lines
  - continuity/residue/tension/sufficiency signals
  - phase decision record
- `next_decision_points`:
  - remain in thickening
  - reopen same family with more evidence
  - review closure readiness

#### route_stage_corridor_probe

- `route_id`: `route_stage_corridor_probe`
- `family_id`: `fam_transition_thickening`
- `route_name`: `stage corridor probe`
- `mode_class`: `validation`
- `purpose_invariant`: corridor stage lineage를 따라 boundary와 transition pressure를 좁혀 본다
- `activation_conditions`:
  - stage corridor outputs exist
  - boundary ambiguity still matters
- `exclusion_conditions`:
  - stage lineage is not relevant to the active blockage
  - route is already reduced to local residue only
- `current_position_schema`:
  - current stage number
  - corridor boundary note
  - accumulated survivor/nonreinforced signals
- `next_decision_points`:
  - advance next stage
  - keep as residue
  - fold back into preflight reread

## 3. fam_operator_readout

### root invariant

- `family_id`: `fam_operator_readout`
- `family_name`: `Operator Readout`
- `family_status`: `active`
- `problem_field`: current engine/process state becoming operator-readable
- `core_distinction`: raw state payload vs operator-facing readout
- `transition_logic`: state/update payload -> adapted model -> board/detail/search route
- `judgment_question`: 현재 상태를 어떤 readout route로 보여주고 조작하게 할 것인가
- `completion_criterion`: operator가 현재 상태, 변화 흔적, 다음 조작점을 읽을 수 있음
- `bounded_spaces`:
  - `operating_readout_space`
- `scope_objects`:
  - engine state latest
  - update events
  - reconstruction supervisor views
  - UI models
- `route_modes`:
  - readonly board
  - activity panel
  - selected detail summary
  - internal search
- `primary_line_types`:
  - `reading_line`
  - `decision_line`
- `primary_facets`:
  - `material_facet`
  - `linkage_facet`
  - `direction_facet`
  - `operation_facet`
- `residue_return_mode`: readout residue returns as presentation caution, attention memory, or next operator explanation hint

### representative routes

#### route_readonly_board

- `route_id`: `route_readonly_board`
- `family_id`: `fam_operator_readout`
- `route_name`: `readonly board`
- `mode_class`: `readout`
- `purpose_invariant`: current state를 broad operator board로 읽히게 한다
- `activation_conditions`:
  - engine_state_latest is available
  - broad overview is requested
- `exclusion_conditions`:
  - operator needs narrow asset-specific explanation only
  - latest state view is missing
- `current_position_schema`:
  - latest state object
  - update event summary
  - board component model
- `next_decision_points`:
  - drill down to selected detail
  - open activity panel
  - launch internal search

#### route_internal_search

- `route_id`: `route_internal_search`
- `family_id`: `fam_operator_readout`
- `route_name`: `internal search`
- `mode_class`: `search`
- `purpose_invariant`: current runtime and reading surfaces 안에서 operator query에 맞는 route를 찾는다
- `activation_conditions`:
  - operator query exists
  - indexed internal search surface is available
- `exclusion_conditions`:
  - no query or no search surface exists
  - direct selected-detail route is already sufficient
- `current_position_schema`:
  - query text
  - search hits across reading/capability surfaces
  - selected result context
- `next_decision_points`:
  - open selected detail
  - jump to capability route
  - return to board overview

## 현재 판단

세 family 모두 이제 문서상으로는
`same-root invariant` 와 `representative route` 를 가진다.

하지만 아직 operational하게 약한 부분도 있다.

- activation/exclusion이 여전히 해석 문장 중심이다
- route별 expected outputs/fallback routes는 일부만 드러나 있다
- projection_line registry는 아직 없다

즉 이 문서는 family contract 초안에 가깝다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `projection_line_schema_v0` 를 세워 family 내부 투영면을 실제 필드로 분리
2. 또는 `route_registry_v0` 를 만들어 지금 적은 route들을 registry 형태로 잠그기

현재로서는 2번이 더 실용적이다.
