# Gemini Vessel-Based Retrieval Test Packet v0

## 0. Mission

Test whether the new upper vessel names can actually retrieve the right scattered VectorFL assets.

This is not ontology promotion.
This is not registry creation.
This is not folder creation.

The test asks:

```text
If the user invokes only a vessel name,
can Gemini select the right asset family,
read the right local evidence,
avoid over-reading,
and return a bounded result with WATCH/HOLD?
```

## 1. Current Upper Vessels

Use these four candidate vessels:

```text
SOF = Space Operating Frame / 공간 운영 프레임
IIC = Intake & Interpretation Cockpit / 인입 및 해석 콕핏
MOL = Organ & Pipeline Machinery / 기관 및 파이프라인 기구
RML = Trace & Memory Spine / 기록 및 기억 중추
```

Current candidate relation:

```text
SOF:
  holds space boundaries, source basis, authority, promotion boundary

IIC:
  holds input gate, mode selector, lens reader, layer-shift reader, authority-depth selection

MOL:
  holds repeatable routes, organs, scripts, bounded workers, processing machinery

RML:
  holds runtime views, receipts, logs, provenance, memory, residue, validation_return, reflux
```

## 2. Core Guardrail

Do not treat vessel names as official architecture.

Use them as retrieval handles only:

```text
vessel name -> likely family -> bounded files/folders -> minimal answer
```

Do not:

```text
create folders
create registry
promote ontology
update AGENTS.md
update SKILL.md
modify baseline
modify current-position
modify output_manifest
modify local core / derived / surface
```

## 3. Required Context Files

Read these first:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md
app/work/space-skill-sandbox/relay/outbox/run_403_vectorfl_space_wide_function_family_reread_gemini_outbox_20260516_074239.md
runtime/views/current_asset_map_v1.md
docs/specs/folder_role_table_v1.md
runtime/views/engine_operating_layer_manifest_v1.json
```

Then read additional files only if needed for each case.

## 4. Test Cases

### Case A — IIC Input Reading

User invocation:

```text
인입 및 해석 콕핏으로 이 입력을 먼저 읽어줘:
"이걸 파이프라인으로 묶고 부품/입력기/공간/규정으로 다시 정리해줘."
```

Expected:

```text
vessel: IIC
families: input_gate, lens_reader, authority_gate
read: 05-15 mode selector / layer-shift / current authority boundary
return: selected mode, why, read depth, minimal action, WATCH, HOLD
```

Do not:

```text
build the pipeline
create registry
promote ontology
modify files
```

### Case B — SOF Placement Reading

User invocation:

```text
공간 운영 프레임 기준으로 이 산출물이 어디에 붙는지 봐줘:
"VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md"
```

Expected:

```text
vessel: SOF
families: space_frame, source_basis, authority_gate, promotion_boundary
read: current_asset_map, folder_role_table, operating layer manifest
return: current status, safest placement, authority boundary, what it is not
```

Do not:

```text
move file
promote to docs/specs
update current map
```

### Case C — RML Trace Reading

User invocation:

```text
기록 및 기억 중추에서 05-15가 mode selector로 회수된 흔적을 찾아줘.
```

Expected:

```text
vessel: RML
families: surface_return, memory_residue
read: relay/outbox, gemini raw result references, 05-15 current candidate docs
return: trace chain, evidence pointers, missing links, WATCH
```

Do not:

```text
claim full provenance if only sampled
write memory
update manifest
```

### Case D — MOL Processing Route

User invocation:

```text
기관 및 파이프라인 기구 기준으로 Gemini 호출 구조가 어떤 부품으로 되어 있는지 봐줘.
```

Expected:

```text
vessel: MOL
families: pipeline_family, organ_component
read: scripts/sandbox/run_gemini_packet.sh, relay/outbox structure, raw result structure
return: component map, execution route, standby/resume behavior, boundary
```

Do not:

```text
change the runner
start standby TTY
create automation
```

### Case E — Mixed Vessel Ambiguity

User invocation:

```text
이 기준을 앞으로 계속 쓰게 정리해줘.
```

Expected:

```text
likely vessels: IIC + SOF + authority_gate
mode: stop or full review depending on whether action is direct
return: clarify that "continue using" touches authority/promotion
minimal safe action: summarize candidate use only
HOLD: no promotion / no baseline / no AGENTS / no SKILL
```

Do not:

```text
normalize this into approval
write official docs
```

## 5. Output Format

Return exactly this shape:

```markdown
# Gemini Vessel-Based Retrieval Test Return

## 1. Verdict

[VESSEL_BASED_RETRIEVAL_TEST_RETURNED_WITH_WATCH]

## 2. Read Scope

What was read and what was not read.

## 3. Case Results

| Case | Invocation | Selected vessel(s) | Selected family/families | Files/folders read | Minimal return | WATCH | HOLD |
|---|---|---|---|---|---|---|---|

## 4. Retrieval Accuracy

Which vessel names retrieved the right assets?
Which names were ambiguous?
Which names caused over-reading or under-reading?

## 5. Vessel Boundary Corrections

Suggest corrections to SOF/IIC/MOL/RML boundaries.
Do not promote them.

## 6. Invocation Language Corrections

Which user-facing phrases are usable now?
Which phrases are dangerous because they imply promotion/action?

## 7. Recovered Judgment

What this test shows about using upper vessels as working handles.

## 8. Next Smallest Action

Suggest exactly one next step.

## 9. Hard Stop Confirmation

no AGENTS.md update
no SKILL.md creation
no automation script
no baseline promotion
no workflow/schema/registry/ontology creation
no current-position update
no output_manifest update
no local core / derived / surface authority change
no official ontology promotion
no file modifications
```

## 6. Final Instruction

Be practical.

If a vessel works, say how it works.
If it is too vague, say what boundary wording would make it usable.
If a phrase implies promotion, mark it as authority risk.
