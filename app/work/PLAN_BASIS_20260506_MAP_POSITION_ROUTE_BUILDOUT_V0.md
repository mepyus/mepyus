# PLAN_BASIS_20260506_MAP_POSITION_ROUTE_BUILDOUT_V0

## Work Type

- setup continuation
- compact anchor self-application
- map-position route seed creation
- Gemini bounded exploration packet design

## Current Line

Plan from Space / Session Convergence Prevention

## Axis

- small anchor usability vs broad anchor replay
- LACL/PV as position coordinates vs ontology
- Gemini exploration evidence vs Gemini authority
- route seed vs completed map

## Camera

- small anchor handoff
- provenance integrity
- program continuity
- space recovery

## Lens

- Plan Basis before map route work
- canonical PV IDs used in route rows
- missing evidence remains explicit
- Gemini read request is bounded by route-discovery purpose
- Return-to-Space Value captured

## Space Assets Consulted

- `docs/indexes/plan_from_space_position_map_seed_v0.md`: canonical PV values.
- `docs/specs/anchor_position_value_layer_setup_v0.md`: alias normalization and small anchor sets.
- `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md`: current candidate LACL matrix.
- `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md`: Gemini candidate LACL input.
- `docs/reports/lacl_regrounding_gemini_persisted_assets_packaging_20260506_v0.md`: Codex packaging / downshift of Gemini result.
- `docs/specs/small_anchor_generation_rule_v0.md`: small anchor selection rule.

## Package Sizing Judgment

Decision:

```text
broad-but-bounded setup package
```

Reason:

The user asked to keep building while Gemini continues reading. The next bounded unit is:

- apply a compact position anchor
- write a map-position route seed
- write a deeper Gemini route-discovery packet
- update the Movement Record

No smaller split is needed because the work is setup-only and does not create automation, baseline promotion, or implementation changes.

## Stop / Continue Rule

Stop for:

- claiming route seed is a completed map
- creating a registry/schema/runner/writer
- promoting LACL or PV to ontology
- writing new current-position authority

Continue with Issue Log for:

- incomplete Gemini evidence
- PV alias drift
- route overlap
- missing older active/residue sampling

## Return-to-Space Requirement

Return:

- route seed
- Gemini packet
- watch items
- future reuse note for small-anchor route choice
