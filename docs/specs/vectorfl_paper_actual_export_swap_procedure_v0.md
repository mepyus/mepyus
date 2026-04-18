# VectorFL Paper Actual Export Swap Procedure v0

## purpose
This note fixes what should happen when the first actual exported host record becomes available.

The rule is simple:
do not redesign the pilot at that moment.
Swap the source into the existing seam.

## current placeholder
- `runtime/contracts/vectorfl_paper_weekend_live_export_shaped_host_record_v2.json`

## canonical slot
- `runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json`

## swap steps
1. Put the actual exported host record into the canonical slot.
2. Keep the same source surface categories:
   - `issues_row`
   - `heartbeat_runs_row`
   - `issue_comments_rows`
   - `approvals_row`
3. Rerun the same thin overlay only.
4. Emit the next translated packet as `v4`.
5. Promote weekend naming toward general pilot naming only after that rerun.

## what not to do
- do not broaden into more host ontology
- do not add new control-plane features
- do not turn the swap into a redesign event

## final lock
The actual export should change the source realism, not the seam logic.
