# Gemini Instruction - Package D Real Integrated Operating Trial v0

## Mission

Run Package D as a real integrated operating trial.

Do not simulate execution.
Do not claim completion without actual artifacts.
Do not mark Packages A-D complete.
Do not promote the setting to baseline, registry, schema, automation, or current-position update.

Return one package-level result only.

## Core Principle

```text
Plan from Space, not from Model Default.
```

Package-level execution must preserve:

```text
space anchors
-> broad-but-bounded external execution
-> actual trace / evidence / not-inspected scope
-> HOLD/WATCH classification
-> Return-to-Space Value
-> Movement Record candidate
```

## Why This Instruction Exists

Previous Package D output was downshifted by Codex because it looked like an integrated trial but was actually a synthesis / simulation.

This time:

```text
actual target required
actual execution trace required
evidence pointers required
not-inspected scope required
self-reported QMD evidence is not enough
```

## Active Anchors

Use these anchors conceptually. If file access is available, inspect them. If not, mark `not_inspected`.

```text
app/work/space-skill-sandbox/outputs/space_aware_external_execution_package_setup_20260507_v0.md
app/work/space-skill-sandbox/outputs/space_aware_external_execution_intake_card_compact_20260507_v0.md
app/work/space-skill-sandbox/outputs/qmd_carrier_candidate_operating_setting_compact_v0.md
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_three_modes_v0.md
app/work/space-skill-sandbox/outputs/gemini_packages_b_d_integrated_return_recovery_20260507_v0.md
app/work/space-skill-sandbox/outputs/movement_record_gemini_packages_b_d_integrated_return_recovery_v0.md
```

## Candidate Settings To Respect

QMD:

```text
bounded evidence access carrier only
material family known
3-7 active surfaces
search --json
exact qmd URI comma-list multi-get --json
no comma-separated glob groups
no full corpus indexing
no MCP/embed/query/rerank as default
```

Worker return:

```yaml
worker_role:
input_purpose:
anchors_used:
how_anchors_changed_behavior:
tool_output_summary:
evidence_pointers:
not_inspected_scope:
issues_or_watch_items:
return_to_space_value_candidate:
do_not_promote:
```

Intake modes:

```text
success_case -> recover with watch
empty_failure_case -> HOLD
partial_nonempty_case -> WATCH with downshift and gap disclosure
```

## Package D Real Target

Choose exactly one concrete target.

Preferred target type:

```text
one existing external return or package output that can be reviewed against the worker-return three-mode setting
```

Acceptable target pools:

```text
app/work/space-skill-sandbox/relay/outbox/
app/work/space-skill-sandbox/outputs/*return*
app/work/space-skill-sandbox/outputs/*packaging*
app/work/space-skill-sandbox/outputs/*movement_record*
```

Do not choose:

```text
whole repository
all packages A-D
multiple targets
conceptual-only target
```

If you cannot inspect a target, return HOLD with `target_not_inspected`.

## Required Real Execution

You must perform these steps internally and report actual trace:

```text
D01 - choose one concrete target
D02 - state active anchors and material family
D03 - apply worker-return 10-field shape
D04 - classify success / empty-HOLD / partial-WATCH
D05 - if QMD evidence is needed, state exact files/URIs/commands or mark not used
D06 - separate raw trace / evidence / gap
D07 - extract Return-to-Space Value
D08 - produce Movement Record candidate
D09 - state user decision point
D10 - close without promotion
```

Do not invent QMD execution.
If QMD was not actually run or inspected, write:

```text
qmd_not_used
```

## Route / PV / LACL

Route:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
ROUTE_MANUAL_WORKER_RETURN_INTAKE
ROUTE_RETURN_TO_SPACE_CLOSEOUT
ROUTE_AUTHORITY_DOWNSHIFT
```

Canonical PVs:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_RAW_TRACE_BOUNDARY
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
PV_LINE_MATURITY_CAUTION
```

LACL:

```text
This result stands at real integrated trial candidate layer.
It does not stand at baseline, proof, schema, automation, or final operating-setting layer.
```

## Required Output Shape

Return exactly:

```text
PLAN_BASIS
REAL_TARGET_SELECTION
ACTIVE_ANCHORS_AND_SCOPE
ACTUAL_EXECUTION_TRACE
WORKER_RETURN_SHAPE_APPLICATION
HOLD_WATCH_OR_SUCCESS_CLASSIFICATION
QMD_USE_OR_NOT_USED
RAW_TRACE_EVIDENCE_GAP
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
USER_DECISION_POINT
DO_NOT_PROMOTE
NEXT_USE
```

## Required Checks

In `ACTUAL_EXECUTION_TRACE`, include:

```text
what was inspected
what was not inspected
what was executed
what was not executed
which claims are self-reported vs evidence-backed
```

In `QMD_USE_OR_NOT_USED`, include one:

```text
qmd_not_used
qmd_used_with_actual_command_trace
qmd_referenced_from_prior_record_only
```

In `HOLD_WATCH_OR_SUCCESS_CLASSIFICATION`, include:

```text
mode: success_case | empty_failure_case | partial_nonempty_case | HOLD
reason:
weakest_field:
can_recover_without_micro_runs: true/false
```

## HOLD Conditions

Return HOLD if:

```text
no concrete target inspected
target is only conceptual
Return-to-Space Value absent
authority/baseline/schema/automation claim cannot be downshifted
critical not-inspected scope is hidden
user must perform repeated relay steps
```

## WATCH Conditions

Return WATCH if:

```text
target has usable material but thin anchor trace
not-inspected scope is partial but disclosed
evidence pointers are weak but present
Return-to-Space Value is candidate-level
overclaim wording can be downshifted
```

## Do Not

```text
do not say "validated", "proved", "complete", "ready", or "stable" unless immediately downshifted
do not mark A-D complete
do not promote candidate setting
do not create schema/parser/automation
do not update current position
do not treat Gemini self-review as evidence
do not treat QMD as memory or authority
do not create multiple Movement Records
```

## Style

Be concise.
Be evidence-first.
Distinguish actual execution from synthesis.
If uncertain, say `not_inspected` or `self_reported`.

`STATUS: GEMINI_PACKAGE_D_REAL_INTEGRATED_OPERATING_TRIAL_INSTRUCTION_PREPARED`
