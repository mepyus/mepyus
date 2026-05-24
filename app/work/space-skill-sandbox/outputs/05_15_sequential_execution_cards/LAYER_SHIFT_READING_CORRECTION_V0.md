# Layer Shift Reading Correction v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  LAYER_SHIFT_READING_CORRECTION_COMPLETED_WITH_WATCH

Purpose:
  Correct the previous layered-lens reread by distinguishing:

```text
input layer:
  the layer where the material arrives

lens-shifted layer:
  the layer revealed when we deliberately reread the same material through another lens

meaning delta:
  what changes when the layer shifts
```

Boundary:
  This correction does not promote any card or create a new operating authority.
  It is not baseline, workflow, schema, registry, ontology, automation, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Correction

The previous layered reread was useful but incomplete.

It asked:

```text
What layer is this answer standing on?
```

The corrected question is:

```text
What layer did the input arrive on?
What layer appears when we reread it through another lens?
What meaning is created or lost in that shift?
```

Important:
  Do not shift every input.
  Some inputs should remain at their arrival layer.
  The meaning appears only when the arrival layer and shifted layer are read together.

## 3. Terms

### Input Layer

The layer where the material is actually given.

Examples:

```text
customer says "I was charged twice":
  input layer = Raw Signal

draft says "We will refund you today":
  input layer = Action Claim

policy excerpt says "refunds require manager approval":
  input layer = Evidence / Authority

user says "계속 밀어":
  input layer = Action Pressure / Direction
```

### Lens-shifted Layer

The layer exposed by rereading the same input through a different lens.

Examples:

```text
customer anger:
  shifted layer = escalation risk / authority boundary

"refund today":
  shifted layer = approval, finance, legal, customer trust

"card number again":
  shifted layer = privacy/payment risk

"계속 밀어":
  shifted layer = autonomy pressure with promotion boundary risk
```

### Meaning Delta

The real meaning produced by comparing the two.

Examples:

```text
raw complaint -> authority boundary:
  customer emotion is not just tone; it changes escalation and approval risk.

draft promise -> finance/legal boundary:
  friendly wording becomes unauthorized action.

user momentum request -> promotion boundary:
  "continue" means proceed inside safe candidate work, not cross into baseline.
```

## 4. Corrected reading rule

Use this rule before applying any candidate card:

```text
1. Preserve the input's arrival layer.
2. Decide whether a layer shift is needed.
3. If shifting, name the shifted layer explicitly.
4. Compare input layer and shifted layer.
5. Record the meaning delta.
6. Act only at the lowest safe action layer.
7. HOLD any implied jump to authority, policy, automation, dispatch, or memory.
```

If no meaningful delta appears:

```text
do not force a card
answer plainly
or keep it as raw observation
```

## 5. Layer-shift matrix

| Input layer | Possible shifted layer | Meaning delta | Risk if missed |
| --- | --- | --- | --- |
| Raw customer complaint | Authority / escalation | The issue may need owner or approval, not just empathy | Friendly but unauthorized reply |
| Draft response | Boundary / privacy | The wording may touch payment, account, legal, or public risk | Customer harm or policy breach |
| Policy excerpt | Action | The policy may permit a narrow reply, but not execution | Over-applying policy |
| User instruction | Promotion boundary | "Continue" may mean safe candidate work only | Unapproved system changes |
| Search result | Evidence strength | Public source may support a lens, not a local rule | Treating external source as authority |
| Codex/Gemini output | Verification / follow-up | Result needs return review before reuse | Treating output as truth |
| Reading guide | Memory | Orientation can look like official state | Accidental current-position |
| Claim/hook | Public interpretation | Compressed wording may imply stronger truth | Overclaim in content |

## 6. Re-reading current candidates with correction

### 업무 문서 검수 카드

Input layer it usually receives:

```text
work artifact
draft
instruction
email
report
model output
```

Common shifted layers:

```text
evidence
boundary
authority
action
follow-up
```

Meaning delta:
  A work artifact is not only text.
  It may reveal missing owner, missing evidence, unauthorized approval, or action pressure.

Correct use:
  Preserve the original artifact first, then shift only where risk or next action depends on it.

### 외부도구 사용 전 점검 카드

