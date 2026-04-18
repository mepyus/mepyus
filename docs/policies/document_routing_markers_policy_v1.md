# document_routing_markers_policy_v1

## 1. Purpose
This policy fixes the lightweight routing markers used at the top of structured documents in `vectorfl_replica`.

The goal is to keep document intake stable without forcing heavy syntax.

## 2. Minimal Markers
Allowed top markers:

```text
[[DOCROLE:directive]]
[[RUNMODE:ingest_then_execute]]
[[PRIORITY:high]]
```

Korean aliases are also allowed.

## 3. Marker Meanings

### `DOCROLE`
Defines what kind of document this is.

Canonical values:
- `declaration`
- `baseline`
- `directive`
- `summary`
- `memo`
- `philosophical_interpretation`

### `RUNMODE`
Defines how the document should be routed.

Canonical values:
- `ingest_only`
- `ingest_then_execute`
- `reference_only`
- `execute_only`

### `PRIORITY`
Defines operational urgency only.

Canonical values:
- `high`
- `normal`
- `low`

## 4. Default Rules

### `DOCROLE`
- If missing and unclear: default to `memo`

### `RUNMODE`
- If missing: default to `ingest_only`

### `PRIORITY`
- If missing: default to `normal`

## 5. Normalization Rule
Users may write Korean aliases or light variants.

Codex must normalize them into canonical internal values before:
- registry update
- ticket creation
- event logging
- receipt writing
- board update

## 6. Recommended Routing
- `declaration` -> usually `ingest_only`
- `baseline` -> usually `ingest_only`
- `summary` -> usually `ingest_only`
- `memo` -> usually `ingest_only`
- `directive` -> usually `ingest_then_execute`
- external reference docs -> usually `reference_only`
- `execute_only` -> exceptional

## 7. Processing Order
Documents with routing markers should be handled in this order:

1. receive
2. parse
3. normalize
4. register
5. derive ticket if needed
6. execute if allowed
7. record events
8. write receipt
9. update latest board

## 8. Non-Marked Documents
Unmarked documents are not blocked from intake.

But they must not jump straight to execution.

Rule:
- missing `RUNMODE` => `ingest_only`

## 9. Output Expectation
Each processed document should leave:
- registry update
- event trail
- optional ticket
- receipt
- latest board reference

## 10. Current Lock
- Routing markers stay lightweight.
- Marker absence does not block intake.
- Execution requires explicit or normalized `RUNMODE`.
- Receipt and board are first-class outputs.
