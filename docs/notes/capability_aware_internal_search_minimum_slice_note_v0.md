# Capability-Aware Internal Search Minimum Slice v0

## Purpose

Close a minimum operating loop for internal search without widening execution surface:

- query
- reading candidate + capability candidate retrieval
- source/context detail
- next action entry visibility

This is not a new global search engine. It is a bounded adapter over existing grounded reading assets and the executable capability registry.

## Contract

Top-level shared fields:

- `query`
- `result_type`
  - `reading_result`
  - `capability_result`
- `candidate_id`
- `title`
- `why_selected`

`reading_result` keeps current reading language intact:

- `candidate_type`
- `line_name`
- `source_ref`
- `fragment_id`
- `source_range`
- `paragraph_index`
- `evidence_kind`
- `matched_text_preview`
- `surrounding_context_preview`
- `validation_profile`
- `primary_only_validation_profile`
- `support_ecology_bias`
- `next_missing_axis`
- `path_signature`
- `path_origin`

`capability_result` is returned as a capability object, not as file search noise:

- `capability_type`
- `intent_aliases`
- `entrypoint`
- `linked_scripts`
- `output_surfaces`
- `runtime_scope`
- `capability_summary`
- `invocation_hint`
- `safety_note`
- `related_assets`

## Search Source Discipline

Reading side:

- `runtime/logs/reread_observation_log.jsonl`
- `runtime/manifests/line_registry.json`
- `runtime/fragments/*.json` for source context preview

Capability side:

- `runtime/manifests/executable_capability_registry_v0.json`

This keeps capability lookup grounded in the registry as source of truth.

## Operating Panel Minimum

The panel only closes the minimum loop:

1. query input
2. result list
3. selected detail
4. next action entry visibility

It does not auto-execute capability results.

## Official Reading Rule

Search result presentation must keep these distinctions visible:

- `reading_result` vs `capability_result`
- `summary_echo` vs `source_linked` vs `direct_span`
- `main` vs `sandbox` vs `mixed`

## Validation Read

For `input_to_reading_organ`, the panel can now expose:

- pointer-bearing primary reading candidates
- current line state
  - `validation_profile=material_heavy_path_narrow`
  - `primary_only_validation_profile=material_heavy_path_narrow`
  - `support_ecology_bias=primary_dominant`
  - `next_missing_axis=path`
- path-origin labels visible in observation-level rows

This is enough to inspect whether the user is seeing broader path diversity or just repeated primary material on a narrow path shape.

## Limits

- Reading search is still a bounded registry/log read, not a search engine.
- Capability search is still registry-driven, not execution-aware planning.
- `path_origin` can expose legacy observation route labels like `raw_surface`; that helps inspection, but it is not a new scope claim.
- No main runtime mutation is needed for this slice.
