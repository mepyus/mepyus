# Minimal Layer Digit System v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  MINIMAL_LAYER_DIGIT_SYSTEM_PREPARED_WITH_WATCH

Purpose:
  Reduce adapter complexity by defining a small reusable digit-like layer system.

Core idea:
  A small finite set of reading digits can generate many practical meanings when combined with input layer, shifted layer, and meaning delta.

Boundary:
  This is candidate thinking material only.
  It is not baseline, workflow, schema, registry, ontology, automation, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Problem

The current structure can hold many layers.
That is useful.

But if every new case creates a new card, field, category, checklist, or adapter, the system will drift toward:

```text
complexity
ceremony
confusion
registry-like behavior
workflow-like behavior
false authority
```

The goal is not to make more surfaces.
The goal is to keep a minimal set of reading digits that can be recombined.

## 3. Number analogy

Digits:

```text
0 1 2 3 4 5 6 7 8 9
```

These are finite.
But by position and combination, they count without practical limit.

Adapter equivalent:

```text
small finite reading primitives
+
position/layer
+
relation between input layer and shifted layer
=
many usable meanings
```

Therefore:

```text
do not create infinite cards
create small reusable reading primitives
```

## 4. Proposed reading digits

Use these as minimal primitives:

```text
0. 관찰
1. 프레임
2. 근거
3. 경계
4. 권한
5. 행동
6. 후속
7. 기억/승격
8. 렌즈 이동
9. 의미 차이
```

These are not workflow steps.
They are reading digits.

## 5. Digit meanings

### 0 — 관찰

Question:
  What arrived?

Examples:
  customer message, draft, source, command, file, note, result, complaint, hook.

Failure:
  Raw input is treated as judgment.

### 1 — 프레임

Question:
  What is this being read as?

Examples:
  complaint, claim, task, decision, exception, support case, tool request.

Failure:
  Framing becomes diagnosis.

### 2 — 근거

Question:
  What supports it?

Examples:
  policy, source, metric, attachment, ticket, product fact, code result.

Failure:
  Unsupported claim becomes action.

### 3 — 경계

Question:
  What must not be crossed?

Examples:
  legal, finance, HR, customer data, credential, browser, API, account, memory, publishing.

Failure:
  Review becomes execution.

### 4 — 권한

Question:
  Who or what can approve this?

Examples:
  reply-ok, approval-needed, escalation-needed, draft-only, execution-not-allowed.

Failure:
  Candidate becomes permission.

### 5 — 행동

Question:
  What is the smallest safe next move?

Examples:
  ask for missing info, do not send, rewrite, escalate, inspect, compare, summarize.

Failure:
  Small action hides a workflow.

### 6 — 후속

Question:
  How will we know it worked?

Examples:
  customer confirms, test passes, owner verifies, source checked, ticket state updated.

Failure:
  One answer becomes final.

### 7 — 기억/승격

Question:
  Is this trying to become standing structure?

Examples:
  baseline, policy, AGENTS.md, SKILL.md, output_manifest, current-position, automation, registry.

Failure:
  Temporary reading becomes official structure.

### 8 — 렌즈 이동

Question:
  What other layer should this be read through, if any?

Examples:
  tone -> authority, claim -> evidence, request -> dispatch, summary -> memory.

Failure:
  Everything is shifted and the input layer disappears.

### 9 — 의미 차이

Question:
  What changes between the input layer and shifted layer?

Examples:
  friendly reply -> unauthorized promise, customer anger -> escalation risk, reading guide -> accidental memory.

Failure:
  The real meaning is missed.

## 6. Minimal formula

Use:

```text
input:
  [0]

frame:
  [1]

support:
  [2]

boundary:
  [3]

authority:
  [4]

next:
  [5]

follow-up:
  [6]

promotion check:
  [7]

shift:
  [8]

delta:
  [9]
```

Short form:

```text
0 -> 1 -> 2/3/4 -> 5 -> 6
with 7 held
and 8/9 used only when meaning changes by layer shift
```

## 7. How this reduces complexity

Instead of creating a new adapter for every use case:

```text
customer response
sales email
contract review
Codex packet
onboarding note
decision memo
support ticket
blog claim
shorts hook
```

use the same digits:

```text
0 what arrived
1 what it is being read as
2 what supports it
3 what boundary exists
4 what authority exists
5 smallest safe next action
6 how to check result
7 whether it is trying to promote
8 whether a layer shift is needed
9 what meaning changes
```

The visible card can still use domain language.
The hidden reading system stays minimal.

## 8. Domain labels become skins, not new systems

Examples:

### Customer Response

```text
0:
  customer message + draft reply
1:
  billing complaint
2:
  refund policy / ticket record
3:
  payment data / public complaint / liability
4:
  escalation-needed
5:
  do not send; rewrite with safe verification
6:
  billing owner confirms status
7:
  no SLA/refund policy promotion
8:
  tone -> authority/privacy
9:
  empathetic draft contains unsafe promise
```

### Codex Tool Request

```text
0:
  user asks Codex to inspect and modify
1:
  tool request
2:
  target files / task evidence
3:
  file write / command / account / memory
4:
  user approval required if boundary crossed
5:
  read-only inspection first
6:
  return packet with evidence
7:
  no AGENTS/SKILL/current-position promotion
8:
  request -> dispatch authority
9:
  "look at this" may imply execution if not bounded
```

### Blog Claim

```text
0:
  blog outline
1:
  public claim
2:
  source coverage / evidence strength
3:
  overclaim / SEO manipulation / unsupported promise
4:
  publish approval absent
5:
  outline only
6:
  check source support
7:
  no baseline prompt
8:
  candidate note -> public truth
9:
  true as internal candidate, false as promoted claim
```

## 9. Practical rule

Do not ask first:

```text
Which card should we create?
```

Ask:

```text
Which digits are needed for this input?
```

If only `0,1,5` are needed:
  use plain chat.

If `2,3,4` appear:
  use a review card.

If `8,9` appear:
  record the layer shift.

If `7` appears:
  stop and require explicit promotion decision.

## 10. Recommended next action

Do one stress test using only the digit system:

```text
Input:
  a customer refund complaint draft

Output:
  0-9 digit reading
  then a human-readable customer response safety card
```

This checks whether the minimal system can generate the richer card without needing a new taxonomy.

## 11. Hard stop confirmation

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

`STATUS: MINIMAL_LAYER_DIGIT_SYSTEM_PREPARED_WITH_WATCH`
