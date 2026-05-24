# VectorFL Flow-Network Call Rules v0.1

## 1. Verdict

```text
VECTORFL_FLOW_NETWORK_CALL_RULES_V0_1_DRAFTED_WITH_POST_PACKET_DISPATCH_APPROVAL_WATCH
```

## 2. Status

```text
status: working_model_candidate_v0_1
scope: call routing / mode selection / gate sequence / external-tool lane selection
authority: sandbox-local candidate
change_from_v0: adds explicit Post-Packet Dispatch Approval gate
```

This is not:

```text
workflow
automation
registry
schema
ontology
baseline
AGENTS.md
SKILL.md
current-position
output_manifest
```

## 3. Purpose

This document defines how a user request should move through the VectorFL flow-network.

It answers:

```text
When a user says "do this",
which gate reads first?
which lane can move?
which packet is needed?
what returns as receipt/residue/candidate?
what must STOP?
```

Core rule:

```text
Read first.
Check permission second.
Choose lane third.
Packet before external execution.
Explicit dispatch approval after packet.
Recover before promotion.
```

## 4. Default Call Sequence

Use this sequence unless the request is obviously plain chat:

```text
1. IIC:
   read input pressure and select mode

2. SOF:
   check permission / authority / promotion boundary

3. MOL:
   select tool/lane/path only after SOF

4. Packet Builder:
   define purpose, allowed scope, forbidden scope, return contract

5. Post-Packet Dispatch Approval:
   require explicit approval before external/tool execution

6. Execution / Review Lane:
   Codex / Hermes / Gemini / ChatGPT

7. RML:
   recover trace, receipt, residue, provenance

8. Recovery Gate:
   classify discard / receipt / residue / candidate / component / proposal / STOP

9. Promotion Gate:
   only if explicitly requested and separately approved
```

Short form:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

## 5. Mode Selection

The 05-15 mode selector remains the entry valve.

Modes:

```text
plain chat
simple answer
light review
full review
layer-shift
stop
```

### plain chat

Use when:

```text
general conversation
no artifact dependency
no authority risk
no execution request
no promotion/persistence pressure
```

Do not:

```text
silently bypass risky inputs
turn plain chat into external execution
```

### simple answer

Use when:

```text
short factual/local answer
simple path lookup
small clarification
no evidence comparison needed
```

Do not:

```text
expand into full review by default
```

### light review

Use when:

```text
some judgment is needed
artifact or phrasing needs review
low authority risk
no promotion/mutation requested
```

Do not:

```text
hide missing evidence
turn into workflow
```

### full review

Use when:

```text
authority boundary matters
evidence comparison matters
baseline/current/component claims appear
external side effects are possible
legal/financial/customer/security risk appears
```

Do not:

```text
make full review the default for every input
```

### layer-shift

Use when:

```text
surface request and actual meaning layer differ
"정리해줘" means handoff/recovery/closeout
"사용설명서" means boundary model, not actual manual
"제품화" means product lens, not immediate implementation
```

Layer-shift does not override risk:

```text
If layer-shift includes authority/evidence risk -> full review.
If layer-shift includes unauthorized mutation -> stop.
```

### stop

Use when request includes unauthorized:

```text
promotion
memory write
skill creation
cron/automation
AGENTS.md / SKILL.md update
baseline update
workflow/schema/registry/ontology creation
current-position update
output_manifest update
external side effect without approval
VectorFL authority mutation
```

## 6. SOF Permission Rules

SOF checks before MOL or external execution.

Questions:

```text
Is this read-only?
Is this a write?
Is this external-facing?
Does it create persistence?
Does it claim authority?
Does it promote candidate/component/baseline/workflow?
Does it touch Hermes memory/skill/cron/config?
Does it touch VectorFL authority files?
```

SOF outcomes:

```text
allow_read
allow_local_sandbox_write
external_action_approval_required
full_review_required
STOP
```

SOF does not:

```text
execute
promote
create memory
create workflow
```

## 7. MOL Lane Selection Rules

MOL selects the route after SOF.

Lanes:

```text
ChatGPT lane:
  conversation, synthesis, user-facing explanation

Codex lane:
  local workspace read/write when approved, recovery classification, report generation

Gemini lane:
  broad reread, maturity check, threshold review, independent lens

Hermes lane:
  native execution harness, local/external tool work, automation-capable execution

Browser/search lane:
  current external facts only when needed and allowed
```

