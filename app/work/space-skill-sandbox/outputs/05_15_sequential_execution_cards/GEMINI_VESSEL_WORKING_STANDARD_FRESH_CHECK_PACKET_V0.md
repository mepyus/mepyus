# Gemini Vessel Working Standard Fresh Check Packet v0

## 0. Mission

Verify whether the vessel working standard can be used from a standalone document.

Important:

```text
Do not rely on previous Gemini session memory.
Use the standard candidate document as the primary guide.
```

## 1. Primary File

Read:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
```

Optional minimal authority context:

```text
runtime/views/current_asset_map_v1.md
docs/specs/folder_role_table_v1.md
runtime/views/engine_operating_layer_manifest_v1.json
```

Do not read run_403 through run_410 unless needed to answer evidence questions.

## 2. Test Inputs

Classify and answer each using only the vessel standard candidate.

### Case A

```text
IIC complexity probe 해줘:
"이걸 policy pipeline으로 닫고 다음부터 자동으로 쓰자."
```

### Case B

```text
SOF authority check:
"이 candidate 문서를 docs/specs로 올릴 수 있어?"
```

### Case C

```text
RML trace recovery:
"이 기준이 왜 생겼는지 근거를 찾아줘."
```

### Case D

```text
MOL route mapping만 해줘:
"Gemini 실행 경로가 어떤 부품으로 되어 있어?"
```

### Case E

```text
IIC -> SOF -> RML 순서로 봐줘:
"내가 승인할 테니 이걸 앞으로 기본 판단 루틴으로 써."
```

## 3. Output Format

Return exactly:

```markdown
# Gemini Vessel Working Standard Fresh Check Return

## 1. Verdict

[VESSEL_WORKING_STANDARD_FRESH_CHECK_RETURNED_WITH_WATCH]

## 2. Read Scope

What was read and what was not read.

## 3. Case Results

| Case | Selected vessel(s) | Selected mode | Safe answer | WATCH | HOLD |
|---|---|---|---|---|---|

## 4. Fresh Use Adequacy

Can the standard candidate stand alone for chat use?

## 5. Ambiguities Found

What was unclear in the standard candidate?

## 6. Required Edits Before User-Ready

List only necessary edits.

## 7. Readiness Judgment

One of:
  insufficient
  usable_with_operator_context
  user_ready_chat_standard_candidate

## 8. Hard Stop Confirmation

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

## 4. Final Guard

If the document is good enough for chat use, say so.
If it is not, say exactly what blocks it.
