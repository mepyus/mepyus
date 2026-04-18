# provenance_compacted_latest

## 1. Source
- raw_provenance_path: `/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json`
- preview_manifest: `/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_compaction/provenance_compaction_preview_latest.json`

## 2. Totals
- total_rows: `139`
- safe_group_count: `3`
- manual_review_group_count: `1`
- safe_candidate_rows: `6`
- manual_review_candidate_rows: `51`

## 3. Classification Counts
- `same_document_reingest_accumulation`: `1`
- `same_idempotency_context_repeated_append`: `3`

## 4. Representative Groups
- `same_document_reingest_accumulation` / `manual_review` / `codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md` / `*` / rows=`51` / runs=`10`
- `same_idempotency_context_repeated_append` / `safe` / `codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md` / `generated_core_label_packet` / rows=`2` / runs=`2`
- `same_idempotency_context_repeated_append` / `safe` / `codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md` / `generated_origin_map_seed` / rows=`2` / runs=`2`
- `same_idempotency_context_repeated_append` / `safe` / `codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md` / `registered_in_structured_doc_registry` / rows=`2` / runs=`2`

## 5. Raw Preservation Rule
- This compacted surface does not replace the raw provenance index.
- Any later apply step must preserve backup/snapshot and emit a summary.