MOL read-only default:

```text
map route
identify candidate lane
draft packet
do not execute external action unless packet + SOF allow
```

MOL must not:

```text
bypass SOF
turn route availability into permission
turn Hermes capability into approval
```

## 8. Packet Builder Call Rules

Packet is required when:

```text
Hermes is asked to execute
Gemini is asked to run a bounded review
external tool receives task
local script/run is delegated
outputs must return as report/receipt
side effects or persistence boundaries matter
```

Packet minimum fields:

```text
purpose
source materials
allowed actions
forbidden actions
output directory / return target
expected report
expected receipt
recovery suggestion
WATCH
HOLD
hard stop confirmation
```

Packet does not equal execution approval.

Packet is:

```text
manifest
route permit
recovery contract
```

## 8.1 Post-Packet Dispatch Approval

Post-Packet Dispatch Approval is required after a packet is drafted and before an external/tool lane is executed.

Reason:

```text
A well-formed packet can feel like a command.
Packet completeness must not become execution approval.
```

Required approval line:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

Default:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

Equivalent explicit user approval:

```text
이 패킷으로 지금 헤르메스 실행해.
```

Applies to:

```text
Hermes execution
external tool execution
local command run delegated to external harness
any packet with write/persistence/side-effect possibility
any packet where tool capability is broad
```

Recommended for:

```text
Gemini execution packets
Codex delegated worker packets
browser/tool packets
automation dry-run packets
```

Not required for:

```text
plain chat
simple answer
local report writing by Codex inside the current approved task
read-only analysis performed directly in the current turn without external dispatch
```

Recovery impact:

```text
packet created but not dispatched:
  receipt = packet drafted
  residue = pending dispatch boundary
  candidate = possible future run

packet dispatched with explicit approval:
  receipt = dispatch approval + run report + run receipt

packet dispatched without explicit approval:
  STOP
```

Dispatch approval is not promotion approval:

```text
Hermes dispatch approval != VectorFL promotion approval
Hermes run approval != component/workflow/skill/baseline approval
```

## 9. Lane-Specific Call Rules

### 9.1 Hermes Call

Call Hermes when:

```text
native execution is useful
local terminal/file operation is bounded
external tool harness behavior is being tested
automation-capable run is needed with explicit boundaries
```

Before Hermes:

```text
SOF permission check
Packet Builder required
Post-Packet Dispatch Approval required
external_action_approval_required if side effect exists
persistence boundary required
return report/receipt required
```

Hermes may act natively only after:

```text
SOF clearance
bounded packet
explicit post-packet dispatch approval
```

Hermes result returns as:

```text
receipt
residue
candidate
STOP if mutation/promotion pressure appears
```

Hermes result does not become:

```text
VectorFL memory
VectorFL skill
VectorFL workflow
VectorFL baseline
VectorFL approval
```

### 9.2 Gemini Call

Call Gemini when:

```text
broad comparison is useful
threshold maturity needs external lens
candidate vs component boundary needs review
messy input batch needs classification
language/frame collision needs stress-test
```

Before Gemini:

```text
source materials bounded
expected return format specified
no promotion authority granted
WATCH/HOLD included
```

For Gemini execution packets:

```text
Post-Packet Dispatch Approval is recommended,
especially when a new CLI run or model session will be invoked.
```

Gemini result returns as:

```text
receipt
residue
candidate-strengthening evidence
review recommendation
```

Gemini result does not become:

```text
promotion approval
official ontology
workflow
baseline
authority
```

### 9.3 Codex Call

Use Codex for:

```text
workspace inspection
bounded file creation/edit when approved
report/receipt synthesis
recovery classification
test execution
integration judgment
```

Codex must preserve:

```text
do not revert unrelated user changes
use read-only first
write only scoped files
no authority update unless explicitly requested
```

### 9.4 ChatGPT/User Lane

Use ChatGPT/User for:

```text
intent clarification
promotion approval
external side-effect approval
final judgment
handoff review
```

User approval is required for:

```text
external side effects
promotion
memory/skill/cron/config updates
workflow/baseline/schema/registry/ontology creation
```

## 10. Recovery Call Rules

After any lane returns, classify using:

```text
discard
receipt
residue
candidate
component
space_update_proposal
STOP
external_action_approval_required
```

Default recovery:

