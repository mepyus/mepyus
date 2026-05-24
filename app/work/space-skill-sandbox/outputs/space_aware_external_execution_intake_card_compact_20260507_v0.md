# Space-Aware External Execution Intake Card Compact v0

## Status

```yaml
status: compact_operating_card_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
purpose: next_reentry_operating_intake
```

## Core Rule

```text
Plan from Space, not from Model Default.
```

Do not create micro-runs by default.
Use one broad-but-bounded external-carrier pass, then one Codex recovery.

## Role Split

```text
User:
  direction judge
  approval / hold / boundary decision

VectorFL Space:
  memory / judgment / recovery body

Codex:
  anchor broker
  instruction writer
  claim downshift editor
  Return-to-Space recovery editor
  package-level Movement Record writer only when reusable judgment exists

Gemini / external carrier:
  broad-but-bounded internal reading / synthesis / candidate return

QMD:
  bounded evidence access carrier candidate only
```

## QMD Candidate Setting

Use QMD only when:

```text
material family is known
active surfaces can stay around 3-7 files
bounded evidence pointers are needed
```

Pattern:

```text
QMD search --json
-> exact qmd URI list
-> QMD multi-get --json
-> external carrier synthesis
-> Codex recovery
```

Do not:

```text
full corpus indexing
embed/query/rerank as default
MCP startup
parser/schema/automation
QMD as memory or anchor authority
comma-separated glob groups for multi-get
```

## Worker Return Intake Shape

Candidate shape only:

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

## Worker Return Intake Modes

```text
success_case:
  fields present
  anchor usage trace present
  Return-to-Space candidate present
  -> recover with watch

empty_failure_case:
  empty result body
  anchors_used missing
  Return-to-Space candidate missing
  -> HOLD; do not infer meaning from silence

partial_nonempty_case:
  result body exists
  usable candidate material exists
  anchor usage / behavior-change / not-inspected scope is thin or missing
  -> WATCH; downshift and disclose gaps
```

## HOLD Before Continuing

```text
authority claim that cannot be downshifted
baseline/schema/automation implementation claim
missing Return-to-Space Value
empty result body with missing anchors
critical not-inspected scope hidden
full corpus indexing request
MCP/embed/query/rerank promotion
user forced into repeated copy-paste relay
```

## WATCH But Continue

```text
thin but present anchor usage
missing not-inspected scope that Codex can disclose
weak but usable evidence pointers
candidate-level return value
overclaim wording that can be downshifted
body content exists and has recoverable candidate material
```

## Internal Convergence Gate

Before any next action, ask:

```text
1. Am I about to create another tiny Codex run?
2. Is the next work better delegated to Gemini as one broad-bounded pass?
3. Is this material ready to compress instead of execute?
4. Am I promoting candidate setting into baseline/schema/automation?
5. Is Return-to-Space Value clear enough for one package-level recovery?
```

If micro-run convergence appears:

```text
stop
compress current material
or write one Gemini instruction packet
```

## Gemini Instruction Default Return Shape

Use this for future Gemini instructions unless task-specific shape is needed:

```text
PLAN_BASIS
TARGET / MATERIAL_SCOPE
EXECUTION_SYNTHESIS
WORKER_RETURN_SHAPE_APPLICATION
HOLD_AND_WATCH
RAW_TRACE_BOUNDARY
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

## Codex Recovery Rule

Codex should:

```text
accept Gemini output as candidate material
downshift overclaims
separate evidence / not-inspected / gap
classify HOLD vs WATCH
extract Return-to-Space Value
write at most one package-level record if reusable judgment exists
avoid internal small execution by default
```

## Do Not Promote

```text
not baseline
not registry
not schema
not automation
not current-position update
not tool authority
not VectorFL memory before Codex recovery
```

## Next Re-Entry Instruction

At next chat start:

```text
Read this intake card first.
Do not restart the QMD trials.
Do not create micro-runs.
If user asks to continue, either:
  1. compress current material, or
  2. create one Gemini broad-bounded instruction packet, or
  3. recover one user-pasted Gemini result.
```

`STATUS: SPACE_AWARE_EXTERNAL_EXECUTION_INTAKE_CARD_COMPACT_PREPARED`
