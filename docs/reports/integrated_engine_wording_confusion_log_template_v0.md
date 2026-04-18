# Integrated Engine Wording Confusion Log Template v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This template defines how to record wording confusion during use observation mode.

It does not approve wording patches. It does not create new UI behavior, new trace behavior, selected-object state, runtime binding, or extension promotion.

## 1. logging rule

Log only wording confusion that appears during manual use.

Do not log as wording confusion:

- known first-fixture read-map scope
- compact trace boundary
- lack of selected-object behavior
- lack of side-inspection value rendering
- lack of runtime binding
- lack of full trace UI
- feature wishes

If in doubt, classify the entry as `not_confusion_watch`.

## 2. required fields

Each log row must include:

- `observation_id`
- `date`
- `scenario`
- `surface`
- `panel`
- `current_wording_or_reading`
- `intended_reading`
- `observed_confusion`
- `repeat_status`
- `classification`
- `structure_issue?`
- `wording_only_candidate?`
- `notes`

## 3. scenario values

Use:

- `S1_user_origin_normal_loop`
- `S2_vectorfl_origin_followup_reactivation`
- `S3_anchor_drift_reprocess_reflux`
- `other_manual_use_observation`

## 4. repeat status values

Use:

| value | meaning |
|---|---|
| `first_seen` | observed once, not enough for patch promotion |
| `repeated_same_scenario` | observed again in the same scenario family |
| `repeated_cross_scenario` | observed across more than one scenario family |
| `not_repeated` | did not recur in later use |
| `resolved_by_reading_order` | confusion disappeared when the operator read center -> packet -> support -> connection record |

## 5. classification values

Use:

| value | meaning |
|---|---|
| `wording_confusion_candidate` | phrasing may confuse use-time reading |
| `repeated_wording_confusion` | enough repeated evidence to review under wording patch gate |
| `fixture_scope_not_confusion` | caused by first-fixture read-map scope, not wording |
| `core_support_trace_boundary_not_confusion` | caused by compact trace boundary, not wording |
| `held_extension_not_confusion` | asks for selected-object, trace UI, runtime binding, or extension behavior |
| `possible_structural_issue` | cannot be solved wording-only; requires separate hold/escalation |
| `not_confusion_watch` | unclear; keep observing |

## 6. copyable log table

| observation_id | date | scenario | surface | panel | current_wording_or_reading | intended_reading | observed_confusion | repeat_status | classification | structure_issue? | wording_only_candidate? | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `uco_0001` | `YYYY-MM-DD` | `S1_user_origin_normal_loop` | `user_surface` | `operating_flow_panel` |  |  |  | `first_seen` | `wording_confusion_candidate` | no | maybe |  |

## 7. initial already observed candidates

These are already observed candidates, not promoted patch items:

| candidate | surface | panel | current issue | current status |
|---|---|---|---|---|
| follow-up request origin wording | user | `request_organization_panel` | "incoming request" may sound user-origin only | candidate only |
| selected wording | user / VectorFL | support inspection / support selection | "selected" may imply selected-object behavior | candidate only |
| evidence history density wording | VectorFL | `evidence_history_panel` | "selected connection records" may imply denser trace UI | candidate only |
| anchor drift braking wording | VectorFL | `anchor_context_panel` | criteria wording may understate drift hold role | candidate only |
| reprocess input wording | engine | `work_input_panel` | "request" may not clearly include reprocess packet | candidate only |
| slot rhythm wording | engine | visual slot rhythm | may be mistaken for state machine if copied without disclaimer | candidate only |
| return draft wording | engine | `result_return_panel` | may understate validation-bound return | candidate only |

## 8. decision after logging

After each observation round:

- If no item repeats, keep `stop and use`.
- If one item repeats, add one more observation before patch promotion unless it blocks use.
- If one item repeats across scenario families, send it to wording patch promotion gate.
- If an item requires structure, do not patch wording; mark hold/escalation.

## 9. closeout sentence

The log protects the baseline by making confusion repeatable evidence, not a trigger for immediate redesign.
