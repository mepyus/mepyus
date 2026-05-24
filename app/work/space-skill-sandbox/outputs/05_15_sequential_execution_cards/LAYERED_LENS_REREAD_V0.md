# Layered Lens Reread v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  LAYERED_LENS_REREAD_COMPLETED_WITH_WATCH

Purpose:
  Reread the current 05-15 adapter candidates through the lens:
  "There is no single correct answer; there are only layers on which an answer temporarily stands."

Boundary:
  This reread does not promote any card.
  It is not a baseline, workflow, schema, registry, ontology, automation, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Materials reread

- `ADAPTER_CARD_FORMS_V0.md`
- `ADAPTER_EXTERNAL_FRAMEWORK_MERGE_V0.md`
- `CUSTOMER_RESPONSE_REVIEW_DISCOVERY_MERGE_V0.md`
- `ADAPTER_USE_CASE_DISCOVERY_WIDE_SCAN_V0.md`

Reread mode:
  Lens change only.
  No new external search.
  No broad 1-26 source replay.

## 3. Core rereading

The current adapter candidates are not answers.
They are answer-staging devices.

Each card lets a judgment stand on one layer long enough to be inspected, used, downgraded, or moved.

The question is therefore not:

```text
Which adapter is correct?
```

The better question is:

```text
On which layer is this answer currently standing,
and what would break if we treat it as standing on a higher layer?
```

## 4. Layers found in the current materials

### Layer 0 — Raw Signal

What stands here:

```text
customer message
draft reply
Codex result
Gemini synthesis
blog idea
shorts hook
meeting note
support ticket
policy excerpt
```

Truth shape:
  "Something was observed."

Risk:
  Treating raw signal as judgment.

Adapter role:
  Capture without approving.

### Layer 1 — Framing

What stands here:

```text
고객 이슈 요약
핵심 판단
문제/결정
관찰된 이상
상황 유형
```

Truth shape:
  "This is what the situation appears to be."

Risk:
  Framing becomes diagnosis.

Adapter role:
  Make the current reading visible.

### Layer 2 — Evidence / Grounding

What stands here:

```text
빠진 근거/첨부
근거 강도
소스 범위
정책/근거/첨부
order state
ticket record
product fact
metric
```

Truth shape:
  "This is what supports or fails to support the judgment."

Risk:
  Unsupported claim rises into action.

Adapter role:
  Stop overclaim.

### Layer 3 — Boundary

What stands here:

```text
건드리는 범위
금지/위험한 주장
지금 하지 말 것
개인정보/계정/결제 리스크
credential/API/browser/account/memory/write boundary
```

Truth shape:
  "This is where the judgment must not cross."

Risk:
  Review becomes execution.

Adapter role:
  Preserve HOLD.

### Layer 4 — Authority

What stands here:

```text
승인 주체/권한
authorization_status
authority_limit
reply-ok
approval-needed
escalation-needed
execution-not-allowed
```

Truth shape:
  "This judgment may or may not be allowed to act."

Risk:
  Candidate becomes approval.

Adapter role:
  Separate recommendation from permission.

### Layer 5 — Action

What stands here:

```text
다음 한 동작
next cut
return_format
safe reply draft
packet draft
```

Truth shape:
  "This is the smallest next move still inside the boundary."

Risk:
  Next action hides larger implied workflow.

Adapter role:
  Keep action small and reversible.

### Layer 6 — Follow-up / Learning

What stands here:

```text
후속 확인
monitor_after
what proves this helped
customer confirmation
ticket close reason
recheck
```

Truth shape:
  "This is how we know the action changed the situation."

Risk:
  One-time answer becomes final memory.

Adapter role:
  Return result to observation.

### Layer 7 — Promotion / Memory

What stands here:

```text
baseline
workflow
schema
registry
ontology
AGENTS.md
SKILL.md
current-position
output_manifest
official policy
automation
```

Truth shape:
  "This has become a standing rule or system surface."

Risk:
  The layer is entered by implication.

Adapter role:
  HOLD unless explicitly approved.

## 5. Reread of current candidates

### 업무 문서 검수 카드

Best layer:
  Layer 1 through Layer 5.

What it does well:
  Turns a work artifact into a visible judgment, evidence check, boundary, and next action.

Where it fails if raised too high:
  It becomes compliance, approval, or policy.

Correct use:
  A temporary inspection surface.

### 외부도구 사용 전 점검 카드

Best layer:
  Layer 3 through Layer 5.

What it does well:
  Prevents tool requests from pretending they are already authorized.

Where it fails if raised too high:
  Packet draft becomes dispatch approval.

Correct use:
  A permission-separation card.

### 글 주장/근거 점검 카드

Best layer:
  Layer 1 through Layer 3.

What it does well:
  Shows claim level, evidence strength, and source coverage.

Where it fails if raised too high:
  Candidate material becomes public truth.

Correct use:
  A grounding lens before writing or publishing.

### 쇼츠 훅/주장 점검 카드

Best layer:
  Layer 1 through Layer 3.

What it does well:
  Preserves forbidden claims in compressed media.

Where it fails if raised too high:
  Creative planning becomes production automation.

Correct use:
  A claim compression safety lens.

### 작업 파악 읽기 카드

Best layer:
  Layer 0 through Layer 2, sometimes Layer 6.

What it does well:
  Makes a temporary reading order and misread prevention visible.

Where it fails if raised too high:
  Reading guide becomes official memory.

Correct use:
  A temporary orientation lens.

### 고객 응답 안전 검수 카드

Best layer:
  Layer 1 through Layer 6.

What it does well:
  Shows issue, claim, allowed response, forbidden response, authority, privacy/payment risk, failure mode, follow-up, and next action.

Where it fails if raised too high:
  It becomes customer-service policy, SLA matrix, refund authority, legal/compliance decision, or automated routing.

Correct use:
  A pre-send safety lens for customer-facing replies.

## 6. Layer errors now visible

The reread makes several earlier risks clearer:

```text
USABLE_NOW:
  useful at Layer 5, dangerous if treated as Layer 7

PRACTICAL_SUPPLEMENTS:
  useful at Layers 1-5, dangerous if treated as final operating law

PROMOTION_GATE:
  useful at Layer 7 boundary, dangerous if read as promotion approval

ADAPTER_CARD_FORMS:
  useful as Layer 1-6 candidate forms, dangerous if read as registry

CUSTOMER_RESPONSE_REVIEW:
  useful as Layer 1-6 pre-send review, dangerous if read as support policy
```

## 7. Revised rule

Use this rule before applying any candidate:

```text
1. Identify the layer where the answer is standing.
2. Do not use it as if it stands one layer higher.
3. If action is needed, keep it at the smallest lower-layer action.
4. If promotion is desired, make the layer jump explicit and require approval.
5. If unsure, downgrade to observation or framing.
```

## 8. Layered adapter prompt

For future use, the smallest general prompt is:

```text
이 답이 지금 서 있는 층위:

관찰:

현재 프레임:

근거:

경계:

권한:

다음 한 동작:

후속 확인:

HOLD:
```

This is not a new official card.
It is a lens that can be applied to any existing card.

## 9. Immediate implication

The next real test should not ask:

```text
Does the customer response card work?
```

It should ask:

```text
At which layer does this customer response judgment stand?
What would be unsafe if it were treated as approval, policy, or automation?
```

This preserves the user's core principle:

```text
정답은 없다.
정답이 서 있는 층위만 존재한다.
```

## 10. Hard stop confirmation

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
no official customer-service policy
no refund/SLA/legal authority
```

`STATUS: LAYERED_LENS_REREAD_COMPLETED_WITH_WATCH`
