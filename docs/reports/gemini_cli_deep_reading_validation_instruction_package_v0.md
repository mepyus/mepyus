# Gemini CLI Deep Reading Validation Instruction Package v0

## 1. status

```yaml
package_status: gemini_deep_reading_validation_instruction_package
verdict: PASS_WITH_NOTE
default_permission: no-write
scope_level_default: G2_deep_draft_only
execution_allowed: read_only_or_sandbox_only
baseline_lock: false
schema_enforcement: false
controller_implementation: false
runtime_manifest: false
index_update: false
```

## 2. purpose

This package gives Gemini CLI a stricter instruction shape for deep reading, detailed validation, and test review.

It exists because Gemini can produce fast output but may stay shallow unless the prompt forces:

- evidence extraction
- source surface separation
- lens-by-lens reading
- expected-vs-observed checks
- risk and HOLD candidate search
- self-audit
- explicit "what I did not verify"

This package does not grant Gemini write authority.

Gemini remains:

```text
execution / validation / listing / draft worker
```

Gemini is not:

```text
editor / final judge / schema designer / controller builder / baseline owner
```

## 3. default safety overlay

Always apply:

- `docs/reports/gemini_cli_safety_overlay_package_v0.md`
- `docs/reports/gemini_cli_no_delete_no_overwrite_policy_v0.md`
- `docs/reports/gemini_cli_command_allowlist_denylist_v0.md`
- `docs/reports/gemini_cli_sandbox_execution_protocol_v0.md`

Default permission:

```text
no-write
```

Gemini may propose changes, but must not apply them.

Any Gemini result must be reread as:

```text
source_surface: worker_return
```

## 4. when to use this package

Use this package when the task needs more than a simple 4-line card.

Good uses:

- validating a generated report
- checking a worker return against expected output
- reading several external materials without merging them
- finding source surface confusion
- testing whether a result over-promoted a claim
- reviewing stdout/stderr from a command
- checking whether a material should be HOLD, PASS_WITH_NOTE, or PASS
- producing a patch proposal without applying it

Do not use this for:

- direct file edits
- code changes
- baseline lock
- schema/controller/runtime/index changes
- repo cleanup
- automatic fix attempts

## 5. deep reading rule

Gemini must not only summarize.

For every material, Gemini must produce:

1. source surface judgment
2. lens order used
3. extracted evidence
4. what the evidence supports
5. what the evidence does not support
6. risk / over-promotion check
7. residue / next-use value
8. HOLD candidates
9. final provisional verdict
10. self-audit

If Gemini cannot provide evidence, it must say:

```text
Evidence insufficient.
```

## 6. source surface reading rules

Gemini must judge the current input role, not only the topic.

Examples:

- Original external article = `external_material_file`
- Report created from that article = `generated_report`
- Gemini's own response = `worker_return`
- Runtime ledger line = `runtime_event`
- Script/helper file = `program_artifact`
- User/assistant discussion = `conversation_material`

Important rule:

```text
If Gemini processes a material and returns a result, that result becomes worker_return when reread.
```

## 7. lens order table

| source_surface | lens order |
| --- | --- |
| `conversation_material` | user-intent -> feature-direction -> line/axis -> residue -> risk |
| `external_material_file` | technical -> maker-intent -> user-intent -> line/axis -> risk -> residue |
| `generated_report` | user-intent -> line/axis -> risk -> residue -> return-state |
| `worker_return` | expected-vs-observed -> risk -> residue -> next-move -> line/axis |
| `program_artifact` | artifact-role -> evidence/event -> technical -> residue -> risk |
| `runtime_event` | evidence/event -> technical -> risk -> residue -> line/axis |

Gemini must state which lens order it used.

## 8. evidence discipline

Gemini must include an evidence table for non-trivial tasks.

Required columns:

| claim | evidence_ref | evidence_summary | supports | does_not_support | confidence |
| --- | --- | --- | --- | --- | --- |

Rules:

