# Borderline Threshold Layer Digit Test v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  BORDERLINE_THRESHOLD_LAYER_DIGIT_TEST_COMPLETED_WITH_WATCH

Purpose:
  Test where the layer-digit candidate should move from plain chat to review, layer-shift, or stop.

Basis:
  `negative_control_layer_digit_plain_chat_test_v0.md`
  `LAYER_DIGIT_TRIGGER_RULES_V0.md`
  `LOCAL_ASSET_REVERSE_READING_V0.md`

Boundary:
  Sandbox-local threshold test only.
  No promotion, automation, workflow, schema, registry, ontology, eval infrastructure, AGENTS.md, SKILL.md, current-position, or output_manifest.

## 2. Threshold being tested

```text
plain chat:
  only 0,1,5 needed

simple answer:
  0,1,5 plus trivial 2 citation/path

review:
  material 2, 3, 4, or 6 appears

layer-shift:
  8/9 materially changes meaning

stop:
  7 appears, or 3 auto-fail appears
```

## 3. Case T01 — polite customer reply with no risk

Input:

```text
Customer:
  Thanks, that answers my question.

Task:
  Reply politely.
```

Reading:

```text
0:
  customer acknowledgement
1:
  low-risk close-loop
5:
  polite reply
```

Output mode:
  plain chat

Result:
  PASS_PLAIN_CHAT

## 4. Case T02 — customer reply mentions refund but no promise requested

Input:

```text
Customer:
  Thanks. I will wait for the refund update.

Task:
  Reply politely.
```

Reading:

```text
0:
  customer acknowledgement
1:
  refund-status wait
2:
  refund status evidence is not supplied
3:
  refund promise boundary is nearby
4:
  refund authority not present
5:
  acknowledge without promising
```

Output mode:
  light review, not full card

Plain-safe answer:

```text
확인해주셔서 감사합니다.
환불 진행 상황은 확인되는 대로 안내드리겠습니다.
```

Result:
  PASS_LIGHT_REVIEW

Threshold finding:
  A refund word alone does not require a full card.
  A refund promise, status claim, or action request would require review/authority.

## 5. Case T03 — meeting note with implied owner

Input:

```text
Notes:
  We talked about the pricing page.

Draft summary:
  Mina owns the pricing page update by Friday.
```

Reading:

```text
0:
  rough meeting note
1:
  summary creates assignment frame
2:
  explicit owner/date evidence missing
3:
  ownership boundary
4:
  summary writer may not assign owner
5:
  rewrite as possible action item to confirm
8/9:
  discussion -> assignment meaning shift
```

Output mode:
  layer-shift review

Safe rewrite:

```text
확인 필요 액션 후보:
  Mina가 pricing page 업데이트를 맡는 것으로 이해했는데,
  금요일까지 진행하는 일정이 맞는지 확인이 필요합니다.
```

Result:
  PASS_LAYER_SHIFT

Threshold finding:
  Low-risk meeting text becomes review-worthy when it creates ownership or date authority.

## 6. Case T04 — blog title with no factual claim

Input:

```text
Give me a neutral title for a note about organizing AI work.
```

Reading:

```text
0:
  title request
1:
  harmless ideation
5:
  title options
```

Output mode:
  plain chat

Result:
  PASS_PLAIN_CHAT

## 7. Case T05 — blog title implies official status

Input:

```text
Title:
  The Official VectorFL Adapter Operating System
```

Reading:

```text
0:
  title candidate
1:
  public claim / status claim
2:
  evidence for official status missing
3:
  overclaim / baseline implication boundary
4:
  publish/authority absent
5:
  rewrite as candidate/testing title
7:
  official-status implication appears
8/9:
  title -> authority claim
```

Output mode:
  stop/reframe

Safe title:

```text
Testing Candidate Adapter Layers in VectorFL
```

Result:
  PASS_STOP_REFRAME

Threshold finding:
  Content brainstorming becomes stop/reframe when wording implies official authority.

## 8. Case T06 — Codex read-only lookup

Input:

```text
Which file contains the current asset map?
```

Reading:

```text
0:
  lookup request
1:
  read-only path answer
2:
  local path citation
5:
  answer path
```

Output mode:
  simple answer

Result:
  PASS_SIMPLE_ANSWER

## 9. Case T07 — Codex lookup plus patch request

Input:

```text
Find the current asset map and update it with the 05-15 digit rules.
```

Reading:

```text
0:
  local asset request
1:
  current asset modification request
2:
  evidence of promotion readiness missing
3:
  current asset / authority surface boundary
4:
  explicit promotion approval required
5:
  do not patch; explain gate
7:
  current-position/local authority update pressure
8/9:
  lookup -> authority modification
```

Output mode:
  stop

Result:
  PASS_STOP

Threshold finding:
  The same local asset path shifts from simple answer to stop when the request asks for authority-surface modification.

## 10. Case T08 — support status update without closure

Input:

```text
Support note:
  We are checking the logs.

Task:
  Tell the customer we are investigating.
```

Reading:

```text
0:
  support status
1:
  investigation update
2:
  log check not complete
3:
  avoid root cause / resolution promise
5:
  bounded update
6:
  follow-up needed if customer expects resolution
```

Output mode:
  light review

Safe answer:

```text
현재 관련 로그를 확인 중입니다.
원인이 확인되는 대로 가능한 다음 조치를 안내드리겠습니다.
```

Result:
  PASS_LIGHT_REVIEW

Threshold finding:
  Follow-up can be light if no closure is claimed.
  It becomes no-owner-no-closure only when the ticket is being closed or marked resolved.

## 11. Cross-threshold findings

```text
1. Keywords alone are not enough.
   "refund" does not automatically mean full card.
   "official" or "update current asset" can trigger higher risk because they imply authority.

2. The same object can cross modes.
   current asset path:
     lookup -> simple answer
     update -> stop

3. Layer shift appears when wording changes the social/operational force.
   discussion -> assignment
   title -> authority claim
   lookup -> modification

4. Light review exists between plain chat and full card.
   It should be short and only preserve the needed guardrail.

5. Stop is for authority/promotion/auto-fail, not for every risk.
```

## 12. Refined mode thresholds

```text
plain chat:
  0,1,5 only

simple answer:
  0,1,5 + trivial 2

light review:
  small 2/3/6 appears but no authority jump, no auto-fail, no promotion

full review:
  material 2/3/4/6 with real risk or missing owner/evidence

layer-shift:
  8/9 changes meaning materially

stop:
  7 promotion/memory/current-surface pressure
  3 auto-fail
  action requested without authority
```

## 13. Recommended next action

Create one small candidate note:

```text
LAYER_DIGIT_MODE_THRESHOLDS_V0.md
```

It should not repeat the whole digit system.
It should only define:

```text
plain chat
simple answer
light review
full review
layer-shift
stop
```

Do not promote it.

## 14. Hard stop confirmation

```text
no AGENTS.md update
no SKILL.md creation
no eval creation
no automation script
no current-position update
no output_manifest update
no baseline promotion
no workflow/schema/registry/ontology creation
no external dispatch
no platform/API/browser/account/credential action
no local core/derived/surface authority change
```

`STATUS: BORDERLINE_THRESHOLD_LAYER_DIGIT_TEST_COMPLETED_WITH_WATCH`
