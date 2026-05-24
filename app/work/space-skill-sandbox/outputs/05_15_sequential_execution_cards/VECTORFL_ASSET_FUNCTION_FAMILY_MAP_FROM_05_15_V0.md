# VectorFL Asset Function Family Map from 05-15 v0

## 1. Verdict

```text
05_15_REFRAMED_AS_INPUT_GATE_FUNCTION_FAMILY_MAP_WITH_HOLD
```

This document is a sandbox-local candidate map.

It does not promote 05-15 into ontology, registry, workflow, schema, AGENTS.md, SKILL.md, baseline, current-position, output_manifest, or local core authority.

## 2. Why This Map Exists

The current problem is not that the space lacks assets.

The problem is that many assets were built while solving adjacent problems, and their names now sit across different folders, surfaces, and maturity levels:

- pipeline assets
- component / organ assets
- space / boundary assets
- input / intake assets
- lens / camera assets
- authority / governance assets
- return / memory assets
- human-language bridge assets
- external-tool relay assets
- sandbox / experiment assets

The 05-15 bundle helps here because it compressed into a small front-gate capability:

```text
input depth / response mode selector candidate
```

That means 05-15 should be used as an intake-side reader that decides what kind of asset family to call next, not as a new master architecture.

## 3. Current Big Frame

The current large frame should be:

```text
Request
  -> mode / depth selection
  -> asset family selection
  -> bounded local read
  -> authority check
  -> return surface
```

In Korean:

```text
요청
  -> 읽기 깊이/응답 모드 선택
  -> 자산군 선택
  -> 제한된 로컬 조회
  -> 권한 경계 확인
  -> 반환면 구성
```

This keeps the user from needing to remember every file path.
The user can ask for a big family, and Codex can retrieve the relevant assets behind that family.

## 4. Candidate 0-9 Reading Frame

This is not a digit ontology.
It is a temporary reading index for asking the space more clearly.

| Digit | Family handle | Korean name | What it groups | Main scattered assets |
|---|---|---|---|---|
| 0 | `space_frame` | 공간틀 | What the space is and how material lives inside it | space language, boundary material flow, current asset map |
| 1 | `source_basis` | 기준 입력층 | Declarations, baselines, directives, handoffs, raw source inputs | `source_assets/`, policies, baselines |
| 2 | `input_gate` | 입력기/유입부 | Intake, input depth, mode selection, source surface detection | 05-15 mode selector, input organ, intake lanes |
| 3 | `lens_reader` | 렌즈/카메라 | Lens rack, layer-shift, line/axis reading, user intent reading | space-boundary camera, LACL matrix, layer-shift reader |
| 4 | `authority_gate` | 권한/승격 게이트 | Stop, hold, promotion boundary, workspace ownership | authority gate, folder role table, operating layer freeze |
| 5 | `pipeline_family` | 파이프라인군 | Request-return-reflux, intake-to-digestion, organ chain, processing routes | pipeline specs, movement maps, route contracts |
| 6 | `organ_component` | 기관/부품군 | Bounded organs, tools, scripts, workers, local helpers | input organ, translation organ, scripts, app/core modules |
| 7 | `surface_return` | 표면/반환군 | Current-reading, process console, report card, validation return | runtime/views, current asset map, operation boards |
| 8 | `memory_residue` | 기억/잔여군 | Provenance, logs, receipts, residue, reflux, reread memory | runtime/logs, receipts, provenance, memory spine |
| 9 | `promotion_boundary` | 승격 경계 | What can become stable and what must remain candidate | provisional criteria, current SSOTs, HOLD lists |

The useful part is not the number itself.
The useful part is that each request can first be located in one or two families before touching files.

## 5. Asset Families

### 5.1 `space_frame`

Role:

```text
Defines what "space" means here and how materials should be read before movement.
```

Representative assets:

- `runtime/views/current_asset_map_v1.md`
- `docs/indexes/space_translation_language_base_v0.md`
- `docs/indexes/space_boundary_material_flow_map_v0.md`
- `docs/specs/folder_role_table_v1.md`

