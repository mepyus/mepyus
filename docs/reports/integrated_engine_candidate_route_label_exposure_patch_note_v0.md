# Integrated Engine Candidate Route Label Exposure Patch Note v0

## 1. Verdict

PASS.

This round adjusted candidate-list wording so route / mark labels remain visible as internal badges while the front action reads as a human operating instruction.

## 2. Why This Was Needed

The shell and surface focus layers had already moved toward human-readable wording. But candidate lists still exposed internal route labels and tool movement as the main action:

- `Send to VectorFL`
- `candidate only`
- `user assignment candidate`
- `engine_request_candidate`

Those labels are structurally useful, but they should not be the first-pass action wording for the user.

## 3. What Changed

### User Candidate List

User assignment candidates now foreground:

- `사용자면 업무 후보`
- `다시 중재 요청`

The internal stage remains as a small badge instead of the main title.

### Engine Candidate List

Engine request candidates now foreground:

- `요청 후보를 다시 중재`
- `후보 상태`

The internal route label remains as a small badge.

### Validation / Extraction Lists

Engine-side validation and extraction buttons now read:

- `다시 중재 요청`

instead of the tool-level action wording.

### Count / Authority Wording

Some English state phrases were lowered or replaced:

- `candidate · 실행 큐 아님` -> `개 후보 · 실행 큐 아님`
- `candidate는 실행 완료가 아니다` -> `후보는 실행 완료가 아니다`
- `not ingested / not canonical` -> `아직 반영/확정 아님`
- `deposit 후보` -> `퇴적 후보`

## 4. What Was Preserved

- Internal route labels remain present.
- Marks are not renamed in data.
- No state semantics changed.
- No routing behavior changed.
- No new panel or component was added.

## 5. Why This Is Safe

The patch changes visible wording and hierarchy only. It keeps route labels as evidence badges while making the first action read as operational mediation rather than raw tool dispatch.

This follows the current rule:

- human-facing action first
- internal mark as badge
- route / authority / state boundaries preserved

## 6. Verification

Passed:

- `npm run build` in `app/ui/integrated_engine`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Watchpoints

1. `다시 중재 요청` should not imply automatic approval or execution.
2. Internal route labels should remain visible enough for debugging and structure reading.
3. If users cannot tell where the item will go after clicking, the next pass should add a compact destination hint, not restore raw tool wording.

## 8. Next Smallest Step

Continue checking front-facing action labels in VectorFL handoff / reread areas. Those should also read as mediation or reread operations first, with CLI/tool labels as support.
