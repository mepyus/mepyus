# Operating Order Principles v0

## 1. Purpose
This document lowers recent external references and Space Skill Sandbox discussion into sandbox operating order candidates.

It is for judging future sandbox, relay, session role, existing program integration, and agent-readable context work.

## 2. Scope
- Applies only inside `app/work/space-skill-sandbox`.
- Describes candidate operating principles, not source-space rules.
- Does not declare Relay v1.0.
- Does not create a baseline, schema, controller, router, ontology, automation, hook, MCP, watch mode, agent implementation, tool installation, existing program merge, or production workflow.

## 3. Source References
1. Agent Harness Engineering - https://addyosmani.com/blog/agent-harness-engineering/
2. 도구는 만든 사람을 떠나서 살아간다 - https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
3. Warp - https://github.com/warpdotdev/warp
4. Browser Harness - https://github.com/browser-use/browser-harness
5. mini-swe-agent - https://github.com/SWE-agent/mini-swe-agent
6. Graphify - https://github.com/safishamsi/graphify
7. AWS sample-deep-insight - https://github.com/aws-samples/sample-deep-insight
8. Laws of Software Engineering - https://lawsofsoftwareengineering.com/

Internal references read:
- `app/work/space-skill-sandbox/review/space_skill_sandbox_v0_3_closeout_card.md`
- `app/work/space-skill-sandbox/review/sandbox_relay_v0_closeout_card.md`
- `app/work/space-skill-sandbox/review/compact_relay_v0_1_closeout_card.md`
- `app/work/space-skill-sandbox/review/source_space_promotion_readiness_audit_v0.md`
- `app/work/space-skill-sandbox/outputs/signal_bundle_cross_review_matrix_v0.md`
- `app/work/space-skill-sandbox/worker_guides/worker_guide_v0_3_candidate.md`

missing_reference:
- path: `app/work/space-skill-sandbox/outputs/sandbox_promotion_pipeline_v0.md`
  reason: file not present in repository at run time
  impact: pipeline language is kept as candidate language from the 04-29 package, not treated as an existing validated file
- path: `app/work/space-skill-sandbox/outputs/session_role_map_v0.md`
  reason: file not present in repository at run time
  impact: session role language is kept as candidate language from the 04-29 package, not treated as an existing validated file

## 4. Why This Order Is Needed
The sandbox already separates candidate work from source-space, manual relay from automation, and readiness from promotion. As external materials and existing programs are considered, the main risk is not lack of ideas. The main risk is crossing boundaries too early.

These principles make the boundary explicit: first define the harness, affordance, route, workspace, context, signal, provenance, readiness gate, user judgment point, and operating trace. Only later can a candidate be audited for possible source-space interface use.

## 5. The 15 Operating Principles
1. Model보다 Harness
2. Function보다 Affordance
3. Skill보다 Route
4. Core보다 Workspace
5. Conversation보다 Agent-readable Context
6. Error보다 Signal
7. Graph보다 Provenance
8. Readiness와 Promotion 분리
9. User as Judge
10. Program as Material
11. Plan before Execution
12. Metadata before Full Context
13. Definition before Prompt
14. File before Chat
15. Ops Trace before Memory Loss

## 6. Principle Details

### 1. Model보다 Harness
principle: Model보다 Harness
meaning: The model matters less than the environment that constrains, equips, verifies, and recovers its work.
external_reference: Agent Harness Engineering; Browser Harness; mini-swe-agent; AWS sample-deep-insight
our_space_interpretation: Agent = Model + Relay + Worker Guide + Session Role + Skill + Run + Validation + Signal Memory + Readiness Gate.
practical_rule: Before adding agent power, define files, permissions, stop points, validation, and recovery.
borrow: Harness thinking, browser/workspace isolation, small agent loop, plan/review pattern.
hold: Production deployment, managed runtimes, automatic tool routing.
reject_for_now: Agent implementation, MCP/hook/watch mode, production workflow.
risk_if_misread: Treating a stronger model as a substitute for boundary design.
risk: Harness language can become overbuilt infrastructure if not kept as candidate structure.
candidate_use: Use as the top-level test for future agent or CLI attachment.
status: operating_order_candidate

