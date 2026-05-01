# Space Boundary Camera-Lens Lens Subtype Clarification Note v0

## 1. status

```yaml
report_status: clarification_note
based_on:
  - docs/reports/space_boundary_camera_lens_session1_lens_order_validation_v0.md
  - docs/reports/space_boundary_camera_lens_session4_helper_patch_readiness_v0.md
purpose: clarify lens labels and source subtypes before patching the lookup helper
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
helper_patch_ready_after_this_note: true
```

## 2. why this note exists

Session 1 and Session 4 showed that the current helper needs source-surface-weighted lens ranking.

However, three useful lenses and two useful source subtypes were not explicit enough:

```text
evidence/event
expected-vs-observed
artifact-role
worker_return
program_artifact
```

This note names them before code changes so the helper patch does not silently introduce new operating language.

## 3. lens clarifications

### 3.1 evidence/event lens

Use when:

- material is a runtime log
- event ledger
- receipt
- manifest
- test output
- actual operation trace

Core question:

```text
What happened, what does it prove, and what does it fail to prove?
```

Do not reduce to:

```text
technical summary
external architecture evidence
promotion proof
```

### 3.2 expected-vs-observed lens

Use when:

- material is a worker return
- structured return
- bounded comparison result
- executor output
- validation return after a requested operation

Core question:

```text
What was expected, what actually returned, and what branch should follow?
```

Do not reduce to:

```text
worker success
final output
promotion evidence
```

### 3.3 artifact-role lens

Use when:

- material is a generated JSON bundle
- label packet
- origin map
- line seed bundle
- folder inventory
- generated index

Core question:

```text
What role does this artifact play in the space, and when should it reappear?
```

Do not reduce to:

```text
proof of line/axis
user-facing output
automatic microspace entry
```

### 3.4 return-state lens

Use when:

- material is a report
- Codex output
- package closeout
- trial note
- validation report

Core question:

```text
What does this output return to the space as?
```

Do not reduce to:

```text
report completed
final answer
baseline wording
```

## 4. source subtype clarifications

### 4.1 worker_return

Subtype of runtime/worker material.

Signals:

- `structured_return.json`
- `worker_return`
- `expected_return`
- `observed_result`
- `cli_sessions`
- bounded worker output

Default lens order:

```text
expected-vs-observed -> risk -> residue -> next-move -> line/axis
```

Default safe state:

```text
validation_return
```

### 4.2 program_artifact

Subtype of generated/runtime artifact.

Signals:

- `line_seed_bundles`
- `camera_support_bundles`
- `content_role_tags`
- `label_packets`
- `origin_maps`
- `folder_inventory`
- generated JSON bundle

Default lens order:

```text
artifact-role -> evidence/event -> technical -> residue -> risk
```

Default safe state:

```text
artifact_residue / reread_priority
```

### 4.3 runtime_event

Subtype of runtime artifact.

Signals:

- `runtime/events`
- `.jsonl`
- `event_ledger`
- receipt/event trace

Default lens order:

```text
evidence/event -> technical -> risk -> residue -> line/axis
```

Default safe state:

```text
reread_priority / evidence_residue
```

## 5. helper patch implication

The helper may now add:

```yaml
source_surface_subtype:
  - worker_return
  - program_artifact
  - runtime_event
```

And may use source-surface-weighted lens ordering.

Guardrail:

```text
The helper still suggests only. Codex still decides.
```

## 6. do-not-change

Do not:

- add object families
- enforce schemas
- decide final state in script
- decide promotion in script
- write return records
- update indexes
- treat these labels as baseline ontology

## 7. verdict

```yaml
verdict: PASS_WITH_NOTE
next_allowed_move: bounded_helper_patch_source_surface_lens_weighting
```
