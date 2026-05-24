# Run 196 - User-Facing Usage Flow Dry Run

Status: USER_FACING_USAGE_FLOW_DRY_RUN_COMPLETE
Authority: dry-run review / not baseline / not official workflow

## 1. Sources

Usage flow:

`app/work/space-skill-sandbox/outputs/operating_model_user_facing_usage_flow_v0.md`

Current position:

`app/work/space-skill-sandbox/outputs/current_position_entry_after_wording_drift_audit_v0.md`

## 2. Goal

Test whether the four-line user-facing card is usable for three representative user inputs.

This is a dry-run only.

No usage flow, operating model, current-position entry, package, or source file was modified.

## 3. Test Case 1 - "이 자료 공간에 넣어봐."

### Four-Line Card

```text
지금 어디까지 왔나?
현재 공간은 candidate/reference와 source-space law를 분리해서 읽는 상태다.

무엇을 움직일 수 있나?
자료를 바로 편입하지 말고, 먼저 어떤 렌즈로 읽을지와 어디까지 읽을지 정할 수 있다.

무엇을 조심해야 하나?
외부자료나 새 자료를 곧바로 baseline, policy, source-space law로 읽으면 안 된다.

다음 판단은 무엇인가?
User가 intake 목적을 정하고, Codex가 bounded intake 범위를 잡은 뒤 필요하면 Gemini 읽기를 별도 승인한다.
```

Judgment: `USABLE_WITH_WATCH`

Reason:

- Understandable to the User.
- Preserves candidate-only boundaries.
- Makes the next decision visible.
- Watch: `lens`, `bounded intake` may still need simpler phrasing for non-technical use.

## 4. Test Case 2 - "다음 패키지 뭐 움직일까?"

### Four-Line Card

```text
지금 어디까지 왔나?
Package 033은 candidate evidence로 닫혔고, Package 034/035/036 이동은 자동 승인되지 않았다.

무엇을 움직일 수 있나?
다음 패키지를 바로 열지 말고, 후보 방향을 metadata-only로 비교하는 preflight는 할 수 있다.

무엇을 조심해야 하나?
Package 034/035/036 이동, Run 117 승인, Gemini artifact read를 자동 추론하면 안 된다.

다음 판단은 무엇인가?
User가 후보 패키지/방향 선택을 승인하면 Codex가 preflight를 만들고, Gemini 실행은 별도 승인 후에만 가능하다.
```

Judgment: `USABLE`

Reason:

- Clear and practical.
- Avoids package movement.
- Preserves User approval and role boundaries.
- Does not read as workflow or task queue.

## 5. Test Case 3 - "이걸 Codex/Gemini에게 맡겨도 될까?"

### Four-Line Card

```text
지금 어디까지 왔나?
현재 역할 기준은 User=결정, ChatGPT=검증, Codex=구조화, Gemini=관찰/실행이다.

무엇을 움직일 수 있나?
Codex에는 범위/지시서/검토 구조를 맡기고, Gemini에는 승인된 읽기나 관찰만 맡길 수 있다.

무엇을 조심해야 하나?
Codex가 구현자로 넘어가거나 Gemini가 설계자/승인자처럼 말하면 안 된다.

다음 판단은 무엇인가?
User가 맡길 목적과 승인 범위를 정하면 Codex가 packet을 만들고, Gemini는 그 packet 안에서만 움직인다.
```

Judgment: `USABLE`

Reason:

- Directly answers delegation.
- Role split is visible.
- Preserves User decision gate.
- Does not imply autonomous worker authority.

## 6. Drift Risks Found

- Some terms in Test Case 1, such as `lens` and `bounded intake`, may still be internal jargon.
- `metadata-only preflight` is safe but may need a plain-language explanation when used outside this workspace.
- Repeating the four-line card too mechanically could become workflow-like if treated as mandatory ceremony.

## 7. Boundary Confirmation

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
- no rewrite of the usage flow

## 8. Recommendation

`KEEP_AS_USAGE_AID`

Reason:

The four-line card is usable for the tested cases. It makes current position, movable action, risk, and next judgment visible without promoting the usage flow into workflow or protocol.

Keep jargon watch for `lens`, `bounded intake`, and `metadata-only preflight`.

`STATUS: USER_FACING_USAGE_FLOW_DRY_RUN_COMPLETE`

