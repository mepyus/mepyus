# Formation-Movement Interface Space Asset Goal Alignment Audit v0

## 1. status

```yaml
status: goal_alignment_audit
verdict: PASS_WITH_NOTE
purpose: evaluate whether current space assets support the intended goal of connecting external technology, user intent, and internal space context into action direction
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. current goal

The current goal is no longer just:

```text
external material
→ read
→ analyze
→ classify
→ report
```

The real goal is:

```text
external technology / material
→ technical meaning
→ maker intent
→ user intent
→ existing space line / lens / axis
→ merge or buffer
→ feature / purpose / direction candidate
→ bounded movement only when aligned
→ return to space
```

Compressed:

```text
기술 발전과 사용자의 욕구 사이에서 기능 방향을 정렬하는 공간 공정.
```

## 3. key question

This audit asks:

```text
우리가 만든 자산은 이 목표를 이루는 데 맞게 배치되어 있는가?
그리고 현재 자산만으로 어떻게 그 목적에 더 가까이 갈 수 있는가?
```

## 4. asset inventory by function

| Asset group | Main files | What it already does | Fit to current goal |
| --- | --- | --- | --- |
| Formation-Movement package | `formation_movement_interface_package_draft_v0.md`, usage manual, cheat sheet | defines provisional objects, sidecar, lifecycle, prepare/execute, validation return | strong safety layer |
| Workflow controller | `formation_movement_interface_workflow_controller_spec_v0.md` | routes external material, Codex task, explanation, overlap, returned result | useful but still type-centric |
| Codex role mapping | `formation_movement_interface_codex_role_default_mapping_note_v0.md`, coupling diagnostic | separates interpreter/output mode from bounded worker-role elevation | important but needs intent-to-role mapping |
| External material microspace | `docs/indexes/external_material_microspace_index_v0.md` | keeps external materials findable and clusterable | newly aligned with re-emergence goal |
| Re-emergence merge | `formation_movement_interface_external_material_reemergence_reread_merge_v0.md` | rediscovered scattered materials and merged into reusable pack | strong correction for findability |
| Process-first note | `formation_movement_interface_process_first_external_material_note_v0.md` | says external material should start from existing lines/process | strongly aligned |
| Weak-signal work | stress-test, seed library, round closeout | prevents overpromotion under ambiguity | strong guardrail, not a direction generator |
| External examples | agent-skills, Flutist, OMX, LLM-Wiki/autoresearch, GoScrapy | provide comparison material across governance, workflow, formation/movement, data-flow | useful material base |
| Asset maps | `space_asset_map_v0.md`, retrieval manual | helps find asset categories | useful but not goal-specific enough |

## 5. what is already aligned

### 5.1 safety against wrong movement

Current assets are strong at preventing:

- premature baseline lock
- schema enforcement
- direct evidence promotion
- prepare/execution confusion
- validation_return becoming final
- user being forced to fill Core 7

This directly reduces rework risk.

If a feature direction is not ripe, the system can hold it.

### 5.2 external materials can now re-emerge

The microspace and re-emergence note corrected a major usability failure:

```text
외부자료가 있었지만 다시 못 찾는 문제.
```

Now the space can preserve:

- alias
- source trace
- cluster
- line/lens contact
- safe next move
- promotion barrier

This is aligned with the goal of letting materials mature and return later.

### 5.3 Codex is no longer only an executor

Current assets already separate:

```text
Codex interpreter/output mode
```

from:

```text
bounded worker-role elevation
```

This is essential.

The user needs Codex to analyze, interpret, compare, align, and only sometimes execute.

### 5.4 external examples cover several needed directions

Current external material set is not random.

It already covers useful poles:

- agent-skills: workflow discipline and quality gates
- Flutist: architecture boundary and check-without-mutate
- OMX: Codex workflow/runtime orchestration
- LLM-Wiki: formation-side accumulation
- autoresearch: constrained movement and keep/discard gate
- GoScrapy: external data-flow pipeline and return/export surface

This means the material base is adequate for early goal alignment.

## 6. what is not yet aligned

### 6.1 the camera/lens device is not explicit

The current system has pieces of a camera:

- process-first reading
- external material microspace
- line/lens placement
- Codex role mapping
- validation return

But it does not yet explicitly operate as:

```text
Space-External Connection Camera
```

Meaning:

```text
same processing device
+ swappable lenses
→ different readings of the same external material
```

This is the missing conceptual operating unit.

### 6.2 current flow still starts too much from material type

The workflow controller routes by:

- external material
- Codex task
- explanation
- overlap
- returned result

That is useful, but the user's current goal requires another first question:

```text
내가 지금 이 자료를 왜 가져왔는가?
```

The route should be shaped by:

```text
user intent
→ process location
→ lens selection
→ Codex role
→ output shape
```

not only by input type.

### 6.3 maker intent is underrepresented

Current reports often cover technical structure and package contact.

They less consistently ask:

```text
이걸 만든 사람은 어떤 불편을 봤는가?
왜 이 구조를 선택했는가?
그 의도가 우리 공간의 어떤 불편과 닿는가?
```

This matters because feature direction alignment depends on intent, not just structure.

### 6.4 feature-direction output is still weak

Most notes end with:

- state
- next_allowed_move
- promotion barrier
- compare_only

But the current goal needs an additional output:

```text
이 자료가 우리 공간에서 어떤 기능/목적/방향 후보를 낳는가?
```

For GoScrapy, for example, the better output was not:

```text
framing_candidate
```

but:

```text
external material intake / return-export surface may be a future function direction.
```

### 6.5 Codex role is still not selected from intent strongly enough

The current Codex coupling diagnostic already found this.

Missing mapping:

```text
user intent
→ needed lens
→ needed Codex role
→ expected output shape
```

Without this, the user still has to manually say:

- analyze only
- compare only
- do not execute
- prepare packet
- reread return

That is exactly the usability bottleneck.

## 7. current asset fit judgment

### fit level

```yaml
overall_fit: partial_but_promising
safety_layer: strong
memory_reemergence_layer: emerging
camera_lens_layer: weak_to_emerging
intent_alignment_layer: weak
feature_direction_layer: weak
execution_layer: intentionally_guarded
```

### compressed judgment

```text
우리가 만든 자산은 과승격과 과실행을 막는 데는 잘 맞는다.
외부자료를 다시 찾고 묶는 microspace도 생겼다.
하지만 사용자의 욕구와 외부 기술을 렌즈별로 연결해 기능 방향을 뽑는 카메라 장치는 아직 명시적 자산으로 분리되지 않았다.
```

## 8. what the assets should become

The current assets should not become more forms.

They should become a smaller operating sequence:

```text
Intent
→ External material
→ Connection camera
→ Lens pass
→ Space contact
→ Direction candidate
→ Bounded movement or buffer
```

In Korean:

```text
의도
→ 외부자료
→ 외부 연결 카메라
→ 렌즈 판독
→ 공간 접점
→ 기능/목적/방향 후보
→ bounded 작업 또는 숙성 버퍼
```

## 9. proposed operating unit

Name candidate:

```text
Space-External Connection Camera
```

Korean:

```text
외부 연결 카메라
```

Role:

```text
외부자료를 그대로 요약하지 않고,
기술적 의미, 만든 사람의 의도, 사용자의 목적, 공간의 기존 맥락을 렌즈별로 대조해
머지/버퍼/작업화 가능한 방향으로 변환하는 장치.
```

This is not a new object family.

It is an operating view over existing assets.

## 10. camera default pipeline

```text
1. user intent capture
2. source capture
3. technical meaning
4. maker intent
5. microspace lookup
6. line / axis / lens contact
7. lens pass
8. merge / buffer / action split
9. feature-direction candidate
10. Codex role decision
11. return-to-space
```

## 11. default lenses

| Lens | Question |
| --- | --- |
| technical lens | What technical structure does this material show? |
| maker-intent lens | What pain or bottleneck did the creator try to solve? |
| user-intent lens | Why did the user bring this material now? |
| line/axis lens | Which existing space lines/axes does this touch? |
| feature-direction lens | What possible feature/purpose/direction does this create? |
| risk lens | What would be over-imported, over-promoted, or over-executed? |
| residue lens | How should this remain available for future re-emergence? |

## 12. how current assets can support this now

Without new implementation, we can already run the camera manually:

1. Use `external_material_microspace_index_v0.md` for source/cluster lookup.
2. Use `workflow_controller_spec_v0.md` for route and output policy.
3. Use `process_first_external_material_note_v0.md` for line-first reading.
4. Use external reports for material-specific comparison.
5. Use `codex_role_default_mapping_note_v0.md` and coupling diagnostic for Codex role selection.
6. Return with a 4-line card plus feature-direction note.

The missing part is not more theory.

The missing part is making this the default response pattern.

## 13. recommended next move

Do not expand Core 7.

Do not add object families.

Do not create runtime automation yet.

Recommended bounded move:

```text
Create a short Space-External Connection Camera usage note.
```

It should define:

- when to use it
- default pipeline
- lens set
- output shape
- relation to external material microspace
- relation to Codex role decision

It should be short enough to actually use.

## 14. target output shape for future external material

For the next external material, the default output should be:

```text
1. 기술적 의미
2. 만든 사람의 의도
3. 사용자가 지금 이걸 가져온 행위의 의미
4. 기존 공간 line/lens/axis 접점
5. 머지 가능한 부분
6. buffer로 남길 부분
7. 기능/목적/방향 후보
8. Codex role decision
9. 사용자면 4줄 카드
```

This is the shape that aligns with the user's actual goal.

## 15. do-not-change

- do not baseline lock
- do not schema-enforce the camera
- do not turn it into a mandatory user form
- do not expand Core 7
- do not add object families
- do not automate before usage stabilizes
- do not treat external material as direct evidence
- do not let Codex execute just because it can analyze

## 16. verdict

```yaml
verdict: PASS_WITH_NOTE
current_assets_are_useful: true
current_assets_match_goal_completely: false
main_strength:
  - safety
  - preservation
  - validation
  - external material re-emergence
main_gap:
  - explicit camera/lens operating unit
  - intent-to-feature-direction mapping
  - intent-to-Codex-role mapping
next_recommended_move:
  - define a short usage note for the Space-External Connection Camera
```

