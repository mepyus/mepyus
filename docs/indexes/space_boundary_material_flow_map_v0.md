# Space Boundary Material Flow Map v0

## 1. status

```yaml
index_status: operating_map_candidate
purpose: reorganize the space around boundary material intake, camera/lens reading, space lookup, movement decision, and return
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest: false
validator_or_script: false
```

## 2. core interpretation

The user's phrase:

```text
재료를 넣는다
```

should not mean:

```text
save a link, summarize it, and write a report
```

It should mean:

```text
trigger the space-boundary material flow.
```

That flow connects:

- user intent
- boundary material
- existing space lines / axes / lenses
- Codex interpretation
- local scripts / runtime artifacts
- external search or reference repos when needed
- merge / buffer / action decisions
- return-to-space records

## 3. new organizing center

The space should be read around this central operating unit:

```text
Space-Boundary Connection Camera
```

Korean:

```text
공간-경계 연결 카메라
```

Role:

```text
경계에서 들어온 재료를 그대로 저장하거나 실행하지 않고,
사용자 의도와 기존 공간 맥락에 비춰 렌즈별로 읽고,
머지 / 버퍼 / 작업화 / 환류 중 어디로 보낼지 판정한다.
```

## 4. boundary material definition

Boundary material includes more than internet references.

| Source surface | Material examples | First question |
| --- | --- | --- |
| Web / internet | GeekNews, GitHub repo, paper, blog | What technical meaning and maker intent does it carry? |
| User conversation | questions, clarifications, conceptual summaries | What user intent or formation object is emerging? |
| Codex output | report, draft, comparison, plan | Is this validation_return, residue, or a next action input? |
| Runtime / logs | events, receipts, manifests, test logs | What actually happened, and what does it prove or fail to prove? |
| Program artifacts | generated docs, indexes, outputs | Should this be merged, buffered, or reread? |
| Worker returns | task result, failure, structured return | Should this refine, hold, downgrade, archive, or promote? |

## 5. reorganized space layers

### Layer 1. input surface

What enters:

- URL
- repo folder
- user thought
- Codex output
- runtime log
- generated document
- worker return

Default state:

```text
unclassified boundary material
```

### Layer 2. source surface detection

Question:

```text
이 재료는 어떤 표면에서 들어왔는가?
```

Possible surfaces:

- internet / external web
- conversation
- Codex output
- runtime evidence
- generated artifact
- worker return

### Layer 3. camera activation

The camera always asks:

```text
왜 지금 이 재료가 들어왔는가?
이 재료는 어떤 문제/욕구/기술 발전과 닿는가?
기존 공간의 어떤 line/lens/axis를 먼저 조회해야 하는가?
```

### Layer 4. lens rack

Default lenses:

| Lens | Question |
| --- | --- |
| technical lens | What structure or mechanism does the material show? |
| maker-intent lens | What pain or bottleneck caused this material to exist? |
| user-intent lens | Why did the user bring this in now? |
| line/axis lens | Which existing space lines or axes does it touch? |
| feature-direction lens | What possible feature, purpose, or direction does this imply? |
| risk lens | What would be over-promoted, over-executed, or over-imported? |
| residue lens | How should this remain available for future re-emergence? |

### Layer 5. space lookup

Lookup starts from indexes and maps:

- `docs/indexes/space_asset_map_v0.md`
- `docs/guides/space_asset_retrieval_manual_v0.md`
- `docs/indexes/external_material_microspace_index_v0.md`

Then route-specific assets:

- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- `docs/reports/formation_movement_interface_process_first_external_material_note_v0.md`
- `docs/reports/formation_movement_interface_codex_role_default_mapping_note_v0.md`
- `docs/reports/formation_movement_interface_boundary_material_scope_clarification_v0.md`
- `docs/reports/formation_movement_interface_space_asset_goal_alignment_audit_v0.md`

### Layer 6. gap check

Question:

```text
현재 공간 안의 자료만으로 읽을 수 있는가?
아니면 웹, 로컬 repo, runtime log, event, script output, existing report를 더 읽어야 하는가?
```

Allowed searches:

- local file search
- local reference repo read
- runtime/event/log read
- web lookup when the source is external and current
- script output read when behavior evidence is required

### Layer 7. movement decision

Possible decisions:

| Decision | Meaning |
| --- | --- |
| `reread_priority` | more formation-side reading needed |
| `framing_candidate` | useful comparison material |
| `bounded_action_candidate` | action can be prepared, not executed |
| `guarded_execution` | execution allowed only with constraints and return conditions |
| `validation_return` | output has returned and needs reread |
| `archive_as_residue` | not currently useful but valuable later |

