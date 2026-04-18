# core_input_layer_labeler_stabilization_smoke_v1

## 1. Purpose
이 문서는 `core input-layer labeler v1` 안정화 smoke 결과를 요약한 보고서다.

범위:
- summary case
- reference case
- default path case
- directive regression case

---

## 2. CASE A — summary / ingest_only / normal
- source:
  - [smoke_structured_doc_summary_case_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_summary_case_v1.md)
- result: `pass`
- normalized:
  - `docrole=summary`
  - `runmode=ingest_only`
  - `priority=normal`
- core labels:
  - `processing_profile=minimal_preprocess`
  - `execution_linkable=false`
- outputs:
  - [doc_smoke_structured_doc_summary_case_v1_label_packet.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets/doc_smoke_structured_doc_summary_case_v1_label_packet.json)
  - [doc_smoke_structured_doc_summary_case_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_smoke_structured_doc_summary_case_v1_operation_receipt.md)

판정:
- 보수적 기본 처리 경로가 잘 유지된다

---

## 3. CASE B — reference / reference_only / low
- source:
  - [smoke_structured_doc_reference_case_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_reference_case_v1.md)
- result: `pass`
- normalized:
  - `docrole=reference`
  - `runmode=reference_only`
  - `priority=low`
- core labels:
  - `processing_profile=reference_only`
  - `execution_linkable=false`
- outputs:
  - [doc_smoke_structured_doc_reference_case_v1_label_packet.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets/doc_smoke_structured_doc_reference_case_v1_label_packet.json)
  - [doc_smoke_structured_doc_reference_case_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_smoke_structured_doc_reference_case_v1_operation_receipt.md)

판정:
- reference 성격이 유지되고 실행 연결이 보수적으로 닫힌다

---

## 4. CASE C — default path / markers missing
- source:
  - [smoke_structured_doc_default_case_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_default_case_v1.md)
- result: `pass`
- normalized:
  - `docrole=memo`
  - `runmode=ingest_only`
  - `priority=normal`
- core labels:
  - `processing_profile=minimal_preprocess`
  - `execution_linkable=false`
- outputs:
  - [doc_smoke_structured_doc_default_case_v1_label_packet.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets/doc_smoke_structured_doc_default_case_v1_label_packet.json)
  - [doc_smoke_structured_doc_default_case_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_smoke_structured_doc_default_case_v1_operation_receipt.md)

판정:
- fallback 경로가 안전하게 동작한다

---

## 5. CASE D — directive regression
- source:
  - [codex_directive_core_input_layer_labeler_realization_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_core_input_layer_labeler_realization_v1.md)
- result: `pass`
- normalized:
  - `docrole=directive`
  - `runmode=ingest_then_execute`
  - `priority=high`
- core labels:
  - `processing_profile=execution_coupled`
  - `execution_linkable=true`
- outputs:
  - [doc_codex_directive_core_input_layer_labeler_realization_v1_label_packet.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets/doc_codex_directive_core_input_layer_labeler_realization_v1_label_packet.json)
  - [doc_codex_directive_core_input_layer_labeler_realization_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_codex_directive_core_input_layer_labeler_realization_v1_operation_receipt.md)

판정:
- 기존 directive 성공 경로에 regression 이 없다

---

## 6. Operational Note
- 병렬 smoke 실행 중 `structured_internal_docs_registry_v1.json` 과 `provenance_link_index_v1.json` 에 race 흔적이 드러났다.
- 이번 턴에서는 malformed tail 을 복구하고 smoke 를 순차로 재실행했다.
- 즉 현재 결론은:
  - labeler 분기 자체는 안정적
  - registry/provenance append 는 병렬-safe 하다고 가정하면 안 됨

---

## 7. One-Line Conclusion
현재 `core input-layer labeler v1` 은 `summary / reference / default / directive` 분기에서 의도한 보수적 동작을 하며, 남은 운영 리스크는 labeler 자체보다 registry/provenance append 의 동시성 쪽에 있다.
