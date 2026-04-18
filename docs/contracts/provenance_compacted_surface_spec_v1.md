# provenance_compacted_surface_spec_v1

## 1. Surface Purpose
`provenance_compacted_latest.md` is a readability surface summarizing duplicate-noise patterns without replacing the raw provenance index.

## 2. Required Sections
- raw provenance path
- preview manifest path
- total rows
- safe group count
- manual-review group count
- classification counts
- representative groups
- raw preservation note

## 3. Preview Manifest Fields
- `preview_name`
- `scan_summary`
- `candidate_summary`
- `candidate_groups`

## 4. Representative Group Fields
- `classification`
- `safety`
- `source_doc_ref`
- `relationship`
- `derived_target_ref`
- `row_count`
- `unique_run_ids`
- `reason`

## 5. Lock
- compacted surface is read-only
- compacted surface points back to raw provenance and preview manifest
- compacted surface never implies raw rows were deleted
