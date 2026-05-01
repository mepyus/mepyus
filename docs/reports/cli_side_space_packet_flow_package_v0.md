# CLI-Side Space Packet Flow Package v0

## 0. Declaration

- read-only
- no implementation
- no source-space modification
- no automation
- no schema lock

## 1. Why This Package Exists

The user intends to use AI, Codex, Gemini, and CLI tools for implementation, work automation, structure design, validation, and external research.

The risk is that CLI tools can execute quickly while missing the user's layer, evidence standard, human-lock boundary, and maturation state.

Therefore the space should act beside the CLI as an operating layer that reads the input, selects the right work packet, constrains the worker, and recovers the residue after the worker returns.

The space is not the execution body replacing CLI. It is a direction surface that provides:

- purpose
- work type
- materials to read
- forbidden actions
- execution scope
- layer judgment
- output format
- verification criteria
- user-confirmation conditions
- residue to recover

## 2. Operating Flow

```text
user input
-> Routing 판독
-> Packet 선택
-> Worker 실행
-> Recovery Card 작성
-> State 분류
-> Transition Card 작성
-> 다음 Packet 후보 제안
```

The flow is provisional. It prepares a bounded worker context and recovery shape; it does not automate routing, execution, promotion, or locking.

## 3. Routing Rules

### 3.1 Research Packet

- trigger phrases: "조사해줘", "비교해줘", "외부 사례 봐줘", "가능성 확인", "레퍼런스 찾아봐"
- routing criteria: external information, comparative landscape, method survey, feasibility reading, or non-implementation research is requested
- allowed actions: gather references, compare methods, identify risks, summarize evidence, propose candidate next packets
- forbidden actions: implementation, architecture lock, schema creation, direct promotion into baseline
- expected output: research summary with evidence anchors, risk notes, and recommended next packet

### 3.2 Implementation Packet

- trigger phrases: "구현해줘", "코드 수정", "버그 고쳐", "기능 추가", "테스트 통과하게"
- routing criteria: user asks for concrete code or file changes in a bounded area
- allowed actions: inspect relevant code, edit scoped files, run focused checks, report changes
- forbidden actions: baseline promotion, broad rewrite, unrequested architecture change, schema/controller creation unless explicitly requested
- expected output: changed files, behavior summary, verification result, recovery card

### 3.3 Validation Packet

- trigger phrases: "검증해줘", "리뷰해줘", "이 결과 맞아?", "다음으로 넘겨도 돼?", "PASS인지 봐줘"
- routing criteria: a worker result, report, implementation, or claim needs checking before reuse
- allowed actions: compare expected vs observed, verify evidence, identify missing tests, classify risk
- forbidden actions: treating summary as truth, auto-locking, ignoring PASS_WITH_NOTE caveats
- expected output: verdict, evidence anchors, risk/warning, next packet candidate

### 3.4 Refactor Packet

- trigger phrases: "정리해줘", "리팩터", "구조만 다듬어", "동작 바꾸지 말고"
- routing criteria: user asks for structure cleanup with no intended behavior change
- allowed actions: rename/localize structure, reduce duplication, improve readability, run behavior checks
- forbidden actions: logic change without explicit escalation, hidden feature change, treating refactor as validation
- expected output: refactor summary with `logic_changed=false` evidence or HOLD if not confirmable

### 3.5 Space Intake Packet

- trigger phrases: "공간에 넣어봐", "이 재료 넣어봐", "우리 공간에서 쓸 수 있어?", "이 결과 회수해줘"
- routing criteria: external material, worker output, idea, or discussion should be read through space lenses
- allowed actions: layer/lens reading, fit/risk comparison, lowering into candidate position, user-facing card
- forbidden actions: immediate implementation, schema lock, registry creation, baseline promotion
- expected output: compact intake judgment, placement candidate, do_not_use_as, reflux residue

### 3.6 Chat Summary Packet

- trigger phrases: "다음 채팅용 정리", "Obsidian에 넣게 정리", "handoff 만들어줘", "요약해줘"
- routing criteria: conversation or worker context needs portable continuation material
- allowed actions: summarize decisions, preserve open questions, list evidence pointers, state next packet candidate
- forbidden actions: turning summary into truth, deleting unresolved caveats, adding unsupported conclusions
- expected output: concise handoff with provenance/caveat notes and next-action boundaries

### 3.7 Hold / Clarify

- trigger phrases: ambiguous or conflicting request, scope too broad, lock/promotion requested without user confirmation, missing material
- routing criteria: action would require human lock, unresolved scope, unsafe transition, or insufficient evidence
- allowed actions: stop, explain blocker, ask targeted question, propose safe packet candidates
- forbidden actions: guessing lock intent, implementing through ambiguity, auto-promoting candidate output
- expected output: HOLD reason, required clarification, safe next choices

## 4. Packet Templates

### Research Packet

- purpose: external investigation, comparison, or material collection
- allowed: read requested sources, compare lenses, extract evidence, identify risks
- forbidden: implementation, direct baseline promotion, schema/controller/automation design as final
- input materials: user question, source list, prior space constraints, evidence requirements
- output format: findings, evidence anchors, risk notes, candidate next packet
- verification criteria: claims have source/evidence pointers; no implementation conclusion is smuggled in
- recovery target: residue_candidate / reuse_hint / risk_memory

### Implementation Packet

