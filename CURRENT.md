# VECTORFL Replica Current Baseline

## Current Definition

The replica currently treats `fragment` as the central object.

Each fragment is expected to preserve:

- source linkage
- anchor handles
- processing values
- provenance steps
- measurement records

The current direction is:

`source -> fragment -> anchor + processing values -> measurement retention -> observer layer -> source/space projection`

## What Is Working

- source documents can be stored under `runtime/source_documents/`
- fragment batches can be ingested through `scripts/ingest_fragments.py`
- source location enrichment works for sample inputs
- anchors are attached to fragments
- processing values remain attached to fragments
- fragments can be projected into materials
- source-side report generation works
- source-side report can separate:
  - cross-source related fragments
  - same-source related fragments
- additional document-like / conversation-like source batches can now be added and compared on the source side
- measurement-side report generation works
- ingest batch and session lineage are retained
- anchor history across retained runs can be summarized per fragment
- seed-bank based ambient anchor probe can be attached as sidecar measurement without changing primary anchors
- observer-layer records can now be retained:
  - `revision_judgment`
  - `connection_observation`
- source-side fragment view can now surface observer summary:
  - revision count
  - deferred connection count
  - rejected connection count

## Current Runtime Baseline

The runtime currently has all of the following:

- fragment store
- source document store
- source report
- measurement report
- work-session log

Current source-side and measurement-side reports:

- `runtime/reports/source_fragment_view.json`
- `runtime/reports/source_fragment_view.html`
- `runtime/reports/measurement_view.json`
- `runtime/reports/measurement_view.html`

## Current Policy Baseline

The current policy direction is already set by:

- `docs/policies/ANCHOR_V1.md`
- `docs/policies/MEASUREMENT_RETENTION_POLICY.md`
- `docs/policies/AMBIGUITY_REVIEW_POLICY.md`

Operationally this means:

- ambiguous values are retained
- re-ingest history is retained
- anchor changes are retained
- ambient seed resonance is retained as shadow measurement
- revision intent can be retained without overwriting current values
- rejected and deferred connection judgments can be retained without forcing edges
- failure to connect is acceptable
- failure to record is not acceptable

## Current Gaps

These are still open:

- viewer runtime confirmation is not fully stabilized because local port collisions happened during checks
- dialogue-specific preprocessing is not implemented yet
- anchor quality is improving but not complete
- document-like anchor ordering has been improved so `source.*` handles no longer dominate primary anchor selection as aggressively for `basic.md`-style inputs
- `basic3.md`-style long conversation blocks can now be ingested as comparison material
- `basic4.md`-style AI trend recap blocks can now be ingested as comparison material
- `basic5.md`-style technical architecture discussion blocks can now be ingested as comparison material
- conversational semantic primaries can now be lifted from surface tokens toward higher-level handles such as:
  - `semantic.future_of_work`
  - `semantic.fast_follower_risk`
  - `semantic.platform_shift`
  - `semantic.verification.difficulty`
- AI trend recap fragments can now retain stronger object/semantic handles such as:
  - `object.model.deepseek_r1`
  - `object.country.china`
  - `semantic.frontier_model_push`
  - `semantic.compute_constraint`
  - `semantic.deepseek_trigger`
- technical architecture fragments can now retain stronger handles such as:
  - `object.architecture.moe`
  - `object.architecture.dense_model`
  - `semantic.compute_multiplier`
  - `semantic.sparsity`
  - `semantic.moe_mainstream_shift`
  - `semantic.deepseek_recipe_diffusion`
- cross-source comparison between `basic.md` and `basic3.md` now has retained observer judgments:
  - accepted comparison candidates
  - deferred comparison candidates
- `basic4.md` now also has retained cross-source observer judgments:
  - accepted comparison candidate with `basic3.md`
  - deferred comparison candidate retained even when source-side related rows are still too weak to surface it
- `basic5.md` now also has retained cross-source observer judgments:
  - accepted comparison candidate with `basic4.md`
  - deferred comparison candidate with `basic3.md`
- source-side related fragment rows can now surface those observer judgments directly:
  - accepted/deferred/rejected relation status
  - retained reason text
- `app/runtime/*` and `app/core/runtime/*` still have wrapper ambiguity
- observer records currently exist as retained measurement types, but manual entry flow and review templates are still thin
- edge/local-space quality is not the current focus yet
- related-fragment quality is still early, but source-side comparison is now less collapsed into same-document-only hints

## Current Priority

The current priority is not forced connectivity.

The current priority is:

1. preserve source/fragment/measurement lineage
2. improve anchor quality without hiding prior outputs
   - especially reduce `source.*` overweight on document-like inputs
   - continue improving conversation-like sources so object / semantic / structural balance remains stable
3. keep observer-layer judgments (`revision`, `deferred`, `rejected`) visible without promoting them to current truth too early
   - include cross-source comparison judgments where useful
4. keep source-side inspection stronger than automatic connection claims
