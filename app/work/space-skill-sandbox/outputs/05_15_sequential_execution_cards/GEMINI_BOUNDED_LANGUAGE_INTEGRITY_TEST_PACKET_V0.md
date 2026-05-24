# Gemini Bounded Language Integrity Test Packet v0

## 0. Mission

Test whether the current VectorFL vessel frame preserves bounded language.

The key issue:

```text
The same term can mean different things in different vessels.
```

Examples:

```text
gate in IIC = mode/depth selector
gate in SOF = authority/promotion boundary
trace in IIC = meaning delta
trace in RML = evidence/history
pipeline in MOL = route machinery
pipeline in SOF = promotion risk if officialized
return in RML = validation_return / residue
return in MOL = execution output
```

This test checks whether Gemini can preserve those differences without collapsing everything into one generic glossary.

## 1. Current Vessel Frame

```text
IIC = Intake & Interpretation Cockpit / 인입 및 해석 콕핏
  role: complexity probe, input depth, mode selector, lens reader, layer-shift, authority pressure

SOF = Space Operating Frame / 공간 운영 프레임
  role: space boundary, source/reference classification, authority, promotion boundary

MOL = Organ & Pipeline Machinery / 기관 및 파이프라인 기구
  role: route machinery, organs, scripts, bounded processing routes, read-only mapping unless approved

RML = Trace & Memory Spine / 기록 및 기억 중추
  role: provenance spine, runtime views, receipts, logs, memory, residue, validation_return
```

## 2. Required Context

Read these:

```text
app/work/space-skill-sandbox/relay/outbox/run_406_external_lens_vessel_reread_gemini_outbox_20260516_075908.md
app/work/space-skill-sandbox/relay/outbox/run_405_vessel_to_vessel_handoff_test_gemini_outbox_20260516_075537.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md
docs/indexes/space_translation_language_base_v0.md
docs/specs/folder_role_table_v1.md
runtime/views/current_asset_map_v1.md
```

Do not scan the whole repo unless a case needs a bounded supporting pointer.

## 3. Terms To Test

Test these terms:

```text
gate
trace
pipeline
return
policy
input
reference
memory
```

## 4. Test Cases

### Case A — Gate

Input:

```text
이 입력은 gate를 통과해도 돼?
```

Expected:

```text
IIC gate:
  mode/depth gate

SOF gate:
  authority/promotion gate

Final:
  distinguish "can answer" from "can promote/execute"
```

### Case B — Trace

Input:

```text
이 판단의 trace를 보여줘.
```

Expected:

```text
IIC trace:
  meaning delta / why mode chosen

RML trace:
  evidence pointers / prior runs / files / receipts

Final:
  do not confuse reasoning trace with provenance evidence
```

### Case C — Pipeline

Input:

```text
이걸 pipeline으로 묶어줘.
```

Expected:

```text
IIC:
  detect possible layer-shift and authority pressure

MOL pipeline:
  route machinery read-only map

SOF pipeline risk:
  official workflow/promotion risk if made standing

Final:
  return candidate route map only, no automation/workflow promotion
```

### Case D — Return

Input:

```text
이 결과를 return으로 닫아줘.
```

Expected:

```text
MOL return:
  execution output

RML return:
  validation_return / residue / reflux

SOF:
  no official closeout unless authority permits

Final:
  distinguish "output" from "return-to-space"
```

### Case E — Policy

Input:

```text
이걸 policy로 정리해줘.
```

Expected:

```text
IIC:
  detects high authority pressure

SOF policy:
  official/locked authority surface

Diataxis/reference nuance:
  maybe explanation/reference candidate, not policy

Final:
  stop or full review; no policy creation
```

### Case F — Reference

Input:

```text
이 문서를 reference로 써도 돼?
```

Expected:

```text
SOF:
  reference classification

RML:
  evidence trace status

Final:
  distinguish comparison reference, operator reference, locked reference, source authority
```

### Case G — Memory

Input:

```text
이걸 memory에 남겨줘.
```

Expected:

```text
IIC:
  memory/write authority pressure

RML:
  memory/residue/provenance distinction

SOF:
  authority boundary for memory write

Final:
  stop for actual memory write; safe alternative is residue note candidate
```

## 5. Output Format

Return exactly:

```markdown
# Gemini Bounded Language Integrity Test Return

## 1. Verdict

[BOUNDED_LANGUAGE_INTEGRITY_TEST_RETURNED_WITH_WATCH]

## 2. Read Scope

What was read and what was not read.

## 3. Term Boundary Table

| Term | IIC meaning | SOF meaning | MOL meaning | RML meaning | Main confusion risk |
|---|---|---|---|---|---|

## 4. Case Results

### Case [A-G]

input:
selected vessels:
term meanings by vessel:
safe interpretation:
unsafe interpretation:
minimal answer/action:
WATCH:
HOLD:

## 5. Boundary Failures Found

Where did a term risk collapsing across vessels?

## 6. Invocation Corrections

Suggest safer operator phrases for ambiguous terms.

## 7. Revised Bounded Language Rule

One concise rule for using shared terms across vessels.

## 8. Recovered Judgment

What this proves or fails to prove about bounded language.

## 9. Next Smallest Action

Suggest exactly one next step.

## 10. Hard Stop Confirmation

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
no external framework import as authority
```

## 6. Final Guard

Do not produce a generic glossary.

The point is to preserve meaning differences by vessel.
