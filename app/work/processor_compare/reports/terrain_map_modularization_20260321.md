# Terrain Map Modularization

Date: 2026-03-21
Target: `/Users/sungsookim/universe/vectorfl_replica`

## Why

The terrain implementation had become too large to extend safely.

Problem:

- one file was holding:
  - runtime loading
  - terrain data building
  - contour generation
  - region aggregation
  - flow generation
  - full HTML rendering

This made the next steps harder:

- SVG overlay
- geometry inspector
- semantic terrain field expansion

## Refactor Result

### Main orchestrator

- [terrain_map.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map.py)

Now responsible only for:

- loading runtime stores
- orchestrating builder modules
- attaching semantic fields and geometry
- writing JSON/HTML outputs

### Data/builders

- [terrain_map_builders.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_builders.py)

Now responsible for:

- fragment points
- imported material points
- terrain cells
- contour lines
- material features
- regions
- region flows
- water flows
- wind fields
- fault lines
- shared helper utilities

### Renderer

- [terrain_map_render.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_render.py)

Now responsible for:

- terrain HTML page generation
- canvas drawing script
- sidebar metrics / legend / explanatory text

## Size Change

Current line counts:

- `terrain_map.py`: `112`
- `terrain_map_builders.py`: `477`
- `terrain_map_render.py`: `215`
- `semantic_terrain_fields.py`: `289`
- `semantic_terrain_geometry.py`: `181`

## Verification

Post-refactor terrain summary remained valid:

- `fragment_count`: `20`
- `imported_point_count`: `845`
- `sample_point_count`: `865`
- `material_count`: `895`
- `local_space_count`: `9`
- `bridge_count`: `6`
- `terrain_cell_count`: `9060`
- `semantic_geometry_count`: `970`

Output regenerated successfully:

- [terrain_map_view.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reports/terrain_map_view.json)
- [terrain_map_view.html](/Users/sungsookim/universe/vectorfl_replica/runtime/reports/terrain_map_view.html)

## Practical Meaning

This refactor does not finish the terrain viewer.

What it does achieve:

- isolates data building from rendering
- makes semantic overlay migration easier
- keeps future SVG inspector work from bloating the main terrain file

This is the right base for the next phase:

- Canvas base field
- SVG semantic overlays
- inspectable geometry layers
