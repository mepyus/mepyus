# Sandbox Promotion Pipeline v0

## 0. Status
- status: sandbox candidate
- source_space_rule: false
- baseline: false
- promotion_executed: false
- automation: false

## 1. Purpose
This document defines candidate stages and gates for how a sandbox asset may move from raw material toward a source-space interface candidate.

샌드박스 자산은 source-space로 직접 올라가지 않는다. 먼저 material definition, intake, route selection, plan review, run, validation, signal recovery, readiness audit, user judgment를 거친다.

This document does not perform promotion. It only describes a candidate pipeline for judging promotion readiness.

## 2. Pipeline Overview
```text
raw material
→ material definition
→ intake
→ route selection
→ plan draft
→ plan review
→ run
→ validation
→ closeout
→ signal bundle
→ cross-review
→ readiness audit
→ user judgment
→ source-space interface candidate
→ ops trace
```

## 3. Stage Definitions

### 1. raw material
- stage name: raw material
- purpose: Receive external material, existing program material, run records, or user-provided context without adopting it.
- allowed action: Read, list, identify source, and preserve original boundary.
- forbidden action: Treat material as truth, baseline, source-space rule, or implementation instruction.
- output: raw material note or source pointer.
- stop point: Material asks for install, automation, source-space edit, deletion, credential, or permission change.
- required evidence: Source path, URL, user-provided context, or run reference.

### 2. material definition
- stage name: material definition
- purpose: Define what the material is before analysis.
- allowed action: Record type, source, caller assumption, scope, possible risk, and intended use.
- forbidden action: Jump directly into synthesis, prompt expansion, or tool exposure.
- output: material definition block.
- stop point: Material identity or ownership is unclear.
- required evidence: Source anchor and scope statement.

### 3. intake
- stage name: intake
- purpose: Lower material into sandbox terms.
- allowed action: Borrow / Hold / Reject classification and boundary notes.
- forbidden action: Merge, install, promote, or convert to baseline.
- output: intake summary.
- stop point: Material requires source-space access or external execution.
- required evidence: Classification rationale and risk note.

### 4. route selection
- stage name: route selection
- purpose: Choose which candidate skill, guide, or session path should handle the material.
- allowed action: Select a manual route from existing candidate guidance.
- forbidden action: Create automatic router, controller, or skill loader.
- output: selected route and reason.
- stop point: Multiple routes conflict or require new authority.
- required evidence: Worker guide or operating principle reference.

### 5. plan draft
- stage name: plan draft
- purpose: Draft the intended sandbox-only work before risky execution.
- allowed action: Define files to create, files to read, forbidden actions, and validation checks.
- forbidden action: Execute risky work before plan review.
- output: plan draft.
- stop point: Plan includes source-space modification, automation, tool installation, or agent implementation.
- required evidence: Scope, write set, and boundary checklist.

### 6. plan review
- stage name: plan review
- purpose: Check whether the plan stays inside sandbox boundaries.
- allowed action: Approve sandbox-only execution or escalate to user judgment.
- forbidden action: Treat plan review as promotion approval.
- output: review decision.
- stop point: Any unclear permission, high-risk write, or source-space contact.
- required evidence: Explicit no-promotion/no-automation check.

### 7. run
- stage name: run
- purpose: Execute the approved sandbox-only work.
- allowed action: Create declared sandbox candidate files and record execution.
- forbidden action: Modify undeclared files, promote assets, install tools, create automation, or implement agents.
- output: run record and declared artifacts.
- stop point: Execution requires a forbidden action or unplanned write.
- required evidence: Created files, modified files, mode, and boundary flags.

### 8. validation
- stage name: validation
- purpose: Check the run against required values and boundaries.
- allowed action: Validate presence, status, forbidden-action absence, and candidate-only language.
- forbidden action: Fix by modifying unrelated existing files or convert validation into policy.
- output: validation round.
- stop point: Missing required artifact, boundary drift, or promotion language.
- required evidence: Required checks and verdict.

### 9. closeout
- stage name: closeout
- purpose: Summarize result, risk, and next user-facing decision.
- allowed action: Record status, summary, risk, next, and exact closeout statement.
- forbidden action: Present completion as approval, lock, baseline, or promotion.
- output: closeout note or footer.
- stop point: Closeout implies automatic next action.
- required evidence: 4-line footer or required closeout statement.

### 10. signal bundle
- stage name: signal bundle
- purpose: Preserve failures, risks, and repeated notes as sourced signals.
- allowed action: Store signal with source anchor, status, and risk.
- forbidden action: Treat signal as rule or immediately update worker guide.
- output: signal bundle candidate.
- stop point: Signal lacks source anchor or is being generalized too early.
- required evidence: Origin, quote or paraphrase anchor, and candidate status.

### 11. cross-review
- stage name: cross-review
- purpose: Compare signal bundles without merging them.
- allowed action: Mark repetition, observe patterns, and identify candidate_later boundaries.
- forbidden action: Merge bundles into source-space rule or worker_guide_v0_4.
- output: cross-review matrix.
- stop point: Repetition is being treated as automatic policy.
- required evidence: Source-specific differences and merge readiness.