- `evidence_ref` must point to the file, section, event id, line hint, or command output segment.
- `does_not_support` must not be empty for strong claims.
- `confidence` must be `high`, `medium`, or `low`.
- If evidence is weak, verdict must not be PASS.

## 9. expected-vs-observed discipline

For `worker_return`, test results, command output, and generated reports, Gemini must compare:

```text
expected:
observed:
fit:
missing:
overbuilt:
under-returned:
risk:
```

Gemini must not read a good-looking return as successful before checking expected-vs-observed.

## 10. HOLD candidate requirement

For every deep validation task, Gemini must list at least three HOLD candidates unless the task is trivial.

Format:

```text
HOLD candidate 1:
Reason:
What would resolve it:

HOLD candidate 2:
Reason:
What would resolve it:

HOLD candidate 3:
Reason:
What would resolve it:
```

If Gemini thinks there are fewer than three, it must explicitly say why.

## 11. over-promotion checks

Gemini must check whether the result improperly implies:

- baseline lock
- schema enforcement
- controller implementation
- runtime manifest
- index/microspace update
- helper/code promotion
- final judgment
- source surface taxonomy change
- 9-field record forced on every input

If any risk appears, verdict should be `PASS_WITH_NOTE` or `HOLD`, not PASS.

## 12. output levels

### Level D0 - Deep read only

Use when:

- Gemini should read and analyze only.

No file changes.

### Level D1 - Deep card draft

Use when:

- Gemini should produce 4-line user card plus internal evidence.

No file changes.

### Level D2 - Deep validation

Use when:

- Gemini should validate a report, return, command output, or trial result.

No file changes.

### Level D3 - Deep sandbox execution review

Use when:

- Gemini runs a permitted read-only/dry-run/stdout/sandbox command and deeply reviews output.

No existing repo file changes.

### Level D4 - Patch proposal only

Use when:

- Gemini sees a needed change.

It returns a patch proposal as text only. It does not apply it.

## 13. required output contract

Gemini must return:

```text
Verdict:
Scope level:
Materials read:
Source surface judgment:
Lens order used:

Evidence table:

Expected vs observed:

4-line card:
쓸 수 있나?
왜?
다음엔?
조심할 점은?

HOLD candidates:

Over-promotion check:

What Gemini did not verify:

Files modified:
Files created:
Files deleted:
Files moved:
Files overwritten:

Risk:
Next:
Self-audit:
```

Expected safe file fields:

```text
Files modified: none
Files created: none
Files deleted: none
Files moved: none
Files overwritten: none
```

If any file field is not `none`, treat the result as HOLD or FAIL until reviewed.

## 14. deep self-audit

Gemini must answer:

```text
1. Did I treat each material independently?
2. Did I preserve source surface distinction?
3. Did I state the lens order used?
4. Did I provide evidence, not just summary?
5. Did I explain what the evidence does not support?
6. Did I identify at least three HOLD candidates or explain why not?
7. Did I avoid baseline/controller/schema/runtime/index over-promotion?
8. Did I avoid file modification/deletion/move/overwrite?
9. Did I mark uncertainty as PASS_WITH_NOTE or HOLD instead of forced PASS?
10. Did I separate user-facing card from internal validation?
```

Allowed answers:

```text
yes
partial
no
```

`partial` and `no` require reasons.

## 15. ready-to-use prompt: deep validation of one material

