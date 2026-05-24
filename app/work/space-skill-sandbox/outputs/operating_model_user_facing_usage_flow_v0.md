# Operating Model User-Facing Usage Flow v0

## 1. Current State

```text
Operating Model Candidate = ACCEPT_WITH_WATCH_ITEMS
Wording Drift Audit = COMPLETE
Patch = NO_PATCH_NEEDED
Risk State = WATCH_ONLY
Latest Current Position = current_position_entry_after_wording_drift_audit_v0.md
```

This note is a usability translation only.

It is not baseline, official workflow, architecture finalization, automation, router, controller, CLI/tool adoption, Package 034/035/036 movement, or Run 117 approval.

## 2. User-Facing Purpose

이 구조는 문서를 더 만들기 위한 구조가 아니다.

사용자가 다음 목적을 말하면,
공간이 현재 위치와 위험을 읽고,
Codex / Gemini / CLI 같은 worker가 필요한 역할만 수행하고,
그 결과가 다시 current-position / process-memory / reusable setting으로 돌아오게 하는 구조다.

짧게 말하면:

```text
사용자가 목적을 정한다.
공간이 현재 위치와 위험을 알려준다.
worker는 정해진 역할 안에서만 움직인다.
결과는 다시 다음 재진입 기억으로 돌아온다.
```

## 3. Four-Line User-Facing Card

### 지금 어디까지 왔나?

- means: 현재 accepted / closed / watch / hold 상태를 확인한다.
- read: latest current-position entry, then active-anchor orientation if needed.
- must not become: official status dashboard or task queue.

### 무엇을 움직일 수 있나?

- means: 지금 사용자 승인을 받아 움직일 수 있는 후보 방향을 고른다.
- read: current-position entry, next-direction options, relevant scope definition.
- must not become: automatic package movement or worker self-routing.

### 무엇을 조심해야 하나?

- means: over-promotion, role drift, tool adoption, package movement, wording drift 같은 위험을 먼저 확인한다.
- read: watch items, wording drift audit, operating model boundaries.
- must not become: policy, compliance framework, or blocking ceremony.

### 다음 판단은 무엇인가?

- means: User / ChatGPT / Codex / Gemini 중 누가 무엇을 판단해야 하는지 정한다.
- read: role model in operating model candidate and current-position entry.
- must not become: approval bypass, workflow, or autonomous execution.

## 4. Example Usage Flow

### Example 1 - "이 자료 공간에 넣어봐."

User input:

```text
이 자료 공간에 넣어봐.
```

Space reading:

- Check latest current-position entry.
- Check whether this is external material, candidate note, source reference, or thought asset.
- Check whether it needs lens/source-map treatment before any promotion.

Worker role decision:

- Codex structures a bounded intake packet or metadata-only placement question.
- Gemini may read/observe only if separately routed.
- ChatGPT validates whether the interpretation over-promotes the material.

Expected user-facing output:

```text
이 자료는 아직 source-space law가 아니라 candidate reference로 읽는 게 안전합니다.
먼저 어떤 렌즈로 읽을지와 어디까지 읽을지 정해야 합니다.
```

Recovery path back into the space:

- Record source refs, authority status, watch items, and next safe action.
- If useful, return to current-position / process-memory / reusable setting.

### Example 2 - "다음 패키지 뭐 움직일까?"

User input:

```text
다음 패키지 뭐 움직일까?
```

Space reading:

- Read latest current-position entry.
- Check Package 033 status and Package 034/035/036 non-inference boundary.
- Check next-direction options if available.

Worker role decision:

- Codex prepares package-selection preflight only.
- Gemini does not open package artifacts unless user-approved.
- ChatGPT checks whether the proposed move respects role and authority boundaries.

Expected user-facing output:

```text
아직 Package 034/035/036 이동은 자동 승인되지 않았습니다.
먼저 후보 방향을 metadata-only로 비교하고, 사용자 승인 후 하나만 움직이는 게 안전합니다.
```

Recovery path back into the space:

- Record target-selection preflight.
- Preserve what was not selected and why.
- Update current-position only after a user-approved move.

### Example 3 - "이걸 Codex/Gemini에게 맡겨도 될까?"

User input:

```text
이걸 Codex/Gemini에게 맡겨도 될까?
```

Space reading:

- Check role model.
- Check whether the task is design/structure, execution/observation, validation, or approval.
- Check Light / Full mode and relevant watch items.

Worker role decision:

- Codex handles structure, scope, packet, and review framing.
- Gemini handles bounded execution/observation only.
- ChatGPT validates boundary and direction.
- User keeps final approval.

Expected user-facing output:

```text
Codex에는 범위와 지시서 구조를 맡기고,
Gemini에는 승인된 읽기/관찰만 맡기는 게 맞습니다.
승인이나 설계 결론은 worker가 직접 내리면 안 됩니다.
```

Recovery path back into the space:

- Save packet/review result as candidate memory.
- Record source refs, authority status, what must not be inferred, and next safe action.

## 5. Boundaries

- no baseline promotion
- no official workflow creation
- no architecture finalization
- no automation / router / controller
- no CLI / tool adoption
- no Package 034 / 035 / 036 movement
- no Run 117 approval
- no Gemini broad run
- no Codex implementation authority
- no rewrite of the operating model

## 6. Final Recommendation

Use this as a user-facing usage aid only.

Do not treat it as a workflow, protocol, or system design.

`STATUS: USER_FACING_USAGE_FLOW_PREPARED`

