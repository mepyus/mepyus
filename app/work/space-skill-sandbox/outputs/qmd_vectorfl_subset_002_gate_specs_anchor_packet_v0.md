# QMD VectorFL Subset 002 Gate Specs Anchor Packet v0

## Status

```yaml
status: anchor_packet_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
execution_scope: bounded_vectorfl_subset
material_family: Task-Mode Gate Specs / Core Operating Anchors
```

## User Purpose

Continue execution while preserving the rule that each operation starts from space and returns recoverable judgment.

## Anchor Use Case

Test whether QMD can retrieve gate-spec anchors that change planning behavior before an external worker starts planning.

## Route / PV / LACL

Route:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
ROUTE_SESSION_REENTRY
ROUTE_AUTHORITY_DOWNSHIFT
```

Candidate PV:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
PV_RAW_TRACE_BOUNDARY
```

LACL signal:

```text
planning answer stands at gate-spec layer, not implementation-readiness layer
```

Signal zone:

```text
worker plan behavior before execution
```

## Active Surfaces

```text
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs/anchor_stack_plan_mode_gate_sequence_v0.md
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs/anchor_stack_gate_checklist_v0.md
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs/small_anchor_generation_rule_v0.md
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs/plan_basis_template_v0.md
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs/external_tool_plan_prompt_wrapper_v0.md
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs/external_tool_plan_return_review_template_v0.md
```

## Recognition Markers

```text
Plan Basis before plan
canonical Position IDs
route
PV
non-inspected scope
hard boundary vs watch
Return-to-Space Value
authority claim absent
do not create automation / schema / registry / baseline
```

## Expected QMD Return

Search should return candidate pointers for:

```text
Plan Basis
canonical Position IDs
Return-to-Space requirement
worker output review gate
```

Follow-up body bundle should use:

```text
exact qmd URI list
multi-get --json
```

Do not use:

```text
comma-separated glob groups
```

## Stop Conditions

```text
stop before full corpus indexing
stop before embed/query/rerank
stop before MCP
stop before parser/schema/automation
stop before baseline/current-position promotion
```

## Return Shape

Codex recovery should return:

```text
accepted candidate gate-spec pointers
held metadata
body bundle observation
whether the retrieved anchors would change worker planning behavior
not-inspected/gap disclosure
Return-to-Space Value
Movement Record
```

## Watch Items

```text
gate_specs_subset_success_overclaim_watch
score_authority_watch
body_bundle_memory_promotion_watch
comma_glob_reuse_watch
plan_basis_as_baseline_watch
```

`STATUS: QMD_VECTORFL_SUBSET_002_GATE_SPECS_ANCHOR_PACKET_PREPARED`
