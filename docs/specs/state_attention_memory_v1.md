# State Attention Memory v1

## Purpose
- Add an asset-centric derived memory layer over attention queue and lifecycle.
- Preserve recurring attention tendencies without changing canonical state.

## Input Basis
- queue-derived attention items
- resolution loop results
- adjacent canonical diffs
- interpretation badges
- queue status transitions

## Memory Window
- recent attention window: latest 20 history-derived attention events per asset

## Core Fields
- `asset_id`
- `memory_window_start`
- `memory_window_end`
- `total_attention_events`
- `active_attention_count`
- `resolved_attention_count`
- `suppressed_attention_count`
- `reopened_attention_count`
- `recurring_attention_signatures`
- `dominant_attention_reasons`
- `dominant_shift_types`
- `provenance_only_cluster_count`
- `provenance_only_repeat_density`
- `blocker_attention_count`
- `grounding_attention_count`
- `traceability_attention_count`
- `packet_texture_attention_count`
- `maturation_attention_count`
- `attention_pattern_summary`
- `last_attention_at`
- `last_reopened_at`
- `last_resolved_at`
- `updated_at`

## Recurring Pattern Rule
- same asset
- same attention reason or shift family
- repeated at least 2 times inside the memory window

## Summary Tone
- controlled, thin, non-ontological
- examples:
  - `mostly provenance_only background updates`
  - `repeated grounding-related attention`
  - `repeated blocker attention pattern`
  - `insufficient_attention_history`

## Guards
- no canonical mutation
- no raw queue/history deletion
- no `experimental_namespace` driven summary
- low data uses neutral summary