### 12. readiness audit
- stage name: readiness audit
- purpose: Judge whether a sandbox asset may become a future source-space interface candidate.
- allowed action: Classify readiness, risks, and needed user judgment.
- forbidden action: Execute promotion or modify source-space.
- output: readiness audit.
- stop point: Audit result is interpreted as approval.
- required evidence: Repeatability, boundary, usability, overgeneralization risk.

### 13. user judgment
- stage name: user judgment
- purpose: Put the final decision in the user's hands.
- allowed action: Present options, risk, and recommended next sandbox-only step.
- forbidden action: Substitute agent decision for user approval on high-risk changes.
- output: user decision or hold state.
- stop point: User has not explicitly approved promotion or risky work.
- required evidence: Clear decision surface.

### 14. source-space interface candidate
- stage name: source-space interface candidate
- purpose: Name a candidate that could later interface with source-space after separate approval.
- allowed action: Describe candidate scope and required evidence before promotion.
- forbidden action: Modify source-space, declare source-space rule, or create baseline.
- output: interface candidate note.
- stop point: Candidate is being copied into source-space.
- required evidence: Readiness audit and user judgment.

### 15. ops trace
- stage name: ops trace
- purpose: Preserve operational evidence for future review.
- allowed action: Record verdict, created files, modified files, risks, missing references, next, and boundary checks.
- forbidden action: Treat trace as production observability or automation.
- output: run/validation/closeout trace.
- stop point: Trace is incomplete or contradicts actual files.
- required evidence: File list, validation values, and closeout statement.

## 4. Gate Rules

### Preflight Gate
- what it checks: Risky work such as deletion, install, source-space modification, baseline creation, hook/MCP/watch mode, automation, permissions, or credentials.
- who/what may perform it: Human operator or sandbox worker following preflight guidance.
- what it cannot do: Approve or execute the risky action.
- required output: Stop point or safe-to-continue note.
- escalation condition: Any high-risk action or unclear authority.

### Validation Gate
- what it checks: Required artifacts, status flags, forbidden-action absence, and boundary language.
- who/what may perform it: Validation Session or manual reviewer.
- what it cannot do: Promote, repair unrelated files, or convert validation into policy.
- required output: PASS, PASS_WITH_NOTE, or FAIL.
- escalation condition: Missing artifact, boundary drift, or baseline/promotion wording.

### Signal Recovery Gate
- what it checks: Whether failures and risks are preserved as sourced signals.
- who/what may perform it: Failure Recovery Session.
- what it cannot do: Update worker guide directly or make rules.
- required output: Signal candidate with source anchor.
- escalation condition: Repeated high-risk signal or missing provenance.

### Cross-Review Gate
- what it checks: Repetition across signal bundles and source-specific differences.
- who/what may perform it: Cross-Review Session.
- what it cannot do: Merge bundles into policy or create worker_guide_v0_4.
- required output: Cross-review matrix and merge readiness.
- escalation condition: A repeated signal appears ready for candidate_later review.

### Readiness Audit Gate
- what it checks: Repeatability, boundary stability, usability, and overgeneralization risk.
- who/what may perform it: Readiness Audit Session.
- what it cannot do: Promote or modify source-space.
- required output: Readiness classification and user judgment requirement.
- escalation condition: Any candidate is proposed for source-space interface.

### User Judgment Gate
- what it checks: Whether the user explicitly approves moving beyond sandbox candidate status.
- who/what may perform it: User only.
- what it cannot do: Be replaced by agent inference.
- required output: Explicit user decision.
- escalation condition: Source-space modification, baseline, install, automation, agent implementation, or production workflow.

### Source-space Interface Gate
- what it checks: Whether a candidate is only being named as an interface candidate, not promoted.
- who/what may perform it: User-approved reviewer in a separate future run.
- what it cannot do: Modify source-space without explicit separate approval.
- required output: Interface candidate scope and required evidence.
- escalation condition: Any write outside sandbox candidate files.

## 5. Non-Promotion Guardrails
readiness audit ≠ promotion

promotion_candidate_later ≠ source-space promotion

source-space interface candidate ≠ source-space modification

sandbox candidate ≠ baseline

signal bundle ≠ rule

validation note ≠ policy

## 6. Relationship To Operating Order Principles
This pipeline is especially connected to:
- Model보다 Harness: the pipeline is part of the operating harness.
- Core보다 Workspace: source-space and sandbox remain separated.
- Error보다 Signal: validation and failure material become sourced signals before guidance.
- Readiness와 Promotion 분리: audit is not promotion.
- User as Judge: only the user can approve high-risk movement.
- Plan before Execution: plan draft and plan review precede risky runs.
- File before Chat: run, validation, output, and review files preserve work.
- Ops Trace before Memory Loss: every stage leaves evidence for later audit.

## 7. Closeout Note
This document is a sandbox promotion pipeline candidate only.
No source-space promotion is performed by this document.
No baseline is created.
No automation, router, controller, ontology, MCP, hook, watch mode, agent implementation, or production workflow is created.

## 8. 4-line Footer
status: 완료
summary: sandbox_promotion_pipeline_v0는 raw material에서 source-space interface candidate까지의 후보 단계와 gate를 정의하되 실제 promotion은 수행하지 않음
risk: pipeline 문서를 promotion 절차 승인서나 source-space rule로 오해하면 candidate/baseline 경계가 무너질 수 있음
next: session_role_map_v0와 함께 validation_round_30에서 candidate-only 경계를 검증
