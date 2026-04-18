# vectorfl_replica repo-wide structure and trace survey v1

## 0. Why this note exists

This note records a repo-wide structural survey of `vectorfl_replica` focused on the full space, not just the current runtime layer.

The point of the survey is not inventory for its own sake. The point is to locate:

- where the governing philosophy is actually declared
- where raw inputs are kept
- where first-pass materials are promoted
- where operational traces are recorded
- where the current reading/observation organs already exist
- where the structure is still thin or missing

## 1. What was actually inspected

The survey walked the repo through these hubs:

- root baseline docs
  - `CURRENT.md`
  - `vectorfl_status.md`
  - `vectorfl_philosophical_interpretation_v1.md`
  - `codex_content_pack.md`
  - `codex_processor_standard.md`
- source asset layers
  - `source_assets/declarations`
  - `source_assets/baselines`
  - `source_assets/directives`
  - `source_assets/external_case_inputs`
- raw input layers
  - `inputs/`
  - `inputs/external_cases/`
- documentation layers
  - `docs/contracts`
  - `docs/policies`
  - `docs/examples`
  - `docs/specs`
  - `docs/reports`
- engine layers
  - `app/core`
  - `app/input_layer`
  - `app/fragment`
  - `app/measurement`
  - `app/runtime`
  - `app/work`
  - `app/events`
- runtime trace layers
  - `runtime/receipts`
  - `runtime/logs`
  - `runtime/manifests`
  - `runtime/observer`
  - `runtime/views`

## 2. What the repo is, structurally

The repo is not just an app, and not just a document archive.

It already has a multi-layer operating structure:

1. `source_assets` and `inputs` hold the raw and first-pass materials.
2. `docs/policies`, `docs/contracts`, and `docs/specs` hold the operating rules and hard boundaries.
3. `app/input_layer`, `app/fragment`, `app/measurement`, `app/runtime`, and `app/core` hold the engine bodies.
4. `runtime/receipts`, `runtime/logs`, `runtime/manifests`, `runtime/observer`, and `runtime/views` hold the persistent operating traces and read surfaces.
5. `docs/reports` and `docs/examples` hold the interpretive outputs, comparative runs, and example-driven learning artifacts.

That means the repo already behaves like a traceable engine workspace, not a passive file tree.

## 3. The main flows that are already alive

### 3.1 Declaration / baseline / directive -> operation

The root philosophy and the source asset folders agree on the same flow:

- `declaration`, `baseline`, `directive` are not just prose.
- They are source assets that become intake material.
- Their top markers (`DOCROLE`, `RUNMODE`, `PRIORITY`) are normalized and routed.

This is not theoretical. The repo already has:

- `source_assets/declarations/*.md`
- `source_assets/baselines/*.md`
- `source_assets/directives/*.md`
- `runtime/receipts/*`
- `runtime/manifests/*`

This means the docs are already feeding execution traces.

### 3.2 Raw input -> first-pass material -> reportable record

The `inputs/external_cases/` folder holds raw inputs such as:

- `choi_ai_classroom_vlm.txt`
- `choi_ai_classroom_cnn.txt`
- `choi_ai_classroom_transformer1.txt`
- `choi_ai_classroom_transformer2.txt`
- `saltlux_ai.txt`
- `saltlux.txt`
- `andrej_karpathy_youtube.txt`
- `dario_amodei_youtube.txt`
- `alexkarp_youtube.txt`

The corresponding first-pass source assets are already split into:

- `source_assets/external_case_inputs/*`
- `docs/examples/external_case_first_pass_*`

This shows the repo already distinguishes:

- raw source
- first-pass case asset
- report / compare artifact

### 3.3 Input layer -> fragment -> measurement -> runtime projection

The current engine definition is still consistent across the root docs and code layers:

- source is preserved
- fragment is the central object
- anchor and processing values are attached
- provenance and measurement are retained
- observer records are kept
- views and reports surface the runtime state

This is visible in:

- `CURRENT.md`
- `vectorfl_status.md`
- `app/input_layer/*`
- `app/fragment/*`
- `app/measurement/*`
- `app/runtime/*`
- `runtime/views/*`
- `runtime/receipts/*`

### 3.4 Work sessions -> reports -> receipts -> latest surfaces

The runtime trace layers are not empty. They already contain:

- receipts
- logs
- manifests
- operation boards
- latest/read surfaces

So the repo is already maintaining a traceable operating history rather than only transient execution.

## 4. What is already strong

### 4.1 The control / policy surface is real

The repo has an explicit operating contract stack:

- `source_assets/declarations`
- `source_assets/baselines`
- `source_assets/directives`
- `docs/policies`
- `docs/contracts`
- `app/work/current_layer_baseline`

