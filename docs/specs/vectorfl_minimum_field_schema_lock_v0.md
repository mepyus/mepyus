# VectorFL Minimum Field Schema Lock v0

이 문서는 이미 잠근 3층 구조, handoff boundary, 필요성 잠금, canonical object ownership 위에서  
현재 바로 내려갈 수 있는 `minimum required fields`만 고정한다.  
완전한 schema 확정 문서가 아니라, 이후 구현과 adapter가 흔들리지 않도록 최소 계약만 잠그는 문서다.

## 1. 목적

지금 단계에서 필요한 것은 많은 필드를 확정하는 것이 아니라

- intake -> core handoff에 반드시 필요한 필드
- core canonical object가 유지해야 하는 최소 필드
- shell adaptation 이전에 보존되어야 하는 기준 필드

를 먼저 잠그는 것이다.

## 2. Field Lock Rule

- 아래 필드는 `minimum required fields`다
- optional / derived / UI convenience field는 지금 잠그지 않는다
- field 이름은 바뀔 수 있어도, 의미 슬롯은 유지해야 한다
- weak/fallback/provenance는 최소 필드에서 빠지지 않는다

## 3. Intake-Layer Minimum Fields

### 3-1. Source Registry Entry

- `source_id`
- `source_kind`
- `source_locator`
- `source_family`
- `source_subgroup`
- `default_context_ref`
- `trust_level`
- `update_policy`
- `registry_status`

### 3-2. Intake Block

- `block_id`
- `source_ref`
- `origin_ref`
- `block_kind`
- `content_ref`
- `split_reason`
- `protected_region_flag`
- `overlap_group_ref`
- `weakness_note`

### 3-3. Intake Packet

- `packet_id`
- `source_ref`
- `matched_context_layers`
- `intake_classification`
- `intake_block_refs`
- `provenance_ref`
- `weakness_note`
- `fallback_used`
- `readiness_level`
- `next_lane_hint`
- `receipt_ref`
- `created_at`

### 3-4. Intake Status Record

- `status_id`
- `packet_ref`
- `source_registered`
- `context_attached`
- `classification_done`
- `split_generated`
- `fallback_used`
- `weak_intake`
- `re_read_needed`
- `downstream_ready`
- `status_level`
- `updated_at`

## 4. Core-Layer Minimum Fields

### 4-1. Case Record

- `case_id`
- `origin_packet_refs`
- `case_kind`
- `case_status`
- `current_lane_ref`
- `linked_program_refs`
- `governance_state_ref`
- `current_surface_ref`
- `trace_refs`
- `updated_at`

### 4-2. Lane State Record

- `lane_state_id`
- `case_ref`
- `lane_kind`
- `lane_status`
- `input_refs`
- `current_output_refs`
- `hold_flags`
- `next_hop_candidates`
- `updated_at`

### 4-3. Governance Record

- `governance_id`
- `case_ref`
- `lane_state_ref`
- `restriction_flags`
- `hold_state`
- `reason_summary`
- `release_condition`
- `next_check_trigger`
- `decision_trace_ref`
- `updated_at`

### 4-4. Surface Packet

- `surface_id`
- `case_ref`
- `surface_kind`
- `headline`
- `summary_body_ref`
- `supporting_unit_refs`
- `governance_refs`
- `trace_preview_refs`
- `updated_at`

### 4-5. Trace / Memory Record

- `trace_id`
- `case_ref`
- `trace_kind`
- `origin_ref`
- `summary`
- `residue_note`
- `reentry_hint`
- `created_at`

## 5. Handoff-Critical Fields

아래 필드는 handoff에서 특히 손실되면 안 되는 필드로 별도 강조한다.

### intake -> core critical

- `source_ref`
- `matched_context_layers`
- `intake_classification`
- `intake_block_refs`
- `provenance_ref`
- `weakness_note`
- `fallback_used`
- `receipt_ref`
- `next_lane_hint`

### core -> shell critical

- `case_id`
- `current_lane_ref`
- `governance_state_ref`
- `current_surface_ref`
- `trace_refs`
- `restriction_flags`
- `hold_state`
- `release_condition`

## 6. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- detailed enum sets
- full context tree schema
- full provenance/origin sub-schema
- queue row UI fields
- current-reading page layout fields
- program connection detail fields
- optional analytics / scoring / confidence expansion fields

즉 지금은 `minimum semantic contract`만 잠근다.

## 7. Usage Note

이 문서는 다음 작업의 기준으로 사용한다.

- field-level schema refinement
- adapter contract 설계
- shell view model 설계
- intake/core persistence 정리

하지만 이 문서 자체가 완결된 DB schema나 API schema를 의미하지는 않는다.

## 8. Final Lock Sentence

현재 최소 필드 기준은 다음 문장으로 잠근다.

`지금 단계에서 먼저 고정할 것은 intake와 core의 canonical object가 handoff와 governance를 버티는 데 필요한 최소 의미 필드이며, optional/UI 편의 필드는 이후 adapter와 화면 설계 단계로 미룬다.`
