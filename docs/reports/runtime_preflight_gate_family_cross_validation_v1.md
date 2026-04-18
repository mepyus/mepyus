# runtime preflight gate family-cross validation v1

## 0. Verdict

**PASS**

## 1. Tested family

- `inputs/external_cases/andrej_karpathy_youtube.txt`

Why this family:
- It is a raw external case family different from the previously validated `saltlux_ai`-centered checks.
- It lets us test whether the same pre-read gate behavior holds when the requested artifact is a different raw case.

## 2. Preflight result summary

### 2.1 Space reading on the new family

- request:
  - `mode=space_reading`
  - `page=explore`
  - `ref=inputs/external_cases/andrej_karpathy_youtube.txt`
- result:
  - `selected_mode=space_reading`
  - `selected_artifact_group=raw_external_cases`
  - `first_read_ref=inputs/external_cases/andrej_karpathy_youtube.txt`
  - `drift_risks` and `guard_actions` were emitted

### 2.2 Reflection on the same gate

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
  - The preflight breadcrumb was recorded before the read began.
  - The breadcrumb first entry explicitly includes:
    - `why_this_was_read`
    - `what_was_seen`
    - `shift_in_understanding`
    - `next_hop`
    - `drift_risk`
    - `repair_signal`
  - The `next_hop` matched the selected first read target for the request.
- weakness:
  - This remains a gate-level breadcrumb, not a thick lineage layer.

## 4. Registry update result

- status: PASS
- evidence:
  - `runtime/manifests/pipeline_observation_registry.jsonl` appended another `raw_to_first_pass_to_report` observation row.
  - The observation count increased again.
- weakness:
  - The path remains observation-only and is not promoted to a locked pipeline.

## 5. Why this is still observation-only

- The gate now works across more than one raw case family, but the observation path is still deliberately not promoted.
- The registry records repeatability, not promotion.
- This turn only checks whether the same preflight -> breadcrumb -> next read target pattern survives on another family.

## 6. Next minimal fix

- Keep the gate as the single pre-read entrypoint.
- Continue appending observations only.
- Do not promote `raw_to_first_pass_to_report` until another family shows the same pattern under the same gate without drift failures.

