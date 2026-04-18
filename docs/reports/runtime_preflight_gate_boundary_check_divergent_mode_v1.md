# runtime preflight gate boundary check divergent mode v1

## 0. Verdict

**PASS**

## 1. Chosen boundary test

- type: divergent-mode check
- family: `inputs/external_cases/andrej_karpathy_youtube.txt`

Why this choice:
- The family already passed the preflight gate in `space_reading`.
- Re-running the same family in `reflection` makes the boundary visible without inventing a new path.
- This is the narrowest way to check when `raw_to_first_pass_to_report` should *not* be treated as the same path.

## 2. Preflight summary

- request:
  - `mode=reflection`
  - `page=memory`
  - `ref=inputs/external_cases/andrej_karpathy_youtube.txt`
- result:
  - `selected_mode=reflection`
  - `selected_artifact_group=report_trace_surfaces`
  - `first_read_ref=docs/reports/today_handoff_index_v1.md`
  - `drift_risks` and `guard_actions` were emitted

## 3. Breadcrumb linkage result

- status: PASS
- evidence:
  - The breadcrumb first entry was recorded before the read began.
  - It still connects to the preflight decision object.
  - `next_hop` is explicit.
- meaning:
  - The gate still behaves correctly.
  - But the path is no longer the same as the raw-case space-reading path.

## 4. Why this is not the same path

- `space_reading` on the same family goes to `raw_external_cases` and keeps the first read on the raw case itself.
- `reflection` on the same family goes to `report_trace_surfaces` and starts from trace/report surfaces instead.
- Therefore the same family under a different mode is not a strong evidence row for the same candidate path.

## 5. Registry update summary

- status: PASS
- evidence:
  - A new structured observation row was appended.
  - The row now includes:
    - `candidate_name`
    - `family`
    - `mode`
    - `first_read_ref`
    - `selected_artifact_group`
    - `next_hop`
    - `drift_risk_present`
    - `guard_action_present`
    - `observation_source`
    - `observation_timestamp`
    - `promotion_status`
    - `not_promoted_reason`
    - `boundary_note=different_mode_leads_to_different_entry_surface`
- effect:
  - The registry now records not just repeatability, but also a mode boundary where the same family should not be grouped into the same candidate path.

## 6. Why the candidate remains observation-only

- The observation candidate is useful, but the boundary check shows that the candidate does not collapse across mode changes.
- This is exactly why it remains observation-only:
  - repeatable under space reading
  - not the same path under reflection
- The path is therefore still a candidate, not a locked pipeline.

## 7. Next minimal fix

- Keep the registry thin.
- Keep `boundary_note` for future divergent-mode observations.
- Do not promote `raw_to_first_pass_to_report` until the same path is confirmed across the intended mode family, not just within raw-case space reading.

