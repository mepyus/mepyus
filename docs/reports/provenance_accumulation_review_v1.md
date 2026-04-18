# provenance_accumulation_review_v1

## 1. Current State
- source:
  - [runtime/manifests/provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)
- current reading:
  - provenance rows are accumulating mainly from structured doc routing outputs
  - the dominant pattern is not exact duplicate spam, but re-ingest accumulation across repeated document processing runs

## 2. Observed Counts
- total rows at review time: `139`
- dominant relationship:
  - `generated_by_structured_doc_routing`
- repeated source examples:
  - `codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md`
  - `codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md`

## 3. Duplicate Pattern Reading
- exact duplicates:
  - currently none observed
- stable relation repeats:
  - same source / same target / same relationship repeated for:
    - `generated_core_label_packet`
    - `registered_in_structured_doc_registry`
    - `generated_origin_map_seed`
- re-ingest accumulation:
  - the same document processed many times creates many run-specific generated outputs
- unsafe-to-merge similarities:
  - `generated_by_structured_doc_routing` rows often differ by target path and therefore remain meaningful run history

## 4. Risk Reading
- storage risk:
  - still manageable in size
- readability risk:
  - already visible
- maintenance risk:
  - grows as the same baseline docs are repeatedly re-processed

## 5. Locked Verdict
- the main hygiene opportunity is compacted reading and bounded derivative compaction
- the current data does not justify destructive raw rewrite
- safe compaction should focus on stable repeated registry/origin-map relations first
