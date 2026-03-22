# Operator UI Phase 1 Surgery — 2026-03-21

## Goal

Promote `/` into the main operator shell, strengthen `/atlas` into a selectable region inspector, and connect `/source` and `/dust` as drill-down evidence views.

Locked scope:

- `graph_view.py`
- `region_atlas.py`
- `region_atlas_render.py`
- `/source` query-param drill-down
- `/dust` query-param drill-down

Out of scope for this turn:

- terrain interaction changes
- full raw observer compare
- global shared state
- full maturation badge system

## Files Changed

- `/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/graph_view.py`
- `/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/region_atlas.py`
- `/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/region_atlas_render.py`
- `/Users/sungsookim/universe/vectorfl_replica/app/runtime/source_view/render.py`
- `/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/dust_field.py`

## `/` Operator Shell Changes

### Added node payload keys in `/api/graph`

- `representative_anchors`
- `supporting_anchors`
- `bridge_reason_summary`
- `dropped_weak_anchors`
- `observer_compare`

### Payload behavior

- `supporting_anchors` is emitted as object rows, not plain strings
- `dropped_weak_anchors` uses `available / items`
- `observer_compare` uses merged-first placeholder shape
- `bridge_reason_summary` includes `reason_line`

### Modal structure

The local space modal was reworked into five sections:

- `Summary`
- `Why`
- `Anchors`
- `Evidence`
- `Compare`

### Evidence drill-down

The Evidence section now emits drill-down links where possible:

- `/source?fragment_id=...`
- `/source?source_ref=...`
- `/dust?dust_id=...`

## `/atlas` Region Inspector Changes

### Region payload additions

- `representative_anchors`
- `supporting_anchors`
- `why_region_exists`
- `bridge_reason_summary`
- `source_links`

### UI changes

- region cards are now selectable
- page-local selection only
- right-side inspector added
- inspector shows:
  - representative anchors
  - supporting anchors
  - why region exists
  - bridge reasons
  - landmarks
  - source links

## `/source` Drill-down Changes

Added query-param targeting:

- `?fragment_id=...`
- `?source_ref=...`

Behavior:

- matching fragment/source is highlighted
- page scrolls to matched target
- explicit status shown when not found

## `/dust` Drill-down Changes

Added query-param targeting:

- `?dust_id=...`

Behavior:

- matching dust node is selected on load
- explicit status shown when not found

## Validation

### Python compile

Ran:

```bash
python3 -m py_compile \
  app/core/runtime/graph_view.py \
  app/core/runtime/region_atlas.py \
  app/core/runtime/region_atlas_render.py \
  app/runtime/source_view/render.py \
  app/core/runtime/dust_field.py
```

Result:

- passed

### Runtime payload check

Confirmed `/api/graph` node payload now contains:

- `representative_anchors`
- `supporting_anchors`
- `bridge_reason_summary`
- `dropped_weak_anchors`
- `observer_compare`

Confirmed `/api/atlas` region payload now contains:

- `representative_anchors`
- `supporting_anchors`
- `why_region_exists`
- `bridge_reason_summary`
- `source_links`

### Static report refresh

Regenerated:

- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/space_graph_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/space_graph_view.html`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/region_atlas_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/region_atlas_view.html`

## Remaining Gaps

- `observer_compare.available` is still `false` by design
- `dropped_weak_anchors.available` may still be `false` for some local spaces
- `/source` does not yet expose full canonical promotion/rejection trace
- `/dust` does not yet expose raw observer disagreement payload
- `graph_view` still uses one modal instead of a dedicated persistent right inspector

## Next Best Follow-up

1. deepen `/source` with canonical promotion / dropped weak evidence
2. deepen `/dust` with observer disagreement trace
3. optionally replace `/` modal with persistent right-side operator inspector

## Follow-up Applied

After the first shell/atlas surgery, the evidence views were deepened.

### `/source`

Added fragment-level summaries:

- `canonical_promotion`
- `dropped_weak_anchor_state`
- `observer_disagreement`
- `ingest_lineage`

Effect:

- canonical promotion is now visible as a separate fragment block
- dropped weak anchors show explicit state even when unavailable
- observer disagreement shows merged status and disagreement items when present
- ingest lineage is visible without opening raw JSON

### `/dust`

Added fragment-derived observer compare payload:

- `observer_compare.available`
- `observer_compare.items`
- `observer_compare.merged`

Effect:

- dust inspector now shows merged observer status
- explicit disagreement rows appear when profile scene/role diverge
- query-param drill-down still works with visible not-found state

### Follow-up Validation

Ran:

```bash
python3 -m py_compile \
  app/runtime/source_view/builder.py \
  app/runtime/source_view/render.py \
  app/core/runtime/dust_field.py
```

Result:

- passed

Rebuilt:

- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/source_fragment_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/source_fragment_view.html`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_views/latest_source_fragment_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/dust_field_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/dust_field_view.html`

## Persistent Inspector Upgrade

The main `/` operator shell was further shifted from modal-first to inspector-first.

### File

- `/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/graph_view.py`

### Change

- node click now updates a persistent right-side inspector
- double-click remains as modal fallback
- inspector keeps the same five sections:
  - `Summary`
  - `Why`
  - `Anchors`
  - `Evidence`
  - `Compare`

### Layout result

- left sidebar: metrics / intake / legend
- center main area: graph + mode-switched latest materials / traces
- right rail: persistent operator inspector

### Selection model

- page-local only
- no global shared state introduced
- recent intake local space is selected by default when available

### Validation

Ran:

```bash
python3 -m py_compile app/core/runtime/graph_view.py
```

Result:

- passed

Rebuilt:

- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/space_graph_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/space_graph_view.html`

## Bottom Support Panels Upgrade

The `/` operator shell was further adjusted so latest materials and latest traces are visible together instead of mode-switched.

### File

- `/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/graph_view.py`

### Change

- latest materials and latest traces now render simultaneously under the graph
- layout uses a two-column bottom support panel
- each row is clickable

### Interaction

- material row click:
  - selects related local space when `local_space_id` is available
  - highlights the selected material row
- trace row click:
  - tries to resolve a related local space via related materials
  - if resolvable, updates node selection and inspector
  - if not resolvable, still highlights the selected trace row

### UI effect

- center stays graph-first
- right stays persistent inspector
- bottom becomes a continuously visible operator support strip

### Validation

Ran:

```bash
python3 -m py_compile app/core/runtime/graph_view.py
```

Result:

- passed

Rebuilt:

- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/space_graph_view.json`
- `/Users/sungsookim/universe/vectorfl_replica/runtime/reports/space_graph_view.html`
