# line thickening second grounded route validation v0

## verdict
PASS

## second route
- `scripts/process_structured_doc_with_routing.py --doc docs/reports/line_thickening_promotion_scope_v0.md --record-line-thickening`

## what changed
- Added a bounded `line_thickening` sink to the structured doc routing path.
- The adapter reads the generated `source_manifest`, `split_units`, `processing_trace`, `readable_input_board`, and `operator_summary`.
- It records one grounded observation packet with:
  - `validation_path_id=structured_doc_routing`
  - `evidence_mode=direct_span`
  - a concrete `split_units` row pointer

## verification result
- The observer route was refreshed first with `scripts/apply_internal_observer.py runtime frag_basic3_002 --record-line-thickening --bounded-recurrence-validation`.
- The structured doc routing path was then run with `--record-line-thickening`.
- `transition_over_surface` now has:
  - `distinct_path_count=2`
  - `distinct_source_family_count=2`
  - `distinct_surface_family_count=2`
  - `promotion_scope=cross_family_candidate`
- `input_to_reading_organ` remains strong, but this turn did not widen it further.

## why this is still bounded
- Only one second route was added.
- The existing observer route semantics remain intact.
- No UI, graph, ontology, or global rollout was added.
- The new packet is grounded and pointer-bearing, but it does not trigger global promotion.

## residual risk
- The second route is still only one additional validation path.
- Global validation remains intentionally out of reach until a separate, broader route exists.
