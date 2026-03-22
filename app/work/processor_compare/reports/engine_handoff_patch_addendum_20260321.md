# Engine Handoff Patch Addendum

- date: 2026-03-21
- mode: engine-first bounded patch
- viewer impact: none intended

## scope

This addendum records a bounded runtime patch after the phase-1 engine review.

The patch goal was not to redesign the engine, but to tighten handoff semantics in two places:

1. input/material -> bridge
2. bridge/material aggregate -> local_space

## changes applied

### 1. live input material convergence bundle persisted more explicitly

File:
- `app/core/runtime/live_input.py`

Persisted on live-input materials:
- `anchor_bundle`
- `dropped_weak_anchors`
- `processing_values`
- `observer_or_ambiguity_trace`
- `transformable_handles`
- `ingest_session_id`
- `ingest_input_path`

Meaning:
- live input evidence now carries a clearer operational baseline before bridge/local-space handoff.

### 2. bridge trace enrichment

File:
- `app/core/runtime/live_input_space.py`

Added / backfilled bridge fields:
- `bridge_reason_kind`
- `processing_overlap`
- `observer_contribution`
- `rejected_overlap_anchors`

Current behavior:
- bridges still open primarily through canonical shared anchors
- but the bridge record now also preserves:
  - scene/flow/material overlap
  - whether observer trace was available
  - whether dropped weak overlap existed

### 3. local space sync enrichment

File:
- `app/core/runtime/runtime_space_anchor_sync.py`

Added / synced local-space fields:
- `processing_baseline`
- `observer_or_ambiguity_trace`
- `state_transition_summary`

Also fixed:
- `source_label="None"` style fallback pollution

Current behavior:
- local space now keeps a minimal transition-oriented summary instead of only anchor/state labels.

### 4. sync/backfill maintenance fix

Files:
- `scripts/sync_runtime_space_anchor_metadata.py`
- `scripts/backfill_live_input_bridges.py`

Changes:
- runtime space sync script now delegates to runtime sync module
- backfill script import path updated to current runtime bridge API

## evidence after patch

### local space example

`lsp_6acb597c7476`

- `source_label`: `engine_phase1_probe_20260321`
- `processing_baseline`:
  - `D=0.5`
  - `I=0.5`
  - `S=0.5`
  - `dominant_scene=review`
  - `dominant_flow=compare`
- `state_transition_summary`:
  - `forming -> bridge_exposed`
  - `bridge_exposure_count=2`
- `observer_or_ambiguity_trace.available=false`
  - this is now preserved rather than disappearing

### bridge example

`brg_7c5135a8f481`

- `bridge_reason_kind`:
  - `canonical_shared_anchor_with_processing_overlap`
- `processing_overlap`:
  - `scene_match=review`
  - `flow_match=compare`
- `observer_contribution`:
  - currently `available=false`
- `rejected_overlap_anchors`:
  - currently empty

Meaning:
- this is still not deep observer-aware interaction,
  but it is no longer anchor-summary-only.

## current reading after patch

### stronger than before

- input convergence line is more explicitly preserved in material metadata
- bridge traces now keep processing-aware overlap explicitly
- local spaces now keep minimal transition summaries
- live probe space labels no longer collapse into `"None"`

### still shallow

- `observer_contribution` is structurally present but often `available=false`
- `rejected_overlap_anchors` is structurally present but often empty
- local-space transition is still inferred summary, not event-grade state history
- imported doc bridges remain mostly canonical-anchor-led

## updated judgment

### already space-like

- input is translated into reusable space material
- bridge formation is no longer purely display-level
- local-space records now retain minimal transition semantics

### still pipeline-like

- observer-aware interaction is still weak
- rejected path evidence is not yet rich enough
- local-space change is summarized after the fact, not tracked as a full transition ledger

## next bounded patch candidates

1. persist observer disagreement / suppression basis directly into bridge traces
2. persist rejected overlap causes, not just rejected labels
3. move local-space transition summary from inferred snapshot to append-only delta records

## bottom line

This patch does not prove the full engine hypothesis.

But it does move the runtime from:
- `anchor-led explanatory pipeline`

toward:
- `anchor-led bridge engine with partial processing-aware handoff`
