# Run 032 - Tool Affordance / Caller Shift Lens v0

## Mode
GEMINI / SANDBOX ONLY / LENS DRAFT / NO PROMOTION / NO AUTOMATION

## Purpose
외부 자료와 기존 sandbox 운영 질서를 바탕으로, 도구 / skill / 기존 프로그램 / relay / session role이 어떤 호출자를 전제로 설계되었는지 판독하는 렌즈를 작성한다.

핵심 질문:

- 이 도구는 인간 호출자를 전제로 하는가?
- LLM 호출자를 전제로 하는가?
- Codex/Gemini 같은 worker session을 전제로 하는가?
- 어떤 상황에서 사용하면 안 되는가?
- 어떤 stop point가 필요한가?
- source-space를 직접 건드릴 위험이 있는가?

## Created Files
- `app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md`
- `app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md`
- `app/work/space-skill-sandbox/review/validation_round_32.md`

## Input References
- `app/work/space-skill-sandbox/outputs/operating_order_principles_v0.md`
- `app/work/space-skill-sandbox/outputs/operating_order_source_map_v0.md`
- `app/work/space-skill-sandbox/outputs/sandbox_promotion_pipeline_v0.md`
- `app/work/space-skill-sandbox/outputs/session_role_map_v0.md`
- `app/work/space-skill-sandbox/outputs/sandbox_execution_chain_v0.md`

## Required Structure for `tool_affordance_caller_shift_lens_v0.md`

```markdown
# Tool Affordance / Caller Shift Lens v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- automation: false

## 1. Purpose

이 렌즈는 도구, skill, 기존 프로그램, relay packet, session role이 어떤 호출자를 전제로 설계되었는지 판독하기 위한 sandbox candidate lens다.

## 2. Core Idea

Function signature만으로는 부족하다.
LLM 또는 agent가 도구를 호출할 때는 다음 정보가 필요하다.

- when to use
- when not to use
- who is the caller
- what context is required
- what output is expected
- what must be stopped
- what requires user judgment

## 3. Caller Types

다음 caller type을 정의한다.

1. Human Caller
2. LLM Caller
3. Codex Worker Session
4. Gemini Analysis Session
5. Validation Session
6. Relay Session
7. Future Agent Session
8. Existing Program Caller

각 caller마다 다음 항목을 작성한다.

- caller description
- likely intent
- risk
- required affordance
- required stop point
- allowed output
- forbidden output

## 4. Affordance Reading Checklist

도구나 프로그램을 읽을 때 다음을 확인한다.

- What does it appear to do?
- Who is expected to call it?
- What hidden assumption does it make about the caller?
- Does it expect a human judgment before action?
- Can an LLM misuse it?
- Does it change files?
- Does it change source-space?
- Does it install tools?
- Does it create automation?
- Does it require preflight?
- Is it reversible?
- What output should be captured?

## 5. Caller Shift Risk

인간용 도구를 LLM이 사용할 때 생기는 위험을 정리한다.

예:

- 설명 부족
- 과잉 실행
- 잘못된 파일 수정
- source-space 오염
- 자동화 오인
- validation 생략
- readiness와 promotion 혼동
- failure를 rule로 오해

## 6. Lens Output Format

이 렌즈를 적용한 결과는 다음 형식으로 남긴다.

- target:
- original caller assumption:
- possible LLM caller:
- required affordance:
- required preflight:
- may read:
- may write:
- must not:
- expected output:
- stop point:
- user judgment required:
- candidate status:

## 7. Relationship to Existing Principles

다음 원칙과 연결한다.

- Function보다 Affordance
- Conversation보다 Agent-readable Context
- Plan before Execution
- Definition before Prompt
- User as Judge
- Core보다 Workspace

## 8. Non-Promotion Note

This lens is a sandbox candidate only.
It does not create a tool.
It does not install a tool.
It does not modify source-space.
It does not create automation.
It does not declare Relay v1.0.
It does not create a baseline.
```

## Run Record
Create:

```text
app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md
```

The run record must include:

- mode
- purpose
- input references
- created files
- modified files: None
- source_space_modified: false
- baseline_created: false
- relay_v1_declared: false
- automation_created: false
- tool_installed: false
- agent_implementation_created: false
- notes

## Validation Record
Create:

```text
app/work/space-skill-sandbox/review/validation_round_32.md
```

Validation checks:

- lens_created: true
- run_record_created: true
- validation_record_created: true
- caller_types_defined: true
- affordance_checklist_included: true
- caller_shift_risk_included: true
- output_format_included: true
- source_space_modified: false
- baseline_created: false
- relay_v1_declared: false
- automation_created: false
- tool_installed: false
- agent_implementation_created: false

## Forbidden Actions
Do not:

- modify source-space
- create baseline
- declare Relay v1.0
- modify worker guide
- create worker_guide_v0_4
- create automation
- install tools
- create MCP/hook/watch mode
- create router/controller/schema/ontology
- merge existing programs
- create production workflow

## Closeout
This is a sandbox lens draft run only.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, router, controller, ontology, schema, agent implementation, tool installation, existing program merge, or production workflow was created.
tool_affordance_caller_shift_lens_v0 remains a sandbox candidate lens, not a source-space rule or baseline.

## Final Report Format
Use:

```text
Verdict: PASS or PASS_WITH_NOTE or FAIL

Created files:
- ...

Modified files:
- None

Validation:
- lens_created:
- run_record_created:
- validation_record_created:
- caller_types_defined:
- affordance_checklist_included:
- caller_shift_risk_included:
- output_format_included:
- source_space_modified:
- baseline_created:
- relay_v1_declared:
- automation_created:
- tool_installed:
- agent_implementation_created:

Closeout:
This is a sandbox lens draft run only.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, router, controller, ontology, schema, agent implementation, tool installation, existing program merge, or production workflow was created.
tool_affordance_caller_shift_lens_v0 remains a sandbox candidate lens, not a source-space rule or baseline.
```
