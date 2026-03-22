# Semantic Terrain Field-First Rollout

Date: 2026-03-21
Target runtime: `/Users/sungsookim/universe/vectorfl_replica/runtime`

## Goal

Shift the terrain work from:

- renderer-first terrain-like drawing

to:

- raw semantic data
- derived terrain fields
- inspectable geometry objects
- terrain rendering

## Added Modules

- [semantic_terrain_fields.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/semantic_terrain_fields.py)
- [semantic_terrain_geometry.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/semantic_terrain_geometry.py)
- runtime aliases:
  - [semantic_terrain_fields.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/semantic_terrain_fields.py)
  - [semantic_terrain_geometry.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/semantic_terrain_geometry.py)

## Wiring

Updated:

- [terrain_map.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map.py)

`build_terrain_map_data(...)` now includes:

- `semantic_fields`
  - `cell_fields`
  - `edge_fields`
  - `region_fields`
- `semantic_geometry`
  - `region_boundaries`
  - `ridge_segments`
  - `valley_segments`
  - `basin_regions`
  - `current_lines`
  - `fault_geometry`
  - `contour_geometry`

## Current Derived Fields

### Cell fields

- `region_identity_signature`
- `region_boundary_mean`
- `ridge_axis_score`
- `valley_channel_score`
- `basin_retention_score`
- `anchor_flow_field`
- `climate_zone_signature`
- `wind_pressure_field`

### Edge fields

- `region_boundary_score`
- `shared_anchor_ratio`
- `scene_divergence`
- `elevation_gradient`
- `stability_gradient`
- `fog_gradient`
- `flow_magnitude`
- `flow_direction`

### Region fields

- `region_boundary_intensity`
- `ridge_presence`
- `valley_presence`
- `basin_presence`
- `wind_pressure_mean`
- `climate_zone`

## Current Geometry Counts

Runtime summary at rollout time:

- `semantic_cell_field_count`: `9060`
- `semantic_edge_field_count`: `17711`
- `semantic_region_field_count`: `9`
- `semantic_geometry_count`: `970`

Geometry breakdown:

- `region_boundaries`: `187`
- `ridge_segments`: `31`
- `valley_segments`: `678`
- `basin_regions`: `9`
- `current_lines`: `6`
- `fault_geometry`: `7`
- `contour_geometry`: `52`

## Meaning

This is the first step where the terrain layer is no longer only a picture.

What now exists:

- derived semantic terrain fields
- named inspectable geometry groups
- region / ridge / valley / basin / current / fault / contour as data objects

What is still missing:

- full SVG overlay separation
- click / hover inspector for geometry objects
- region-native contour extraction instead of simple box-derived region shells
- more selective ridge / valley tracing

## Practical Effect

The terrain JSON is now suitable for the next transition:

- Canvas for base field
- SVG for inspectable semantic overlays

That means the terrain viewer can now evolve toward the `canva.md` direction without discarding the current runtime work.
