# Pre-1.12 Lower Input Organ Inventory Report v0

## Verdict

`PASS_WITH_NOTE`

The lower input organ is a distributed organ, not a single module. It is spread across structured document routing, observer ingest, raw runtime inputter/labeler helpers, external transcript preprocess, source assets, manifests, reports, and generated trace/readable artifacts.

This inventory only maps material-intake lower organs. It does not treat the Phase 1.x question packet / exploration / merge / reingress CLI spine as the input organ; that upper spine is referenced only as a later bridge target.

## Inventory Table

| asset path | kind | role | input | transformation | output | trace | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `scripts/process_structured_doc_with_routing.py` | script | Structured-doc front door and lower-organ orchestrator | structured doc with routing markers | marker parse, label normalization, observer ingest call, origin/provenance/receipt/event write | observer outputs, label packets, origin maps, receipts, events, multi-lens views | engine ledger, provenance index, receipt, folder activity | explicit |
| `app/input_layer/labeler/labeler.py` | script | Normalizes lower intake labels | `DOCROLE`, `RUNMODE`, `PRIORITY`, alias map | external labels -> core intake labels -> label packet | `structured_doc_intake_label_packet` | label packet timestamp | explicit |
| `app/input_layer/source_locator/origin_map_minimum_v1.py` | script | Minimal source origin handle | source doc text | heading block / char span locator | origin map with heading path and char span | `derived_at`, source preview | explicit |
| `app/work/observer_ingest_min/run_observer_ingest_min.py` | script | Minimal material ingest and split organ | file or input registry | profile detect, split mode select, timestamp/heading/paragraph split, merge short segments | source manifest, split units, processing trace, readable board, operator summary | processing trace, run id | explicit |
| `app/work/observer_ingest_min/observer_ingest_min_spec.md` | spec | Declares lower ingest purpose and non-goals | lower ingest design | defines easy ingest + visible split + readable trace | spec-level contract | output contract summary | explicit |
| `app/work/observer_ingest_min/contracts/input_registry_contract_v1.md` | contract | Input registry shape | registry rows | defines source path, input kind, split mode, tags | registry contract | explicit required/optional fields | explicit |
| `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md` | contract | Lower observer output shape | observer run | defines manifest/split/trace/board/summary | output contract | field lists | explicit |
| `app/work/observer_ingest_min/generated/source_manifest_*.json` | generated | Source identity and run manifest | observer ingest run | records source path, profile, split mode, unit count | source manifest | run id | explicit |
| `app/work/observer_ingest_min/generated/split_units_*.json` | generated | Split unit surface | source text | timestamp/heading/paragraph segmentation | unit list with refs and excerpts | unit ids / source segment ids | explicit |
| `app/work/observer_ingest_min/generated/processing_trace_*.json` | generated | Minimal processing trace | observer ingest run | records stage and split mode | trace JSON | `engine_stage=summary_written` | explicit |
| `app/work/observer_ingest_min/generated/readable_input_board_*.md` | generated | Human-readable lower input board | source manifest + split units | summarizes input, split mode, units, flow note | readable board | run id and unit excerpts | explicit |
| `app/work/observer_ingest_min/generated/operator_summary_*.md` | generated | Operator summary of input and split | source manifest + units + trace | summarizes recognition, decomposition, front/middle/end flow | operator summary | engine stage | explicit |
| `app/work/observer_ingest_min/generated/gmd_native_read_*.json` | generated | Native read bridge artifact | source manifest + split units + processing trace | preserves segmentation basis, ordering, role hints, relation clues, uncertainty | GMD/native read payload | provenance link and event | distributed strong |
| `app/core/runtime/inputter.py` | script | Engine-only raw material splitter | material dict or raw source fields | sentence/code/log/bullet split into `DustInput` | dust units with source refs and siblings | source span is mostly none | explicit |
| `app/core/runtime/labeler.py` | script | Generic dust labeler | dust units | scene/flow/DIS/anchor inference | labeled dust | labels, anchors, scene/flow values | explicit |
| `scripts/run_external_case_raw_intake_probe.py` | script | Raw intake diagnostic probe | external case files | inputter + labeler; counts scene/flow/anchors | JSON stdout probe | dust count, avg D/I/S, top anchors | explicit |
| `app/core/runtime/external_input_comparison.py` | script | Transcript preprocess before/after comparison | transcript path | gate, preprocess, probe before/after, readiness read | preprocess comparison payload | before/after gate and metrics | explicit |
| `scripts/run_transcript_preprocess_comparison.py` | script | CLI wrapper for transcript preprocess compare | external transcript | calls comparison builder | `*_transcript_preprocess_comparison.json` | readiness status in stdout | explicit |
| `app/core/runtime/post_preprocess_first_pass.py` | script | First-pass read after preprocess | transcript and sidecar | preprocess sidecar, inputter/labeler probe, flatness summary | first-pass probe payload | caution notes / next read | explicit |
| `scripts/run_post_preprocess_first_pass_probe.py` | script | CLI wrapper for post-preprocess probe | transcript path | creates sidecar, writes probe JSON | sidecar `.txt` + probe JSON | generated timestamp | explicit |
| `app/work/external_input_preprocess/README.md` | spec/report | Defines transcript preprocess belt | external transcript artifacts | declares compare/regroup/post-preprocess pass as emergent line belt | folder-level role | generated folder policy | explicit |
| `app/work/external_input_preprocess/generated/*preprocess_comparison.json` | generated | Before/after preprocess comparison | raw transcript | gate metrics, regroup, before/after probe | readiness/status comparison | before/after gate, metrics, check surface | explicit |
| `app/work/external_input_preprocess/generated/*regroup*.txt` | generated | Preprocessed sidecar text | raw transcript | transcript-aware regroup | sidecar material | filename timestamp | explicit |
| `app/work/external_input_preprocess/generated/*first_pass_probe.json` | generated | Post-preprocess first-pass diagnostic | preprocessed sidecar | scene/flow flatness and sample rows | probe report | caution/next read | explicit |
| `source_assets/external_case_inputs/*` | source | External raw/first-pass material pool | external cases, YouTube/interview inputs | stored as source material | lower intake source assets | folder/status and generated observer outputs | distributed strong |
| `source_assets/directives/raw_intake_gap_analysis_before_middle_layer_fix_instruction_v1.md` | directive | Lower intake diagnostic directive | three intake paths | directs compare-first analysis | report requirements | do-not-modify boundaries | explicit |
| `source_assets/directives/middle_layer_thickening_program_instruction_v1.md` | directive | Middle-layer program directive | raw intake gap | defines target layers | plan/notes/examples allowed | do-not-patch guardrails | explicit |
| `docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md` | report | Lower intake gap diagnosis | structured path, external path, raw engine path | compares identity, anchors, frame extraction, output discipline | middle-layer requirements | explicit examples | explicit |
| `docs/reports/integrated_engine_lower_input_runtime_belt_map_v0.md` | report | Runtime belt map | lower input runtime assets | maps label/split/provenance/receipt/view stages | belt summary | role table | explicit |
| `docs/reviews/entry_execution_loop_v0.md` | report/spec | Conceptual lower entry loop | source/artifact | signal -> classifier -> family -> projection -> route -> residue | operational loop map | route examples | distributed strong |
| `docs/reviews/route_selection_policy_v0.md` | policy | Lower family route choice | signal/projection context | chooses direct ingest vs preprocess compare | route decision | fallback policy | distributed strong |
| `docs/reviews/projection_selection_policy_v0.md` | policy | Family projection precedence | family + issue root | chooses preprocess shaping vs input visibility | projection decision | fallback policy | distributed strong |
| `docs/reviews/signal_kind_taxonomy_v0.md` | taxonomy | Entry signal vocabulary | raw material / preprocess ambiguity | classifies signal kind before family | signal taxonomy | family/projection/route hints | distributed strong |
| `docs/specs/vectorfl_inputs_intake_adapter_contract_v0.md` | spec | Intake adapter visibility contract | source registry/intake packet/status/block | adapts source/context/block/status for reading | view model | weakness/fallback visibility | partial |
| `docs/specs/vectorfl_inputs_intake_organ_entry_link_lock_v0.md` | spec | Input organ entry link lock | Inputs/Intake surface | declares material/provenance/organ bridge surface | semantic link rule | explicit boundary | partial |
| `docs/specs/space_three_axis_operating_loop_and_material_intake_spec_v0.md` | spec | Material intake in wider operating loop | external/internal material | material intake -> construction -> line reading -> inspection | loop discipline | output discipline | partial |
| `app/work/processor_compare/inputs/*` and `app/work/processor_compare/reports/*` | generated/spec | Processor compare source/fragment lane | source docs/fragments | split/compare/canonicalization reviews | reports and splits | report JSON/MD pairs | partial |
| `runtime/manifests/*routing*`, `runtime/manifests/origin_maps/*`, `runtime/receipts/*`, `runtime/events/*` | runtime | Trace/registry/receipt substrate | structured routing runs | append ledgers and handles | manifests, receipts, events | append-only traces | distributed strong |

## Interpretation

The lower input organ is distributed for a good reason. Different material shapes need different entry behavior:

- structured docs already carry role and boundary signals;
- raw transcripts need preprocess shaping;
- external cases rely on source/derived/report separation;
- raw engine inputter/labeler can diagnose flattening but does not create compare-ready case structure alone.

The strong parts are source manifests, split units, processing traces, readable boards, operator summaries, provenance links, preprocess comparison metrics, and explicit route/projection policy docs.

The weak parts are not basic ingestion. The weak parts are the middle layer: topic-bearing aggregation, compare-ready packaging, and the exact bridge from lower output readiness into upper CLI evidence/query packets.

## Validation

- Lower material-intake assets were found across scripts, app/work, app/input_layer, source_assets, docs, and runtime traces: PASS.
- Upper question-packet assets were not treated as lower input organ: PASS.
- The inventory includes input / transformation / output / trace: PASS.
- The organ is distributed strong, not a single clean module: PASS.

## Next Stage Entry

Proceed to remap the lower organ by the user frame: 분절, 생성, 번역, 추출, 흐름.
