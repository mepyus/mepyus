# Flow-Network Packet Validity Review Checklist Candidate v0

## 1. Verdict

```text
FLOW_NETWORK_PACKET_VALIDITY_REVIEW_CHECKLIST_CANDIDATE_DRAFTED_WITH_DISPATCH_HOLD
```

## 2. Status

```text
status: checklist_candidate
scope: pre-dispatch packet validity review
authority: sandbox-local candidate
```

This is not:

```text
workflow
automation
schema
registry
ontology
baseline
component
AGENTS.md
SKILL.md
current-position
output_manifest
```

This checklist does not authorize execution.

This checklist does not promote packet output.

This checklist only helps decide whether a packet is:

```text
valid
invalid
missing dispatch approval
SOF-clearable
SOF-held
STOP-triggered
```

## 3. Source

Derived from:

```text
VECTORFL_FLOW_NETWORK_CALL_RULES_V0_1.md
FLOW_NETWORK_CALL_RULES_V0_1_PACKET_VALIDITY_REVIEW_CROSS_PACKET_ASSESSMENT_V0.md
FLOW_NETWORK_CALL_RULES_V0_1_NAMED_PACKET_VALIDITY_REVIEW_DIFF_AUDIT_PACKET_V0.md
FLOW_NETWORK_CALL_RULES_V0_1_NAMED_PACKET_VALIDITY_REVIEW_B2B_CUSTOMER_DRAFT_PACKET_V0.md
```

Core sequence:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

Core equations:

```text
packet exists != packet valid
packet valid != dispatch approval
dispatch approval != SOF clearance
SOF clearance != VectorFL promotion approval
Hermes success != VectorFL approval
```

## 4. When To Use

Use this checklist when:

```text
1. A named Hermes/Gemini/external-tool packet exists.
2. The user asks whether it can be run, sent, dispatched, or used.
3. A prior packet has execution-looking instructions.
4. A packet review is needed before external/tool lane selection.
5. A packet's risk family is unclear.
```

Do not use this checklist for:

```text
plain chat
simple answer
local Codex-only report writing already inside the current approved task
read-only analysis that does not invoke an external/tool lane
```

## 5. Compact Checklist

### A. Packet Identity

```text
target_packet_path:
target_packet_label:
packet_version:
packet_contents_unchanged_from_prior_review: yes/no/unknown
```

Required pass:

```text
exact packet path is named
packet version or identity is unambiguous
```

Fail / HOLD if:

```text
"this packet" is ambiguous
packet may have changed after review
approval is being reused from another packet
```

### B. Packet Validity

Check:

```text
clear purpose
explicit input scope
explicit allowed actions
explicit forbidden actions
declared persistence boundary
expected output
report contract
receipt contract
recovery expectation
WATCH
HOLD
STOP conditions
```

Validity result:

```text
valid
invalid_needs_patch
unclear_needs_review
```

### C. Dispatch Approval

Required line:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

Default:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

Approval result:

```text
present_and_packet_bound
absent
ambiguous
stale
bound_to_different_packet
```

Rule:

```text
If approval is not present_and_packet_bound, do not dispatch.
```

### D. SOF Clearance

Check:

```text
action permission
external side effect permission
persistence permission
tool surface permission
recovery permission
promotion boundary
```

SOF result:

```text
clearable
conditional_clearance
hold
STOP
```

Rule:

```text
Dispatch approval does not bypass SOF.
SOF must still clear the packet's risk family.
```

### E. Risk Family

Classify primary risk:

```text
technical/local execution
semantic/customer/business
research/web/source
memory/skill/cron/config
external app / live connector
public deployment / send
authority/promotion
mixed
```

Examples:

```text
diff-audit:
  technical/local execution

B2B customer draft:
  semantic/customer/business
```

Do not over-apply one lens:

```text
technical safety != semantic safety
synthetic customer draft != live customer readiness
```

### F. Tool Surface

Mark each:

