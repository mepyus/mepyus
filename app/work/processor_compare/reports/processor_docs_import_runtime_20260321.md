# Processor Compare Docs Import Into Replica Runtime

Date: 2026-03-21
Target runtime: `/Users/sungsookim/universe/vectorfl_replica/runtime`

## Goal

Import the reference documents used in `processor_compare` into Replica runtime so they are no longer only calibration artifacts, but actual runtime materials that can participate in:

- material formation
- cell formation
- local space formation
- terrain-style viewing

## Source Set

Imported from:

- `/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/inputs/source_docs`

Files:

- `doc_001.txt`
- `doc_002.txt`
- `doc_003.txt`
- `doc_004.txt`
- `doc_005.txt`
- `doc_006.txt`
- `doc_007.txt`
- `doc_008.txt`
- `doc_009.txt`

## Import Path

Implemented script:

- [import_processor_compare_docs.py](/Users/sungsookim/universe/vectorfl_replica/scripts/import_processor_compare_docs.py)

The script:

1. imports each document through Replica `live_input`
2. creates runtime materials
3. creates one document-level pressure profile
4. creates one document-level space cell
5. forms one local space per imported document

## Runtime Result

### Imported material counts by document

- `processor_compare/doc_001.txt`: `12`
- `processor_compare/doc_002.txt`: `9`
- `processor_compare/doc_003.txt`: `19`
- `processor_compare/doc_004.txt`: `15`
- `processor_compare/doc_005.txt`: `73`
- `processor_compare/doc_006.txt`: `73`
- `processor_compare/doc_007.txt`: `149`
- `processor_compare/doc_008.txt`: `182`
- `processor_compare/doc_009.txt`: `313`

### New cell / local space counts after import

- `local_spaces`: `9`
- `space_cells`: `9`
- `bridge_traces`: `0`

### Graph summary immediately after import

- `local_space_count`: `9`
- `bridge_count`: `0`
- `terrain_component_count`: `9`
- `quiet_local_space_count`: `9`
- `bridge_exposed_local_space_count`: `0`
- `forming_local_space_count`: `9`

### Terrain summary immediately after import

- `fragment_count`: `20`
- `material_count`: `895`
- `local_space_count`: `9`
- `terrain_cell_count`: `994`
- `water_flow_count`: `18`
- `wind_field_count`: `16`
- `source_count`: `5`

## Soft Bridge Registration Follow-up

After import, a second pass was added to register softer document-to-document bridges based on:

- filtered shared material-anchor values
- rarity weighting across imported docs
- pressure similarity from document-level `D/I/S` means

Implemented script:

- [register_processor_compare_doc_bridges.py](/Users/sungsookim/universe/vectorfl_replica/scripts/register_processor_compare_doc_bridges.py)

Current bridge result:

- `bridge_traces`: `6`
- filesystem-level runtime counts:
  - `local_spaces`: `9`
  - `space_cells`: `9`
  - `bridge_traces`: `6`

Current bridge set:

- `doc_004 -> doc_006`
  - `soft doc proximity: 데이터, 데이터는, 데이터를, 사용자`
- `doc_004 -> doc_005`
  - `soft doc proximity: Foundry, 개념을, 데이터, 데이터는`
- `doc_007 -> doc_008`
  - `soft doc proximity: 것인가, 것처럼, 관계는, 관점이`
- `doc_008 -> doc_009`
  - `soft doc proximity: 가지고, 것처럼, 그다음에, 그런데`
- `doc_005 -> doc_006`
  - `soft doc proximity: API, LLM, Property, RDB`
- `doc_007 -> doc_009`
  - `soft doc proximity: 가치가, 것들은, 것들을, 것들이`

## Document-Level Cells

- `doc_001` -> `cel_ac723b5a00f5` / `lsp_b15cd69dc242`
- `doc_002` -> `cel_41c617feac4e` / `lsp_b7ce8e0abf2f`
- `doc_003` -> `cel_287dbd8be592` / `lsp_3e994a127e88`
- `doc_004` -> `cel_10a538658944` / `lsp_00018441d497`
- `doc_005` -> `cel_9d9fddd4dcff` / `lsp_2dde7aef787a`
- `doc_006` -> `cel_c6e68542ed68` / `lsp_4eadb2fe7a96`
- `doc_007` -> `cel_f19ee775eb5a` / `lsp_f7d3ec6f155d`
- `doc_008` -> `cel_6984f05f9329` / `lsp_4542bbda31fb`
- `doc_009` -> `cel_5ed0b9117ea6` / `lsp_295ffc8c5b72`

## Important Constraint

The first import pass alone was not enough to create cross-space topology.

The current runtime now has a usable first soft-bridge layer, but it is still provisional:

- bridges are based on softened semantic proximity, not strict anchor identity
- some imported-doc linkages may still be noisier than future calibrated region bridges

## Interpretation

This is still a meaningful step.

What now exists:

- the reference calibration documents are inside Replica runtime
- each imported document has a concrete local space shell
- terrain and graph layers now have actual region candidates to work from

What still needs work:

- better bridge scoring across imported docs
- terrain contour refinement from imported material points
- region-level terrain rendering based on `local_spaces` and bridge exposure

## Practical Meaning

The calibration documents are no longer separate research-only records.

They now act as:

- runtime materials
- first-pass region seeds
- future terrain regions

This is the first point where `processor_compare` history begins to feed Replica space directly.