- purpose: bounded code or document change requested by user
- allowed: scoped edits, focused tests/checks, change report
- forbidden: broad rewrite, lock/promotion, unrelated architecture, unrequested automation
- input materials: task goal, files/modules, constraints, acceptance checks
- output format: changed files, behavior summary, verification, recovery card
- verification criteria: requested behavior changed; tests or checks run; side effects disclosed
- recovery target: validation_required / reuse_hint / risk_memory

### Validation Packet

- purpose: verify worker output, implementation result, report, or claim
- allowed: compare output against task, inspect evidence, identify gaps, issue verdict
- forbidden: auto-lock, evidence-free acceptance, PASS_WITH_NOTE note dropping
- input materials: original request, worker result, evidence anchors, expected output contract
- output format: verdict, findings, missing evidence, next packet candidate
- verification criteria: each major claim is traceable or marked as claim
- recovery target: risk_memory / reuse_hint / human_review_candidate

### Refactor Packet

- purpose: structure cleanup without logic change
- allowed: local simplification, naming cleanup, duplication reduction, focused equivalence checks
- forbidden: logic change, feature addition, hidden behavior migration
- input materials: target files, no-logic-change requirement, current tests/checks
- output format: refactor summary, `logic_changed=false` evidence, validation result
- verification criteria: equivalence is checked or uncertainty is declared
- recovery target: reuse_hint / human_review_candidate if equivalence is uncertain

### Space Intake Packet

- purpose: read external material, idea, or worker result through the space before adoption
- allowed: layer/lens reading, comparison, lowering, quarantine/future option placement
- forbidden: immediate implementation, schema lock, asset registry creation, baseline promotion
- input materials: material, source surface, relevant space lines/axes, guardrails
- output format: user-facing card, placement candidate, do_not_use_as, reflux target
- verification criteria: lens/layer is named; useful value and risk are both preserved
- recovery target: residue_candidate / risk_memory / reuse_hint / pattern_candidate

### Chat Summary Packet

- purpose: portable summary for next chat, Obsidian, or worker handoff
- allowed: compress context, preserve decisions, list open questions, state next safe packet
- forbidden: summary-as-truth, unsupported claims, caveat removal
- input materials: conversation, decisions, artifacts, unresolved risks
- output format: handoff summary, evidence pointers, next packet recommendation
- verification criteria: no critical caveat is removed; evidence gaps are marked
- recovery target: raw_trace_only / residue_candidate / reuse_hint

### Hold / Clarify Packet

- purpose: stop unsafe or under-specified action
- allowed: explain hold, ask narrow question, identify required human lock
- forbidden: proceeding through ambiguity, auto-promoting, guessing user approval
- input materials: ambiguous request, conflict, lock/promotion signal, missing evidence
- output format: HOLD reason, required user decision, safe next packet options
- verification criteria: blocker is concrete and tied to a guardrail
- recovery target: human_review_candidate / quarantine

## 5. Recovery Card v0

```text
packet_type:
source_task:
verdict:
primary_event:
evidence_anchor:
what_changed:
what_was_learned:
risk_or_warning:
reuse_hint:
pattern_candidate:
human_lock_required:
recommended_next_state:
do_not_promote_as:
next_packet_candidate:
```

## 6. State Classification

- discard: no useful residue remains
- raw_trace_only: keep only as source trace or evidence context
- residue_candidate: may matter later but is not yet reusable
- risk_memory: records a warning, failure trace, or dangerous assumption
- reuse_hint: useful repeated move or reminder
- pattern_candidate: recurring pattern that may deserve human review
- human_review_candidate: AI can raise this for user judgment
- locked_rule: only possible after explicit user lock
- quarantine: preserve separately because reuse is risky or authority is suspect

Notes:

- `locked_rule` is possible only after explicit user lock.
- AI can raise material only up to `human_review_candidate`.
- Status is a maturation signal, not ontology.

## 7. Transition Rules

### Safe transitions

- Research -> Space Intake -> Discussion / Validation
- Space Intake -> Thought Asset / Caution Asset / Future Option
- Implementation -> Validation -> Recovery
- Refactor -> Validation with logic_changed=false
- Validation PASS_WITH_NOTE -> next packet with note included
- Repeated reuse_hint -> pattern_candidate -> human review

### Forbidden transitions

- Research -> Implementation
- Space Intake -> Locked Rule
- AI Candidate -> Locked Rule
- Confidence High -> Auto Lock
- Summary -> Truth
- Refactor -> Logic Change
- PASS_WITH_NOTE -> Ignore Note

## 8. Transition Card v0

```text
current_packet:
verdict:
recovered_state:
risk_level:
human_lock_required:
can_continue:
next_packet:
must_include_note:
forbidden_next_step:
why:
```

## 9. Dry-run Candidate Cases

### Candidate A: Codex result validation and next packet creation

- input: Codex returned a report or package, and the user wants to know whether it can move forward
- expected route: Validation Packet
- dry-run value: checks Recovery Card, State Classification, and Transition Card without implementation
- recommendation: default dry-run case

### Candidate B: External material space intake

- input: one external article, transcript, or tool reference should be read into the space
- expected route: Space Intake Packet
- dry-run value: tests layer/lens reading, do_not_use_as, and lowering into candidate position

### Candidate C: Small implementation request simulation

- input: a small bounded code request is routed as an Implementation Packet
- expected route: Implementation -> Validation -> Recovery
- dry-run value: checks whether implementation remains bounded and recovery captures evidence

For the first dry-run, choose Candidate A.

## 10. Closeout

This package is structure-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, UI, reingestion design, JSON schema, CLI trace contract, aggregation threshold, or agent architecture was created.
All packet, recovery, state, and transition structures remain provisional operating candidates.