### 2. Function보다 Affordance
principle: Function보다 Affordance
meaning: A tool must reveal when it should and should not be used, not only what arguments it accepts.
external_reference: 도구는 만든 사람을 떠나서 살아간다
our_space_interpretation: Worker guide, skill trigger, forbidden drift, and preflight stop point are tool handles for LLM/Codex/Gemini.
practical_rule: Every candidate tool or guide needs intended caller, allowed use, forbidden use, and stop point language.
borrow: Tool description as caller-facing affordance.
hold: Direct MCP exposure of existing tools.
reject_for_now: Existing program auto-tooling without caller/affordance analysis.
risk_if_misread: Thinking a function signature is enough for agent use.
risk: Over-describing tools can make routing rigid.
candidate_use: Create a Tool Affordance / Caller Shift Lens candidate.
status: operating_order_candidate

### 3. Skill보다 Route
principle: Skill보다 Route
meaning: Small skills are useful, but user intent usually needs a route across several skills.
external_reference: AWS sample-deep-insight; mini-swe-agent
our_space_interpretation: Skills remain small candidate handles, while routes organize external review, existing program integration, promotion readiness, and run review.
practical_rule: Name the route before adding or invoking multiple skills.
borrow: Planner/coordinator separation and skill lazy loading as concepts.
hold: Automatic skill discovery/loader.
reject_for_now: Automatic route execution.
risk_if_misread: Treating one skill as a whole workflow.
risk: Route maps can drift into router/controller implementation.
candidate_use: Draft Intent-Level Route Map v0 later.
status: operating_order_candidate

### 4. Core보다 Workspace
principle: Core보다 Workspace
meaning: Protected core and editable workspace must remain separate.
external_reference: Agent Harness Engineering; Browser Harness; mini-swe-agent
our_space_interpretation: source-space is protected core, sandbox is candidate workspace, relay is handoff surface.
practical_rule: New work starts in sandbox outputs/runs/review unless the user explicitly authorizes source-space modification.
borrow: Isolated workspace and file-based execution ideas.
hold: Stronger deployment isolation.
reject_for_now: Direct source-space modification from sandbox results.
risk_if_misread: Treating sandbox completion as permission to alter core.
risk: Too much separation can hide useful candidates if closeout is weak.
candidate_use: Use in promotion readiness checks.
status: operating_order_candidate

### 5. Conversation보다 Agent-readable Context
principle: Conversation보다 Agent-readable Context
meaning: Important operating context should live in files that agents can read, not only in chat memory.
external_reference: AWS sample-deep-insight; mini-swe-agent; Warp
our_space_interpretation: Worker guides, session role maps, promotion pipelines, relay task packets, signal bundles, and closeout cards are agent-readable context.
practical_rule: If a decision must survive compaction or handoff, record it in a run, validation, outbox, output, or closeout file.
borrow: File-based context and reusable skill docs.
hold: Full context loading.
reject_for_now: Treating chat-only instructions as durable operating rules.
risk_if_misread: Creating too many files without validation or closeout.
risk: File context can become stale if not tied to runs.
candidate_use: Use in all future relay/session package design.
status: operating_order_candidate

### 6. Error보다 Signal
principle: Error보다 Signal
meaning: Failure is not immediately a rule; it is a sourced signal.
external_reference: Laws of Software Engineering; sandbox failure-to-guide runs
our_space_interpretation: Failure flows from validation note to guide candidate to signal bundle to cross-review to readiness audit.
practical_rule: Preserve source anchor, repetition level, and merge readiness before turning a failure into guidance.
borrow: Failure learning and operational feedback.
hold: Automatic rule updates from failure.
reject_for_now: Promoting one failure into baseline.
risk_if_misread: Freezing temporary mistakes as permanent rules.
risk: Signals can pile up without cross-review.
candidate_use: Continue using signal bundles and cross-review matrices.
status: operating_order_candidate

### 7. Graph보다 Provenance
principle: Graph보다 Provenance
meaning: Connections are useful only when their source and confidence are visible.
external_reference: Graphify; sandbox graph-layer-evaluation runs
our_space_interpretation: Graph Layer is a map, not Deep Space; Mini Graph is not ontology; source-claimed is not truth.
practical_rule: Label source-claimed, inferred-pattern, ambiguous-link, and synthesis nodes separately.
borrow: Graph as navigation aid.
hold: Graph tooling installation.
reject_for_now: Ontology/schema/baseline creation from Mini Graph.
risk_if_misread: Treating visual or graph structure as truth.
risk: Provenance labels can be skipped when work gets rushed.
candidate_use: Use in external material and existing program analysis.
status: operating_order_candidate

