# Adapter External Framework Merge v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  ADAPTER_EXTERNAL_FRAMEWORK_MERGE_COMPLETED_WITH_WATCH

Purpose:
  Merge unrelated external operating frameworks with the existing 05-15 adapter criteria.

Boundary:
  This is a candidate merge note only.
  It is not a registry, workflow, schema, ontology, baseline, automation plan, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. External material searched

The search intentionally moved outside AI use-case lists.

Source families:

```text
NASA human factors / procedure design:
  human factors, operability, task steps, human-in-the-loop evaluation

Checklist practice:
  short safety checklists, pre-action confirmation, missing-critical-step prevention

NIST Risk Management Framework:
  prepare, categorize, select, implement, assess, authorize, monitor

OODA loop:
  observe, orient, decide, act in uncertain situations

Cynefin:
  distinguish clear, complicated, complex, chaotic, and confused contexts

A3 problem solving:
  one-page problem, current condition, goal, root cause, countermeasure, follow-up

Pre-mortem:
  assume failure happened, then identify causes before acting
```

Key sources:

- NASA Human Factors Checklist, NTRS:
  https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160006485.pdf
- NASA Spaceflight Human System Standard:
  https://www.nasa.gov/reference/nasa-std-3001v2/
- NIST Risk Management Framework overview:
  https://csrc.nist.gov/projects/risk-management/risk-management-framework-%28rmf%29-overview
- AHRQ PSNet note on The Checklist Manifesto:
  https://psnet.ahrq.gov/issue/checklist-manifesto-how-get-things-right
- Gary Klein PreMortem:
  https://www.gary-klein.com/premortem
- Lean Enterprise Institute A3 report:
  https://www.lean.org/lexicon-terms/a3-report/
- Cynefin domains:
  https://cynefin.io/wiki/Cynefin_Domains

## 3. Existing 05-15 criteria before merge

Current adapter cards:

```text
업무 문서 검수 카드
외부도구 사용 전 점검 카드
글 주장/근거 점검 카드
쇼츠 훅/주장 점검 카드
작업 파악 읽기 카드
```

Current shared fields:

```text
검수 결과
핵심 판단
주의할 점
빠진 근거/첨부
지금 하지 말 것
건드리는 범위
다음 한 동작
```

Current hard line:

```text
candidate card is not approval
packet draft is not dispatch
reading guide is not memory
claim check is not publishing
USABLE_NOW is not baseline
```

## 4. Merge result

The unrelated frameworks do not require a new architecture.
They strengthen five missing checks:

```text
1. Human usability:
   can a person actually use this card under time pressure?

2. Context classification:
   is this clear, complicated, complex, chaotic, or confused?

3. Authorization boundary:
   who is allowed to approve action, and is this only a draft?

4. Failure anticipation:
   if this goes wrong, what likely caused it?

5. Follow-up loop:
   how do we know whether the next action worked?
```

## 5. External framework to adapter mapping

| External framework | Useful lesson | Merge into 05-15 adapter |
| --- | --- | --- |
| NASA human factors | Procedure must fit actual human use, task steps, interface, and error risk | Add `사용자 실행 가능성` check |
| Checklist practice | Keep checks short and focused on critical misses | Keep adapter cards small; only add critical fields |
| NIST RMF | Separate preparation, categorization, assessment, authorization, monitoring | Make `승인 주체/권한` visible before action |
| OODA | Observe and orient before deciding or acting | Split `관찰` from `판단` when context is unclear |
| Cynefin | Different contexts need different action style | Add `상황 유형` to high-ambiguity cases |
| A3 | One-page clarity forces problem/current/goal/countermeasure/follow-up | Use one-page compression for decision memo and ops exception cards |
| Pre-mortem | Imagine failure first to reveal hidden risk | Add optional `실패한다면 이유` field for high-risk decisions |

## 6. Merged adapter criteria v0

Use these criteria when testing any adapter candidate:

```text
1. User surface:
   Can this be understood without internal VectorFL terms?

2. Context type:
   clear / complicated / complex / chaotic / confused

3. Evidence:
   What source, metric, attachment, observation, or artifact supports the claim?

4. Boundary:
   What file, account, API, browser, credential, memory, policy, customer, legal, HR, finance, or publishing boundary is touched?

5. Authority:
   Is this review, recommendation, draft, approval, or execution?

6. Human usability:
   Is the card short enough to use during real work?

7. Failure anticipation:
   If this output causes trouble, what likely failed?

8. Next action:
   What is the smallest next action that does not cross HOLD?

9. Follow-up:
   What would prove the next action helped?

10. Downgrade path:
   If the card becomes ceremony, how do we return to plain chat?
```

