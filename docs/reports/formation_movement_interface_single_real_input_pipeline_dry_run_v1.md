# Formation-Movement Interface Single Real Input Pipeline Dry Run v1

## 1. status

```yaml
status: single_real_input_pipeline_dry_run
verdict: PASS_WITH_NOTE
input_type: external_material_reference
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. input

```text
팀랄프 자료를 우리 공간에서 쓸 수 있게 봐줘
```

Assumption:

- `팀랄프 자료` is treated as an external material reference.
- The user is not asking for immediate execution.
- The user is asking whether the material can be made useful inside the space.

## 3. initial route judgment

Route:

```text
external material
```

Reason:

- the input says “자료”
- the requested action is “우리 공간에서 쓸 수 있게 봐줘”
- this points to space ingestion / reread / placement, not immediate Codex task execution

Initial internal path:

```text
external material
→ unclassified seed
→ space-first line/lens check
→ safe temporary state
→ Codex worker-role elevation decision
→ return-to-space state
→ 4-line user card
```

## 4. initial state

State:

```text
unclassified seed
```

Reason:

- the material has entered, but its role is not yet known
- it may become `reread_priority`, `framing_candidate`, `hold`, or `archive_as_residue`
- direct evidence, baseline, and execution are not available states at entry

## 5. Codex base mode

Base mode:

```text
Codex interpreter/output mode only
```

Meaning:

- Codex reads the user input
- Codex treats the material as something to be understood through the space/process
- Codex can produce the user-facing 4-line card
- Codex does not automatically enter a bounded worker role

This is not absence of Codex.

It is the base interpretive operating mode.

## 6. worker-role elevation decision

Decision:

```text
do not elevate Codex into a bounded worker role yet
```

Why elevation is not needed yet:

- the user did not ask for a comparison report
- no specific internal scene was named
- no bounded comparison question is visible yet
- no packet preparation target exists
- the first required operation is space-first reread and role placement

Possible later elevation:

```text
elevate Codex to bounded comparer
```

only if the material stabilizes enough and a specific internal comparison question appears.

Not appropriate now:

```text
elevate Codex to packet preparer
```

Reason:

- there is no worker packet, action boundary, expected return form, or guardrail request.

## 7. space-first reading

The material should first be checked for:

- existing line contact
- candidate lens
- formation-side or movement-side first contact
- whether it is direct evidence, defensive logic, comparison frame, or residue
- whether it should remain in `reread_priority`

Because the specific content of the `팀랄프 자료` is not present in this dry run, the controller cannot honestly assign a strong internal line yet.

Healthy provisional reading:

```text
object_type: reread_priority
```

Reason:

- the user wants the material to become usable in the space
- but the material's actual content has not been inspected
- placing it directly as a framing candidate would over-read the input

## 8. return-to-space state

Return state:

```text
reread_priority / pending content inspection
```

Space meaning:

- the material is accepted into the space intake path
- it is not yet reusable comparison material
- it needs content-level reading before line/axis/lens placement

Next internal move:

```text
read material content
→ check existing lines/lenses
→ decide reread_priority / framing_candidate / hold / archive_as_residue
```

## 9. user-facing 4-line card

```text
현재 판정: 더 읽을 자료
이유: 팀랄프 자료라는 외부자료 입력은 공간에서 쓸 가능성은 있지만, 아직 실제 내용이 없어 line/lens나 역할을 확정할 수 없음
다음 이동: 자료 내용을 먼저 읽고 기존 line/lens와 접점을 확인
금지선: 증거화 / baseline 반영 / Codex worker-role 승격 / 실행 금지
```

## 10. observed friction

### what worked

- the route is obvious enough from a short user input
- the pipeline does not ask the user to pick object_type
- Codex stays in interpreter/output mode
- worker-role elevation is correctly blocked
- the final output can be compact

### what still blocks full operation

The actual content of the `팀랄프 자료` is missing.

Without the material body, the controller can only:

- open the intake path
- keep the object at `reread_priority`
- request content-level reading

It cannot yet:

- identify a specific internal line
- choose a strong lens
- decide whether bounded comparison is needed
- place the material as reusable comparison object

## 11. verdict

Overall verdict:

```text
PASS_WITH_NOTE
```

Why:

- the default pipeline works at the front door
- the corrected Codex terminology holds
- Codex remains in interpreter/output mode
- worker-role elevation is not triggered prematurely
- the result stays user-facing and compact

Note:

- a real material body is required before the pipeline can complete line/lens placement and space insertion.
