# Runtime Commonization Scan

- scope: minimum observer-aware runtime baseline commonization
- mode: bounded backfill / no viewer change / no full rebuild

## current diagnosis

### live path
- already had observer-aware handoff
- material metadata carried `observer_or_ambiguity_trace`
- bridge/local-space enrichment was already visible

### imported docs
- before this patch: almost entirely `observer trace missing`
- after this patch: imported-doc materials now carry the same minimum observer baseline contract

### legacy materials
- before this patch: mixed state
- after this patch: almost all legacy/manual/live-probe materials now carry the same minimum observer baseline contract

### current bottleneck
- runtime baseline is now much more aligned
- but `live -> imported doc` mixed bridge formation is still weak under current bridge semantics

## exact changes

Files:
- [runtime_observer_baseline.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/runtime_observer_baseline.py)
- [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
- [runtime_space_anchor_sync.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/runtime_space_anchor_sync.py)
- [commonize_runtime_observer_baseline.py](/Users/sungsookim/universe/vectorfl_replica/scripts/commonize_runtime_observer_baseline.py)

Applied:
- observer materialization logic extracted into a common helper
- imported docs / legacy materials with missing observer baseline were selectively backfilled
- local spaces touching those materials were resynced
- bridges touching those local spaces were re-enriched
- `available=false` bridge cases now keep `unavailable_reason`

Not changed on purpose:
- viewer routes
- viewer rendering
- terrain
- region semantics
- full runtime rebuild

## verification

### material baseline counts

- imported docs
  - `available=true`: 845
  - `available=false`: 0
  - `none`: 0
- legacy or live-like
  - `available=true`: 12
  - `available=false`: 1
  - `none`: 0

The remaining `available=false` row is an older live probe placeholder path and is now an edge case, not the dominant path.

### fixed cases

#### imported docs
- `doc_004 <-> doc_005`
  - bridge: `brg_e4d1fa10fa46`
  - `bridge_reason_kind = canonical_shared_anchor_with_processing_overlap`
  - `observer_contribution.available = true`
- `doc_005 <-> doc_006`
  - bridge: `brg_f30a3a351a8b`
  - `bridge_reason_kind = canonical_shared_anchor_with_processing_overlap`
  - `observer_contribution.available = true`

#### legacy / live-like
- `test_live_space_sync_20260321 <-> test_canonical_ingest_20260321`
  - bridge: `brg_c84da4760249`
  - `observer_contribution.available = true`

#### mixed live ↔ legacy
- `engine_phase1_observer_probe_20260321 <-> test_canonical_ingest_20260321`
  - bridge: `brg_d138637f3f01`
  - `observer_contribution.available = true`

### local-space parity

- `doc_004`
  - `observer_or_ambiguity_trace.available = true`
  - `state_transition_summary = forming -> bridge_exposed`
- `test_canonical_ingest_20260321`
  - `observer_or_ambiguity_trace.available = true`
  - `bridge_exposure_count = 3`
- `engine_phase1_observer_probe_20260321`
  - `observer_or_ambiguity_trace.available = true`
  - `bridge_exposure_count = 2`

## mixed pair review

### live ↔ legacy
- yes
- verified through `engine_phase1_observer_probe_20260321 <-> test_canonical_ingest_20260321`

### live ↔ imported doc
- not yet observed as a stable bridge case
- attempted:
  - `engine_phase1_imported_doc_probe_20260321`
  - `engine_phase1_imported_doc_probe2_20260321`
- current reading:
  - observer-aware baseline is now commonized
  - but imported-doc-facing bridge opening still tends to stay weak or route toward other live/legacy spaces first

This means baseline commonization succeeded more clearly than bridge-parity commonization.

## current reading

Current level:
- `runtime-common observer baseline with partial legacy parity`

More precisely:
- materials: near-common baseline
- local spaces: common baseline present
- bridges: common field contract present
- mixed bridge formation: still uneven

## next recommendation

### next patch
- do not go back to viewer
- next engine patch should target bridge opening semantics for `live -> imported doc`

### likely next mismatch
- current bridge opening still favors canonical/shared-anchor plus existing relation traces
- imported docs now carry observer baseline, but bridge creation does not yet use that baseline strongly enough to open mixed bridges

### next question
- when a live probe semantically targets imported-doc anchors strongly enough to produce only `weak` traces,
  should bridge opening remain summary-threshold based,
  or should observer/process overlap be allowed to upgrade some weak paths into explicit possibility links?

## bottom line

This turn did not fully equalize richness.

But it did move the runtime from:
- `live-aware / imported-legacy-blind mixed runtime`

toward:
- `runtime-common observer baseline with partial legacy parity`

The remaining mismatch is no longer “observer trace missing everywhere”.

It is now:
- `bridge opening semantics are still uneven for live -> imported doc mixed cases`
