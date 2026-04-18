# VectorFL Paper Actual Export Swap Stub Note v0

## purpose
This stub exists so the pilot does not need a new design pass when the first actual exported host record arrives.

## what it does
- validates the current slot occupant against the canonical export template
- materializes a `v4` packet preview from the slot occupant
- writes a dry-run manifest for inspection

## current use
Right now it runs against the export-shaped placeholder.
Later it should run against the actual exported host record without changing the seam logic.