### Layer 8. Codex role decision

Default:

```text
Codex interpreter/output mode
```

Elevate only when needed:

| Role | Use when |
| --- | --- |
| bounded comparer | concrete comparison target exists |
| packet preparer | boundary, expected return, guardrail, return hook are ready |
| executor | execution constraint, fallback, trust scope, and return conditions are attached |
| return summarizer | returned material needs structured reread |
| rewrite assistant | explanation or surface output needs refinement |

### Layer 9. return-to-space

Every result returns as one of:

- refined material
- hold note
- downgrade note
- residue
- updated microspace entry
- validation return
- future action candidate

Do not treat output as final by default.

## 6. current assets mapped into this flow

| Existing asset | New role in reorganized flow |
| --- | --- |
| `formation_movement_interface_package_draft_v0.md` | safety and lifecycle grammar |
| `formation_movement_interface_workflow_controller_spec_v0.md` | route/state/output policy |
| `formation_movement_interface_codex_role_default_mapping_note_v0.md` | Codex base/elevation distinction |
| `formation_movement_interface_boundary_material_scope_clarification_v0.md` | boundary material scope |
| `external_material_microspace_index_v0.md` | first concrete boundary-material microspace |
| `formation_movement_interface_external_material_reemergence_reread_merge_v0.md` | re-emergence and merge pattern |
| `formation_movement_interface_space_asset_goal_alignment_audit_v0.md` | goal alignment diagnosis |
| `space_asset_map_v0.md` | repository-level retrieval map |
| `space_asset_retrieval_manual_v0.md` | asset role retrieval rule |

## 7. what changes in use

Before:

```text
사용자가 URL/자료를 줌
→ Codex가 읽고 분석
→ report 작성
→ 사용자가 다음 지시
```

After:

```text
사용자가 재료를 줌
→ source surface 판정
→ camera/lens 작동
→ 기존 공간 lookup
→ 부족하면 추가 search/read
→ 기술/의도/사용자 목적/공간 접점 판독
→ 기능 방향 후보 또는 buffer 산출
→ 필요한 경우에만 bounded movement
→ return-to-space
```

## 8. default user-facing output

The user should usually see:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

When the material is direction-relevant, add:

```text
기능/목적/방향 후보:
공간에 남길 버퍼:
```

## 9. example: GoScrapy through the reorganized flow

Input:

```text
https://news.hada.io/topic?id=28862
```

Flow:

```text
source surface: internet / external technology
technical lens: staged scraping framework
maker-intent lens: reduce scraping orchestration burden and let developer focus on parsing logic
user-intent lens: test how external materials enter and become usable space material
line/axis lens: external ingest, movement pipeline, return/export, boundary-role
feature-direction lens: external material intake / return-export surface candidate
risk lens: do not implement scraper, do not import GoScrapy architecture as schema
residue lens: store as data extraction pipeline cluster
```

Returned result:

```text
GoScrapy is not mainly a scraper to adopt.
It is a comparison material showing that our own boundary-material intake may need clearer stage and return/export surfaces.
```

## 10. immediate reorganization decision

Do now:

- use this map as the top-level entry for boundary material intake
- read `external_material_microspace_index_v0.md` as a subspace, not the whole concept
- treat internet references, Codex outputs, conversation notes, runtime logs, and generated artifacts as boundary material
- add direction output when a material touches user purpose

Do not do now:

- rename existing files
- move existing reports
- expand Core 7
- add object families
- build automation
- create a mandatory form

## 11. healthy trigger phrases

When the user says:

```text
이 재료 넣어봐.
공간에 태워봐.
이걸 우리 흐름으로 읽어봐.
이 결과를 다시 공간에 넣어봐.
이 로그/출력/대화가 무슨 재료인지 봐줘.
```

Default interpretation:

```text
Run the Space-Boundary Material Flow.
```

## 12. verdict

```yaml
verdict: PASS_WITH_NOTE
reorganization_type: operating_map_not_file_move
what_changed:
  - boundary material becomes the broader input class
  - Space-Boundary Connection Camera becomes the operating center
  - external material microspace becomes one subspace
  - feature/purpose/direction candidate becomes a required reading when relevant
what_remains_manual:
  - actual lookup/search
  - lens selection judgment
  - microspace updates
  - Codex role elevation
next_recommended_move:
  - test this flow on one non-internet material, such as a Codex output or runtime log
```

