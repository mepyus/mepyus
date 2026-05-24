# Flow-Network Call Rules State After Dispatch Approval Patch v0

## 1. Verdict

```text
FLOW_NETWORK_CALL_RULES_STRENGTHENED_WITH_POST_PACKET_DISPATCH_APPROVAL_GATE
```

## 2. Source

Hermes boundary sanity review identified the weakest boundary:

```text
Packet draft -> Hermes dispatch
```

Reason:

```text
A complete packet can feel like execution approval.
```

Patch source:

```text
FLOW_NETWORK_CALL_RULES_POST_PACKET_DISPATCH_APPROVAL_PATCH_V0.md
```

Updated call rules:

```text
VECTORFL_FLOW_NETWORK_CALL_RULES_V0_1.md
```

## 3. Updated Call Sequence

Old:

```text
IIC -> SOF -> MOL -> Packet -> Lane -> RML -> Recovery -> Promotion Gate
```

New:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

## 4. New Gate

```text
Post-Packet Dispatch Approval
```

Required approval line:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

Default:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

## 5. Meaning

Packet means:

```text
manifest
route permit
recovery contract
```

Packet does not mean:

```text
execution approval
promotion approval
workflow approval
skill approval
baseline approval
```

Dispatch approval means:

```text
this specific packet may be sent/executed now
```

Dispatch approval does not mean:

```text
VectorFL promotion
component approval
workflow creation
memory/skill/cron/config approval
```

## 6. Applies To

Required:

```text
Hermes execution
external tool execution
local command run delegated to external harness
any packet with write/persistence/side-effect possibility
any packet where tool capability is broad
```

Recommended:

```text
Gemini execution packets
Codex delegated worker packets
browser/tool packets
automation dry-run packets
```

Not required:

```text
plain chat
simple answer
local report writing by Codex inside the current approved task
read-only analysis performed directly in the current turn without external dispatch
```

## 7. Recovery Impact

Packet created but not dispatched:

```text
receipt:
  packet drafted

residue:
  pending dispatch boundary

candidate:
  possible future run
```

Packet dispatched with explicit approval:

```text
receipt:
  dispatch approval + run report + run receipt
```

Packet dispatched without explicit approval:

```text
STOP
```

## 8. Current Recovery Classification

```text
receipt:
  call rules v0.1 created with dispatch approval gate.

residue:
  packet-to-dispatch psychological pressure captured.

candidate:
  call rules strengthened.

component:
  no.

space_update_proposal:
  no.

STOP:
  any execution without explicit post-packet approval.
```

## 9. WATCH

```text
1. Dispatch approval hidden inside a long packet.
2. Old approval reused for a modified packet.
3. Read-only packet approval reused for execution packet.
4. Hermes dispatch approval treated as VectorFL promotion approval.
5. Dispatch gate becoming workflow/automation.
```

## 10. HOLD

```text
no Hermes dispatch without explicit post-packet approval
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
