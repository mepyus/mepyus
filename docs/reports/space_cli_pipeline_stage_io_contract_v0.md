# Space-CLI Pipeline Stage I/O Contract v0

## 1. purpose

This document records the input and output shape of each manual pipeline stage.

It is not a schema.

It is not JSON.

It is not runtime structure.

It is a manual operating contract for human-supervised runs.

## 2. stage I/O

```text
stage_name:
input:
operation:
output:
stop_condition:
human_check_needed:
script_candidate:
```

## 3. stages

## Trigger / Input

```text
stage_name:
Trigger / Input

input:
user message, material, worker return, external source summary, runtime event, or conversation excerpt

operation:
capture raw input and first user goal candidate

output:
raw_input
user_goal_candidate

stop_condition:
input is missing or user intent is not recoverable

human_check_needed:
yes

script_candidate:
presence check only
```

## Intake Routing

```text
stage_name:
Intake Routing

input:
raw_input
user_goal_candidate

operation:
judge source surface and confidence

output:
source_surface
surface_confidence
embedded_surface_candidate

stop_condition:
source surface is confused or multiple surfaces are collapsed

human_check_needed:
yes

script_candidate:
candidate label presence check only
```

## Lightweight Memory Retrieval

```text
stage_name:
Lightweight Memory Retrieval

input:
source_surface
user_goal_candidate
known risk / reuse / hold memories

operation:
retrieve only relevant memory cards and source pointers

output:
memory_cards
source_pointers
guardrails

stop_condition:
more than five memory cards are needed or full source reading is required

human_check_needed:
yes

script_candidate:
memory card count checker
```

## Minimum Task Packet

```text
stage_name:
Minimum Task Packet

input:
source_surface
user_goal
memory_cards
source_pointers
guardrails

operation:
compose a bounded worker packet

output:
request_summary
source_surface
user_goal
guardrails
cli_role
expected_output
stop_conditions
memory_cards
source_pointers
reflux_candidate

stop_condition:
packet becomes full onboarding, schema, JSON, or authority transfer

human_check_needed:
yes

script_candidate:
required field checker
```

## Worker Assignment

```text
stage_name:
Worker Assignment

input:
minimum task packet
task risk
required action type

operation:
choose primary route and risk boundary

output:
primary_route
secondary_route
not_recommended_route
risk

stop_condition:
route would give final judgment or baseline authority to a worker

human_check_needed:
yes

script_candidate:
none for final route decision
```

## Worker Execution or Draft

```text
stage_name:
Worker Execution or Draft

input:
worker packet
assignment route
stop conditions

operation:
worker drafts, verifies, reviews, implements, or formats within scope

output:
worker_output
files_modified
files_created
declared_verdict

stop_condition:
worker expands role, edits outside scope, or claims final authority

human_check_needed:
yes

script_candidate:
files_modified / files_created field presence check
```

## Return Intake

```text
stage_name:
Return Intake

input:
worker_output
original task packet

operation:
reread the output as worker_return

output:
current_input_surface: worker_return
expected_vs_observed
issue_list
verdict

stop_condition:
expected task cannot be compared to observed result

human_check_needed:
yes

script_candidate:
worker_return field checker
```

## Native vs Space-Referenced Diff

```text
stage_name:
Native vs Space-Referenced Diff

input:
raw input
space-referenced result
native expected behavior

operation:
compare likely native output and space-referenced output

output:
missing
overreach
alignment
contradiction
residue

stop_condition:
comparison collapses into a single merged answer

human_check_needed:
yes

script_candidate:
section presence checker
```

## Reflux Memory Classification

```text
stage_name:
Reflux Memory Classification

input:
return intake
diff result
risk / residue / next notes

operation:
classify candidate reflux memory without final promotion

output:
note_only
reuse_hint
risk_memory
pattern_candidate
hold_signal
next_move_candidate
deeper_probe_needed

stop_condition:
candidate is treated as baseline or automatic execution trigger

human_check_needed:
yes

script_candidate:
label presence checker only
```

## User-Facing Return

```text
stage_name:
User-Facing Return

input:
manual pipeline judgment
reflux candidates
next candidate

operation:
compress to user-facing 4-line card

output:
쓸 수 있나?
왜?
다음엔?
조심할 점은?

stop_condition:
internal structure overwhelms user-facing answer

human_check_needed:
yes

script_candidate:
user card presence checker
```

## Next Loop Candidate

```text
stage_name:
Next Loop Candidate

input:
user-facing return
reflux candidates
remaining hold signals

operation:
identify possible next step without executing

output:
next_candidate
auto_execute: no
required_user_decision

stop_condition:
next candidate becomes automatic action

human_check_needed:
yes

script_candidate:
auto_execute value checker
```