How to bring it in:

Use this family when the user asks:

- "우리 공간 기준으로 봐줘"
- "이게 어디에 붙는지 봐줘"
- "큰 틀로 다시 정리해줘"
- "이 개념이 우리 공간에서 뭐가 되는지 설명해줘"

Do not:

- turn space language into a final glossary
- flatten space into a folder list
- treat a candidate map as current authority

### 5.2 `source_basis`

Role:

```text
Holds official or semi-official source material that gives direction, baseline, or guidance.
```

Representative assets:

- `source_assets/declarations/`
- `source_assets/baselines/`
- `source_assets/directives/`
- `source_assets/handoffs/`
- `docs/policies/`

How to bring it in:

Use this family when the user asks:

- "기준이 뭐였지?"
- "이건 기존 원칙과 맞아?"
- "이걸 어디까지 근거로 볼 수 있어?"

Do not:

- overwrite source assets from a sandbox result
- confuse active guidance with locked SSOT
- treat every baseline-like note as baseline authority

### 5.3 `input_gate`

Role:

```text
Decides how deeply to read incoming material and which response mode is appropriate.
```

Representative assets:

- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/CURRENT_CANDIDATE_STATE_V0.md`
- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/LAYER_DIGIT_MODE_THRESHOLDS_V0.md`
- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/LAYER_SHIFT_READING_CORRECTION_V0.md`
- `docs/specs/vectorfl_handoff_boundary_lock_v0.md`
- `docs/specs/vectorfl_first_organ_chain_example_v0.md`

Current named functions:

- `mode_selector`
- `layer_shift_reader`
- `review_ladder`

How to bring it in:

Use this family before answering messy input:

```text
mode:
why:
read depth:
minimal action:
WATCH:
HOLD:
```

Do not:

- make full review the default
- make plain chat bypass risky inputs
- convert 05-15 into an official input router

### 5.4 `lens_reader`

Role:

```text
Chooses the reading lens: technical, maker intent, user intent, line/axis, feature direction, risk, residue, layer shift.
```

Representative assets:

- `docs/indexes/space_boundary_material_flow_map_v0.md`
- `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md`
- `app/work/space-skill-sandbox/lenses/`
- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/LAYERED_LENS_REREAD_V0.md`

Current named functions:

- `layer_shift_reader`
- `space_boundary_camera`
- `line_axis_lens`

How to bring it in:

Use this family when the user wording is simple but the meaning may be shifted:

- "정리해줘"
- "사용설명서로 만들어봐"
- "제품화 관점에서 봐봐"
- "B2B로 다시 봐봐"

Do not:

- force a hidden meaning into every short input
- treat a lens as proof
- merge camera, lens, line, and axis just because they share words

### 5.5 `authority_gate`

Role:

```text
Stops or holds movement when the request touches promotion, memory, policy, file mutation, automation, or workspace authority.
```

Representative assets:

- `runtime/views/engine_operating_layer_manifest_v1.json`
- `docs/specs/folder_role_table_v1.md`
- `docs/specs/provisional_stable_subset_criteria_v0.md`
- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/GEMINI_MODE_SELECTOR_SOFT_ACTION_THRESHOLD_RECHECK_V0.md`
- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/GEMINI_MODE_SELECTOR_B2B_CUSTOMER_CONTRACT_RECHECK_V0.md`

Current named function:

- `authority_gate`

How to bring it in:

Use this family when the user asks:

- "반영해"
- "확정해"
- "baseline으로 넣어"
- "AGENTS.md에 넣어"
- "자동화해"
- "계속 기준으로 써"

Do not:

- block discussion as if it were action
- treat "검토해도 될까?" as permission to modify files
- turn stop into an automatic policy engine

### 5.6 `pipeline_family`

Role:

```text
Groups repeatable movement structures: request-return-reflux, intake-to-digestion, organ chain, validation-return, reprocess.
```

Representative assets:

