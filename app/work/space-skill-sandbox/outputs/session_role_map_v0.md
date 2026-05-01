# Session Role Map v0

## 0. Status
- status: sandbox candidate
- agent_implementation: false
- automation: false
- source_space_rule: false
- baseline: false

## 1. Purpose
This document defines candidate session roles, boundaries, inputs, outputs, and stop points so that Gemini, Codex, or future agents can later be attached to a specific role.

에이전트를 먼저 붙이는 것이 아니라, 먼저 세션 역할과 권한 경계를 만든다. 그 다음 에이전트는 특정 세션 담당으로 붙는다.

This document is not an agent implementation, automatic router, MCP, hook, or watch mode.

## 2. Core Principle
Bad structure:

```text
Gemini야, 공간 전체 보고 알아서 해줘.
Codex야, 적당히 고쳐줘.
```

Good structure:

```text
너는 Intake Session 담당이다.
너는 Validation Session 담당이다.
너는 Readiness Audit Session 담당이다.
너는 source-space를 수정할 수 없다.
stop point가 나오면 사용자 판단으로 올려라.
```

## 3. Session Role List
1. Intake Session
2. Routing Session
3. Preflight Session
4. Provenance Session
5. Validation Session
6. Failure Recovery Session
7. Run Record Review Session
8. Cross-Review Session
9. Readiness Audit Session
10. Relay Session
11. User Surface Session

## 4. Role Card Format
Each role is defined using:

```text
### Role Name

- purpose:
- may read:
- may write:
- must not:
- input:
- output:
- stop point:
- escalation condition:
- related pipeline stage:
- related operating principles:
```

## 5. Role Definitions

### Intake Session
- purpose: Read external material or existing program material without direct adoption and lower it into sandbox terms.
- may read: User-provided material, source URLs, sandbox outputs, prior closeout cards, worker guide candidates.
- may write: Intake notes, material definitions, Borrow / Hold / Reject summaries inside sandbox candidate outputs or runs.
- must not: Modify source-space, install tools, merge programs, declare truth, or create baseline.
- input: Raw material, external article, repo/program reference, or user note.
- output: Intake summary and Borrow / Hold / Reject classification.
- stop point: Material asks for install, automation, source-space write, sensitive data access, or unclear ownership.
- escalation condition: Any source-space, permission, credential, install, automation, or merge request.
- related pipeline stage: raw material; material definition; intake.
- related operating principles: Function보다 Affordance; Program as Material; Definition before Prompt; Core보다 Workspace.

### Routing Session
- purpose: Decide which candidate skill, route, or session should handle the task.
- may read: Worker guide candidates, operating principles, run records, validation records, user request.
- may write: Route selection notes and run planning notes.
- must not: Create automatic router, controller, schema, or skill loader.
- input: User request or material definition.
- output: Selected manual route and rationale.
- stop point: No safe existing route exists or route requires forbidden action.
- escalation condition: New route requires automation, source-space modification, or user approval.
- related pipeline stage: route selection.
- related operating principles: Skill보다 Route; Metadata before Full Context; Plan before Execution.

### Preflight Session
- purpose: Detect high-risk actions before execution.
- may read: Plan draft, requested commands, target paths, worker guide candidate, validation notes.
- may write: Stop point note, safe-to-continue note, or escalation note.
- must not: Execute deletion, installation, hook/MCP/watch mode, promotion, baseline creation, or permission changes.
- input: Proposed action or plan.
- output: Preflight gate result.
- stop point: Delete, install, hook, MCP, watch mode, source-space promotion, baseline, credential, permission, or external side effect.
- escalation condition: Any high-risk action or unclear authority.
- related pipeline stage: plan review; run.
- related operating principles: Model보다 Harness; Plan before Execution; User as Judge; Core보다 Workspace.

### Provenance Session
- purpose: Separate source-claimed, inferred-pattern, ambiguous-link, and synthesis material.
- may read: External materials, graph candidates, source maps, signal bundles, run records.
- may write: Provenance labels and source boundary notes.
- must not: Create truth, ontology, schema, or baseline.
- input: Claim, link, graph node, or synthesis statement.
- output: Provenance classification.
- stop point: A claim is being used as fact without source boundary.
- escalation condition: Provenance uncertainty affects promotion, baseline, or user-facing judgment.
- related pipeline stage: material definition; validation; cross-review.
- related operating principles: Graph보다 Provenance; Error보다 Signal; Definition before Prompt.

### Validation Session
- purpose: Check whether a run obeyed required checks and boundaries.
- may read: Run records, created candidate files, required checklists, operating principles.
- may write: Validation round files inside sandbox review.
- must not: Modify existing worker guides, source-space files, relay templates, signal bundles, or run outputs beyond declared validation.
- input: Run record and created files.
- output: PASS, PASS_WITH_NOTE, or FAIL validation record.
- stop point: Missing artifact, forbidden action, baseline language, promotion drift, or undeclared write.
- escalation condition: Boundary drift or missing required evidence.
- related pipeline stage: validation.
- related operating principles: Readiness와 Promotion 분리; File before Chat; Ops Trace before Memory Loss.

