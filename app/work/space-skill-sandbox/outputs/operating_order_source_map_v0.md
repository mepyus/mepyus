# Operating Order Source Map v0

## 0. Purpose
This source map records how the 8 external references and current sandbox references support the 15 Operating Order Principles.

It is a source-to-principle map only. It is not a citation baseline, source-space rule, Relay v1.0 declaration, or production workflow.

## 1. Source List
| ID | Source | URL | Reading Status | Boundary |
|---|---|---|---|---|
| S1 | Agent Harness Engineering | https://addyosmani.com/blog/agent-harness-engineering/ | external reference from 04-29 package | reference only |
| S2 | 도구는 만든 사람을 떠나서 살아간다 | https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/ | summarized in 04-29 package | reference only |
| S3 | Warp | https://github.com/warpdotdev/warp | external reference from 04-29 package | reference only |
| S4 | Browser Harness | https://github.com/browser-use/browser-harness | external reference from 04-29 package | reference only |
| S5 | mini-swe-agent | https://github.com/SWE-agent/mini-swe-agent | external reference from 04-29 package | reference only |
| S6 | Graphify | https://github.com/safishamsi/graphify | prior sandbox graph reference | no installation |
| S7 | AWS sample-deep-insight | https://github.com/aws-samples/sample-deep-insight | summarized in 04-29 package | no structure copy |
| S8 | Laws of Software Engineering | https://lawsofsoftwareengineering.com/ | external reference from 04-29 package | reference only |

Internal sandbox references:
- I1: `space_skill_sandbox_v0_3_closeout_card.md`
- I2: `sandbox_relay_v0_closeout_card.md`
- I3: `compact_relay_v0_1_closeout_card.md`
- I4: `source_space_promotion_readiness_audit_v0.md`
- I5: `signal_bundle_cross_review_matrix_v0.md`
- I6: `worker_guide_v0_3_candidate.md`

missing_reference:
- `app/work/space-skill-sandbox/outputs/sandbox_promotion_pipeline_v0.md`
- `app/work/space-skill-sandbox/outputs/session_role_map_v0.md`

## 2. Principle Matrix
| Principle | Main Sources | Internal Anchors | Borrow | Hold | Reject for Now |
|---|---|---|---|---|---|
| Model보다 Harness | S1, S4, S5, S7 | I1, I6 | harness before agent power | managed deployment | agent implementation |
| Function보다 Affordance | S2 | I6 | caller-facing tool handles | MCP tool exposure | existing program auto-tooling |
| Skill보다 Route | S5, S7 | I1, I6 | route over isolated skill | auto discovery | router/controller |
| Core보다 Workspace | S1, S4, S5 | I1, I4 | protected core/editable workspace | stronger isolation | source-space modification |
| Conversation보다 Agent-readable Context | S3, S5, S7 | I2, I3, I6 | durable file context | full context loading | chat-only operating rule |
| Error보다 Signal | S8 | I1, I5 | failure as sourced signal | auto rule update | baseline from one failure |
| Graph보다 Provenance | S6 | I5, I6 | provenance-labeled map | graph tool install | ontology/schema |
| Readiness와 Promotion 분리 | S7 | I4 | review gate | formal promotion workflow | automatic approval |
| User as Judge | S7 | I2, I3, I4 | HITL judgment | Web UI | autonomous approval |
| Program as Material | S2, S3, S7 | I4, I6 | caller/risk/session mapping | adapter design | direct merge |
| Plan before Execution | S1, S7 | I4 | plan review | supervisor implementation | production workflow |
| Metadata before Full Context | S5, S7 | I6 | skill metadata/lazy loading | auto loader | full dump default |
| Definition before Prompt | S1, S2 | I6 | define material before synthesis | formal schema | raw broad prompting |
| File before Chat | S3, S7 | I2, I3 | file-based run/outbox | watch mode | chat-only closeout |
| Ops Trace before Memory Loss | S7, S8 | I1, I4, I5 | run/validation trace | ops dashboard | observability stack |

## 3. Source-by-Source Reading

