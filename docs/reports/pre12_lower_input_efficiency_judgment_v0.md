# Pre-1.12 Lower Input Efficiency Judgment v0

## Verdict

`PASS_WITH_NOTE`

Efficiency should not be improved by changing everything. The first useful move is middle-layer thickening around compare-ready packaging, while keeping the existing segmentation and lower trace substrate mostly intact.

## Judgment Table

| area | judgment | reason |
| --- | --- | --- |
| 분절 단위 | `revise selectively` | Observer heading/timestamp/paragraph split is useful; raw dust sentence split is too fine for transcripts. Do not rewrite splitters globally. Add source-type-aware aggregation after split. |
| 의미단위 크기 | `thicken` | Raw transcript units remain too small or too generic. Meaning units should be lifted into topic/case blocks before line/axis use. |
| middle layer | `thicken first` | Existing reports already identify this as the main gap: noise suppression, case block aggregation, provisional frame sketch, compare-ready packaging. |
| preprocessing | `keep + refine` | External transcript preprocess already has before/after gates and probes. Refine criteria before direct ingest; do not replace it. |
| provenance/origin | `keep` | Structured routing has strong provenance, origin maps, receipts, and ledgers. The issue is not provenance absence. |
| label / anchor | `revise selectively` | Generic labels and anchors are useful diagnostics but overflatten raw transcripts. Add middle-layer separation of generic discourse vs topic-bearing anchors before changing labeler.py. |
| compare-ready packaging | `thicken` | This is the most important missing handoff object. Evidence-ready outputs are not always packet-candidate. |
| line/axis 연결 준비도 | `hold direct promotion; thicken prerequisites` | Lower can provide source and split evidence, but line/axis connection needs stable case blocks, candidate frames, and bridge rules first. |

## Most Important First Axis

The first axis to touch is not raw segmentation itself. It is compare-ready packaging after segmentation and preliminary extraction.

The target shape should preserve:

- source identity;
- split unit refs;
- generic vs topic-bearing anchor separation;
- candidate case blocks;
- readiness level;
- route residue;
- next upper bridge hint.

## Should Meaning Units Grow?

Yes, but not by simply making every segment larger. Meaning units should grow when:

- transcript markers and filler dominate dust units;
- flow remains flat after preprocessing;
- topic-bearing anchors are split across adjacent dust units;
- upper use needs case-level frame, not raw sentence evidence.

## Should Segmentation Rules Change?

Only selectively. The existing split modes are useful for visibility and trace. The safer move is to add a post-split grouping layer for raw/transcript-like materials. Directly patching `inputter.py` or `labeler.py` remains out of scope.

## Is Middle-Layer Thickening Still Core?

Yes. The missing layer is between generic extraction and case-level/line-level use. Without it, lower outputs look complete but require heavy human synthesis before upper CLI can use them.

## What Must Stabilize Before Line/Axis Reading Improves?

- source identity and origin;
- split unit refs;
- preprocess readiness;
- case block aggregation;
- generic/topic-bearing anchor separation;
- compare-ready packet-candidate criteria;
- lower -> upper field mapping.

## Validation

- Each keep/revise/thicken/hold judgment has a reason: PASS.
- The conclusion is not “fix everything”: PASS.
- The first action axis is narrow enough: PASS.
- The report avoids patching inputter/labeler/promotion logic: PASS.

## Next Stage Entry

Proceed to Pre-1.12 action map.
