# Integrated Engine Lower To Upper Bridge Candidate Selection v0

## 1. Verdict

PASS_WITH_NOTE

The safest first bridge example is a source bundle:

```text
source manifest + split units + processing trace
```

using one real lower-input run:

```text
codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_160042
```

This selection does not make the lower bundle an upper packet. It only selects a bounded evidence bundle for translation testing.

## 2. Candidate Bundles Considered

| candidate bundle | strength | weakness / risk | selection judgment |
| --- | --- | --- | --- |
| source manifest + split units + processing trace | Strong source identity, concrete segmentation, run trace, real generated artifacts | Split units can be overread as lines if not guarded | selected |
| label packet + routing basis + receipt | Strong route/authority evidence and low line-overread risk | Less content-bearing; bridge would test routing packet more than input evidence packet | not selected for first example |
| origin map + provenance link + source manifest | Strong provenance/source return support | Too source-handle-heavy; thinner as upper packet evidence body | not selected |
| GMD native read + split units + uncertainty notes | Rich reread support and closer to later line/translation work | Higher line-overread and maturity-overread risk | deferred |

## 3. Chosen Lower Bundle

### Bundle Type

Source bundle.

### Real Artifact Paths

- `app/work/observer_ingest_min/generated/source_manifest_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_160042.json`
- `app/work/observer_ingest_min/generated/split_units_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_160042.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_160042.json`

Optional readable support, not selected as packet body:

- `app/work/observer_ingest_min/generated/operator_summary_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_160042.md`

## 4. Why This Is The Safest First Bridge Example

It is strongest because:

- source identity is explicit
- source path is recoverable
- split mode is visible
- unit count and unit excerpts are visible
- run id is stable across the three selected artifacts
- processing trace states the lower engine stage

It is safer than GMD/multi-lens for the first example because:

- it stays closer to lower input formation
- it avoids immediate line/axis pressure
- it tests lower-to-upper evidence transfer before testing richer reread surfaces

It is more useful than a label/receipt routing bundle because:

- it carries content-bearing segmentation
- it can test whether lower evidence can become upper packet evidence input

## 5. What This Selection Does Not Claim

- It does not claim the bundle is an upper work packet.
- It does not claim automatic packetization.
- It does not claim a canonical lower-to-upper bridge.
- It does not treat split units as line artifacts.
- It does not claim the selected source document should be executed.

## 6. Phase 1 Validation

- Grounding check: passed. The selected bundle uses real generated lower-input artifacts.
- Line-overread check: passed with note. Split units are used as evidence chunks only, not lines.
- Canonical bridge check: passed. This is one bridge example, not a canonical bridge path.

