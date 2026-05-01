# Internal Asset Recapitalization Map v0

## 1. status

```yaml
index_status: recapitalization_map_candidate
purpose: restate existing internal assets as usable capital for the Space-Boundary Material Flow
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest: false
validator_or_script: false
```

## 2. why this map exists

The repository already has many assets.

The current bottleneck is not asset absence.

The bottleneck is:

```text
자산이 많지만, 경계 재료가 들어왔을 때 어떤 자산을 어떤 순서로 꺼내 써야 하는지 즉시 떠오르지 않음.
```

This map restates internal assets as capital for:

```text
boundary material intake
→ camera / lens reading
→ space lookup
→ gap check
→ movement decision
→ Codex role decision
→ return-to-space
```

## 3. recapitalization principle

Do not reorganize by folder only.

Reorganize by role in the flow.

```text
asset value = where it helps the Space-Boundary Material Flow make a better decision
```

## 4. capital groups

| Capital group | Primary role | Main assets |
| --- | --- | --- |
| orientation capital | tells what the space is trying to do | source assets, baselines, closeouts |
| routing capital | decides where input goes | workflow controller, request matrices, route specs |
| lens capital | decides how material is read | process lens specs, multi-lens specs, camera notes |
| boundary/safety capital | prevents wrong movement | package draft, policies, contracts, guardrails |
| microspace capital | stores and re-emerges material | external material microspace, boundary flow map, re-emergence notes |
| evidence capital | provides actual behavior traces | runtime logs, receipts, manifests, observer outputs |
| execution lane capital | decides script/Codex/hybrid | execution lane map, script maps, worker contracts |
| return capital | brings results back to space | validation return notes, reingress specs, output/reinjection manuals |
| translation capital | makes results user-operable | translation bridge notes, explanation guides, surface manuals |

## 5. orientation capital

Use when asking:

```text
우리는 왜 이 공간을 만들고 있는가?
이 재료가 내 목적과 맞는가?
```

Primary zones:

- `source_assets/declarations/`
- `source_assets/baselines/`
- `source_assets/directives/`
- `docs/reports/*closeout*`
- `docs/reports/formation_movement_interface_round1_closeout_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_round_closeout_v0.md`

Role in new flow:

```text
user-intent lens and goal-alignment lens support
```

Do not use as:

- direct runtime proof
- automatic implementation permission

## 6. routing capital

Use when asking:

```text
이 입력은 어떤 route/state/output policy를 타야 하는가?
```

Primary assets:

- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- `docs/specs/space_request_type_matrix_v1.md`
- `docs/specs/question_interpretation_contract_v0.md`
- `docs/guides/space_entry_and_request_manual_v0.md`
- `docs/indexes/space_boundary_material_flow_map_v0.md`

Role in new flow:

```text
source surface detection
→ route/state decision
→ user-facing output policy
```

Current weakness:

```text
routing still tends to read input type before user intent.
```

Needed use:

```text
route by source surface + user intent + process location.
```

## 7. lens capital

Use when asking:

```text
이 재료를 어떤 렌즈로 읽어야 하는가?
```

Primary assets:

- `docs/specs/integrated_engine_process_lens_registry_v0.md`
- `docs/specs/multi_lens_strength_heuristic_spec_v0.md`
- `docs/specs/multi_lens_document_reading_v0_minimum_implementation_package_spec.md`
- `docs/reports/integrated_engine_process_camera_closeout_note_v0.md`
- `docs/reports/integrated_engine_lens_slot_compatibility_matrix_v0.md`
- `docs/reports/formation_movement_interface_space_asset_goal_alignment_audit_v0.md`

Role in new flow:

```text
technical lens
maker-intent lens
user-intent lens
line/axis lens
feature-direction lens
risk lens
residue lens
```

Current weakness:

```text
lens values exist but are not always surfaced in live output.
```

Needed use:

```text
each meaningful boundary-material reading should expose selected lenses, even briefly.
```

## 8. boundary and safety capital

Use when asking:

```text
무엇을 하면 안 되는가?
이 재료를 어디까지 움직여도 되는가?
```

