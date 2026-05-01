# Whole-Space Handoff Checklist v1 Candidate

## Run Identity Note

The first run record for this candidate was misnumbered as `run_134`, which conflicts with an existing invalid/orphaned run identity. See `app/work/space-skill-sandbox/outputs/run_identity_correction_note_whole_space_handoff_checklist_v1_candidate.md`.

## 0. Status

```text
Status: Candidate
Authority: Not baseline / Not official workflow / Not source-space promotion
Scope: Current whole-space handoff design candidate
Purpose: Translate external lens + internal principles + sandbox 15 principles + process-memory rules into a stronger handoff checklist candidate.
```

This document is not law.
This document is not an automation spec.
This document is not a merge plan.
This document lists candidate judgment fields that should not be missed when preparing or reviewing a handoff.

## Usage Mode

Full mode is for cross-agent, cross-session, approval-gated, high-risk, or whole-space handoffs.

Compact mode is for ordinary handoffs:

```text
identity / context / authority_status / source_refs / next / forbidden_actions
```

Do not apply this checklist to trivial single-turn requests.

## Anti-Schema Warning

These fields are judgment prompts, not required schema fields.

Missing fields may be acceptable when the handoff is low-risk and current position is clear.

Do not turn this checklist into a parser, ledger, ontology, controller, router, policy, automation, or enforcement mechanism.

## Gemini Calibration Warning

Gemini should read this as boundary training and return-format guidance.

It is not permission to execute, approve, promote, modify files, open package work, or create automation.

Gemini output remains worker evidence for Codex / ChatGPT / User review.

## 1. Purpose

The v0 checklist protected the basic entry surface, but it was too thin for a whole-space handoff.

This v1 candidate lowers the current connection map into handoff structure:

```text
external lens set
-> internal philosophy / baseline
-> sandbox 15 principles
-> process-memory rules
-> handoff checklist fields
```

The goal is to preserve line / axis / connection work across User, ChatGPT, Codex, and Gemini without turning any connection into baseline law.

## 2. Field Layers

### A. Who / Where Layer

Fields:

```text
identity
context
memory_layer
source_refs
```

Purpose:

This layer prevents a worker from acting without knowing who it is, where the task sits, what memory temperature applies, and which records support the handoff.

### B. Authority / Permission Layer

Fields:

```text
authority_status
permission
allowed_actions
forbidden_actions
```

Purpose:

This layer prevents candidate material, worker confidence, or recent runs from being mistaken for approval, baseline, or execution authority.

### C. Movement / Routing Layer

Fields:

```text
routing
next
```

Purpose:

This layer tells the work where to move next, who should handle it, what capability is required, and when to stop.

### D. Safety / Validation Layer

Fields:

```text
validation
risk
```

Purpose:

This layer preserves evidence boundaries, interpretation limits, invalidation conditions, and drift risks.

## 3. Field Definitions

### 3.1 identity

- field purpose: identify the actor, role, capability, and current authority.
- failure prevented: worker role collapse; Gemini or Codex acting as approver.
- linked external lens: AWS sample-deep-insight as `connection_candidate` for role separation; Google Cloud governance as `connection_candidate` for identity/posture.
- linked internal / sandbox principle: User as Judge; Readiness와 Promotion 분리; role-aware handoff.
- example value: `actor: Gemini; role: bounded observation worker; capability: long-read observation; current_authority: evidence only`.
- must not infer: identity does not grant permission to execute, promote, or modify source-space.

### 3.2 context

- field purpose: state current position, prior accepted anchor, active package/run, and why this handoff exists.
- failure prevented: latest-file bias; sandbox run state mistaken for whole-space state.
- linked external lens: Warp as `connection_candidate` for workspace/file context; mini-swe-agent as `connection_candidate` for compact instruction.
- linked internal / sandbox principle: File before Chat; Agent-readable Context; Current Position Memory.
- example value: `current_position: Package 033 approval gate; prior_accepted_anchor: Package 011 / Run 060; why: recover whole-space entry signal`.
- must not infer: current context is not proof of acceptance or readiness.

### 3.3 memory_layer

