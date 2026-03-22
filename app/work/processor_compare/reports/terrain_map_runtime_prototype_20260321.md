# Terrain Map Runtime Prototype

Date: 2026-03-21
Target: `/Users/sungsookim/universe/vectorfl_replica/runtime`

## Goal

Shift the current Replica-side runtime view from graph-first inspection toward a terrain-style reading:

- `I` -> elevation
- `S` -> terrain stability
- `observer_ambiguity` -> fog
- `scene` -> terrain biome
- `observer_role` -> feature function
- `observer_signals` -> wind / fault markers

## Initial Runtime Constraint

Current runtime state:

- `fragments`: present
- `materials`: present
- `local_spaces`: empty
- `space_cells`: empty
- `bridge_traces`: empty

Because `local_space` and `space_cell` layers were still empty at first, the first terrain prototype was built from:

- fragment points
- material features

This kept the terrain pipeline usable while leaving room to add region-level rendering later.

## Current Runtime State After Processor-Doc Import

The runtime is no longer fragment/material only.

Current state:

- `fragments`: present
- `materials`: present
- `local_spaces`: `9`
- `space_cells`: `9`
- `bridge_traces`: `6`

Imported processor-compare documents now contribute:

- document-level local spaces
- imported material sample points
- first-pass soft bridges across selected document regions
- bridge-based region flows

## Added Files

- [terrain_map.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map.py)
- [terrain_map.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/terrain_map.py)

## Viewer Wiring

Updated:

- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

Added routes:

- `/terrain`
- `/terrain.html`
- `/api/terrain`

## Terrain Data Model

The current prototype now emits:

- `cells`
  - interpolated terrain surface cells from fragment points
- `fragment_points`
  - raw terrain sample points derived from runtime fragments
- `imported_material_points`
  - additional terrain sample points derived from imported processor-doc materials
- `material_features`
  - feature markers derived from runtime materials
- `regions`
  - local-space regions derived from `local_spaces` + `space_cells`
- `contour_lines`
  - elevation threshold boundaries derived from terrain cells
- `region_flows`
  - bridge-based inter-region flow paths
- `water_flows`
  - shared-anchor convergence paths
- `wind_fields`
  - observer-signal / contrast / comparison vector hints
- `fault_lines`
  - problem/signal driven fracture hints

## Current Mapping

### Fragment -> terrain point

- x/y:
  - source grouping + within-source order + scene offset + stability offset
- elevation:
  - fragment `I`
- stability:
  - fragment `S`
- direction:
  - fragment `D`
- fog:
  - `metadata.observer_ambiguity`
- biome:
  - fragment `scene`
- feature function:
  - `metadata.observer_role`
- signal markers:
  - `metadata.observer_signals`

### Imported material -> terrain point

- used when processor-doc material has no direct runtime fragment backing
- x/y:
  - grouped by `source_ref`
  - ordered by material index
  - offset by `scene`, `D`, `S`
- carries:
  - `I`
  - `S`
  - `D`
  - `scene`
  - anchor values normalized into terrain-anchor keys

### Material -> terrain feature

- material-level marker placed near its originating fragment when `fragment_id` exists
- carries:
  - `observer_role`
  - `observer_ambiguity`
  - `observer_confidence_numeric`
  - `observer_signals`
  from `metadata.fragment_metadata`

### Water flow

- built from fragment pairs with:
  - shared anchor keys
  - relatively low ambiguity

### Wind field

- built from:
  - observer signals
  - comparison scene
  - contrast role

### Fault line

- built from:
  - `problem` role
  - non-empty observer signals

### Region -> terrain region

- built from:
  - `local_spaces`
  - referenced `space_cells`
  - aggregated material feature positions
- carries:
  - `local_space_id`
  - `label`
  - `bridge_trace_refs`
  - `state`
  - center position
  - dominant scene
  - dominant role
  - average elevation/fog

### Contour line

- built from terrain-cell elevation thresholds
- current thresholds:
  - `0.34`
  - `0.50`
  - `0.66`
  - `0.82`

### Region flow

- built from:
  - `bridge_traces`
  - region centers
  - soft bridge note strength
- used as first inter-region topological stream layer

## Smoke Check

Code-level checks passed.

- Terrain summary:
  - fragment_count: `20`
  - imported_point_count: `845`
  - sample_point_count: `865`
  - material_count: `895`
  - local_space_count: `9`
  - bridge_count: `6`
  - terrain_cell_count: `9060`
  - contour_line_count: generated and rendered
  - water_flow_count: `18`
  - wind_field_count: `16`
  - region_flow_count: `6`
  - source_count: `5`
- HTML renderer contains:
  - water legend
  - wind/fault legend
  - terrain canvas
  - region contours
  - region labels
  - region flow lines
  - imported material points

## Viewer Note

An existing viewer was already bound to `127.0.0.1:8421`, so the new terrain route was also started on:

- `http://127.0.0.1:8435`

Server startup log confirmed:

```text
viewer_server: http://127.0.0.1:8435
runtime_root: /Users/sungsookim/universe/vectorfl_replica/runtime
```

## Interpretation

This is now a real terrain-transition stage rather than only a fragment sketch.

What exists now:

- terrain surface from fragment + imported material pressure values
- material features from runtime materials
- local-space region contours from imported processor docs
- region labels and dominant-role hints
- contour-line pass from terrain cells
- first soft bridges across selected imported-doc regions
- first bridge-based inter-region flow lines
- converging anchor paths as water hints
- observer drift and contrast as wind/fault hints

What comes later:

- ridge / valley extraction from region clusters
- contour refinement
- stronger bridge scoring
- layered terrain controls

## Next Step

The next terrain revision should:

- refine current region contours into terrain-native boundaries
- strengthen bridge-based inter-region flow scoring
- aggregate water/wind at local-space level