Primary assets:

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_usage_manual_v0.md`
- `docs/reports/formation_movement_interface_cheat_sheet_v0.md`
- `docs/reports/formation_movement_interface_validation_work_package_v0.md`
- `docs/policies/AMBIGUITY_REVIEW_POLICY.md`
- `docs/policies/MEASUREMENT_RETENTION_POLICY.md`
- `docs/specs/engine_operator_automation_split_v1.md`
- `docs/specs/space_first_llm_last_principle_v0.md`

Role in new flow:

```text
prevent baseline lock, schema enforcement, premature execution, direct evidence promotion, and final-result confusion.
```

Core guardrails to keep active:

- prepare is not execute
- validation_return is not final
- external/boundary material is not direct evidence by default
- Codex output returns to space before lock
- user should not fill full internal sidecars

## 9. microspace capital

Use when asking:

```text
비슷한 재료가 이미 있었는가?
이 재료는 어떤 작은 공간에서 숙성되어야 하는가?
```

Primary assets:

- `docs/indexes/external_material_microspace_index_v0.md`
- `docs/indexes/space_boundary_material_flow_map_v0.md`
- `docs/reports/formation_movement_interface_boundary_material_scope_clarification_v0.md`
- `docs/reports/formation_movement_interface_external_material_reemergence_reread_merge_v0.md`
- `docs/reports/external_material_microspace_goscrapy_observation_v0.md`

Role in new flow:

```text
re-emergence, cluster membership, line/lens memory, safe next move.
```

Current weakness:

```text
the current microspace is mostly internet-reference oriented.
```

Needed use:

```text
extend reading to conversation outputs, Codex outputs, runtime logs, and generated artifacts without renaming everything yet.
```

## 10. evidence capital

Use when asking:

```text
실제로 무슨 일이 일어났는가?
이 주장은 실행/로그/이벤트로 뒷받침되는가?
```

Primary zones:

- `runtime/events/`
- `runtime/receipts/`
- `runtime/manifests/`
- `runtime/views/`
- `runtime/query_packets/`
- `runtime/exploration_results/`
- `runtime/reingress_records/`
- `runtime/observer/exploration/`

Role in new flow:

```text
runtime evidence, behavior traces, validation material, residue.
```

Use with:

- script-first collection when bounded
- Codex-first interpretation when meaning-sensitive
- hybrid when evidence plus structural judgment is needed

Do not use as:

- source intent
- baseline authority
- automatic success proof

## 11. execution lane capital

Use when asking:

```text
스크립트가 먼저인가, Codex가 먼저인가, hybrid인가?
```

Primary asset:

- `docs/guides/space_asset_execution_lane_map_v0.md`

Supporting assets:

- `scripts/`
- `scripts/cli/`
- `docs/specs/integrated_engine_worker_adapter_prompt_contract_v0.md`
- `docs/specs/integrated_engine_worker_return_normalization_policy_v0.md`
- `docs/reports/integrated_engine_real_worker_spine_validation_closeout_v0.md`

Role in new flow:

```text
gap check and movement decision.
```

Decision rule:

- script-first for bounded evidence collection, probe, preprocessing, sweep, validation
- Codex-first for meaning, mapping, attach/reject, user-facing judgment
- hybrid for external analysis plus space mapping

## 12. return capital

Use when asking:

```text
결과가 돌아왔을 때 공간에 어떻게 재투입되는가?
```

Primary assets:

- `docs/guides/space_output_and_reinjection_manual_v0.md`
- `docs/specs/answer_reinjection_handoff_contract_v0.md`
- `docs/specs/space_reingress_package_v0.md`
- `docs/specs/review_package_to_memory_package_handoff_minimum_v0.md`
- `docs/specs/digestion_package_to_review_package_handoff_minimum_v0.md`
- `docs/reports/formation_movement_interface_llm_wiki_autoresearch_complete_cycle_note_v0.md`

Role in new flow:

```text
validation_return, residue, refine, hold, downgrade, re-emergence.
```

Needed use:

```text
every non-trivial Codex/script/worker output should be read as return material, not final answer by default.
```

## 13. translation and user surface capital

Use when asking:

```text
사용자에게 어떻게 보이게 할 것인가?
의미가 납작해지지 않게 어떻게 설명할 것인가?
```

Primary assets:

- `docs/reports/integrated_engine_translation_bridge_usage_trial_closeout_note_v0.md`
- `docs/reports/integrated_engine_translation_bridge_lexicon_closeout_note_v0.md`
- `docs/reports/integrated_engine_provisional_human_explanation_guide_closeout_note_v0.md`
- `docs/reports/formation_movement_interface_user_surface_explanation_validation_case_v0.md`
- `docs/guides/space_as_product_manual_v0.md`

Role in new flow:

```text
user-facing card, explanation draft, flattening risk control, surface exposure.
```

Needed use:

```text
default user output stays short, but internal lens/camera result remains available.
```

## 14. practical retrieval order for boundary material

When a material enters:

```text
1. Read `space_boundary_material_flow_map_v0.md`.
2. Identify source surface.
3. Check microspace if it is reference-like or prior-output-like.
4. Check routing capital for route/state.
5. Check lens capital for selected lenses.
6. Check evidence capital if behavior proof is required.
7. Check execution lane capital if scripts/workers may be needed.
8. Check return capital before treating output as final.
9. Use translation capital for user-facing output.
```

## 15. current recapitalization verdict

```yaml
verdict: PASS_WITH_NOTE
asset_absence_problem: false
asset_activation_problem: true
strong_assets:
  - boundary/safety capital
  - routing capital
  - evidence capital
  - external microspace capital
weak_assets:
  - lens activation in live output
  - intent-to-feature-direction mapping
  - automatic retrieval of relevant internal assets
  - return-to-space habit for generated outputs
recommended_next_move:
  - test this map on one existing Codex output or runtime log as boundary material
```

## 16. do-not-change

- do not move existing files
- do not rename external material microspace yet
- do not create a mandatory schema
- do not expand Core 7
- do not add object families
- do not automate before the manual flow stabilizes
- do not treat runtime evidence as source intent
- do not treat reports as direct baseline

