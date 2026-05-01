# Pre-1.12 Lower Input Process Remap v0

## Verdict

`PASS_WITH_NOTE`

The repository maps reasonably well to the user frame `분절 -> 생성 -> 번역 -> 추출 -> 흐름`, but the real process is not a clean linear pipeline. It is a set of partially overlapping lower-organ belts.

## Process Map

| user process | current 담당 자산 | 실제 기능 | 비어 있는 층 | 중복되는 층 | 얇은/섞인 층 |
| --- | --- | --- | --- | --- | --- |
| 분절 | `observer_ingest_min/run_observer_ingest_min.py`, `app/core/runtime/inputter.py`, `app/input_layer/segmenter/*`, `gpt_run/out_chat_split/*` | timestamp/heading/paragraph split; sentence/code/log/bullet dust split; raw chat split | source-type-aware semantic segmentation after preprocess | observer split vs dust split vs chat split | dust split is too fine for transcripts; observer split can be heading/title-only |
| 생성 | `process_structured_doc_with_routing.py`, observer generated outputs, receipts, manifests, external preprocess generated sidecars | creates manifest, split units, trace, board, operator summary, receipt, origin map, preprocess sidecars | compare-ready packet generation is not stable | generated board/summary/gmd read overlap | generated residue exists, but readiness level varies |
| 번역 | `gmd_native_read`, multi-lens runtime views, readable boards, operator summaries, docs/reports reinterpretation | translates split/source into operator-readable flow and role hints | source-to-line semantic translation remains manual-heavy | readable board vs operator summary vs multi-lens readout | translation and extraction blur in summaries |
| 추출 | `app/core/runtime/labeler.py`, `app/input_layer/labeler/labeler.py`, raw intake probes, preprocess comparison metrics, source locator | extracts labels, anchors, scene/flow, D/I/S, origin spans, gate metrics | topic-bearing anchors vs generic discourse anchors not separated enough | label extraction overlaps with translation summaries | extraction often occurs before middle-layer aggregation |
| 흐름 | readable input board, operator summary, `entry_execution_loop_v0`, projection/route policies, preprocess comparison readiness | records front/middle/end, route flow, residue return, next route/family hints | lower output -> upper packet admission rule | entry loop docs overlap with adapter contracts | flow is conceptual strong but runtime bridge thin |

## Where Stages Mix

### 분절 and 생성

Observer ingest splits and immediately writes generated artifacts. That is useful for visibility, but it means segmentation quality and generated output readiness are tightly coupled. A poor split still produces a complete-looking board and summary.

### 번역 and 추출

Operator summaries and GMD/native reads translate split units into readable claims while also extracting role hints and relation clues. This is productive, but it blurs whether a field is source-grounded extraction or human-facing interpretation.

### 추출 and 흐름

Route/projection policies read extracted signals such as `raw_input` or `preprocess_ambiguity` and immediately imply flow. The missing piece is a durable readiness gate between extracted signal and upper/next-loop handoff.

## Middle Layer Location

The middle layer sits between:

```text
raw split / generic label extraction
-> topic-bearing aggregation and compare-ready packaging
-> route or upper packet use
```

It is not a replacement for the inputter or labeler. It is the layer that suppresses discourse noise, preserves source identity, aggregates case-level blocks, sketches provisional frames, and packages compare-ready signals.

## Interpretation

The user’s 5-process language is accurate as an operating map, but the repository currently implements it as overlapping belts:

- 분절 is technically strong.
- 생성 is abundant.
- 번역 is present but manual/derived.
- 추출 is present but generic.
- 흐름 is documented but not fully bound to lower output readiness.

## Validation

- Each process is tied to actual files: PASS.
- The map avoids abstract-only claims: PASS.
- The map distinguishes lower material intake from upper request intake: PASS.
- The main thin layer is clearly identified as middle-layer packaging between extraction and flow: PASS.

## Next Stage Entry

Proceed to lower output readiness recheck.