Input layer it usually receives:

```text
tool request
packet draft
model instruction
command idea
API/browser/account task
```

Common shifted layers:

```text
permission
dispatch
credential/account boundary
monitoring
```

Meaning delta:
  A harmless-looking tool request may actually ask for execution authority.

Correct use:
  The input remains a request until explicit approval changes its layer.

### 글 주장/근거 점검 카드

Input layer it usually receives:

```text
idea
outline
claim
source excerpt
draft
```

Common shifted layers:

```text
evidence strength
public truth
publishing risk
reader interpretation
```

Meaning delta:
  A draft claim may be acceptable as a note but false as a promoted public claim.

Correct use:
  Always name whether the claim is note, candidate, tested_candidate, or promoted_rule.

### 쇼츠 훅/주장 점검 카드

Input layer it usually receives:

```text
hook
short claim
script premise
compressed story
```

Common shifted layers:

```text
public interpretation
forbidden claim
platform/publishing action
```

Meaning delta:
  Compression changes the claim's perceived certainty.

Correct use:
  Read the hook both as creative input and as public implication.

### 작업 파악 읽기 카드

Input layer it usually receives:

```text
folder state
project notes
handoff text
session summary
```

Common shifted layers:

```text
memory
workflow
authority
current state
```

Meaning delta:
  A reading guide can accidentally become "the official state."

Correct use:
  Keep `what_this_is_not` visible.

### 고객 응답 안전 검수 카드

Input layer it usually receives:

```text
customer message
support reply draft
refund request
complaint
public review reply
billing issue
```

Common shifted layers:

```text
tone
policy evidence
priority/SLA
authority
privacy/payment risk
public complaint risk
follow-up
```

Meaning delta:
  A customer message is not merely a text to answer.
  It can be a signal of escalation, authorization need, privacy risk, policy gap, or public reputational risk.

Correct use:
  Read the original customer issue and the shifted operational risk together.

## 7. Corrected prompt

Use this instead of the previous layered prompt when the layer matters:

```text
입력된 상태의 층위:

입력 그대로의 의미:

바꿔 읽는 렌즈:

렌즈로 드러난 층위:

층위가 바뀌며 생긴 의미:

층위가 바뀌며 잃을 수 있는 것:

근거:

경계:

권한:

가장 낮은 안전한 다음 행동:

HOLD:
```

This is not a new official card.
It is a correction to how existing cards are read.

## 8. Example correction

Input:

```text
Draft reply:
Sorry about that. We will refund you today.
Please send your card number again so we can check.
```

Bad reading:

```text
Layer:
  customer response

Verdict:
  make it more empathetic
```

Corrected layer-shift reading:

```text
입력된 상태의 층위:
  draft customer reply / action claim

입력 그대로의 의미:
  The agent intends to reassure the customer and solve the issue quickly.

바꿔 읽는 렌즈:
  authority + payment privacy + legal/public complaint risk

렌즈로 드러난 층위:
  approval-needed / execution-not-allowed / privacy boundary

층위가 바뀌며 생긴 의미:
  The reply is not just poor wording.
  It contains an unauthorized refund promise and unsafe payment-data request.

층위가 바뀌며 잃을 수 있는 것:
  If over-shifted, we may ignore the customer's emotional need for acknowledgement.

근거:
  refund promise, payment-card request, billing issue, complaint threat

경계:
  refund approval, payment data, liability, public complaint

권한:
  escalation-needed

가장 낮은 안전한 다음 행동:
  do not send; rewrite as acknowledgement plus safe verification path

HOLD:
  no refund promise
  no full card-number request
  no liability admission
```

## 9. Why this matters

Layer shifting is powerful but dangerous.

If everything is shifted:

```text
raw signals disappear
customer emotion becomes only risk
creative hooks become only compliance
user direction becomes only governance
candidate notes become too heavy
```

If nothing is shifted:

```text
hidden authority risk remains invisible
unsupported claims rise into action
tool requests become execution
reading guides become memory
customer replies create real-world harm
```

Meaning appears in the relation:

```text
arrival layer + shifted layer + meaning delta
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

`STATUS: LAYER_SHIFT_READING_CORRECTION_COMPLETED_WITH_WATCH`