- `docs/indexes/space_boundary_material_flow_map_v0.md`
- `docs/specs/intake_package_to_digestion_package_handoff_minimum_v0.md`
- `docs/specs/question_route_contract_v0.md`
- `docs/specs/vectorfl_first_organ_chain_example_v0.md`
- `source_assets/baselines/space_request_orchestration_baseline_v1.md`

How to bring it in:

Use this family when the user asks:

- "이걸 흐름으로 묶어봐"
- "어떤 순서로 붙이면 돼?"
- "다음 이동을 정리해줘"
- "작업 루프로 보면 뭐야?"

Do not:

- promote a candidate route into workflow
- create automation just because the flow is visible
- hide authority checks inside a pipeline

### 5.7 `organ_component`

Role:

```text
Groups bounded tools, organs, scripts, workers, and helpers that do one role inside a larger movement.
```

Representative assets:

- `scripts/`
- `app/core/`
- `app/work/observer_ingest_min/`
- `docs/specs/vectorfl_organ_delegation_and_handoff_translation_v0.md`
- `docs/specs/vectorfl_first_organ_chain_example_v0.md`

Current candidate organs:

- input organ
- translation organ
- flow interpretation organ
- governance/current-reading return
- bounded comparer
- packet preparer
- return summarizer

How to bring it in:

Use this family when the user asks:

- "이 기능은 어느 부품이 맡아?"
- "이건 스크립트야, 기관이야, 표면이야?"
- "어느 실행 팔에 붙여야 해?"

Do not:

- make every helper a permanent organ
- turn a sandbox script into core
- confuse worker execution with judgment authority

### 5.8 `surface_return`

Role:

```text
Shows current state, returned material, latest read, validation return, or operator-facing summary.
```

Representative assets:

- `runtime/views/`
- `runtime/reports/`
- `runtime/commands/`
- `runtime/receipts/`
- `docs/indexes/space_translation_language_base_v0.md`

How to bring it in:

Use this family when the user asks:

- "지금 상태 보여줘"
- "이 결과를 다음 채팅에 넘기게 닫아줘"
- "운영면에서 보이게 정리해줘"
- "반환 카드로 줘"

Do not:

- treat latest surface as raw source
- treat a return surface as final authority
- bury HOLD/WATCH in prose

### 5.9 `memory_residue`

Role:

```text
Keeps traces, provenance, receipts, logs, residue, and future reread material available.
```

Representative assets:

- `runtime/logs/`
- `runtime/receipts/`
- `runtime/manifests/`
- `runtime/memory/`
- `runtime/views/engine_memory_spine_v1.json`
- `source_assets/baselines/input_reading_maturation_and_operating_space_baseline_v1.md`

How to bring it in:

Use this family when the user asks:

- "이걸 나중에 다시 떠오르게 하려면?"
- "기억 바닥에 뭐가 남아?"
- "결과 말고 흔적 기준으로 봐줘"
- "residue로 남길 건 뭐야?"

Do not:

- promote residue to memory without authority
- delete weak/fallback traces too early
- treat logs as interpreted truth

### 5.10 `promotion_boundary`

Role:

```text
Reads when a candidate is mature enough to move, and when it must stay as candidate, hold, watch, or residue.
```

Representative assets:

- `runtime/views/current_asset_map_v1.md`
- `runtime/views/engine_operating_layer_manifest_v1.json`
- `docs/specs/provisional_stable_subset_criteria_v0.md`
- `source_assets/directives/codex_future_scaling_guardrails_directive_v1.md`
- `app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/CURRENT_CANDIDATE_STATE_V0.md`

How to bring it in:

Use this family when the user asks:

- "승격 가능해?"
- "이 이름을 공식화해도 돼?"
- "이걸 기준으로 써도 돼?"
- "어디서 멈춰야 해?"

Do not:

- convert usefulness into authority
- infer maturity from repeated wording alone
- promote a sandbox-local probe into global rule

## 6. How To Retrieve Assets By Request

Use this sequence.

```text
1. Run input_gate first.
2. Decide selected mode:
   plain chat / simple answer / light review / full review / layer-shift / stop
3. Pick one or two asset families, not the whole repo.
4. Read current reality first when authority matters.
5. Read family-specific assets second.
6. Return with WATCH and HOLD.
```

