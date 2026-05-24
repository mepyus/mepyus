# LACL Re-Grounding Result Packaging Template v0

## Status

```yaml
status: packaging_template_candidate
date: 2026-05-06
baseline_lock: false
automation: false
```

Use this after Gemini returns the LACL re-grounding report.

```markdown
# LACL_REGROUNDING_GEMINI_RETURN_PACKAGING

## Status

status: worker_return_packaging
date:
source_worker: gemini
delivery_route: user_manual_relay | runner_outbox
baseline_lock: false
automation: false
raw_trace_promoted: false

## Source Trace

- original_packet:
- delivered_result:
- runner_outbox:
- raw_result:
- stderr:

## Read Trace Summary

- read:
- missing:
- not_inspected:
- lightly_inspected:

## Candidate Lines

| line | maturity_state | evidence | watch | do_not_infer |
| --- | --- | --- | --- | --- |

## Candidate Axes

| axis | plan_decision_changed | evidence | paired_risk | watch |
| --- | --- | --- | --- | --- |

## Candidate Cameras

| camera | wrong_completion_prevented | evidence | use_when | watch |
| --- | --- | --- | --- | --- |

## Candidate Lenses / Gates

| lens | pass | hold | watch | return_shape |
| --- | --- | --- | --- | --- |

## Position Value Mapping

| LACL item | existing PV | new PV candidate | action |
| --- | --- | --- | --- |

Actions:

- keep_existing
- revise_candidate
- add_candidate
- hold_for_evidence
- reject_overreach

## Best Small-Anchor Sets

### External Tool Planning

- [PV_*]

### Bounded Gemini Reread

- [PV_*]

### Manual Relay / Worker Return Packaging

- [PV_*]

## Conflict / Overlap / Missing Data

- [conflict or missing data]

## Codex Judgment

[candidate map input / hold / user decision needed / reject overpromotion]

## Return-to-Space Value

- reusable finding:
- map update candidate:
- watch:
- future reuse note:

## Do Not

- no baseline
- no ontology
- no schema
- no registry
- no workflow
- no automation
- no current-position update
```

