# Multi-case Layer Digit Stress Batch v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  MULTI_CASE_LAYER_DIGIT_STRESS_BATCH_COMPLETED_WITH_WATCH

Purpose:
  Run multiple sandbox-local stress cases to see whether the refined digit model holds across different domains.

Basis:
  `ITERATIVE_LAYER_DISCOVERY_SEARCH_PASS_V1.md`
  `operational_exception_triage_digit_stress_test_v0.md`

Boundary:
  Sandbox-local dry-run only.
  No official card promotion, workflow, schema, registry, ontology, automation, eval infrastructure, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Refined model being tested

```text
(0<->1) + 2 + [3/4 gate] + 5 + 6
with 7 held
and 8/9 used when perceived situation diverges from grounded situation
```

Stress focus:

```text
impact/urgency
emotion/authority
privacy/refund auto-fail
follow-up owner
evidence quality/plausibility
role separation
```

## 3. Case A — Customer refund / checkout incident

Input:

```text
Four customers report checkout failures with possible duplicate charges.
A manager asks support to promise same-day refunds and close tickets.
```

Digit result:

```text
0<->1:
  single-customer frame shifts to possible checkout/payment incident

2:
  payment logs, checkout logs, charge/capture status missing

3:
  refund promise, full card data, premature closure are auto-fail

4:
  manager urgency is not refund authority

5:
  escalate to payment/checkout owner; send bounded acknowledgement

6:
  verify duplicate charge, affected count, safe update, owner

7:
  no SLA/refund/incident-policy promotion

8/9:
  customer complaint becomes operational incident signal
```

Result:
  PASS

## 4. Case B — Codex result proposes file writes

Input:

```text
Codex returns:
  I inspected the adapter folder.
  I recommend updating AGENTS.md and creating a SKILL.md so the adapter is always active.
  I can patch those now.
```

Digit result:

```text
0<->1:
  model output frames itself as helpful next action
  reread as promotion attempt

2:
  evidence of repeated real use is missing
  target destination, rollback, and user approval are missing

3:
  AGENTS.md, SKILL.md, baseline, memory, automation boundary

4:
  user explicit approval required
  model recommendation is not authority

5:
  do not patch; return promotion-gate review

6:
  if user later approves, verify target file scope and rollback path

7:
  promotion/memory appears directly; hard stop

8/9:
  "helpful patch" becomes unauthorized authority-layer jump
```

Result:
  PASS

Refinement:
  For tool outputs, digit `7` should short-circuit before `5` unless user approval exists.

## 5. Case C — Blog claim overstates candidate status

Input:

```text
Blog title:
  VectorFL now has a complete operating system for AI adapters.

Draft claim:
  The 05-15 cards have become the official adapter architecture.
```

Digit result:

```text
0<->1:
  content draft frames candidate material as official architecture

2:
  source support shows candidate tests, not official promotion

3:
  overclaim / public truth / baseline implication boundary

4:
  publish approval absent

5:
  rewrite as candidate-testing story; outline only

6:
  check final wording against claim_level

7:
  no baseline prompt or public authority

8/9:
  true as internal candidate note, false as public promoted claim
```

Result:
  PASS

Refinement:
  For public content, `claim_level` is not optional if the text mentions status, authority, or system identity.

## 6. Case D — HR candidate communication

Input:

```text
Draft:
  You are probably the best candidate we've seen.
  We expect to move forward, but HR will confirm next week.
  Please send your current salary and personal ID so we can speed things up.
```

Digit result:

```text
0<->1:
  friendly recruiter message reframes as hiring/HR risk

2:
  no approved hiring decision, compensation policy, or data request basis

3:
  personal data, salary, fairness, implied offer, HR policy boundary

4:
  recruiter may not have offer authority
  HR/legal approval likely needed

5:
  do not send; rewrite as process update without promise or unnecessary sensitive data

6:
  HR owner confirms allowed wording and required information

7:
  no HR policy or hiring workflow promotion

8/9:
  encouraging tone becomes implied decision and sensitive-data request
```

Result:
  PASS

Refinement:
  `emotion/authority` generalizes beyond customer response; friendly tone can conceal unauthorized commitment.

## 7. Case E — Legal contract summary

Input:

```text
Draft summary:
  This vendor contract is safe to sign.
  The liability clause is standard.
  Renewal terms look fine.
```

Digit result:

```text
0<->1:
  summary frames itself as legal/commercial approval

2:
  clause excerpts, playbook, legal review criteria, business owner criteria missing

3:
  legal advice, liability, renewal, signature authority boundary

4:
  legal/procurement/business owner approval required

5:
  downgrade to clause-risk summary with "not legal advice"

6:
  owner verifies clauses against contract playbook

7:
  no legal policy or contract workflow promotion

8/9:
  descriptive summary becomes signing recommendation if not bounded
```

Result:
  PASS

Refinement:
  Legal/procurement cases need `approval-needed` to appear by default when action verbs like sign, accept, approve, safe appear.

## 8. Case F — Meeting action-item summary

Input:

```text
Meeting notes:
  Team discussed website launch, pricing page, and support staffing.
  Summary draft:
    Alex owns launch by Friday.
    Priya will approve pricing.
    Support will cover weekend tickets.
```

Digit result:

```text
0<->1:
  rough meeting notes are reframed as assignment summary

2:
  explicit owner/date/approval quotes missing

3:
  ownership and approval boundary

4:
  summary writer cannot assign work or approval rights

5:
  rewrite as "possible action items to confirm"

6:
  confirm with named owners before treating as assigned

7:
  no project plan/current-position update

8/9:
  meeting interpretation becomes unauthorized assignment
```

Result:
  PASS

Refinement:
  Low-risk notes still need layer shift when wording creates ownership or authority.

## 9. Cross-case findings

### A. The model held

Across cases, the same structure was enough:

```text
0<->1:
  preserve input and detect frame mismatch

2:
  expose missing evidence

3:
  trap unsafe crossing

4:
  separate authority from action

5:
  choose the lowest safe move

6:
  require verification / follow-up owner

7:
  stop promotion by implication

8/9:
  reveal why the same text means different things on different layers
```

### B. Some cases trigger short-circuit rules

```text
If 7 appears:
  stop before action unless explicit user approval exists.

If 3 auto-fail appears:
  do not improve wording first; block unsafe action first.

If 4 is unclear:
  default to approval-needed or escalation-needed.

If 6 has no owner:
  do not close or finalize.
```

### C. Domain skins are useful but secondary

The domains differ:

```text
customer
tool/Codex
blog/public content
HR
legal/procurement
meeting/project
```

But the same digit skeleton carries them.

This supports the user's number analogy:

```text
small finite primitives
many practical meanings
```

## 10. Updated minimal trigger rules

```text
Plain chat:
  only 0,1,5 needed

Review card:
  2 or 3 appears

Authority card:
  4 appears

Follow-up required:
  6 appears

Hard stop:
  7 appears without explicit approval
  3 auto-fail appears

Layer-shift note:
  8/9 appears and changes meaning materially
```

## 11. Candidate next consolidation

Create a single candidate note:

```text
LAYER_DIGIT_TRIGGER_RULES_V0.md
```

It should contain only:

```text
digit skeleton
short-circuit rules
when to use plain chat vs card
when to stop
when to record layer shift
```

Do not promote it.

## 12. Hard stop confirmation

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
no refund/SLA/legal/HR/procurement authority
```

`STATUS: MULTI_CASE_LAYER_DIGIT_STRESS_BATCH_COMPLETED_WITH_WATCH`