### 8. Readiness와 Promotion 분리
principle: Readiness와 Promotion 분리
meaning: Being ready for consideration is not the same as being promoted.
external_reference: Source-space Promotion Readiness Audit v0; AWS sample-deep-insight
our_space_interpretation: readiness audit does not modify source-space; promotion_candidate_later is not promotion.
practical_rule: Use readiness status only as a recommendation for user judgment.
borrow: Review gates before production movement.
hold: Formal promotion workflow.
reject_for_now: Treating audit output as automatic approval.
risk_if_misread: Collapsing candidate and rule boundaries.
risk: Repeated PASS results can create false confidence.
candidate_use: Keep audit files separate from promoted source-space files.
status: operating_order_candidate

### 9. User as Judge
principle: User as Judge
meaning: The user is not a copy-paste relay; the user is the final judgment point.
external_reference: AWS sample-deep-insight; Sandbox Relay v0
our_space_interpretation: User gives request and judgment; agents read task packets and return outbox results.
practical_rule: Escalate source-space, installation, automation, deletion, permissions, and baseline decisions.
borrow: Human-in-the-loop plan review.
hold: Web UI review surface.
reject_for_now: Autonomous approval of high-risk work.
risk_if_misread: Burdening the user with all operational detail instead of judgment.
risk: Too many escalations can slow low-risk read-only work.
candidate_use: Define session role read/write boundaries later.
status: operating_order_candidate

### 10. Program as Material
principle: Program as Material
meaning: Existing programs are not merge targets first; they are material to analyze by caller, affordance, state, risk, and session role.
external_reference: 도구는 만든 사람을 떠나서 살아간다; AWS sample-deep-insight; Warp
our_space_interpretation: existing program -> caller/affordance analysis -> session role mapping -> preflight -> shadow run -> adapter candidate -> readiness audit.
practical_rule: Never expose a program to agents before mapping inputs, outputs, state mutation, filesystem writes, external calls, failure traces, and stop points.
borrow: Program/tool reuse through controlled interfaces.
hold: Wrapper/adapter design until a lens exists.
reject_for_now: Direct merge or direct agent tool exposure.
risk_if_misread: Importing old assumptions and hidden side effects.
risk: Over-analysis can delay harmless read-only reuse.
candidate_use: Draft Existing Program Integration Lens v0 later.
status: operating_order_candidate

### 11. Plan before Execution
principle: Plan before Execution
meaning: Risky or expensive work needs plan review before execution.
external_reference: AWS sample-deep-insight; Agent Harness Engineering
our_space_interpretation: Plan review belongs before existing program absorption, source-space contact, Relay v1.0, worker guide upgrade, MCP/hook/watch mode, and graph tool installation.
practical_rule: If an action changes state, installs tools, declares a baseline, or affects source-space, stop and draft a plan.
borrow: Planner/reviewer separation and HITL plan review.
hold: Full planner/supervisor implementation.
reject_for_now: Production workflow creation.
risk_if_misread: Planning everything, including trivial read-only checks.
risk: Plan docs can be mistaken for approval.
candidate_use: Add plan draft/review steps to a future pipeline candidate.
status: operating_order_candidate

### 12. Metadata before Full Context
principle: Metadata before Full Context
meaning: Agents should discover relevant context through metadata before loading everything.
external_reference: AWS sample-deep-insight; mini-swe-agent
our_space_interpretation: Worker guide should behave like a compact discovery index, not a full manual.
practical_rule: Candidate skills and documents should expose purpose, scope, allowed use, forbidden use, and source anchor.
borrow: Skill lazy loading and compact descriptions.
hold: Automatic skill loader.
reject_for_now: Full-context dump as default operation.
risk_if_misread: Metadata becomes shallow labels with no boundary value.
risk: Insufficient metadata can cause wrong route selection.
candidate_use: Draft Skill Metadata Discipline Lens v0 later.
status: operating_order_candidate

### 13. Definition before Prompt
principle: Definition before Prompt
meaning: Define the material, role, and boundary before asking an agent to analyze.
external_reference: Agent Harness Engineering; 도구는 만든 사람을 떠나서 살아간다
our_space_interpretation: External sources, existing programs, and run records need source/material/role definitions before synthesis.
practical_rule: Start with material definition, caller assumption, status, risk, and intended route.
borrow: Upfront task framing and tool affordance definition.
hold: Formal schema for every input.
reject_for_now: Prompting raw material directly into broad conclusions.
risk_if_misread: Definitions turn into rigid ontology.
risk: Weak definitions can hide source boundaries.
candidate_use: Add definition step to future route maps.
status: operating_order_candidate

