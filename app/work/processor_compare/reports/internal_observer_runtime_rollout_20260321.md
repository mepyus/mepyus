# Internal Observer Runtime Rollout

Date: 2026-03-21
Target: `/Users/sungsookim/universe/vectorfl_replica/runtime/fragments`

## Scope

- Applied the internal observer ensemble to all existing runtime fragments.
- Observer profiles:
  - `codex_like`
  - `chatgpt_like`
  - `gemini_like`
- Merge policy:
  - `codex_like + chatgpt_like` as main decision axis
  - `gemini_like` as secondary signal

## Command

```bash
python3 scripts/apply_internal_observer.py runtime
```

## Update Result

- Updated fragment count: `20`
- Updated fragment ids:
  - `frag_basic3_001`
  - `frag_basic3_002`
  - `frag_basic3_003`
  - `frag_basic3_004`
  - `frag_basic4_001`
  - `frag_basic4_002`
  - `frag_basic4_003`
  - `frag_basic4_004`
  - `frag_basic5_001`
  - `frag_basic5_002`
  - `frag_basic5_003`
  - `frag_basic5_004`
  - `frag_basic_001`
  - `frag_basic_002`
  - `frag_basic_003`
  - `frag_basic_004`
  - `frag_basic_005`
  - `frag_ytex_001`
  - `frag_ytex_002`
  - `frag_ytex_003`

## Aggregate Snapshot

- Scene counts:
  - `explanation`: `13`
  - `comparison`: `5`
  - `reflection`: `1`
  - `evidence`: `1`
- Confidence counts:
  - `mid`: `20`
- Observer role counts:
  - `support`: `9`
  - `contrast`: `5`
  - `definition`: `4`
  - `expansion`: `1`
  - `problem`: `1`
- Observer signal counts:
  - `gemini_reflection_signal`: `5`
  - `gemini_expansion_signal`: `5`
  - `role_disagreement`: `1`
- Anchor count range:
  - min: `4`
  - max: `8`
  - avg: `6.9`

## Sample Fragments

### `frag_basic_001`

- scene: `explanation`
- observer_role: `definition`
- confidence: `mid`
- numeric confidence: `0.685`
- ambiguity: `0.39`
- D/I/S: `0.77 / 0.63 / 0.64`
- sample anchors:
  - `AI`
  - `Claude`
  - `Agentic`
  - `Coding`
  - `CLAUDE.md`
  - `발표문`

### `frag_ytex_001`

- scene: `explanation`
- observer_role: `support`
- confidence: `mid`
- numeric confidence: `0.685`
- ambiguity: `0.39`
- D/I/S: `0.72 / 0.58 / 0.64`
- sample anchors:
  - `Google DeepMind`
  - `AlphaGo`
  - `이세돌`
  - `signature move`
  - `public shock`
  - `role.open_question`

### `frag_basic5_004`

- scene: `explanation`
- observer_role: `support`
- confidence: `mid`
- numeric confidence: `0.725`
- ambiguity: `0.47`
- D/I/S: `0.72 / 0.58 / 0.52`
- sample anchors:
  - `MoE`
  - `DeepSeek`
  - `MoE mainstream shift`
  - `routing modularity`
  - `sparsity`
  - `moe`

## Data Placement

The rollout writes observer outputs into each fragment record under:

- `anchors`
- `D`
- `I`
- `S`
- `scene`
- `confidence`
- `metadata.internal_observer`
- `metadata.observer_role`
- `metadata.observer_ambiguity`
- `metadata.observer_confidence_numeric`
- `metadata.observer_signals`
- `provenance_log`

Note:
- The fragment schema uses `provenance_log`, not `provenance`.
- Observer trace details are stored primarily in `metadata.internal_observer.merged` and `metadata.internal_observer.profiles`.

## Operational Meaning

- New ingest runs will now populate internal observer values automatically through `scripts/ingest_fragments.py`.
- Existing runtime fragments are now retrofitted and can be used as immediate Replica-side inputs for:
  - anchor connection
  - scene-aware grouping
  - conservative score-based filtering
  - observer signal inspection

## Immediate Next Steps

- Use the updated runtime fragment set as the first Replica-side test bed.
- Inspect how `scene`, `observer_role`, and merged anchors affect existing connection or layout logic.
- If needed, add a viewer-side debug panel for:
  - merged observer scene/role
  - ambiguity
  - observer signals

## Replica Integration Status

The rollout is now connected to Replica-side runtime consumers.

- Connection engine:
  - `observer_role` agreement and `observer_ambiguity` proximity now participate in relation scoring.
  - Edge reasons now expose:
    - `role_reason`
    - `ambiguity_reason`
- Dust field viewer:
  - node payload now includes:
    - `observer_role`
    - `observer_ambiguity`
    - `observer_confidence_numeric`
    - `observer_signals`
  - inspector and summary cards now show observer-side values
- Source fragment page:
  - fragment chips now expose:
    - `observer_role`
    - `observer_ambiguity`
    - `observer_confidence_numeric`
    - `observer_signals`

## Smoke Check

- `build_dust_field_data(runtime)` succeeded
  - dust nodes: `20`
  - edges: `9`
  - edge reason keys include `role_reason`, `ambiguity_reason`
- `build_source_fragment_view_data(runtime)` succeeded
  - source count: `5`
  - fragment count: `20`
  - observer metadata is present in source fragment records
