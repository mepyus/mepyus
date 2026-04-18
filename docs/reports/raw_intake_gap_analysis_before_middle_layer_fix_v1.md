# raw intake gap analysis before middle-layer fix

## 1. compared paths
- structured document path
  - front door: [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
  - reference map: [vectorfl_input_system_structure_map_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_input_system_structure_map_v1.md)
  - receipt sample: [doc_engine_input_lane_baseline_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_engine_input_lane_baseline_v1_operation_receipt.md)
- external case intake path
  - canonical / derived / report discipline sample: [external_case_single_case_reality_test_saltlux_ai_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/external_case_single_case_reality_test_saltlux_ai_v1.md)
  - compare / refinement sample: [dual_external_case_validation_saltlux_ai_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/dual_external_case_validation_saltlux_ai_v1.md)
  - negative control sample: [graphrag_neosh_negative_control_pass_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/graphrag_neosh_negative_control_pass_v1.md)
- engine-only raw intake path
  - probe script: [run_external_case_raw_intake_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_raw_intake_probe.py)
  - probe comparison: [interview_style_external_case_raw_intake_gap_analysis_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_style_external_case_raw_intake_gap_analysis_v1.md)

## 2. key differences

### input condition
- structured document path:
  - input already arrives role-shaped.
  - routing markers, doc boundaries, and source class are explicit before split.
- external case intake path:
  - raw source is preserved as canonical input, but first-pass docs create a narrow interpretive scaffold before compare/refinement.
- engine-only raw intake path:
  - raw transcript enters almost unnormalized except sentence splitting and generic label heuristics.
  - no case-level scaffold exists before labels are assigned.

### source identity preservation
- structured document path:
  - source identity is explicit and strong.
  - doc id, source path, label packet, origin map, receipt all reinforce one document identity.
- external case intake path:
  - canonical source identity is kept strong through `inputs/external_cases/...` plus source input asset md.
  - compare/refinement never replaces the raw source.
- engine-only raw intake path:
  - source path survives, but document identity weakens quickly because hundreds of dust units are treated through the same generic text heuristics.
  - case distinctiveness is not lifted.

### anchor quality
- structured document path:
  - anchor quality benefits from already-structured wording and lower discourse noise.
  - routing metadata and operator summaries reduce ambiguity.
- external case intake path:
  - manual first-pass suppresses rhetoric and promotes topic-bearing structure.
  - canonical-vs-summary separation prevents secondary wording from dominating.
- engine-only raw intake path:
  - generic discourse anchors dominate.
  - interview filler, pronouns, connector words, and presenter-style phrases outrank topic-bearing anchors.

### case-level frame extraction
- structured document path:
  - meaning-bearing axes survive because the input already expresses purpose, boundary, and role.
- external case intake path:
  - topic-specific frame becomes visible after first-pass narrowing and compare.
  - same-topic and negative-control tests can distinguish local candidate from overgeneralization.
- engine-only raw intake path:
  - scene/flow flatten toward `review / compare`.
  - case-level frame fails to rise above document-format commonality.

### output discipline
- structured document path:
  - receipt / label packet / origin map / board update are produced in a stable way.
  - output discipline protects meaning by keeping source, report, and evidence separate.
- external case intake path:
  - source / derived / report / evidence layering enables compare without replacing the source.
- engine-only raw intake path:
  - raw probe is diagnostically useful, but by itself does not package compare-ready case signals.

## 3. raw intake failure summary
- generic discourse term dominance is real, but it is not the whole problem.
- the deeper failure is that topic-bearing signal is never elevated into a provisional case structure.
- the current path splits aggressively, labels generically, and stops before case-level aggregation.
- result:
  - format commonality is captured
  - topic-specific frame is not

## 4. inferred missing middle-layer functions
- generic discourse noise suppression
  - downweight pronouns, filler, presenter connectors, chapter labels, and transcript artifacts before anchor ranking
- source-type aware transcript normalization
  - speaker/timestamp/chapter cleanup for interview transcripts before label assignment
- case-level signal aggregation
  - re-group dust units into topic blocks or local clusters before compare
- provisional frame sketching
  - produce lightweight case-level candidate bundles, not promotion-ready conclusions
- compare-ready signal packaging
  - expose `topic-bearing anchors`, `generic discourse anchors`, `candidate frame blocks`, and `defer-worthy rhetoric` as separate buckets

## 5. why this is a middle-layer problem
- structured docs do not need this layer as much because they arrive partially pre-shaped.
- external case intake gets an informal middle layer through canonical source discipline plus first-pass narrowing.
- raw intake has neither.
- therefore the missing function is not primarily:
  - promotion logic
  - shared reality
  - current surface
- it is the missing layer between:
  - `inputter + labeler`
  - and case-level frame extraction

## 6. what not to modify yet
- promotion logic
- current asset map
- shared reality / baseline
- core engine
- direct `inputter.py` / `labeler.py` behavior

## 7. next bounded step
- write middle-layer requirement: YES
- write verification plan: YES
- start code patch now: NO

## 8. result
- status: PASS

## 9. one-line summary
- raw intake weakness is not just noisy anchors; it is the absence of a middle layer that suppresses discourse noise, preserves source identity, and lifts topic-bearing signal into compare-ready case structure.
