# Pre-1.12B Bridge Examples With Real Artifacts v0

## Verdict

`PASS_WITH_NOTE`

The minimum bridge rules apply cleanly to real repository artifacts. Most lower artifacts should enter upper as `evidence_only` or `ingest_ready`; only artifacts with explicit gate/readiness/checkpoint structure should be treated as `packet_candidate`.

## Example 1: Runtime Event Ledger

| field | value |
| --- | --- |
| lower artifact | `runtime/events/engine_event_ledger.jsonl` |
| lower artifact type | runtime residue / operational trace |
| current readiness | `residue-only` |
| upper admission result | `reject_for_upper` |
| allowed transition | lower trace context in a report |
| blocked transition | evidence unit, packet candidate, line/axis support |
| mapped fields | none by default; possible trace summary only |
| ambiguity | event entries can explain that something ran, not what source means |
| why not higher | no bounded source evidence, segmentation, or packet-worthy goal |
| why not lower | it can still be retained as operational trace |

## Example 2: Observer Source Manifest

| field | value |
| --- | --- |
| lower artifact | `app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260328_071128.json` |
| lower artifact type | source manifest |
| current readiness | `evidence-ready` |
| upper admission result | `evidence_only` |
| allowed transition | selected asset reason; evidence source provenance; search target support |
| blocked transition | direct packet candidate |
| mapped fields | `source_path -> source_ref/search_targets`; `input_id -> selected_asset_reason`; `detected_profile -> constraints`; `split_mode_used/unit_count -> evidence confidence note` |
| ambiguity | manifest tells how lower saw the source, not the source's full meaning |
| why not higher | no upper interpreted goal or expected output shape |
| why not lower | provenance and split-mode signal are strong enough for evidence support |

## Example 3: Observer Split Units

| field | value |
| --- | --- |
| lower artifact | `app/work/observer_ingest_min/generated/split_units_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` |
| lower artifact type | generated split units |
| current readiness | `evidence-ready` |
| upper admission result | `evidence_only` |
| allowed transition | evidence units with `source_ref`, `pointer`, and `excerpt_or_pointer` |
| blocked transition | packet candidate; line/axis support by itself |
| mapped fields | `unit_id -> evidence pointer`; `start_ref/end_ref -> pointer`; `text_excerpt -> excerpt`; `char_count -> excerpt quality note` |
| ambiguity | some units are title-only or heading-only, so excerpt quality varies |
| why not higher | split units do not state the upper task or route decision |
| why not lower | bounded excerpts and source segment ids can ground upper exploration |

## Example 4: Preprocessed Transcript Regroup Text

| field | value |
| --- | --- |
| lower artifact | `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_regroup_compare_20260405T074527Z.txt` |
| lower artifact type | preprocessed external input material |
| current readiness | `engine-ingest-ready` with evidence-ready local excerpts |
| upper admission result | `ingest_ready` |
| allowed transition | upper search target; next probe candidate; constraint that preprocessed material is preferred over raw subtitle shards |
| blocked transition | direct packet candidate without comparison JSON or readiness note |
| mapped fields | file path -> `search_targets`; local paragraphs -> candidate evidence after exploration; preprocess context -> `constraints` |
| ambiguity | the text is more readable, but it does not itself encode the before/after gate |
| why not higher | no embedded admission checklist or packet goal |
| why not lower | it is a usable lower ingest target and contains meaning-sized paragraphs |

## Example 5: Transcript Preprocess Comparison JSON

| field | value |
| --- | --- |
| lower artifact | `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json` |
| lower artifact type | preprocess comparison and readiness surface |
| current readiness | `packet-candidate` |
| upper admission result | `packet_candidate` |
| allowed transition | seed upper comparison/verification packet; selected evidence source; ambiguity and next-probe fields |
| blocked transition | baseline promotion; final line/axis promotion |
| mapped fields | `input_path/preprocessed_path -> search_targets`; `before_gate.decision -> constraints`; `decision_reason -> why_it_matters`; `metrics -> evidence/supporting context`; `checkpoints -> expected_output_shape/next_probe_candidates`; `after_gate.decision -> ambiguity_notes` |
| ambiguity | `after_gate.decision` can be `uncertain_needs_probe`, so packet should stay cautious |
| why not higher | packet-candidate is not baseline or final naming lock |
| why not lower | it has provenance, gate decisions, metrics, and next checkpoints |

## Example 6: GMD Native Read

| field | value |
| --- | --- |
| lower artifact | `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` |
| lower artifact type | lower interpretation surface |
| current readiness | `packet-candidate` when paired with source manifest and split units |
| upper admission result | `packet_candidate` or `evidence_only` depending on checklist |
| allowed transition | packet seed if provenance, scope, and route are clear; otherwise evidence-only support |
| blocked transition | direct authority promotion |
| mapped fields | native read summary -> `interpreted_goal` seed or `selected_asset_reason`; source refs -> evidence refs; uncertainty -> `ambiguity_notes` |
| ambiguity | interpretation surface may blend translation and extraction |
| why not higher | it is derived lower interpretation, not authority ladder change |
| why not lower | paired source and split artifacts can make it usable for upper framing |

## Interpretation

The examples show the practical difference between `evidence_only` and `packet_candidate`.

`evidence_only` means the lower artifact can ground an upper exploration result. It should answer "what can we cite or inspect?" not "what is the upper request?"

`packet_candidate` means the lower artifact contains enough handoff structure to seed upper interpretation. The transcript preprocess comparison qualifies because it includes before/after paths, gate decisions, reasons, metrics, and checkpoints.

Engine-ingest-ready material sits between those two. The regrouped transcript is useful material, but without the comparison JSON it lacks the admission context that would make it a packet candidate.

## Validation

- Examples are based on real repository artifacts: `PASS`.
- Examples include residue, evidence-ready, engine-ingest-ready, and packet-candidate artifacts: `PASS`.
- Allowed and blocked transitions are named for each example: `PASS`.
- Upper and lower surfaces remain separate: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/reports/pre12_bridge_examples_with_real_artifacts_v0.md`
3. What was fixed at the bridge level: bridge rules were tested against real artifact classes.
4. What remains unresolved: automated admission is not implemented.
5. Whether user decision is required: no.
6. Can Phase 1.12 start after this? yes, after final action decision records the guardrails.
7. Recommended next move: write Pre-1.12 action decision.