This is enough to tell that the project is not ad hoc. It has rule memory.

### 4.2 The runtime trace stack is real

The repo has a substantial runtime trace layer:

- `runtime/receipts`
- `runtime/logs`
- `runtime/manifests`
- `runtime/observer`
- `runtime/views`

This means the repo already stores operations as records, not just as current state.

### 4.3 The raw input / first-pass split is real

The repo does not collapse raw inputs into derived outputs too early.

That split is visible in:

- `inputs/`
- `source_assets/external_case_inputs/`
- `docs/examples/`

This is important because the whole space is trying to preserve read path, not only end state.

## 5. What is still thin or missing

### 5.1 Some folders are present only as conceptual layers

The root and status docs talk about `references/`, but no `references/` directory is present in this checkout.

That means the repo currently describes a reference memory layer more strongly than it materializes it on disk.

### 5.2 Some status surfaces are missing or not yet synchronized

Examples encountered during the survey:

- `runtime/events/folder_status.md` was not present
- `runtime/reports/folder_status.md` was not present
- `docs/reviews/folder_status.md` was not present
- `docs/specs/operation_surface_min_spec_v1.md` was referenced in one status path but not present under that exact filename in this checkout

This does not break the repo, but it shows that the status surface is not fully synchronized everywhere.

### 5.3 `app/work` is rich but still uneven

`app/work/current_layer_baseline` is clearly mature and acts like a baseline memory.

But many other work subfolders are still experimental/probe-like:

- `concept_segment_probe`
- `middle_layer_experiments`
- `mixed_*`
- `youtube_transcript_probe_*`
- `processor_compare`

So the work tree already contains a lot of operator memory, but not all branches are equally locked.

## 6. What the key documents are actually doing

### `CURRENT.md`

This is the current engine definition note.
It says the engine is fragment-centered and organized around:

`source -> fragment -> anchor + processing values -> measurement retention -> observer layer -> source/space projection`

### `vectorfl_status.md`

This is the repo-level status and philosophy summary.
It tells the same story at a higher level:

- the repo is an engine workspace
- the current engine is fragment-centered
- document, script, runtime, and reference layers all matter

### `vectorfl_philosophical_interpretation_v1.md`

This is the philosophy note that explains the engine as a system that:

- preserves incomplete meaning
- keeps hold corridors
- values re-entry and repetition
- rejects premature closure
- uses observer-first judgment

### `codex_content_pack.md` and `codex_processor_standard.md`

These are the comparative and operational standards:

- the project is not a simple RAG
- the goal is to learn by repeated comparison and anchor labeling
- fragments are the comparison unit
- outputs must remain comparable, not just fluent

### `source_assets/*`

These are the actual source assets that supply the engine with operating material:

- declarations
- baselines
- directives
- first-pass external case inputs

### `inputs/external_cases/*`

These are the raw external materials that feed first-pass case handling.

### `docs/contracts`, `docs/policies`, `docs/specs`

These are the hard boundaries and operating rules.
They already define:

- routing
- intake lanes
- ambiguity policy
- observation contracts
- surface contracts
- refinement triggers

### `runtime/*`

This is where traces, receipts, manifests, views, and observer surfaces live.
It is not just output. It is the working memory of the repo.

## 7. Current reach point

The repo is already beyond a plain codebase.

It is already a mixed engine space with:

- raw inputs
- source assets
- operating contracts
- runtime traces
- read surfaces
- example outputs
- comparative reports

What is still missing is not “data.”
What is still missing is the fully synchronized reading/trace architecture across every branch.

## 8. The practical conclusion

The repo is in a real intermediate state:

- the philosophy is already declared
- the intake lanes are already declared
- the fragment/anchor/measurement engine is already declared
- the runtime trace surfaces are already real
- example and report strata are already present

But:

- not every folder has the same level of status synchronization
- not every conceptual layer is fully materialized
- reference memory and some report/status surfaces still need alignment

## 9. What should be read next

The next useful reading sequence is:

1. `source_assets/declarations/*`
2. `source_assets/baselines/*`
3. `source_assets/directives/*`
4. `source_assets/external_case_inputs/*`
5. `inputs/external_cases/*`
6. `docs/policies/*`
7. `docs/contracts/*`
8. `app/work/current_layer_baseline/*`
9. `runtime/receipts/*`
10. `runtime/views/*`

That sequence follows the actual engine path:

source -> intake -> contract -> operation -> receipt -> view

## 10. Breadcrumb for this survey

This survey should be treated as a process record, not just a summary.
It establishes that the repo-wide reading path must include:

- root philosophy docs
- source assets
- raw inputs
- docs/policies and contracts
- app/work baseline
- runtime receipts / logs / manifests / views

That is the reading order that matches the space the user described.
