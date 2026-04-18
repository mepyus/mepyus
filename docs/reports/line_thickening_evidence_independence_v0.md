# line thickening evidence independence v0

## verdict
PASS

## what changed
- Added `evidence_origin_kind` and `independence_class` to `RereadObservation`.
- Added registry / promotion basis fields:
  - `distinct_primary_source_family_count`
  - `distinct_derived_source_family_count`
  - `distinct_independent_evidence_count`
  - `has_self_referential_derived_support`
  - `evidence_independence_summary`
- Hardened promotion interpretation so global reading does not open just because the route count is two.

## verification result
- `internal_observer` observations classify as `primary_raw` / `primary`.
- `structured_doc_routing` observations classify as `derived_report` / `self_referential_derived`.
- `transition_over_surface` now reads as:
  - `distinct_path_count=2`
  - `promotion_scope=cross_family_candidate`
  - `distinct_independent_evidence_count=1`
  - `has_self_referential_derived_support=true`
- That is the intended split:
  - route diversity is real
  - independent corroboration is still limited

## why this matters
- It prevents one grounded route plus one derived report route from being misread as two independent corroborating sources.
- It keeps strong local/cross-path lines intact while blocking premature global interpretation.

## residual risk
- Historical logs still contain older rows without the new origin fields.
- Global corroboration still needs a third genuinely independent route if later warranted.