## 7. Existing card updates as candidate guidance

Do not edit the official card forms yet.
For future candidate tests, apply these optional overlays.

### A. 업무 문서 검수 카드 overlay

Add only when risk or ambiguity is nontrivial:

```text
상황 유형:
  clear / complicated / complex / chaotic / confused

승인 주체/권한:
  review / recommendation / approval-needed / execution-not-allowed

실패한다면 이유:
  [likely failure mode]

후속 확인:
  [what proves the next action worked]
```

### B. 외부도구 사용 전 점검 카드 overlay

Add:

```text
authorization_status:
  draft_only / user_approval_required / approved_for_bounded_action

monitor_after:
  what to check after tool return
```

Hard line:
  If authorization_status is not explicit, the packet remains draft_only.

### C. 글 주장/근거 점검 카드 overlay

Add:

```text
context_type:
  clear / complicated / complex / confused

failure_if_published:
  [overclaim / weak source / missing context / misleading implication]
```

### D. 작업 파악 읽기 카드 overlay

Add:

```text
what_this_is_not:
  not memory / not workflow / not authority / not final map

follow_up_check:
  what must be re-read or verified later
```

## 8. New candidate card implications

The previous wide scan suggested three possible new cards:

```text
Customer Response Safety Card
Decision Memo Review Card
Operational Exception Triage Card
```

The external-framework merge supports these, but only as future candidates.

### Customer Response Safety Card

Why supported:
  Checklist practice and human factors both favor short pre-send checks for customer-facing communication.

Core fields:

```text
검수 결과:
고객에게 말해도 되는 주장:
금지 주장:
빠진 정책/근거:
승인 필요 여부:
실패한다면 이유:
다음 한 동작:
```

### Decision Memo Review Card

Why supported:
  A3, Cynefin, and pre-mortem all point to the need to separate context, evidence, decision authority, and failure risk.

Core fields:

```text
검수 결과:
문제/결정:
상황 유형:
근거:
선택지:
권한/승인:
실패한다면 이유:
다음 한 동작:
후속 확인:
```

### Operational Exception Triage Card

Why supported:
  OODA and incident-style thinking fit bugs, incidents, SLA risks, inventory exceptions, and quality defects.

Core fields:

```text
검수 결과:
관찰된 이상:
영향:
긴급도:
건드리는 범위:
지금 하지 말 것:
다음 한 동작:
후속 확인:
```

HOLD:
  Do not create these as official forms until real repeated tests show that `업무 문서 검수 카드` is too broad.

## 9. Practical merged test order

Run tests in this order:

```text
1. Customer-facing reply review
   test overlay:
     authority, missing evidence, failure_if_sent

2. Codex result verification
   test overlay:
     authorization_status, monitor_after

3. Decision memo review
   test overlay:
     context_type, pre-mortem, follow-up

4. Operational exception triage
   test overlay:
     observe/orient split, urgency, next action

5. Onboarding/folder reading guide
   test overlay:
     what_this_is_not, follow_up_check
```

## 10. What changed after the merge

Before:

```text
The adapter cards mostly checked:
  claim
  risk
  boundary
  next action
```

After:

```text
The merged criteria also check:
  context type
  authorization status
  human usability
  likely failure mode
  follow-up proof
```

This is a real improvement because it prevents the adapter layer from becoming only a critique template.
It turns each card into a controlled work-action review.

## 11. Still HOLD

```text
promotion
automation
external dispatch
AGENTS.md / SKILL.md changes
eval infrastructure
current-position update
output_manifest update
baseline
workflow/schema/registry/ontology creation
official approval flow
policy/compliance/legal/HR/finance decisions
platform/API/browser/account/credential action
```

## 12. Next smallest action

Create one sandbox-local merged stress test:

```text
customer-facing reply review

Input:
  a synthetic customer reply with missing policy basis and unclear refund authority

Use:
  업무 문서 검수 카드
  plus merged overlay:
    상황 유형
    승인 주체/권한
    실패한다면 이유
    후속 확인
```

This test is better than another broad scan because it exercises the newly merged criteria against a concrete high-value use case.

## 13. Hard stop confirmation

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
```

`STATUS: ADAPTER_EXTERNAL_FRAMEWORK_MERGE_COMPLETED_WITH_WATCH`
