# X pointer graph operator view v0

Status: POINTER_ONLY_HOLD_NOT_AUTHORITY

## Purpose

This view connects the asset families discovered by Hermes into a Codex space-operation graph.

It does not move, delete, archive, promote, or authorize anything. It only says which family should be read with which other family when Codex needs to operate the space.

## Core Difference

Hermes result:

```text
asset families found
execution/cleanup/promotion boundary reached
STOP_AND_REVIEW
```

Codex space graph:

```text
which family lives in which layer
which family is safe to retrieve with which other family
which links are blocked
which reentry handles are missing
```

## Family Graph

```text
T/L_SCHEMA
  -> classifies all families
  -> NOT registry

U_RUN_BUNDLE_ASSET
  -> can feed P_PACKET_HANDOFF_ASSET
  -> only through validation/receipt/closeout evidence

G_GATE_GUARD_ASSET
  -> protects S_STATE_PROMOTION_ASSET
  -> guard is not approval

S_STATE_PROMOTION_ASSET
  -> marks authority-sensitive edges in X_POINTER_GRAPH
  -> does not promote anything

X_POINTER_GRAPH_ASSET
  -> connects P/U/G/S for retrieval
  -> pointer-only, not source of truth

B_BRIDGE_ADAPTER_ASSET
  -/-> S_STATE_PROMOTION_ASSET
  -> direct edge blocked
```

## Safe Links

```text
T/L_SCHEMA -> all families
G_GATE_GUARD -> S_STATE_PROMOTION
U_RUN_BUNDLE -> P_PACKET_HANDOFF
S_STATE_PROMOTION -> X_POINTER_GRAPH
X_POINTER_GRAPH -> P/U/G/S retrieval
```

## Blocked Or Scoped Links

```text
B_BRIDGE_ADAPTER -> S_STATE_PROMOTION
  blocked: external tool result must not mutate authority

P_PACKET_HANDOFF -> B_BRIDGE_ADAPTER
  scoped only: packet existence is not live-call approval

U_RUN_BUNDLE -> cleanup apply
  blocked: generated/evidence bundles cannot imply deletion

X_POINTER_GRAPH -> AUTHORITY
  blocked: pointer graph is not source of truth
```

## Retrieval Routes

Future Hermes closeout:

```text
U_RUN_BUNDLE
-> G_GATE_GUARD
-> S_STATE_PROMOTION
-> P_PACKET_HANDOFF
-> X_POINTER_GRAPH
```

Return product:

```text
space contact map
space effect classification
HOLD-only maturation proposal
```

Packet review without live call:

```text
P_PACKET_HANDOFF
-> U_RUN_BUNDLE
-> G_GATE_GUARD
-> B_BRIDGE_ADAPTER boundary
```

State/promotion confusion check:

```text
S_STATE_PROMOTION
-> G_GATE_GUARD
-> X_POINTER_GRAPH
```

## Current Pressures

```text
P/U duplicate pressure:
  packet summaries and run receipts can overlap but have different roles

S matured-authority confusion:
  matured evidence is still not authority

X graph-authority overclaim:
  pointer graph points at risky handles but is not itself authority
```

## Missing Handles

```text
ROLLBACK_MANIFEST_TEMPLATE
LAYER_POLICING_HANDLE
CODEX_SPACE_REENTRY_RECEIPT_SCHEMA
X_POINTER_GRAPH_NOT_AUTHORITY_HEADER
STALE_PACKET_RETENTION_POLICY
MATURED_VS_AUTHORITY_DECISION_GATE
```

## Next Safe Lane

```text
CODEX_SPACE_REENTRY_RECEIPT_SCHEMA_HOLD_ONLY
```

Reason:

Future Hermes outputs need a Codex-specific reentry receipt shape. That lets Codex separate:

```text
execution closeout
from
space operation / retrieval / maturation judgment
```

## Boundary

```text
NO_MOVE
NO_ARCHIVE
NO_DELETE
NO_SOURCE_EDIT
NO_PROMOTION
NO_AUTHORITY_MUTATION
NO_REGISTRY_MUTATION
NO_CURRENT_POSITION_MUTATION
NO_CLEANUP_APPLY
NO_LIVE_EXTERNAL_CALL
```

Final status:

```text
HOLD_NOT_AUTHORITY
```
