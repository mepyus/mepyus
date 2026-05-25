# Codex space operating reading from Gemini v0

Status: HOLD_NOT_AUTHORITY
Owner namespace: codex_space
Created: 2026-05-25 KST

## What changed

The Hermes asset-family material was re-read through Gemini as a Codex space-design problem, not as an execution-closeout problem.

Hermes reading:
- Which asset families were discovered?
- Which runs, packets, guards, receipts, and closeouts exist?
- Where did execution/cleanup/promotion risk force a stop?

Codex reading:
- What does each family do to the space?
- Which layer should receive it?
- Which links are useful for future retrieval?
- Which links create authority/promotion/live-call risk?
- How should later Hermes execution results re-enter space without becoming authority?

## Source handles read

- `app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/internal_asset_family_map_and_position_rollup_v0.json`
- `app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/internal_asset_family_map_ascii_v0.txt`
- `app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/internal_asset_cleanup_stop_and_review_closeout_v0.json`
- `app/work/publish_drafts/vectorfl/VECTORFL_STRUCTURE_ASSET_USAGE_GUIDE_PUBLISH_DRAFT_V0.md`
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_vectorfl_publishable_structure_user_guide_v0/validation/01_validation_vectorfl_publishable_structure_guide_v0.json`
- `app/work/space-skill-sandbox/relay/outbox/codex_space_design_gemini_asset_family_recheck_v0_gemini_outbox_20260525_204955.md`

## Gemini contribution

Gemini confirmed the key distinction:

- Hermes sees the families as execution/discovery/closeout material.
- Codex should read them as structural grammar for space operation.

Useful Gemini points:

- `G_GATE_GUARD` and `S_STATE_PROMOTION` must be strongly linked because guards prevent accidental promotion.
- `U_RUN_BUNDLE` should feed `P_PACKET` only through validated evidence, not raw execution output.
- `B_BRIDGE` must not connect directly to `S_STATE_PROMOTION`; bridge outputs must enter through inbox/review.
- Hermes reentry should enter as execution trace first, then review/maturation, not authority.
- Missing handles include rollback manifest and layer-policing handle.
- `P_PACKET` and `U_RUN_BUNDLE` create duplicate/stale pressure.
- `MATURED` and `AUTHORITY` remain a high-risk confusion pair.

## Codex correction to Gemini

Gemini suggested `X_POINTER_GRAPH_ASSET` as `L2_AUTHORITY`.

Codex correction:

`X_POINTER_GRAPH_ASSET` must not be treated as authority. It should be treated as:

```text
L1/L3 reference-control view with L2-sensitive edges
```

Reason:

- pointer graphs may point at authority-sensitive handles;
- but the graph itself is not authority;
- treating the pointer map as authority would recreate the candidate/authority confusion that `S_STATE_PROMOTION` is meant to prevent.

## Codex layer assignment v0

```text
T/L schema lens:
  L3_CONTROL_READ_LENS

P_PACKET_HANDOFF_ASSET:
  L1_CONTEXT_TRANSFER + L6_ADAPTER_BOUNDARY_SENSITIVE

U_RUN_BUNDLE_ASSET:
  L5_EXECUTION_TRACE_EVIDENCE

G_GATE_GUARD_ASSET:
  L3_CONTROL_GUARD

S_STATE_PROMOTION_ASSET:
  L4_MATURATION_BOUNDARY + L2_AUTHORITY_SENSITIVE

B_BRIDGE_ADAPTER_ASSET:
  L6_ADAPTER_BOUNDARY_DEFERRED

X_POINTER_GRAPH_ASSET:
  L1_REFERENCE_GRAPH + L3_CONTROL_VIEW + L2_AUTHORITY_SENSITIVE_EDGES
```

## Cross-link design v0

Safe/necessary links:

```text
T/L_SCHEMA -> all families
  use as classification lens only

G_GATE_GUARD -> S_STATE_PROMOTION
  use guards to prevent candidate/matured/authority confusion

U_RUN_BUNDLE -> P_PACKET_HANDOFF
  only validated receipts/closeouts may become packet source material

X_POINTER_GRAPH -> P/U/G/S families
  pointer-only map for retrieval and stale-handle detection

S_STATE_PROMOTION -> X_POINTER_GRAPH
  mark authority-sensitive edges without promoting the graph
```

Dangerous links:

```text
B_BRIDGE_ADAPTER -> S_STATE_PROMOTION
  can imply external tool result changes authority; block direct link

P_PACKET_HANDOFF -> B_BRIDGE_ADAPTER
  can imply packet existence authorizes live call; require explicit scope

U_RUN_BUNDLE -> cleanup apply
  can imply generated output may be deleted; require retention rule and approval

X_POINTER_GRAPH -> AUTHORITY
  can imply the map is source of truth; keep NOT_AUTHORITY
```

## Reentry model for future Hermes closeouts

Hermes outputs should re-enter Codex space as:

```text
execution/result material
-> L5 execution trace
-> receipt/validation check
-> space contact map
-> space effect classification
-> HOLD-only maturation proposal
-> optional pointer graph update candidate
-> no authority mutation
```

Minimum reentry fields:

```text
source_execution_id
hermes_run_dir
original_input_handle
space_refs_used
space_refs_sha256
output_artifacts
validation_verdict
mutation_statement
authority_impact_statement
reentry_summary
stale_or_duplicate_pressure
recommended_codex_route
promotion_status
```

## Missing handles

```text
ROLLBACK_MANIFEST_TEMPLATE
LAYER_POLICING_HANDLE
CODEX_SPACE_REENTRY_RECEIPT_SCHEMA
X_POINTER_GRAPH_NOT_AUTHORITY_HEADER
STALE_PACKET_RETENTION_POLICY
MATURED_VS_AUTHORITY_DECISION_GATE
```

## Space delta judgment

Primary judgment:

```text
STRENGTHEN_EXISTING_PATTERN
```

Reason:

The material strengthens an existing VectorFL pattern: execution artifacts must be read as space contact and reentry evidence before any maturation or authority decision.

Secondary judgment:

```text
NEW_PATTERN_CANDIDATE
```

Candidate:

```text
HERMES_EXECUTION_READING_TO_CODEX_SPACE_OPERATING_READING_SPLIT
```

Meaning:

The same artifact set should produce two different products:

- Hermes product: execution closeout / validation / stop boundary.
- Codex product: space layer assignment / retrieval graph / reentry model / HOLD maturation proposal.

## Next safe lane

Codex decision:

```text
X_POINTER_GRAPH_ASSET_POINTER_ONLY_MAP
```

Why:

- It connects the known families without moving files.
- It helps Codex retrieve the right family from future Hermes closeouts.
- It can include stale/duplicate pressure without changing authority.
- It is safer than `B_BRIDGE_ADAPTER_READONLY_BOUNDARY_MAP`, which is near live tool/API boundary.

Gemini suggested `STOP_AND_REVIEW`; Codex accepts STOP as the current boundary but selects `X_POINTER_GRAPH_ASSET_POINTER_ONLY_MAP` as the next safe lane if the user continues.

## Boundary

- source edit: false
- file move: false
- archive: false
- delete: false
- cleanup apply: false
- authority mutation: false
- registry mutation: false
- current-position mutation: false
- promotion: false
- Gemini used: true, user-requested Codex-internal space analysis only
- Gemini authority: false

Final status:

```text
HOLD_NOT_AUTHORITY
```
