# Gemini Instruction - QMD Carrier Broad-Bounded Execution v0

## Mission

You are acting as an external execution carrier for VectorFL.

Do not create many tiny session returns.
Do not split the work into analysis / execution / verification / closeout sessions unless there is a blocking reason.

Your job is to run a broad-but-bounded internal execution pass and return one packaged result that Codex can recover into VectorFL space.

## Operating Principle

```text
Plan from Space, not from Model Default.
```

VectorFL Space is not a storage layer.
It is the memory / judgment / recovery body.

External tool execution must follow this loop:

```text
space anchors
-> external execution
-> result / evidence / gap / watch
-> Return-to-Space Value
-> Movement Record candidate
```

## Current Context

Codex already ran QMD trials and recovered the following candidate operating pattern:

```text
QMD is not VectorFL memory.
QMD is a bounded evidence access carrier candidate.

Safe current pattern:
active surfaces 3-7 by material family
-> QMD search --json
-> exact qmd URI list
-> QMD multi-get --json
-> Codex recovery
-> package-level Movement Record
```

Important watch:

```text
Do not use comma-separated glob groups for QMD multi-get.
Use exact qmd URI lists after pointer discovery.
```

## Your Task

Evaluate whether this QMD carrier pattern can become a reusable candidate setting for future external execution, without promoting it to baseline, schema, registry, automation, or current-position update.

You should treat prior run-level evidence as material, but avoid expanding into more micro-runs.

## Space Anchors To Use

Use these anchors conceptually. If file access is available, read them. If not, use the summaries below and state `not_inspected`.

```text
app/work/space-skill-sandbox/outputs/movement_record_qmd_vectorfl_subset_001_trial_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_multi_get_pattern_behavior_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_vectorfl_subset_002_gate_specs_trial_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_gate_anchor_application_to_gemini_anchor_request_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_subset_002_gate_specs_codex_recovery_v0.md
app/work/space-skill-sandbox/outputs/next_chat_reentry_summary_after_space_aware_external_execution_loop_v0.md
```

## Required Material Families

```text
Task-Mode Gate Specs
Worker Return / Packaging Records
Run Records
External Material Intake Records
Current Position / Re-Entry Notes
Maturation / Residue Policy
```

## Route / PV / LACL Signals

Route:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
ROUTE_SESSION_REENTRY
ROUTE_AUTHORITY_DOWNSHIFT
ROUTE_MANUAL_WORKER_RETURN_INTAKE
```

Canonical PVs:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
PV_LINE_MATURITY_CAUTION
```

LACL:

```text
The result stands at candidate operating-setting layer.
It does not stand at baseline, schema, registry, automation, or authority layer.
```

## Hard Boundaries

Do not:

```text
do not propose full corpus indexing
do not propose embed/query/rerank as default
do not propose MCP startup as default
do not create schema/parser/automation
do not create registry/baseline/current-position update
do not treat QMD scores/snippets/body bundles as VectorFL memory
do not make QMD the anchor authority or reviewer
do not create many tiny Movement Records
```

## What To Decide

Answer these questions:

1. Is the QMD carrier pattern mature enough to be used as a candidate operating setting?
2. What exact setting should be reused next time?
3. What must remain watch / issue / hold?
4. What should Codex do, and what should Gemini or another external carrier do?
5. What should not be promoted?
6. What is the package-level Return-to-Space Value?

## Required Output Shape

Return exactly these sections.

```text
PLAN_BASIS
EXECUTION_SYNTHESIS
CANDIDATE_OPERATING_SETTING
ROLE_SPLIT
WATCH_AND_HOLD_ITEMS
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

## Section Requirements

### PLAN_BASIS

Include:

```text
work_type
current_line
axis
camera
lens
route
canonical_PVs
space_assets_consulted
not_inspected_scope
package_sizing_judgment
```

### EXECUTION_SYNTHESIS

Synthesize prior evidence in one pass.
Do not list every micro-run unless needed.

Cover:

```text
QMD runtime availability
fixture trial
VectorFL subset 001
multi-get pattern behavior
VectorFL subset 002 gate specs
application to Gemini Anchor Request review
```

### CANDIDATE_OPERATING_SETTING

Write a concise reusable setting.

It should include:

```text
when_to_use
active_surface_count
material_family_selection
QMD_command_pattern
return_shape
stop_conditions
Codex_recovery_requirement
```

### ROLE_SPLIT

Use this direction:

```text
Gemini / external carrier:
  execute broad-but-bounded internal reading / synthesis / candidate return

Codex:
  broker anchors
  downshift claims
  recover Return-to-Space Value
  write final package-level Movement Record

User:
  direction judgment
  approval / hold / boundary decisions
```

### WATCH_AND_HOLD_ITEMS

Must include:

```text
score_zero_repeat_watch
body_bundle_memory_promotion_watch
qmd_as_anchor_authority_watch
micro_run_proliferation_watch
full_corpus_indexing_hold
embed_mcp_automation_hold
```

### RETURN_TO_SPACE_VALUE

State the reusable judgment in 3-7 bullets.

### MOVEMENT_RECORD_CANDIDATE

Do not write a full long Movement Record.
Return a compact candidate that Codex can recover.

### DO_NOT_PROMOTE

Explicitly list what must not be promoted.

### NEXT_USE

State the next practical use in one paragraph:

```text
Use this setting when Codex wants Gemini or another external carrier to perform the small internal execution work without Codex spending tokens on every micro-step.
```

## Style Constraints

Be concise.
Do not expand into philosophy.
Do not create a new framework.
Do not invent new PVs.
Do not call the result final.
Do not call the setting baseline.

`STATUS: GEMINI_QMD_CARRIER_BROAD_BOUNDED_EXECUTION_INSTRUCTION_PREPARED`