### 14. File before Chat
principle: File before Chat
meaning: Important execution should leave file-based run, validation, and outbox traces.
external_reference: Sandbox Relay v0; Compact Relay v0.1; AWS sample-deep-insight
our_space_interpretation: Relay/inbox, runs, relay/outbox, review, and outputs are the durable handoff surface.
practical_rule: Create or update sandbox files for substantive runs; keep chat as trigger and final report.
borrow: File-based execution and result artifacts.
hold: Watch mode and automatic triggers.
reject_for_now: Chat-only completion for structural work.
risk_if_misread: Creating files without clear closeout.
risk: File trace can look like production workflow if status is unclear.
candidate_use: Use for all sandbox run packages.
status: operating_order_candidate

### 15. Ops Trace before Memory Loss
principle: Ops Trace before Memory Loss
meaning: Record the operation, not only the result, before context is lost.
external_reference: AWS sample-deep-insight; Laws of Software Engineering; sandbox run/validation pattern
our_space_interpretation: Verdict, created files, modified files, risk, next, manual steps, missing references, and boundary checks are operating trace.
practical_rule: Every run package needs run record, validation, and closeout language.
borrow: Token/cost/duration and operations tracking as future ideas.
hold: Ops dashboard implementation.
reject_for_now: Production observability stack.
risk_if_misread: Treating trace as bureaucracy instead of recovery material.
risk: Missing trace makes future readiness audits unreliable.
candidate_use: Use run and validation files to preserve package state.
status: operating_order_candidate

## 7. How This Order Maps To Our Sandbox
- `worker_guide_v0_3_candidate` already acts as a compact route guide for candidate skills.
- `Sandbox Relay v0` and `Compact Relay v0.1` already show file-based handoff without automation.
- `signal_bundle_cross_review_matrix_v0` already separates repeated signals from premature merge.
- `source_space_promotion_readiness_audit_v0` already separates readiness from actual promotion.
- This document does not replace those assets. It names the higher operating order they point toward.

## 8. How This Order Maps To Future Agents
Future agents should be attached to roles, not to the whole space.

Candidate role families:
- Intake / Material Definition
- Route Selection
- Plan Draft
- Plan Review
- Run Execution
- Validation
- Signal Review
- Readiness Audit
- Ops Trace

Each role needs explicit read/write boundaries before any agent implementation.

## 9. How This Order Maps To Existing Program Integration
Existing programs should be read through:
- input and output
- state mutation
- filesystem writes
- external calls
- permissions
- failure trace
- caller assumption
- tool affordance
- session role mapping
- preflight stop points
- shadow run possibility
- adapter candidate possibility

Direct merge remains forbidden in this package.

## 10. Forbidden Misreadings
- This is not a source-space rule.
- This is not a baseline.
- This is not Relay v1.0.
- This is not a worker guide update.
- This is not a schema, controller, router, or ontology.
- This is not automation.
- This is not hook, MCP, or watch mode.
- This is not an agent implementation.
- This is not a production workflow.
- This is not existing program merge.
- This is not tool installation.

## 11. Candidate Next Documents
1. Sandbox Promotion Pipeline v0
2. Session Role Map v0
3. Tool Affordance / Caller Shift Lens v0
4. Intent-Level Route Map v0
5. Existing Program Integration Lens v0
6. Skill Metadata Discipline Lens v0

## 12. Not A Baseline Notice
This document is a sandbox operating order candidate. It records a candidate interpretation of recent external materials and sandbox discussion. It does not modify source-space and does not approve future promotion.

## 13. 4-line Footer
status: 완료
summary: 15개 Operating Order Principles를 sandbox candidate 문서로 정리하고, 외부 자료와 현재 sandbox/relay/readiness/signal 구조를 연결함
risk: 이 문서를 source-space rule, baseline, Relay v1.0, 자동화, agent implementation, production workflow, 기존 프로그램 merge의 근거로 오해하면 안 됨
next: 사용자 판단 후 Sandbox Promotion Pipeline v0 또는 Session Role Map v0 후보 문서를 별도 run으로 작성할지 결정

---
This is a sandbox operating order principles document only.
No source-space promotion was performed.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, tool installation, baseline, schema, controller, router, ontology, agent implementation, or production workflow was created.
operating_order_principles_v0 remains a sandbox candidate structural document, not a source-space rule or baseline.
