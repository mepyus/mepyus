# Gemini CLI Safe Execution Prompt Templates v0

## 1. status

```yaml
template_status: safe_execution_prompt_templates
default_permission: no-write
baseline_lock: false
schema_enforcement: false
controller_implementation: false
```

## 2. Template 1 - Safe read-only inspection

```markdown
# Gemini CLI 지시서: Safe read-only inspection

## 목적

지정된 파일만 읽고, 요청된 정보만 추출한다.

## scope level

G0 - Read only

## 먼저 읽을 파일

[파일 목록]

## 수정할 파일

없음

## 생성할 파일

없음

## 해야 할 일

[읽기/목록화/확인 작업]

## 금지

- 파일 수정 금지
- 파일 삭제 금지
- 파일 이동 금지
- 파일 생성 금지
- repo 전체 읽기 금지
- 자동 정리 금지

## 출력 형식

Verdict:
Findings:
Files modified:
Files created:
Files deleted:
Risk:
Next:
```

## 3. Template 2 - Safe material listing

```markdown
# Gemini CLI 지시서: Safe material listing

## 목적

지정된 입력에서 테스트 후보 material을 목록화한다.

## scope level

G1 - List only

## 먼저 읽을 파일

[파일 목록]

## 수정할 파일

없음

## 생성할 파일

없음

## 출력 형식

candidate_id:
material_ref:
source_surface_candidate:
why_candidate:
risk:
recommended_task_type:

## 금지

- 파일 수정 금지
- 파일 삭제 금지
- 실제 trial 실행 금지
- 4줄 카드 생성 금지
- 전체 요약 금지
```

## 4. Template 3 - Safe single material card draft

```markdown
# Gemini CLI 지시서: Safe single material card draft

## 목적

재료 1개에 대해 4줄 카드 초안을 만든다.

## scope level

G2 - Draft only

## test material

[재료]

## 수정할 파일

없음

## 생성할 파일

없음

## 출력 형식

case_id:
test_material:
source_surface:
lens_order:
record_candidate:
verdict:

쓸 수 있나?

왜?

다음엔?

조심할 점은?

risk_note:
next_move:

## 금지

- 파일 수정 금지
- 파일 삭제 금지
- baseline/controller/schema/index/runtime 제안 금지
- 9-field 강제 금지
```

## 5. Template 4 - Safe sandbox script execution

```markdown
# Gemini CLI 지시서: Safe sandbox script execution

## 목적

지정된 스크립트를 지정된 입력으로 실행하고 결과를 보고한다.

## scope level

G3 - Sandbox execution only

## 실행할 명령

[명령 1개]

## 입력

[input ref]

## output mode

stdout-only 또는 sandbox-output

## output path

runtime/gemini_sandbox/[case_id]/

## 수정할 파일

없음

## 생성할 파일

sandbox output 외 없음

## 실행 전 확인

command:
purpose:
read paths:
write paths:
expected output:
risk:
allowed_level:

## 실행 후 출력 형식

Verdict:
Task type:
Scope level:
Command run:
Exit code:
Output mode:
Output path:
Files modified:
Files created:
Files deleted:
Files overwritten:
Stdout summary:
Stderr summary:
Risk:
Next:

## 금지

- 기존 파일 수정 금지
- 기존 파일 삭제 금지
- 기존 파일 덮어쓰기 금지
- 실패 시 자동 수정 금지
- 전체 repo scan 금지
- 전체 테스트 스위트 실행 금지
```

## 6. Template 5 - Safe self-audit

```markdown
# Gemini CLI 지시서: Safe self-audit

## 목적

이전 Gemini 결과를 다시 읽고 위험을 찾는다.

## scope level

G4 - Validation only

## 검산 대상

[이전 결과]

## 수정할 파일

없음

## 생성할 파일

없음

## 질문

1. Did I modify, delete, move, or overwrite any file?
2. Did I merge materials that should remain separate?
3. Did I confuse source surfaces?
4. Did I use PASS where PASS_WITH_NOTE or HOLD was safer?
5. Did I imply baseline/controller/schema/index/runtime changes?
6. Did I omit risk or residue?

## 출력 형식

Verdict:
Self-audit:
HOLD candidates:
PASS_WITH_NOTE reasons:
Files modified:
Files deleted:
Files moved:
Files overwritten:
Risk:
Next:

## 금지

- 자기 결과 자동 정당화 금지
- 모든 항목 yes 처리 금지
- 파일 수정 금지
- 새 구조 제안 금지
```

## 7. common footer for Gemini prompts

Append this footer to Gemini prompts unless explicitly inappropriate:

```text
Gemini default permission is no-write.
If a change seems needed, propose it only.
Do not modify, delete, move, or overwrite files.
If execution fails, do not fix files. Report the failure.
Your result will be reread as worker_return.
```
