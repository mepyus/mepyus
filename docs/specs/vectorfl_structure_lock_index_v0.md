# VectorFL Structure Lock Index v0

이 문서는 현재까지 잠근 VectorFL Paper 관련 구조 문서를 한 장에서 묶어 보는 index다.  
새 구조를 추가하지 않고, 어떤 기준이 이미 잠겼는지와 다음 하강 순서를 빠르게 확인하기 위한 문서다.

## 1. Core Lock Set

### 3층 구조

- [vectorfl_three_layer_structure_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_three_layer_structure_lock_v0.md)
- 잠금 내용:
  - `qmd-ref intake layer`
  - `VectorFL core layer`
  - `paperclip-ref host shell layer`

### handoff 경계

- [vectorfl_handoff_boundary_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_handoff_boundary_lock_v0.md)
- 잠금 내용:
  - intake -> core lossless handoff
  - core -> shell display-only boundary
  - governance decision vs display boundary
  - weak/fallback carry rule

### 외부 source / host 필요성

- [vectorfl_external_source_and_host_need_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_external_source_and_host_need_lock_v0.md)
- 잠금 내용:
  - 왜 내부 재독해만으로는 부족한가
  - 왜 qmd와 Paperclip가 필요한가
  - 왜 외부 원본 자산을 source로 보존해야 하는가

## 2. Canonical Object Lock Set

### ownership

- [vectorfl_canonical_object_ownership_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_canonical_object_ownership_lock_v0.md)
- 잠금 내용:
  - intake / core / shell 객체 소유권
  - canonical object와 adaptation object 구분

### minimum fields

- [vectorfl_minimum_field_schema_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_minimum_field_schema_lock_v0.md)
- 잠금 내용:
  - Source Registry Entry
  - Intake Block
  - Intake Packet
  - Intake Status Record
  - Case Record
  - Lane State Record
  - Governance Record
  - Surface Packet
  - Trace / Memory Record

## 3. Shell Adapter Lock Set

### current-reading

- [vectorfl_current_reading_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_adapter_contract_v0.md)

### inputs / intake

- [vectorfl_inputs_intake_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_inputs_intake_adapter_contract_v0.md)

### cases / queue

- [vectorfl_cases_queue_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_cases_queue_adapter_contract_v0.md)

## 4. Paperclip Shell Usage Lock Set

### shell extraction boundary

- [paperclip_shell_extraction_boundary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/paperclip_shell_extraction_boundary_v0.md)
- 잠금 내용:
  - shell composition만 참조
  - company / issue / heartbeat ontology는 canonical로 들이지 않음

### shell mapping

- [vectorfl_paper_shell_mapping_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_paper_shell_mapping_v0.md)
- 잠금 내용:
  - canonical object -> shell view model 매핑
  - current-reading 중심 우선순위

## 5. Current Priority Order

현재 우선순위는 아래처럼 읽는다.

1. `Current Reading shell`
2. `Inputs / Intake shell`
3. `Cases / Queue shell`
4. `Programs / Connections shell`
5. `History / Trace shell`

## 6. What Is Locked vs Not Yet Locked

### already locked

- 3층 구조
- handoff 경계
- 외부 source / host 필요성
- canonical object ownership
- minimum semantic fields
- current-reading / intake / queue adapter 최소 계약
- Paperclip shell extraction boundary
- shell mapping 기본표

### not yet locked

- programs / connections adapter contract
- history / trace panel adapter contract
- full page layout / widget composition
- live integration contract
- persistence/API schema 상세

## 7. Final Note

이 index는 현재까지의 구조 잠금을 빠르게 다시 찾기 위한 묶음이다.  
다음 구현 단계는 이 index에 있는 문서를 기준선으로 삼고, 아직 잠기지 않은 adapter 또는 integration contract부터 내려가면 된다.
