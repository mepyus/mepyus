# Formation-Movement Interface External Material Default Pipeline Runtime Test v0

## 1. status

```yaml
status: runtime_behavior_dry_run
focus: external_material_default_pipeline
verdict: PASS_WITH_NOTE
purpose: test whether the external material default pipeline actually runs as a user-facing workflow
test_type: operational_dry_run
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. what is being tested

This is not a code-runtime test.

The pipeline is not implemented as an executable script.

This test checks whether the documented workflow can run as an operational sequence:

```text
short user input
→ space reads first
→ existing line/lens check
→ safe temporary state
→ Codex worker-role elevation decision
→ optional elevated Codex role
→ space placement
→ 4-line user card
```

## 3. source documents

- `docs/reports/formation_movement_interface_external_material_default_pipeline_v0.md`
- `docs/reports/formation_movement_interface_codex_role_default_mapping_note_v0.md`
- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- `docs/reports/formation_movement_interface_external_governance_architecture_cluster_note_v0.md`

## 4. test input

### user-facing input

```text
이 두 링크 넣어봐.
```

### assumed material

- `agent-skills`
- `Flutist`

### user should not need to specify

- object type
- route
- lens
- Codex role
- sidecar fields
- validation format

## 5. test checklist

- [x] user starts with a short input
- [x] pipeline starts at `unclassified seed`
- [x] space reads before classification
- [x] existing lines/lenses are checked
- [x] direct evidence lock is avoided
- [x] execution is avoided
- [x] Codex default is `interpreter/output mode only`
- [x] Codex can elevate only to `bounded comparer`
- [x] merged object can be placed in space
- [x] final output can be a 4-line card

## 6. step-by-step run

## 6.1 step 1. receive input

### pipeline behavior

The input enters as:

```text
unclassified seed
```

### result

`PASS`

### note

The user did not need to choose a route or object type.

## 6.2 step 2. space reads first

### pipeline behavior

The material is checked against existing internal lines before classification.

For this case:

- `agent-skills` touches workflow discipline, bounded preparation, and validation gate lines
- `Flutist` touches architecture boundary, rules-as-code, and check-without-mutate lines

### result

`PASS`

### note

The pipeline does not collapse both materials into one generic B-adjacent label at entry.

## 6.3 step 3. safe temporary state

### pipeline behavior

The two inputs stabilize differently before merge:

- `agent-skills`: closer to `reread_priority`
- `Flutist`: strong enough for `framing_candidate`

After merge:

```text
external governance-architecture comparison cluster
```

Safe state:

```text
framing_candidate
```

### result

`PASS`

### note

The merge produces a usable space object without treating either source as direct evidence.

## 6.4 step 4. Codex worker-role elevation decision

### pipeline behavior

Default:

```text
Codex interpreter/output mode only
```

Reason:

- the external material can be safely placed as a comparison cluster first
- no immediate bounded comparison task is required by the user input

Possible later upgrade:

```text
elevate Codex to bounded comparer
```

only if a specific internal scene needs comparison.

### result

`PASS_WITH_NOTE`

### note

This is where the pipeline now behaves better than before.

The earlier workflow often felt like it had to decide manually whether to call a separate Codex worker role.

Here the default is clear:

```text
do not elevate Codex into a worker role at entry
```

The remaining ambiguity is when to upgrade to comparer.

## 6.5 step 5. space placement

### pipeline behavior

The result is placed as:

```text
reusable comparison object
```

Working name:

```text
external governance-architecture comparison cluster
```

Useful for:

- Codex prepare / execution gate reread
- external ingest reread
- validation gate reread
- architecture / boundary discussion

### result

`PASS`

### note

The material enters the space as reusable support, not as doctrine.

## 6.6 step 6. final user output

### pipeline behavior

The user sees only the compact card:

```text
현재 판정: external governance-architecture comparison cluster
이유: 두 자료 모두 구조/경계/검증을 강하게 비추지만, 직접 증거라기보다 재사용 가능한 비교재료임
다음 이동: prepare / ingest / validation 장면에서 compare_only로 사용
금지선: direct evidence lock / 외부 workflow 수입 / baseline 반영 금지
```

### result

`PASS`

### note

The final output is usable without exposing the full internal pipeline.

## 7. user-perspective result

### what the user had to do

The user only supplied:

```text
이 두 링크 넣어봐.
```

### what the user did not have to do

- choose `reread_priority` or `framing_candidate`
- decide whether Codex should be called
- decide whether the material is evidence or comparison frame
- ask for a validation return
- request a cluster note

### verdict

`PASS`

## 8. where it actually runs

The pipeline runs cleanly through these stages:

```text
short input
→ unclassified seed
→ space-first line/lens reading
→ safe state
→ interpreter/output mode at entry
→ space placement
→ 4-line card
```

This is enough for the common external-material case.

## 9. where it still does not fully run

The pipeline is still not fully automatic in two places:

### A. interpreter/output mode to bounded comparer upgrade

The pipeline says Codex is elevated to `bounded comparer` when bounded comparison is needed.

But the trigger is still partly judgment-based:

```text
when is comparison actually needed now?
```

### B. space placement strength

The pipeline can place the object as reusable comparison material.

But it still does not automatically decide how strongly that object should affect future line rankings.

## 10. overall verdict

```text
The external-material default pipeline runs as an operational dry-run.
It is usable for short user input and avoids the major failure modes.
It is not yet an executable controller, and two judgment thresholds remain manual.
```

Overall verdict:

`PASS_WITH_NOTE`

## 11. next test

The next useful test is not another external-material case.

It should be a different route:

```text
Codex task request:
"이거 Codex에게 맡겨도 돼?"
```

This will test whether the same front-door behavior works when the user's input explicitly mentions Codex.
