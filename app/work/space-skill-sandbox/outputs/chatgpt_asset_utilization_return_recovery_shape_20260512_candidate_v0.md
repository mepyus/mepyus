# ChatGPT Asset Utilization Return Recovery Shape 2026-05-12 Candidate v0

## 1. Status

```text
Document = return recovery shape
Status = CANDIDATE_RECOVERY_SHAPE
Authority = recovery preparation only
Not baseline
Not official workflow
Not automation
Not schema
Not current-position update
```

## 2. Purpose

When ChatGPT returns a response to the asset utilization growth-frame packet, recover it without over-promoting it.

## 3. Recovery Inputs

```text
ChatGPT returned text
chatgpt_asset_utilization_growth_frame_send_packet_20260512_candidate_v0.md
objective_asset_inventory_for_chatgpt_20260512_candidate_v0.md
sandbox_worker_hold_watch_decision_gate_20260512_candidate_v0.md
```

## 4. Recovery Questions

```text
Did ChatGPT follow the required return shape?
Did it classify assets by gate output?
Did it preserve candidate/watch/hold boundaries?
Did it propose automation?
Did it promote assets to baseline/workflow?
Did it name user-judgment-required items?
Did it name falsification/failure conditions?
Did it recommend a low-risk next test?
Did it name which cost would be reduced?
Did it identify a raw worker-return landing zone if it recommends worker packet?
```

## 5. Placement Rules

```text
If return follows shape and preserves boundaries:
  Placement = RETURN_TO_SPACE_VALUE_WITH_WATCH

If return is useful but too broad/generic:
  Placement = WATCH

If return proposes automation or promotion:
  Placement = HOLD_AUTHORITY_DOWNSHIFT_REQUIRED

If return ignores gate outputs:
  Placement = PARTIAL_NEEDS_RECOVERY
```

## 6. Minimum Recovery Record

```text
source packet:
return received:
shape followed:
useful judgment:
gate-output quality:
over-promotion risk:
user-judgment items:
recommended next test:
failure/falsification named:
cost reduced:
worker return landing:
placement:
watch:
next pull:
```

## 7. What Must Not Happen

```text
Do not treat ChatGPT response as approval.
Do not update current-position from response alone.
Do not implement recommended automation.
Do not treat recommended next test as user-approved.
Do not erase WATCH/HOLD items.
```

`STATUS: CHATGPT_ASSET_UTILIZATION_RETURN_RECOVERY_SHAPE_PREPARED`
