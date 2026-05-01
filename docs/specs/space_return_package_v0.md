# Space Return Package v0

## Purpose

사용자에게 돌려주는 최종 응답의 최소 구조를 정한다.

## Execution

Return package minimum sections:

- `final_answer_summary`
- `what_was_read`
- `space_position`
- `codex_position`
- `chosen_mode`
- `what_changed_or_was_created`
- `validation_result`
- `unresolved_notes`
- `next_recommended_move`

The user-facing answer can be shorter than the full package, but the package fields must be recoverable in the reingress record.

## Interpretation

최종 답만 저장하면 다음 질문에서 왜 그런 결론이 나왔는지 복구할 수 없다. Phase 1의 목적은 답변 생산이 아니라 공간이 다시 읽을 수 있는 운영 흔적을 남기는 것이다.

## Validation

- answer includes result and basis.
- created artifacts are listed.
- unresolved notes are not hidden.