- field purpose: assign HOT / WARM / COLD and memory-spine placement.
- failure prevented: all markdown being read with equal authority; old runner receipts becoming current truth.
- linked external lens: mini-swe-agent as `connection_candidate` for trace-before-interpretation; harness evolution as `connection_candidate` for locating rigor.
- linked internal / sandbox principle: Metadata before Full Context; Ops Trace before Memory Loss; Engine Memory Spine; HOT / WARM / COLD.
- example value: `hot: current entry / packet / review; warm: recent closeout and process memory; cold: harvested external lens`.
- must not infer: memory temperature is an access strategy, not deletion or promotion.

### 3.4 source_refs

- field purpose: list source files, runs, packages, external lenses, and internal principles used.
- failure prevented: graphing connections without evidence; confident prose without provenance.
- linked external lens: Graphify as `connection_candidate` for graph temptation; Fowler as `connection_candidate` for verification pressure.
- linked internal / sandbox principle: Graph보다 Provenance; Append-only correction; Space First / LLM Last.
- example value: `source_files: whole_space_external_lens_connection_map_v0.md; operating_order_source_map_v0.md`.
- must not infer: references do not automatically make the conclusion authoritative.

### 3.5 authority_status

- field purpose: classify candidate / accepted / hold / invalid-orphaned / baseline / needs-user-confirmation.
- failure prevented: candidate treated as baseline; preserved failure treated as sequence evidence.
- linked external lens: AWS sample-deep-insight as `connection_candidate` for review gates; Skillify as `connection_candidate` for failure-to-guide caution.
- linked internal / sandbox principle: Readiness와 Promotion 분리; User as Judge; Invalid / orphaned separation.
- example value: `authority_status: candidate; needs_user_confirmation: true`.
- must not infer: accepted evidence is not the same as baseline or permission.

### 3.6 permission

- field purpose: state who may decide, execute, review, and approve.
- failure prevented: implicit approval, worker overreach, approval-gate bypass.
- linked external lens: Agent Harness Engineering as `connection_candidate` for permissioned harness; Google Cloud governance as `connection_candidate` for access posture.
- linked internal / sandbox principle: User as Judge; Core보다 Workspace; Capability-aware routing.
- example value: `decide: User; execute: Gemini if bounded; review: Codex / ChatGPT; approve: User`.
- must not infer: a task packet does not equal user approval.

### 3.7 allowed_actions

- field purpose: define actions explicitly allowed in the handoff.
- failure prevented: broad prompts expanding into implementation or source modification.
- linked external lens: Tools Live Beyond Their Maker as `connection_candidate` for caller affordance; Browser Harness as `connection_candidate` for bounded environment.
- linked internal / sandbox principle: Function보다 Affordance; Core보다 Workspace; Definition before Prompt.
- example value: `allowed: read listed files; return observation block; no file writes`.
- must not infer: if an action is not forbidden but also not allowed, it is not authorized.

### 3.8 forbidden_actions

- field purpose: define actions explicitly blocked.
- failure prevented: automation creation, artifact deep-read, package promotion, external tool adoption.
- linked external lens: Laws of Software Engineering as `connection_candidate` for avoiding overbuild; Skillify as `connection_candidate` for not skillifying every failure.
- linked internal / sandbox principle: Non-goals / anti-overlogging; Program as Material; Readiness와 Promotion 분리.
- example value: `forbidden: Package 032 artifact read; Package 033 promotion; automation/schema/controller creation`.
- must not infer: forbidden actions are not permanent bans; they are current handoff boundaries.

### 3.9 routing

- field purpose: identify next actor, required capability, route reason, and blocker condition.
- failure prevented: Codex becoming default executor; Gemini becoming designer; ChatGPT becoming runner.
- linked external lens: AWS sample-deep-insight as `connection_candidate` for planner/supervisor/tool-agent split; GStack as `connection_candidate` for visible workflow stage.
- linked internal / sandbox principle: Skill보다 Route; Plan before Execution; Role-aware handoff; Capability-aware routing.
- example value: `next_actor: Gemini; required_capability: bounded observation; blocker: cannot read listed scope`.
- must not infer: route selection is not approval or promotion.

### 3.10 next

