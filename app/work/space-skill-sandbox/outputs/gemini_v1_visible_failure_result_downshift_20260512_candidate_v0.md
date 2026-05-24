# Gemini v1 Visible Failure Result Downshift 2026-05-12 Candidate v0

## 1. Status

```text
Document = worker result downshift
Status = WATCH_INSUFFICIENT_DEPTH
Authority = result-quality correction only
Not baseline
Not official workflow
Not automation
Not registry
Not current-position update
```

## 2. Source Result

```text
app/work/space-skill-sandbox/relay/outbox/run_320_gemini_visible_failure_packet_test_gemini_outbox_20260512_212038.md
```

## 3. Problem

Gemini returned:

```text
PASS_V1_CLEARER_WITH_WATCH
```

But the return did not actually demonstrate full package operation.

The v1 packet said:

```text
read the required package files named by the package manifest
```

The package manifest required these files that were not clearly present in Gemini's Files Read Table:

```text
app/work/space-skill-sandbox/outputs/movement_record_chatgpt_asset_utilization_return_20260512_v0.md
app/work/space-skill-sandbox/outputs/movement_record_selection_cost_test_active_surface_20260512_v0.md
app/work/space-skill-sandbox/outputs/movement_record_selection_cost_test_substantive_input_20260512_v0.md
app/work/space-skill-sandbox/outputs/reservoir_pipeline_repo_seed_scriptable_setup_audit_current_20260512_candidate_v0.md
```

## 4. Downshift

```text
Original worker verdict = PASS_V1_CLEARER_WITH_WATCH
Recovered placement = WATCH_INSUFFICIENT_DEPTH
```

## 5. Recovered Judgment

```text
v1 improved completion/failure wording,
but it did not force enough actual package traversal.
The next packet must list every required file explicitly and require one extracted evidence item per file.
```

## 6. Watch

```text
checkbox completion hides shallow reading
worker claims package sufficiency without reading full package
PASS becomes approval
visible failure fields become ceremonial
```

## 7. Next Pull

```text
Run v2 strict full-package evidence packet.
```

`STATUS: GEMINI_V1_VISIBLE_FAILURE_RESULT_DOWNSHIFTED_TO_WATCH`
