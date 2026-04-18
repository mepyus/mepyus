# structured_doc_routing_commands_v1

## 1. Document Processing Command
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc runtime/views/current_asset_map_v1.md`

## 1A. Run Identity
- `run_20260328_080631_657375_41cceed5_5fa00e`

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
