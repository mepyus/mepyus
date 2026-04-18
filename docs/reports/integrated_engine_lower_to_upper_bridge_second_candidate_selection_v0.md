# Integrated Engine Lower To Upper Bridge Second Candidate Selection v0

## 1. Verdict

PASS_WITH_NOTE

The second controlled bridge example selects a routing bundle:

```text
label packet + routing basis + receipt
```

This bundle is different from the first source bundle and tests whether routing/authority material can support an upper packet input without becoming execution approval.

## 2. Preconditions Applied

| precondition | result |
| --- | --- |
| provenance sufficiency | pass: source doc id/ref and source path appear in label packet/receipt |
| segmentation legibility | not central: this is a routing bundle, not content split bundle |
| trace sufficiency | pass: operation receipt includes run identity, events, generated files, commands |
| bundling sufficiency | pass: label packet + receipt + registry/ticket references are complementary |
| route legibility | pass: `DOCROLE=directive`, `RUNMODE=ingest_then_execute`, `PRIORITY=high`, ticket created |
| non-line-overread condition | pass: no split/GMD line material is used as evidence body |
| packetization threshold | caution: upper purpose, authority, actions, output, and route must still be added |

## 3. Candidate Bundles Considered

| candidate | bridge value | blocker pressure | judgment |
| --- | --- | --- | --- |
| label packet + routing basis + receipt | Strong route/authority evidence; low line-overread pressure | Execution-linkable can be mistaken for execution complete | selected |
| origin map + provenance link + source manifest | Strong source-return evidence | Too source-handle-heavy for second contrast | not selected |
| GMD native read + split units + uncertainty | Rich reread evidence | Higher line and maturity overread risk | deferred |

## 4. Selected Real Artifacts

- `runtime/manifests/label_packets/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_label_packet.json`
- `runtime/receipts/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_operation_receipt.md`
- registry/ticket references in:
  - `runtime/manifests/structured_internal_docs_registry_v1.json`
  - `runtime/manifests/ticket_registry_v1.json`

## 5. Why This Is The Best Second Example

It tests a different bridge dimension:

- first example tested source/content evidence transfer
- second example tests route/authority evidence transfer

It is safer than a GMD/multi-lens second example because:

- it avoids line-overread pressure
- it keeps the bridge focused on routing and authority boundaries
- it exposes a different failure pattern: execution-linkable vs executed/approved confusion

## 6. What This Selection Does Not Claim

- `execution_linkable=true` is not execution complete.
- `ticket_created=yes` is not user approval.
- receipt final status is not semantic correctness.
- routing bundle is not an upper packet by itself.
- this is not a canonical lower-to-upper bridge.

## 7. Phase 2 Selection Validation

- Preconditions check: passed with caution. The bundle is eligible, but upper context remains mandatory.
- Blocker usage check: passed. Execution-linkable overread is named as the key caution.
- Honest evaluation setup: passed. The example may remain dependency-heavy; improvement is not forced.

