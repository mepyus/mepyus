# Sandbox Standard Output Contract v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- relay_v1: false
- automation: false
- agent_implementation: false

## 1. Purpose

이 문서는 sandbox 작업에서 Codex / Gemini / Runner / Reviewer가 공통으로 따라야 하는 기본 출력 형식을 정의한다.

핵심 문장:

Packet마다 출력 형식을 반복해서 정의하지 않는다.
기본 출력은 이 contract를 따른다.
Packet에는 run-specific additions 또는 exceptions만 적는다.

## 2. Applies To

이 contract는 다음 출력에 적용된다.

- Codex validation report
- Gemini execution report
- runner outbox report
- run record closeout
- validation round closeout
- supervisor review report

## 3. Standard Report Format

모든 sandbox 작업 보고는 기본적으로 다음 형식을 따른다.

### Verdict

Use one of:

- PASS
- PASS_WITH_NOTE
- FAIL

### Created

새로 생성한 파일 목록.

없으면:

- None

### Modified

수정한 파일 목록.

없으면:

- None

### Tested

테스트한 명령 또는 확인 항목.

해당 없으면:

- Not applicable

### Validation

작업별 validation checklist 결과.

각 항목은 true / false / note 형태로 기록한다.

### Boundary Check

반드시 다음 항목을 포함한다.

- source_space_modified:
- baseline_created:
- relay_v1_declared:
- worker_guide_modified:
- worker_guide_v0_4_created:
- automation_created:
- hook_created:
- mcp_created:
- watch_mode_created:
- agent_implementation_created:
- router_created:
- controller_created:
- ontology_created:
- schema_created:
- tool_installed:
- existing_program_merged:
- production_workflow_created:

### Closeout

작업의 경계와 금지사항 준수 여부를 짧게 기록한다.

### Next

다음 가능한 sandbox-only step을 기록한다.
단, 다음 작업을 자동 실행하지 않는다.

## 4. Verdict Meaning

### PASS

요구된 산출물이 생성되었고, 금지사항 위반이 없으며, validation checklist를 충족한 경우.

### PASS_WITH_NOTE

핵심 작업은 완료되었지만 다음 중 하나가 있는 경우.

- missing reference 발견
- dry-run과 real-run 구분 필요
- 외부 환경 상태 불확실
- 다음 작업 전 확인이 필요한 note 존재
- 문서 후보는 성립하지만 후속 정렬 필요

### FAIL

다음 중 하나가 발생한 경우.

- 요구 산출물 누락
- packet 요구사항 미충족
- source-space 수정
- baseline 생성
- Relay v1.0 선언
- worker guide 임의 수정
- automation / hook / MCP / watch mode 생성
- agent implementation 생성
- production workflow 생성
- Gemini self-packet execution 발생
- dry-run을 실제 실행으로 오인

## 5. Standard Boundary Check Values

기본적으로 sandbox-only 작업에서는 다음 값이 기대된다.

```text
source_space_modified: false
baseline_created: false
relay_v1_declared: false
worker_guide_modified: false
worker_guide_v0_4_created: false
automation_created: false
hook_created: false
mcp_created: false
watch_mode_created: false
agent_implementation_created: false
router_created: false
controller_created: false
ontology_created: false
schema_created: false
tool_installed: false
existing_program_merged: false
production_workflow_created: false
```

## 6. Packet Reference Rule

앞으로 next task packet에는 긴 최종 보고 형식을 반복하지 않는다.

대신 다음 문장을 사용한다.

```text
Output format:
Use app/work/space-skill-sandbox/outputs/sandbox_standard_output_contract_v0.md.
Do not invent a new report format unless this packet explicitly overrides it.
```

Run-specific additions가 필요하면 packet에 별도로 적는다.

예:

```text
Run-specific validation additions:
- lens_created:
- caller_types_defined:
- affordance_checklist_included:
```

## 7. Runner Output Rule

Runner는 full validation을 수행하지 않는다.
Runner는 transport-level facts만 기록한다.

Runner output must include:

* packet_path
* run_id
* timestamp
* dry_run
* gemini_invoked
* timeout_status
* raw_output_path
* outbox_path

Runner must not declare full PASS for the task unless a separate validation record exists.

## 8. Gemini Output Rule

Gemini는 packet을 실행한 결과를 보고할 수 있다.

Gemini must include:

* Created
* Modified
* Validation
* Boundary Check
* Closeout
* Next

Gemini must not:

* create next packet for itself
* validate its own authority
* declare promotion
* declare baseline
* declare Relay v1.0

## 9. Codex Output Rule

Codex는 validation과 next packet preparation을 담당한다.

Codex output must include:

* whether previous run is valid
* whether output artifacts exist
* whether dry-run was mistaken for real run
* whether forbidden actions occurred
* whether next packet may be created

Codex must not create next packet if previous required artifacts are missing or invalid.

## 10. Non-Promotion Note

This output contract is a sandbox candidate only.
It is not a baseline.
It is not a source-space rule.
It is not Relay v1.0.
It does not create automation.
It does not create agent implementation.