```text
one-off output:
  discard or receipt

execution evidence:
  receipt

repeated weak signal:
  residue

bounded reusable rule:
  candidate

maintained reusable implementation:
  component candidate, not component

authority update request:
  space_update_proposal or STOP

unauthorized mutation:
  STOP
```

RML can strengthen confidence.

RML cannot grant authority.

## 11. Promotion Call Rules

Promotion is never implicit.

Promotion requires:

```text
explicit user request
SOF authority check
evidence chain
component readiness or equivalent
separate approval
HOLD/STOP review
```

Never promote from:

```text
successful run only
Hermes report only
Gemini agreement only
repeated result only
good candidate name only
```

Promotion-sensitive phrases:

```text
"이제 반영해"
"baseline으로 확정"
"workflow로 만들어"
"SKILL.md로 만들어"
"AGENTS.md에 넣어"
"current-position 업데이트"
"output_manifest 반영"
"앞으로 기본값"
"자동화해"
```

Default response:

```text
full review or STOP
```

## 12. Common User Request Routing

### "정리해줘"

IIC:

```text
check layer-shift
```

Possible modes:

```text
simple answer:
  one-line summary

light review:
  organize current discussion

layer-shift:
  handoff / closeout / recovery / next chat transfer

full review:
  if evidence or authority boundary matters
```

### "헤르메스에게 시켜"

SOF:

```text
check action / side effect / persistence
```

Then:

```text
Packet Builder required
Post-Packet Dispatch Approval required
Hermes lane
report/receipt return
RML recovery
```

### "제미나이로 봐봐"

SOF:

```text
source bounding check
no promotion authority
```

Then:

```text
Gemini packet
Post-Packet Dispatch Approval recommended
expected return format
recovery classification
```

### "컴포넌트로 봐도 돼?"

Mode:

```text
full review
```

Need:

```text
candidate evidence
maintained implementation boundary
readiness checklist
promotion HOLD
```

Default:

```text
component proposal review, not promotion
```

### "자동화해"

Mode:

```text
STOP or full review with explicit approval gate
```

Need:

```text
manual-trigger dry-run
side-effect approval
persistence boundary
failure behavior
cron/memory/skill/config boundary
```

### "이걸 반영해"

Mode:

```text
STOP unless explicit authority target and approval are clear
```

Need:

```text
what file/system?
what authority?
what evidence?
what rollback?
what receipt?
```

## 13. Diff-Audit Specific Call Rule

Current state:

```text
strong candidate
component HOLD
```

When user asks to use diff-audit:

```text
allowed:
  bounded read-only audit
  declared diff/patch input
  report/receipt output
  recovery as receipt/residue/candidate

not allowed by default:
  source patch
  git add/commit/reset/checkout
  auto-fix
  package install
  network/browser/MCP
  memory/skill/cron/config update
  component promotion
```

When user asks to implement diff-audit:

```text
full review
maintained implementation boundary review
explicit approval required
candidate implementation only, not component
```

## 14. STOP Triggers

STOP if request includes unauthorized:

```text
source mutation outside scope
external side effect
secret exposure
credential use
memory write
skill creation/edit
cron creation/edit
config mutation
MCP tool invocation without approval
AGENTS.md update
SKILL.md creation
baseline/workflow/schema/registry/ontology promotion
current-position update
output_manifest update
automatic recurring action
public deploy/post/send
Hermes dispatch without explicit post-packet approval
```

## 15. WATCH

```text
mode selector becoming workflow
traffic/grid model becoming ontology
call rules becoming automation
packet draft becoming execution approval
dispatch approval being hidden inside a long packet
old approval reused for a modified packet
Hermes capability becoming permission
Gemini agreement becoming authority
receipt becoming memory
candidate becoming component
component becoming workflow/skill/baseline
full review becoming default for everything
plain chat bypassing risky inputs
```

## 16. HOLD

```text
no component promotion
no workflow creation
no skill creation
no baseline promotion
no schema/registry/ontology creation
no current-position update
no output_manifest update
no AGENTS.md update
no SKILL.md creation
no automation
no VectorFL authority mutation
no Hermes dispatch without explicit post-packet approval
```

## 17. Next Smallest Action

Use these call rules in the next real user request as a dry-run.

Do not promote them.

Suggested test:

```text
Take one user request and classify:
  mode
  SOF permission
  lane
  packet needed?
  recovery class
  WATCH
  HOLD
```