### S1. Agent Harness Engineering
Borrow:
- Treat agent quality as the result of model plus environment, tools, permissions, validation, and recovery.
- Use plan/review concepts before risky execution.
Hold:
- Any direct framework or infrastructure commitment.
Reject for Now:
- Agent implementation or production harness construction.
Contributes To:
- Model보다 Harness
- Core보다 Workspace
- Plan before Execution
- Definition before Prompt

### S2. 도구는 만든 사람을 떠나서 살아간다
Borrow:
- Tool description is affordance for an LLM caller.
- Caller shift changes what a function means operationally.
Hold:
- MCP exposure.
Reject for Now:
- Directly turning existing programs into tools.
Contributes To:
- Function보다 Affordance
- Program as Material
- Definition before Prompt

### S3. Warp
Borrow:
- Terminal/workspace tools can be read as operating surfaces, not only commands.
Hold:
- Product-specific workflow adoption.
Reject for Now:
- Replacing current relay with external product structure.
Contributes To:
- Conversation보다 Agent-readable Context
- Program as Material
- File before Chat

### S4. Browser Harness
Borrow:
- Harness and environment boundary thinking.
Hold:
- Browser execution stack.
Reject for Now:
- Tool installation or browser automation implementation.
Contributes To:
- Model보다 Harness
- Core보다 Workspace

### S5. mini-swe-agent
Borrow:
- Small loop, workspace discipline, compact agent instructions.
Hold:
- Direct agent runner adoption.
Reject for Now:
- Automatic coding agent implementation.
Contributes To:
- Model보다 Harness
- Skill보다 Route
- Core보다 Workspace
- Conversation보다 Agent-readable Context
- Metadata before Full Context

### S6. Graphify
Borrow:
- Graph as possible map of relationships.
Hold:
- Actual Graphify installation.
Reject for Now:
- Ontology, schema, or baseline from graph output.
Contributes To:
- Graph보다 Provenance

### S7. AWS sample-deep-insight
Borrow:
- Coordinator/planner/supervisor/tool-agent role separation as a reading lens.
- HITL plan review, skill lazy loading, file-based execution, and ops trace as concepts.
Hold:
- Bedrock/AgentCore, managed deployment, Web UI, ops dashboard.
Reject for Now:
- Deep Insight structure copy, production workflow, automatic skill invocation.
Contributes To:
- Model보다 Harness
- Skill보다 Route
- Conversation보다 Agent-readable Context
- Readiness와 Promotion 분리
- User as Judge
- Program as Material
- Plan before Execution
- Metadata before Full Context
- File before Chat
- Ops Trace before Memory Loss

### S8. Laws of Software Engineering
Borrow:
- Treat repeated failures and operational friction as learning material.
Hold:
- Turning laws into local source-space rules.
Reject for Now:
- Baseline creation from generalized maxims.
Contributes To:
- Error보다 Signal
- Ops Trace before Memory Loss

## 4. Cross-Source Convergence
The strongest convergence is:
- Harness before agent implementation.
- Affordance before tool exposure.
- Workspace before core modification.
- File/context before chat memory.
- Signal/provenance before rule/baseline.
- Readiness/user judgment before promotion.
- Plan/definition/metadata before execution.
- Ops trace before future memory loss.

## 5. Non-Promotion Note
This source map does not prove that any external source should be adopted. It records how each source is being lowered into sandbox candidate language.

## 6. 4-line Footer
status: 완료
summary: 8개 외부 자료와 현재 샌드박스 내부 근거를 15개 Operating Order Principles에 매핑하고 Borrow/Hold/Reject 경계를 기록함
risk: source map을 citation baseline이나 source-space rule로 오해하면 외부 자료가 과잉 승격될 수 있음
next: 사용자 판단 후 missing_reference로 남은 Sandbox Promotion Pipeline v0와 Session Role Map v0 후보를 별도 작성할지 결정

---
This is a sandbox operating order source map only.
No source-space promotion was performed.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, tool installation, baseline, schema, controller, router, ontology, agent implementation, or production workflow was created.
operating_order_source_map_v0 remains a sandbox candidate structural document, not a source-space rule or baseline.
