# Flow-Network Call Rules Post-Packet Dispatch Approval Patch v0

## 1. Verdict

```text
FLOW_NETWORK_CALL_RULES_NEED_POST_PACKET_DISPATCH_APPROVAL_PATCH_WITH_HOLD
```

## 2. Source

Hermes boundary sanity review:

```text
HERMES_FLOW_NETWORK_CALL_RULES_BOUNDARY_SANITY_RETURNED_WITH_WATCH
```

Report:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_flow_network_call_rules_boundary_sanity_v0/flow_network_call_rules_boundary_sanity_report.md
```

Hermes confirmed:

```text
IIC -> SOF -> MOL -> Packet -> Lane -> RML -> Recovery -> Promotion Gate is preserved.
Vague Hermes payload stops before execution.
Packet Builder is required before Hermes execution.
Packet draft != execution approval.
Hermes capability != permission.
Hermes success = receipt, not VectorFL approval.
```

## 3. Weakest Boundary

Hermes identified:

```text
Packet draft -> Hermes dispatch
```

Why:

```text
A well-formed packet can feel like a command.
Even if the document says "Packet does not equal execution approval",
operators may psychologically treat a finished packet as ready-to-run.
```

## 4. Patch Rule

Add this call rule:

```text
Post-Packet Dispatch Approval:
  After a Hermes packet is drafted,
  actual Hermes dispatch requires a separate explicit approval line.
```

Required approval line:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

or user-equivalent explicit approval:

```text
이 패킷으로 지금 헤르메스 실행해.
```

Default:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

## 5. Where This Fits

Updated sequence:

```text
IIC
  ->
SOF
  ->
MOL
  ->
Packet Builder
  ->
Post-Packet Dispatch Approval
  ->
Lane Execution
  ->
RML
  ->
Recovery
  ->
Promotion Gate
```

Short form:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

## 6. Applies To

Required for:

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
local report writing by Codex inside current approved task
read-only analysis that is performed directly in the current turn without external dispatch
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

## 8. WATCH

```text
1. Treating "packet complete" as "run approved".
2. Hiding dispatch approval inside a long prompt.
3. Reusing old approval for a modified packet.
4. Treating read-only sanity packet approval as approval for execution packet.
5. Treating Hermes dispatch approval as VectorFL promotion approval.
```

## 9. HOLD

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

## 10. Status

This is a call-rule candidate patch.

It is not:

```text
workflow
automation
policy
schema
registry
ontology
baseline
component
```