Minimum card:

```text
selected_family:
selected_mode:
why:
files_to_read_first:
files_not_to_touch:
safe_output:
WATCH:
HOLD:
```

## 7. User-Facing Invocation Handles

These are useful request handles the user can use without remembering files.

| User says | Interpret as | First family to call |
|---|---|---|
| "공간 기준으로 봐줘" | locate meaning inside current VectorFL space | `space_frame` |
| "입력기로 먼저 읽어봐" | choose read depth and response mode | `input_gate` |
| "층위가 바뀌는지 봐줘" | detect surface/meaning mismatch | `lens_reader` |
| "게이트 걸어봐" | check stop/hold/promotion risk | `authority_gate` |
| "파이프라인으로 묶어봐" | map repeatable route, not automate | `pipeline_family` |
| "부품으로 나눠봐" | identify bounded organs/tools/helpers | `organ_component` |
| "반환면으로 닫아줘" | create current-readable return | `surface_return` |
| "기억/잔여로 남길 걸 봐줘" | preserve future reread material | `memory_residue` |
| "승격 가능성만 봐줘" | evaluate candidate maturity without promotion | `promotion_boundary` |

## 8. What 05-15 Adds To This Larger Map

05-15 does not add a new global asset class.

It adds a front-gate behavior:

```text
Before deciding what to do,
decide how deeply to read,
which family to call,
and where the authority boundary sits.
```

Most stable recovered names:

- `mode_selector`
- `authority_gate`
- `layer_shift_reader`
- `review_ladder`

Useful but more bounded:

- `macro_drafter`
- `handoff_builder`
- `return_recovery_splitter`
- `external_packet_boundary`

Not ready:

- `digit_system`
- `workflow_adapter`
- `official_router`
- `policy_engine`
- `operating_system`

## 9. Structural Comparison

| Current scattered structure | Family reading | What changes |
|---|---|---|
| Many docs under `docs/reports`, `docs/specs`, `docs/indexes` | `space_frame`, `pipeline_family`, `promotion_boundary` | Read by role, not by folder volume |
| Many source baselines/directives | `source_basis` | Treat as source guidance, not runtime result |
| Many runtime views/logs/receipts | `surface_return`, `memory_residue` | Separate latest surface from evidence trace |
| Many app/work experiments | `organ_component`, `input_gate`, `lens_reader` | Keep as sandbox unless promoted later |
| 05-15 mode selector work | `input_gate` + `authority_gate` | Use as front-gate probe, not architecture |
| LACL and line/axis materials | `lens_reader` + `promotion_boundary` | Use to read repeated lines, not force ontology |

## 10. WATCH

- The 0-9 frame becoming ontology.
- `mode_selector` becoming official router.
- `authority_gate` becoming over-blocking policy.
- `pipeline_family` being mistaken for automation approval.
- `organ_component` causing every helper to become a permanent organ.
- `surface_return` being treated as final truth.
- `memory_residue` being promoted without user authority.
- Folder counts being mistaken for maturity.

## 11. HOLD

- no AGENTS.md update
- no SKILL.md creation
- no automation script
- no baseline promotion
- no workflow/schema/registry/ontology creation
- no current-position update
- no output_manifest update
- no local core / derived / surface authority change
- no official ontology promotion

## 12. Next Smallest Action

Run a small gate-integrity trial using this map:

```text
Input:
  "이걸 파이프라인으로 묶고 부품/입력기/공간/규정으로 다시 정리해줘."

Expected behavior:
  mode_selector selects layer-shift or full review.
  asset family selection chooses:
    input_gate
    space_frame
    pipeline_family
    organ_component
    authority_gate

Return:
  a compact family map, not a registry.
```

## 13. One-Line Recovery

```text
05-15는 VectorFL 전체를 새로 정의하는 온톨로지가 아니라,
흩어진 자산군을 요청 전에 어느 깊이와 어느 가족으로 불러올지 정하는
입력기 앞단의 function-family selector 후보로 회수된다.
```