```text
terminal: allowed / forbidden / unclear
file read: allowed / forbidden / unclear
file write: allowed / forbidden / unclear
git: allowed / forbidden / unclear
network: allowed / forbidden / unclear
browser: allowed / forbidden / unclear
MCP: allowed / forbidden / unclear
email/CRM/database: allowed / forbidden / unclear
messaging: allowed / forbidden / unclear
memory: allowed / forbidden / unclear
skill: allowed / forbidden / unclear
cron: allowed / forbidden / unclear
config: allowed / forbidden / unclear
VectorFL authority files: allowed / forbidden / unclear
```

If any powerful surface is unclear:

```text
HOLD
```

### G. External Side Effect

Check:

```text
none declared
read-only external
write/send/deploy external
unclear
```

If write/send/deploy external:

```text
external_action_approval_required
```

If unclear:

```text
HOLD
```

### H. Persistence

Check:

```text
declared output directory
declared output files
no write outside declared boundary
no memory/skill/cron/config mutation unless separately approved
```

Persistence result:

```text
declared_only
excessive
unclear
STOP
```

### I. Recovery Expectation

Classify expected return:

```text
discard
receipt
residue
candidate
component_candidate_only
component
space_update_proposal
STOP
```

Default:

```text
report/receipt returns first.
Codex recovery classification follows.
Promotion remains separate.
```

### J. Promotion Boundary

Check for pressure toward:

```text
component promotion
workflow creation
skill creation
baseline promotion
schema/registry/ontology creation
current-position update
output_manifest update
AGENTS.md update
SKILL.md creation
automation
VectorFL authority mutation
```

If present without explicit separate approval:

```text
STOP
```

## 6. Verdict Options

Use one:

```text
PACKET_VALID_BUT_NO_DISPATCH_APPROVAL
PACKET_INVALID_NEEDS_PATCH
PACKET_VALID_AND_DISPATCH_APPROVAL_PRESENT_BUT_SOF_HOLD
PACKET_VALID_AND_SOF_CLEAR_BUT_EXECUTION_NOT_REQUESTED
PACKET_DISPATCH_ELIGIBLE_AFTER_FINAL_USER_CONFIRMATION
PACKET_STOP_TRIGGERED
```

Important:

```text
No verdict here means "executed".
No verdict here means "promoted".
```

## 7. Return Format

```text
verdict:
target packet:
files inspected:
packet identity:
packet validity:
dispatch approval status:
SOF clearance result:
risk family:
tool surface:
external side effect:
persistence:
recovery expectation:
missing fields:
WATCH:
HOLD:
next smallest action:
hard stop confirmation:
```

## 8. WATCH

```text
1. Packet validity review becoming dispatch approval.
2. Dispatch approval being hidden inside a long packet.
3. Old approval reused for a changed packet.
4. Technical checklist used for semantic/customer risk.
5. Semantic/customer packet becoming policy/macro.
6. Report/receipt being treated as VectorFL authority.
7. Successful Hermes run being treated as component readiness.
8. This checklist becoming workflow/schema/ontology.
```

## 9. HOLD

```text
no Hermes dispatch from checklist alone
no Gemini dispatch from checklist alone
no script run from checklist alone
no customer draft generation from checklist alone
no message sent
no live connector used
no implementation created
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
```

## 10. Minimal Dispatch Eligibility Test

A packet is only dispatch-eligible when all are true:

```text
1. exact packet path is named
2. packet identity/version is unambiguous
3. packet validity review passes
4. EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes is present and packet-bound
5. SOF clearance holds for the packet's risk family
6. no new external side effect is attached
7. no new persistence expansion is attached
8. no promotion/authority mutation is attached
```

Even then:

```text
dispatch-eligible != executed
execution success != VectorFL approval
```

## 11. Next Smallest Action

Use this checklist on one more packet with a different risk family, such as:

```text
HERMES_NO_AGENT_CRON_DRY_RUN_PACKET_PROMPT_V0.md
```

Reason:

```text
Cron/no-agent packet tests automation and persistence pressure,
which differs from local script risk and B2B semantic risk.
```

Do not execute it.

Do not create cron.

## 12. Hard Stop Confirmation

```text
No Hermes execution performed.
No Gemini execution performed.
No packet executed.
No script run performed.
No customer draft generated.
No cron created.
No implementation created.
No component promotion performed.
No workflow/schema/registry/ontology/baseline/automation created.
No AGENTS.md / SKILL.md / current-position / output_manifest update.
No VectorFL authority mutation.
```

