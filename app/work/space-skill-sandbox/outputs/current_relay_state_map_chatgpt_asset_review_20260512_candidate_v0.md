# Current Relay State Map - ChatGPT Asset Review 2026-05-12 Candidate v0

## 1. Status

```text
Document = current relay state map
Status = CANDIDATE_STATE_SURFACE
Authority = current handoff state only
Not workflow engine
Not automation
Not registry
Not baseline
Not current-position update
```

## 2. Current State

```text
State = READY_TO_SEND
Return = AWAITING_CHATGPT_RETURN
Recovery = PREPARED_NOT_STARTED
```

## 3. Send Surface

Send this:

```text
app/work/space-skill-sandbox/outputs/chatgpt_asset_utilization_dispatch_bundle_20260512_candidate_v0.md
```

The actual relay prompt inside it is:

```text
app/work/space-skill-sandbox/relay/prompts/chatgpt_asset_utilization_growth_frame_send_packet_20260512_v0.md
```

## 4. Awaited Return

When return arrives, paste/store it in:

```text
app/work/space-skill-sandbox/outputs/chatgpt_asset_utilization_return_intake_slot_20260512_candidate_v0.md
```

## 5. Recovery Surface

Recover with:

```text
app/work/space-skill-sandbox/outputs/chatgpt_asset_utilization_return_recovery_shape_20260512_candidate_v0.md
```

## 6. Required Checks On Return

```text
shape followed
gate outputs present
candidate/watch/hold preserved
automation proposed
baseline/workflow promotion
user judgment named
cost type named
worker return landing named
recommended next test
placement
```

## 7. State Transitions

```text
READY_TO_SEND
-> SENT_AWAITING_RETURN
-> RETURN_RECEIVED
-> RECOVERY_IN_PROGRESS
-> RECOVERED_WITH_WATCH / HOLD / PARTIAL_NEEDS_RECOVERY
```

These are tracking labels only.

They are not automation states.

## 8. Do Not

```text
Do not mark SENT unless user actually sends it.
Do not mark RETURN_RECEIVED unless a real ChatGPT return exists.
Do not recover from an empty placeholder.
Do not act on ChatGPT output before recovery.
Do not promote any return to current-position without explicit user decision.
```

## 9. Current Watch

```text
ready-to-send mistaken for sent
return intake slot mistaken for returned result
state map becomes workflow
manifest used instead of active surface
```

`STATUS: CURRENT_RELAY_STATE_MAP_CHATGPT_ASSET_REVIEW_READY_TO_SEND`
