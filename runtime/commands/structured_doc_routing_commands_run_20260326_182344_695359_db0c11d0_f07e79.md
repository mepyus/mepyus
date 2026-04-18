# structured_doc_routing_commands_v1

## 1. Document Processing Command
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc external_case_example_saltlux_goover_relation_reading_v0.md`

## 1A. Run Identity
- `run_20260326_182344_695359_db0c11d0_f07e79`

## 2. Receipt Check
- `ls runtime/receipts`
- `cat runtime/receipts/<doc_id>_operation_receipt.md`

## 3. Board Check
- `cat runtime/views/operation_board_latest.md`

## 4. Recent Events
- `tail -n 20 runtime/events/engine_event_ledger.jsonl`

## 5. Manifest Checks
- `cat runtime/manifests/structured_internal_docs_registry_v1.json`
- `cat runtime/manifests/ticket_registry_v1.json`
- `cat runtime/manifests/provenance_link_index_v1.json`