```markdown
# Gemini CLI 지시서: Deep validation of one material

## 목적

지정된 재료 1건을 깊게 읽고, 요약이 아니라 검증 가능한 판단을 반환한다.

## safety level

D2 - Deep validation

## permission

no-write

## 먼저 읽을 파일

[파일 목록]

## test material

[재료 경로 또는 붙여넣은 재료]

## expected task

[기대한 작업 / 판단]

## source surface candidate

[source surface 후보]

## lens order

[lens order]

## 해야 할 일

1. 현재 입력의 source surface를 판정한다.
2. 지정 lens order가 맞는지 확인한다.
3. evidence table을 작성한다.
4. expected-vs-observed를 작성한다.
5. 사용자-facing 4줄 카드 초안을 만든다.
6. HOLD 후보를 최소 3개 찾는다.
7. over-promotion 위험을 점검한다.
8. 무엇을 검증하지 못했는지 적는다.
9. self-audit을 수행한다.

## 출력 형식

Verdict:
Scope level:
Materials read:
Source surface judgment:
Lens order used:

Evidence table:

Expected vs observed:

4-line card:
쓸 수 있나?
왜?
다음엔?
조심할 점은?

HOLD candidates:

Over-promotion check:

What Gemini did not verify:

Files modified:
Files created:
Files deleted:
Files moved:
Files overwritten:

Risk:
Next:
Self-audit:

## 금지

- 파일 수정 금지
- 파일 생성 금지
- 파일 삭제 금지
- 파일 이동 금지
- 파일 덮어쓰기 금지
- repo 전체 읽기 금지
- baseline/controller/schema/runtime/index 제안 금지
- 실패 시 자동 수정 금지
```

## 16. ready-to-use prompt: deep batch validation

```markdown
# Gemini CLI 지시서: Deep batch validation

## 목적

여러 재료를 하나로 합치지 않고, 각 재료를 독립적으로 깊게 읽고 검증한다.

## safety level

D2 - Deep validation

## permission

no-write

## 먼저 읽을 파일

[공통 기준 파일 목록]

## materials

1. [material 1]
2. [material 2]
3. [material 3]

## 해야 할 일

각 material마다 별도 섹션을 만든다.

각 섹션에는 반드시 포함한다:

- material_id
- source surface judgment
- lens order used
- evidence table
- expected-vs-observed
- 4-line card
- HOLD candidates
- over-promotion check
- what was not verified
- material verdict

마지막에는 batch-level self-audit을 작성한다.

## 금지

- 여러 재료를 하나의 통합 요약으로 합치지 말 것
- 파일 수정 금지
- 파일 생성 금지
- baseline/controller/schema/runtime/index 제안 금지
- 모든 material을 PASS로 강제하지 말 것

## batch-level self-audit

Did Gemini treat each material independently?
Did Gemini avoid merging materials into one summary?
Did Gemini preserve source surface distinction?
Did Gemini provide evidence per material?
Did Gemini identify HOLD candidates per material?
Did Gemini avoid over-promotion?
Did Gemini report file modification status?
```

## 17. ready-to-use prompt: command output deep review

```markdown
# Gemini CLI 지시서: Command output deep review

## 목적

지정된 명령 출력(stdout/stderr)을 깊게 읽고, 성공/실패/위험/다음 이동을 판정한다.

## safety level

D3 - Deep sandbox execution review

## permission

no-write

## command output

[stdout/stderr 붙여넣기 또는 경로]

## expected result

[기대 결과]

## 해야 할 일

1. expected-vs-observed를 작성한다.
2. stdout과 stderr를 분리해 읽는다.
3. 성공처럼 보이지만 아닌 신호를 찾는다.
4. 실패처럼 보이지만 범위 밖인 신호를 구분한다.
5. HOLD 후보를 찾는다.
6. 다음 확인 명령이 필요하면 read-only/check/dry-run으로만 제안한다.

## 출력 형식

Verdict:
Expected:
Observed:
Stdout summary:
Stderr summary:
Evidence:
HOLD candidates:
Risk:
Next read-only check:
Files modified:
Files created:
Files deleted:
Files moved:
Files overwritten:
```

## 18. do not

- Do not let Gemini edit files.
- Do not let Gemini delete files.
- Do not let Gemini overwrite files.
- Do not let Gemini solve uncertainty by inventing structure.
- Do not accept Gemini PASS without checking evidence.
- Do not accept Gemini batch output if materials were merged.
- Do not accept Gemini output that lacks "what was not verified."

## 19. next use

Use this package when asking Gemini to deeply validate:

- a live trial result
- a generated report
- a worker return
- a command output
- a batch of external materials
- a suspected source surface confusion

After Gemini returns, Codex/assistant should reread the result as `worker_return`.
