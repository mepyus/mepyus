# Space-CLI Pipeline Run Template v0

This template is not a schema.

This template is not JSON.

This template is a manual operating record format.

Default:

```text
auto_execute: no
```

## Template

```text
# Space-CLI Manual Pipeline Run

run_id:

date:

input_material:

user_goal:

## 1. Intake Routing

source_surface:
surface_confidence:
embedded_surface_candidate:
why:

## 2. Lightweight Memory Retrieval

memory_cards:
  - memory_type:
    one_line_summary:
    why_relevant_now:
    weight:

source_pointers:
guardrails:

## 3. Minimum Task Packet

request_summary:
source_surface:
user_goal:
guardrails:
cli_role:
expected_output:
stop_conditions:
relevant_lines:
relevant_axis:
memory_cards:
source_pointers:
return_surface:
reflux_candidate:

## 4. Worker Assignment

primary_route:
secondary_route:
not_recommended_route:
reason:
risk:

## 5. Worker Result / Draft

worker:
worker_output_summary:
files_modified:
files_created:
declared_verdict:

## 6. Return Intake

current_input_surface:
expected:
observed:
detected_issues:
review_verdict:

## 7. Native vs Space-Referenced Diff

native_cli_expected:
space_referenced_expected:
missing:
overreach:
alignment:
contradiction:
residue:

## 8. Reflux Memory Candidate

risk_memory:
reuse_hint:
pattern_candidate:
hold_signal:
next_move_candidate:
deeper_probe_needed:

## 9. User-Facing Card

쓸 수 있나?

왜?

다음엔?

조심할 점은?

## 10. Next Loop Candidate

next_candidate:
auto_execute: no
required_user_decision:
```

## Use rule

Use this template for one real material at a time.

Do not use this template to combine unrelated materials into one run.

Do not treat the filled template as baseline.

Do not treat `next_candidate` as permission to act.

Every worker output must be reread as `worker_return` or another current source surface before acceptance.