### Failure Recovery Session
- purpose: Recover failures, risks, and validation notes as guide candidate material.
- may read: Validation notes, closeout cards, failure bundles, run records.
- may write: Failure signal candidates or guide candidate notes in sandbox bundles.
- must not: Modify worker guide directly, create worker_guide_v0_4, or promote signal to rule.
- input: Failure, PASS_WITH_NOTE, validation note, risk, or stop point.
- output: Sourced failure signal or guide candidate phrase.
- stop point: A signal is being generalized without repetition or source anchor.
- escalation condition: Repeated high-risk signal appears across bundles.
- related pipeline stage: signal bundle.
- related operating principles: Error보다 Signal; Graph보다 Provenance; Ops Trace before Memory Loss.

### Run Record Review Session
- purpose: Reread multiple runs to find repeated operational patterns.
- may read: Runs, validations, closeout cards, signal bundles.
- may write: Run review notes or signal candidates.
- must not: Treat a single run as global policy or update baseline.
- input: Set of run records or validation records.
- output: Repetition observations and risk notes.
- stop point: Pattern is being promoted without cross-review.
- escalation condition: Repeated pattern suggests a future guide or readiness candidate.
- related pipeline stage: cross-review; ops trace.
- related operating principles: Error보다 Signal; Ops Trace before Memory Loss; Readiness와 Promotion 분리.

### Cross-Review Session
- purpose: Compare signal bundles without merging them.
- may read: Signal bundles, run review notes, validation notes, closeout cards.
- may write: Cross-review matrix and merge readiness notes.
- must not: Merge bundles into policy, create worker_guide_v0_4, or declare source-space rule.
- input: Multiple signal bundles.
- output: observe / candidate_later / not_ready classifications.
- stop point: Repetition is being treated as automatic rule.
- escalation condition: A repeated signal may need user judgment or readiness audit.
- related pipeline stage: cross-review.
- related operating principles: Error보다 Signal; Graph보다 Provenance; Readiness와 Promotion 분리.

### Readiness Audit Session
- purpose: Audit whether a sandbox asset could later become a source-space interface candidate.
- may read: Runs, validations, closeouts, signal reviews, source maps, operating principles.
- may write: Readiness audit candidate document.
- must not: Perform promotion, modify source-space, create baseline, or approve itself.
- input: Sandbox asset or bundle of assets.
- output: Readiness classification and required user judgment.
- stop point: Audit language implies approval or source-space modification.
- escalation condition: Any asset is labeled promotion_candidate_later or source-space interface candidate.
- related pipeline stage: readiness audit.
- related operating principles: Readiness와 Promotion 분리; User as Judge; Core보다 Workspace.

### Relay Session
- purpose: Operate file-based inbox / task packet / outbox handoff.
- may read: Relay inbox requests, task packets, worker guide candidates, operating principles.
- may write: Outbox results, run records, validation references when declared.
- must not: Create watch mode, hook, MCP, automation, production workflow, or Relay v1.0 declaration.
- input: Inbox request or task packet.
- output: Outbox result and status footer.
- stop point: Request implies automatic execution or external system integration.
- escalation condition: Any automation, MCP, hook, watch mode, source-space write, or production workflow request.
- related pipeline stage: route selection; run; closeout.
- related operating principles: File before Chat; Conversation보다 Agent-readable Context; User as Judge.

### User Surface Session
- purpose: Create a clear decision surface for the user through closeout card and 4-line footer.
- may read: Run record, validation record, output files, risk notes, closeout requirements.
- may write: Closeout note, final report, footer, next-step options.
- must not: Present completion as approval, lock, baseline, or promotion.
- input: Completed run and validation result.
- output: User-facing closeout and next-step suggestion.
- stop point: Wording implies final approval or automatic next action.
- escalation condition: User decision is needed for promotion, baseline, automation, install, source-space modification, or agent implementation.
- related pipeline stage: closeout; user judgment; ops trace.
- related operating principles: User as Judge; File before Chat; Ops Trace before Memory Loss; Readiness와 Promotion 분리.

## 6. Agent Attachment Rule
Agent is attached to a session role, not to the whole space.

This means:
- Gemini does not receive unrestricted whole-space authority.
- Codex does not arbitrarily modify the whole space.
- An agent works only within the `may read`, `may write`, and `must not` boundaries in its role card.
- A stop point is escalated to user judgment.
- Role attachment does not create automation, MCP, hook, watch mode, or production workflow.

## 7. Non-Automation Note
This document is not an automatic execution structure.
This document is not MCP, hook, or watch mode.
This document is not an agent implementation.
This document is a session role candidate map.

## 8. Closeout Note
This document is a sandbox session role map candidate only.
No agent implementation was created.
No automation was created.
No source-space rule or baseline was created.
No Relay v1.0 was declared.

## 9. 4-line Footer
status: 완료
summary: session_role_map_v0는 미래 Gemini/Codex/agent를 전체 공간이 아니라 제한된 session role에 붙이기 위한 후보 역할표를 정의함
risk: role map을 agent implementation, automatic router, Relay v1.0, source-space rule로 오해하면 안 됨
next: sandbox_promotion_pipeline_v0와 함께 validation_round_30에서 role boundary와 non-automation 경계를 검증
