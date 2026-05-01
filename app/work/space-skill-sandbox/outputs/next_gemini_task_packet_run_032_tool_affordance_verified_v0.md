# Run 032 - Tool Affordance / Caller Shift Lens v0

## Packet Metadata

- packet_id: next_gemini_task_packet_run_032_tool_affordance_verified_v0
- intended_run: run_032
- created_by: Codex
- created_for: Gemini
- allowed_executor: Gemini via user-triggered manual runner only
- source_references:
  - app/work/space-skill-sandbox/outputs/operating_order_principles_v0.md
  - app/work/space-skill-sandbox/outputs/sandbox_promotion_pipeline_v0.md
  - app/work/space-skill-sandbox/outputs/session_role_map_v0.md
  - app/work/space-skill-sandbox/outputs/agent_handoff_boundary_rule_v0.md
  - app/work/space-skill-sandbox/outputs/packet_provenance_discipline_v0.md
  - app/work/space-skill-sandbox/outputs/sandbox_standard_output_contract_v0.md
- creation_context: Run 032 packet retrofitted after Run 031e/031f boundary and output contract setup
- execution_mode: user-triggered manual runner
- self_execution_allowed: false
- validation_separated_from_execution: true

## Mode

GEMINI / SANDBOX ONLY / LENS DRAFT / NO PROMOTION / NO AUTOMATION

## Purpose

외부 자료와 기존 sandbox 운영 질서를 바탕으로,
도구 / skill / 기존 프로그램 / relay / session role이 어떤 호출자를 전제로 설계되었는지 판독하는 렌즈를 작성한다.

핵심 질문:

- 이 도구는 인간 호출자를 전제로 하는가?
- LLM 호출자를 전제로 하는가?
- Codex/Gemini 같은 worker session을 전제로 하는가?
- 어떤 상황에서 사용하면 안 되는가?
- 어떤 stop point가 필요한가?
- source-space를 직접 건드릴 위험이 있는가?

## Input References

- app/work/space-skill-sandbox/outputs/operating_order_principles_v0.md
- app/work/space-skill-sandbox/outputs/sandbox_promotion_pipeline_v0.md
- app/work/space-skill-sandbox/outputs/session_role_map_v0.md
- app/work/space-skill-sandbox/outputs/agent_handoff_boundary_rule_v0.md
- app/work/space-skill-sandbox/outputs/packet_provenance_discipline_v0.md
- app/work/space-skill-sandbox/outputs/sandbox_standard_output_contract_v0.md

## Created Files

- app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md
- app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md
- app/work/space-skill-sandbox/review/validation_round_32.md

## Required Output Document Structure

Create:

app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md

Required sections:

1. Status
2. Purpose
3. Core Idea
4. Caller Types
5. Affordance Reading Checklist
6. Caller Shift Risk
7. Lens Output Format
8. Relationship to Existing Principles
9. Non-Promotion Note

Caller Types to include:

1. Human Caller
2. LLM Caller
3. Codex Worker Session
4. Gemini Analysis Session
5. Validation Session
6. Relay Session
7. Future Agent Session
8. Existing Program Caller

## Run Record

Create:

app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md

## Validation Record

Create:

app/work/space-skill-sandbox/review/validation_round_32.md

## Output Format

Use:

app/work/space-skill-sandbox/outputs/sandbox_standard_output_contract_v0.md

Do not invent a new report format unless this packet explicitly overrides it.

Run-specific validation additions:

- lens_created:
- run_record_created:
- validation_record_created:
- caller_types_defined:
- affordance_checklist_included:
- caller_shift_risk_included:
- lens_output_format_included:
- output_contract_referenced:
- packet_metadata_preserved:
- self_execution_allowed: false
- source_space_modified: false
- baseline_created: false
- relay_v1_declared: false
- automation_created: false
- tool_installed: false
- agent_implementation_created: false
- production_workflow_created: false

## Forbidden Actions

Do not:

- create next Gemini packet
- validate your own authority
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
- promote candidate documents

## Closeout Requirement

Use the standard output contract closeout section.

Include this boundary sentence:

This is a sandbox lens draft run only.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, router, controller, ontology, schema, agent implementation, tool installation, existing program merge, or production workflow was created.
tool_affordance_caller_shift_lens_v0 remains a sandbox candidate lens, not a source-space rule or baseline.
