# Formation-Movement Interface Process-First External Material Note v0

## 1. status

```yaml
status: process_first_note
mode: bounded_reread_only
verdict: PASS_WITH_NOTE
purpose: read external material through existing internal process flow and existing lines/axes before any stronger classification
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. why this note exists

The current bottleneck is not just classification accuracy.

It is workflow usability:

- external material enters
- package logic exists
- space insertion exists
- Codex interpretation exists
- validation return exists

But if these remain too segmented, the user has to decide too many steps manually.

So the safer front-door is:

```text
외부자료를 먼저 내부 공정 흐름으로 읽고,
이미 존재하는 line/axis가 있는지 확인한 다음,
거기에서 출발한다.
```

## 3. internal process-first rule

Before asking what the external material is, ask:

```text
이 자료가 지금 내부 공정의 어느 지점과 먼저 닿는가?
이미 살아 있는 내부 line/axis가 있는가?
이 자료는 공간에서 숙성되어야 하는가, 아니면 바로 bounded compare에 태워도 되는가?
```

That means the order becomes:

```text
1. existing internal line/axis check
2. process-stage contact check
3. external material provisional typing
4. bounded compare or space insertion
5. validation return / reread
```

Not:

```text
외부자료 분류 먼저
→ 그다음 내부 적용 고민
```

## 4. existing internal lines found before classification

For the current governance-architecture cluster, the existing internal lines are already present.

### line 1. Codex prepare / execution gate

Why it exists:

- already validated in:
  `docs/reports/formation_movement_interface_codex_oneshot_validation_case_v0.md`
- already reinforced in:
  `docs/reports/formation_movement_interface_external_cluster_internal_line_ranking_note_v0.md`

Core internal question:

```text
이 작업은 prepare까지만 열려 있는가, 아니면 execution까지 열려 있는가?
```

### line 2. external ingest / comparison-frame line

Why it exists:

- already validated in:
  `docs/reports/formation_movement_interface_external_reference_ingest_validation_case_v0.md`

Core internal question:

```text
이 외부자료는 direct evidence인가, defensive logic인가, comparison frame인가?
```

### line 3. validation gate / return line

Why it exists:

- already defined in package draft
- repeatedly reinforced in validation notes

Core internal question:

```text
결과를 final로 닫는가, 아니면 validation_return으로 다시 읽는가?
```

### line 4. A/B/C overlap line

Why it exists:

- already present in weak-signal and threshold comparison material

Core internal question:

```text
이 자료를 하나의 축으로 잠그면 다른 후보를 흡수하는가?
```

## 5. process-first reading of the current external cluster

Current external cluster:

- `agent-skills`
- `Flutist`
- merged as:
  `external governance-architecture comparison cluster`

### step 1. do we already have an internal line?

Yes.

The closest lines already exist:

1. Codex prepare / execution gate
2. external ingest / comparison-frame
3. validation gate / review-return

Therefore this material should **not** start from abstract ontology lock.

It should start from line contact.

### step 2. which process stage does it hit first?

First process-stage contact:

`formation-layer reread of existing gate/boundary scenes`

Reason:

- the material is not first of all an execution object
- it is not first of all a final axis proof
- it first helps reread already-existing internal scenes

### step 3. what is the safe provisional type?

Current safe type:

`framing_candidate`

Reason:

- enough role clarity for stable reuse
- still not enough for direct evidence
- best used as bounded comparison object

### step 4. what is the actual workflow?

Healthy workflow:

```text
external material enters
→ check existing internal line/axis
→ identify first process-stage contact
→ assign provisional object_type
→ bounded compare against that line
→ return as validation/reread material
→ only then consider stronger spatial placement
```

## 6. what "space insertion" should mean here

Space insertion should not mean:

- save the link
- declare a doctrine
- pick an axis immediately

It should mean:

```text
이미 있는 내부 공정 line에 다시 태울 수 있는
reusable reread-support object로 배치한다
```

So the current cluster enters the space as:

```text
external governance-architecture comparison cluster
→ framing_candidate
→ compare_only
→ reusable reread-support object
```

## 7. process-first practical card

If the same kind of material arrives again, the default first response should be:

```text
현재 판정: 기존 내부 gate/boundary line에 먼저 태워볼 수 있는 comparison object
이유: 이미 Codex prepare / external ingest / validation gate line이 존재하므로, 새 축 잠금보다 line contact 확인이 먼저입니다.
다음 이동: 가장 가까운 내부 line 1개에 bounded compare
금지선: direct evidence lock, axis promotion, workflow import 금지
```

## 8. what this changes in practice

Before:

```text
외부자료가 들어오면
이게 무엇인지부터 결정하려고 함
```

After:

```text
외부자료가 들어오면
이미 있는 내부 공정 line 어디에 먼저 태울지부터 본다
```

This reduces fragmentation because:

- the front-door becomes process-first
- the user does not need to choose between ingest / space / compare / Codex too early
- the external object starts from an already existing internal track

## 9. current verdict

`PASS_WITH_NOTE`

Reason:

- existing internal lines are present and usable
- the external cluster can start from them instead of floating as abstract material
- the remaining note is that this still requires discipline to keep "line-first" ahead of "classification-first"

## 10. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_external_governance_architecture_cluster_note_v0.md`
- any validation case
- Core 7
- object family 5종
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 11. unresolved questions

- in future real work, should the first line contact always be single-line, or can multi-line contact sometimes be the safer default?
- when does line-first reread become strong enough to justify axis-level strengthening?