- field purpose: define next action, halt condition, and user decision need.
- failure prevented: open-ended continuation; orphaned work auto-resume.
- linked external lens: mini-swe-agent as `connection_candidate` for small loop; Agent Harness Engineering as `connection_candidate` for plan/review before execution.
- linked internal / sandbox principle: Orphan / unfinished-work detection; Plan before Execution; Current Position Memory.
- example value: `next_action: return supplemental observation; halt_condition: missing context; user_decision_needed: before artifact read`.
- must not infer: next action is not a sequence of implied future actions.

### 3.11 validation

- field purpose: state evidence required, interpretation limits, approval gate, and invalidation condition.
- failure prevented: confident output treated as truth; evidence-free summary promoted.
- linked external lens: Fowler as `connection_candidate` for verification and intent surfaces; AWS sample-deep-insight as `connection_candidate` for review-return.
- linked internal / sandbox principle: Readiness와 Promotion 분리; User as Judge; Append-only correction.
- example value: `evidence_required: listed source_refs only; interpretation_limit: observation not design authority`.
- must not infer: validation pass does not create baseline.

### 3.12 risk

- field purpose: name over-promotion, category confusion, inward-collapse, memory pollution, and authority drift risks.
- failure prevented: hidden drift becoming workflow, baseline, or automation.
- linked external lens: Laws of Software Engineering as `connection_candidate` for failure as signal; harness evolution as `connection_candidate` for not jumping to harness build.
- linked internal / sandbox principle: Error보다 Signal; Ops Trace before Memory Loss; Open Interpretation Space.
- example value: `risk: surface-collapse; candidate treated as baseline; sandbox rule applied as source-space law`.
- must not infer: naming a risk does not prove the risk occurred.

## 4. External Lens Connections

All links in this section are `connection_candidate`, not proof or baseline.

```text
Agent Harness Engineering
-> Model보다 Harness
-> structure before worker action

Tools Live Beyond Their Maker
-> Function보다 Affordance
-> caller / capability / forbidden use in handoff

mini-swe-agent
-> Metadata before Full Context
-> small stateless execution unit + linear trace

AWS sample-deep-insight
-> User as Judge / Ops Trace before Memory Loss
-> role-aware handoff + user gate + trace preservation

Graphify
-> Graph보다 Provenance
-> provenance before graph/ontology

Laws of Software Engineering
-> Error보다 Signal
-> failure-to-pipeline / no overbuild

Fowler / Skillify / GStack / Google Cloud / harness evolution
-> identity / context / permission / validation / routing / risk / next
```

Do not treat these external materials as internal law. They explain why the checklist fields are useful.

## 5. Internal Principle Connections

| Internal basis | Handoff fields required | Drift prevented | Role boundary protected | Memory layer |
| --- | --- | --- | --- | --- |
| space first / LLM last | source_refs, validation, authority_status | LLM fluency manufacturing meaning | ChatGPT/Codex/Gemini as readers, not meaning source | directionality memory |
| open interpretation space | risk, authority_status, validation | hold/failure/weak discarded or overclosed | User and ChatGPT preserve interpretation | directionality / feedback memory |
| current layer baseline contract | authority_status, risk, next | mixed hold promoted to canonical | User approval and Codex review | current reality / episodic memory |
| engine input lane baseline | source_refs, context, memory_layer | external input treated as core rule | Codex intake classification | directionality / current reality memory |
| three-axis operating loop | routing, next, validation | lock before reread | Codex line-reading / inspection role | feedback / episodic memory |
| engine memory spine | memory_layer, context, source_refs | all memory placed in one note/folder | Codex current-reality recovery | current reality / feedback / resource memory |
| sandbox 15 principles | all fields as audit lens | sandbox law overreach | User approval / Codex review / Gemini boundary | episodic / process memory |
| process-memory operating layer | context, next, authority_status, memory_layer | session loss and orphan continuation | all handoff roles | current reality / process memory |

## 6. Sandbox 15 Principles To Field Map

