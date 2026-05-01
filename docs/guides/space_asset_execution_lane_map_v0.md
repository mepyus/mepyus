# Space Asset Execution Lane Map v0

## Purpose

This map organizes current space assets by execution lane:

- `space-script-first`
- `codex-first`
- `hybrid`

It does not propose new scripts.
It only says which existing assets should be used through scripts first, which should stay interpretation-first, and which should stay mixed.

## 1. First Rule

Do not ask one lane to do the other lane's job.

- Use scripts first for bounded evidence collection, gating, preprocessing, sweep, and generated evidence surfaces.
- Use Codex first for meaning judgment, structural mapping, attach/reject decisions, and user-facing report shaping.
- Use hybrid when the request needs both scripted evidence and Codex-side synthesis.

## 2. Space-Script-First Assets

### A. input gate / preprocess / first-pass surfaces

Use scripts first for:

- [run_external_input_gate.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_input_gate.py)
- [run_external_case_raw_intake_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_raw_intake_probe.py)
- [run_transcript_aware_regroup.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transcript_aware_regroup.py)
- [run_transcript_preprocess_comparison.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transcript_preprocess_comparison.py)
- [run_post_preprocess_first_pass_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_post_preprocess_first_pass_probe.py)

Why:

- these surfaces already produce bounded evidence;
- they reduce raw reading cost before Codex interpretation starts;
- they are safer than manual full-text rereads for repeated intake questions.

Primary output zones:

- `stdout json`
- `app/work/external_input_preprocess/generated/`

### B. sweep / plan-first scan surfaces

Use scripts first for:

- [run_external_case_flowline_sweep.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_flowline_sweep.py)
- [run_external_case_folder_sweep_loop.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_folder_sweep_loop.py)

Why:

- these are candidate-narrowing surfaces;
- they are cheaper than asking Codex to scan broad folders repeatedly.

### C. structured doc intake surfaces

Use scripts first for:

- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)

Why:

- structured docs should become receipts, label packets, origin maps, and observer outputs before semantic interpretation;
- repeated direct reread is more expensive than normalized intake.

Primary output zones:

- `runtime/receipts/`
- `runtime/manifests/label_packets/`
- `runtime/manifests/origin_maps/`
- `app/work/observer_ingest_min/generated/`

### D. bounded line / validation / sandbox surfaces

Use scripts first for:

- [apply_internal_observer.py](/Users/sungsookim/universe/vectorfl_replica/scripts/apply_internal_observer.py)
- [build_source_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_source_view.py)
- [run_runtime_preflight.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_runtime_preflight.py)
- `run_transition_over_surface_*`

Why:

- these are bounded validation or measurement surfaces;
- they are not final semantic authority;
- they should feed Codex judgment, not replace it.

## 3. Codex-First Assets

### A. source intent assets

Read with Codex first:

- `source_assets/declarations/`
- `source_assets/baselines/`
- `source_assets/directives/`
- `source_assets/handoffs/`

Why:

- these are intent / authority / boundary materials;
- they are not cheap probe surfaces;
- they require interpretation, not only extraction.

### B. stable boundary assets

Read with Codex first:

- `docs/specs/`
- `docs/contracts/`
- `docs/policies/`

Why:

- these define what is allowed, forbidden, or still thin;
- over-automating them would blur boundary judgment.

### C. closeout / feasibility / lock reports

Read with Codex first:

- boundary notes
- closeout notes
- feasibility reports
- package lock notes

Why:

- these are already interpreted outputs;
- the main job here is synthesis, tension reading, and next-step judgment.

## 4. Hybrid Assets

### A. imported references

Use hybrid for:

- `references/git_search/`

Pattern:

1. script or narrow search to collect bounded source refs;
2. Codex maps those refs into current-space boundaries;
3. Codex decides attach / pattern / reference-only.

### B. generated observer outputs

Use hybrid for:

- `app/work/observer_ingest_min/generated/`
- `runtime/views/multi_lens_document_reading/`
- `runtime/logs/reread_observation_log.jsonl`

Why:

- script-first creates these surfaces;
- Codex must still decide what they mean;
- line seed / camera support / reread observations are not self-executing judgments.

### C. package-style external adaptation work

Use hybrid for:

- external repo attach analysis
- tool comparison
- pattern translation
- report-first / structure-second requests

Why:

- scripts can narrow and collect;
- Codex must still do the final structural read.

## 5. Assets To Keep Out Of Default Script-First

Do not make these default script-first even if scripts exist:

- `main_runtime_mutating` capabilities without a bounded gate
- final attach / reject judgment
- reinjection class judgment
- line / axis / promotion-sensitive interpretation
- unresolved boundary adjudication

## 6. Current Practical Reading

### script-first if the request is mainly:

- gate
- probe
- preprocess
- comparison
- sweep
- bounded validation

### codex-first if the request is mainly:

- what does this mean
- how should this map into our space
- what should we attach, reject, or hold
- what should the user-facing result be

### hybrid if the request is mainly:

- external analysis plus our-space mapping
- generated evidence plus structural judgment
- report-first / structure-second

## 7. One-Line Summary

Scripts should gather bounded evidence from active execution surfaces; Codex should decide what that evidence means and whether it changes the structure.
