# operation_surface_data_requirements_v1

## 1. 필수 데이터
- `source_doc_ref`
- `doc_id`
- `run_id`
- `ticket_id`
- `started_at`
- `status`
- `expected_scenario`
- `generated_files`
- `receipt_ref`
- `observation_refs`
- `reference_refs`
- `next_actions`

## 2. 권장 데이터
- `namespace`
- `company_scope`
- `priority`
- `processing_profile`
- `hold_reason`
- `retry_count`
- `owner`

## 3. 공급원
- manifests
  - structured docs registry
  - ticket registry
  - provenance index
- events
  - engine ledger
  - folder activity
- outputs
  - receipts
  - reports
  - observer generated outputs

## 4. 현재 부족한 데이터
- stable `run_id`
- hold / retry normalized field
- observation/reference pointer normalized slots
- company scope / namespace slot

## 5. 우선순위
1. source, run, output pointer
2. status, failure/hold/retry
3. observation/reference links
4. namespace/company boundary data

## 6. 결론
최소 operation surface 는 UI 보다 데이터 계약이 먼저다. 지금은 latest board 가 있으나 run identity 와 pointer richness 가 부족하다.