| Sandbox principle | Checklist fields | Prevents |
| --- | --- | --- |
| Model보다 Harness | identity, context, permission | worker action before structure |
| Function보다 Affordance | allowed_actions, forbidden_actions | tool function mistaken for permission |
| Core보다 Workspace | permission, forbidden_actions | source-space contamination |
| Error보다 Signal | risk, validation | deleting failure or overbuilding from one failure |
| Readiness와 Promotion 분리 | authority_status, validation | candidate mistaken for baseline |
| User as Judge | permission, validation, next | worker approval drift |
| Plan before Execution | routing, next, validation | action before bounded plan |
| Metadata before Full Context | memory_layer, context, source_refs | full-context dumping |
| File before Chat | source_refs, context | chat-only memory loss |
| Ops Trace before Memory Loss | source_refs, validation, risk | unrecoverable run state |
| Skill보다 Route | routing, allowed_actions | isolated skill replacing route judgment |
| Agent-readable Context | context, source_refs, allowed_actions | worker guessing from prose |
| Graph보다 Provenance | source_refs, memory_layer | unsupported graph/ontology |
| Program as Material | allowed_actions, forbidden_actions, risk | external program adoption |
| Definition before Prompt | identity, allowed_actions, forbidden_actions | broad prompt before boundary |

## 7. Process-Memory Rule Map

| Process-memory rule | Checklist fields |
| --- | --- |
| Current Position Memory | context, next |
| HOT / WARM / COLD memory layer | memory_layer |
| Append-only correction | source_refs, validation |
| Invalid / orphaned separation | authority_status, risk |
| Role-aware handoff | identity, permission, routing |
| Capability-aware routing | routing, allowed_actions, forbidden_actions |
| Non-goals / anti-overlogging | forbidden_actions, risk |
| Orphan / unfinished work detection | validation, next |

## 8. Usable Template

```markdown
# Whole-Space Handoff Checklist v1 Candidate

## 1. Identity
- actor:
- role:
- capability:
- current authority:

## 2. Context
- current position:
- prior accepted anchor:
- active package / run:
- why this handoff exists:

## 3. Memory Layer
- hot:
- warm:
- cold:
- local/context-bound:

## 4. Source Refs
- source files:
- related runs:
- related packages:
- external lenses:
- internal principles:

## 5. Authority Status
- candidate:
- accepted:
- hold:
- invalid/orphaned:
- baseline:
- needs_user_confirmation:

## 6. Permission
- who may decide:
- who may execute:
- who may review:
- who must approve:

## 7. Allowed Actions
- allowed:

## 8. Forbidden Actions
- forbidden:

## 9. Routing
- next actor:
- required capability:
- route reason:
- blocker condition:

## 10. Validation
- evidence required:
- interpretation limits:
- approval gate:
- invalidation condition:

## 11. Risk
- over-promotion risk:
- category confusion risk:
- inward-collapse risk:
- memory pollution risk:
- authority drift risk:

## 12. Next
- next action:
- halt condition:
- user decision needed:
```

## 9. Example Application

This example is explanatory only.

The example is historical-pattern illustration only. Do not follow it as a live package instruction.

It does not analyze Package 035 target contents.
It does not open Package 036.
It does not instruct Run 148.
It does not create an official workflow.
Do not analyze package targets from the example.

```text
Scenario:
package_035 target selection failed; package_017 replacement loop became unsafe.

Checklist reading:
identity = Gemini as bounded execution worker
context = package_035 target reset needed
authority_status = acceptance_pending / needs_user_confirmation
forbidden_actions = artifact analysis before approval, package_036 opening, metadata_scan_report candidate
risk = category confusion / approval gate violation / inward collapse
next = target reset preflight, then halt for user approval
```

## 10. Watch Items

- The checklist can become too heavy if applied to trivial single-turn requests.
- The connection map can be overread as ontology.
- External lens names can sound authoritative unless marked `connection_candidate`.
- Memory layer classification can become bookkeeping if it stops serving re-entry.
- Handoff fields must remain judgment aids, not mandatory schema enforcement.

## 11. Candidate Closeout

This v1 checklist candidate strengthens v0 by adding:

```text
identity
context
permission
validation
routing
risk
next
source_refs
allowed_actions
forbidden_actions
authority_status
memory_layer
```

It remains candidate-only.
No baseline, official workflow, source-space promotion, automation, policy, router, controller, graph, ontology, or schema was created.
