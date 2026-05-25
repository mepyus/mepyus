# VectorFL Structuring Workspace — Big Frame Readonly Staging v0

created_at: 2026-05-25T12:41:02.987935+09:00
status: READONLY_STAGING / NOT_AUTHORITY / SAFE_TO_DELETE_VIEW

## 핵심 판단

지금 원본 자산을 `mv`로 재배치하면 혼란이 커진다.
아직 VectorFL 구조가 완성된 것이 아니고, 원본 경로 자체가 current-position, registry, handoff, receipt, trace의 일부로 쓰일 수 있기 때문이다.

따라서 이 폴더는 "정리 적용본"이 아니다.
이 폴더는 원본을 천천히 읽고 연결하기 위한 큰틀 workspace / staging view다.

## 절대 원칙

- 원본 파일 이동 금지
- 원본 파일 수정 금지
- authority / registry / current-position mutation 금지
- promotion 금지
- 이 폴더 안의 파일은 authority가 아님
- 이 폴더는 source of truth가 아님
- 원본은 기존 위치에 그대로 둠
- 이 폴더는 pointer, manifest, review batch, copied-view 후보를 담는 작업대임

## 왜 cp/view는 가능하고 mv는 아직 안 되는가

- mv는 원본 경로를 바꿔서 내부 링크/맥락/권위 경계를 흔든다.
- cp/view는 원본을 그대로 둔 채 사람이 보기 위한 검토면을 만든다.
- 단 cp도 authority처럼 보이면 안 되므로 manifest와 NOT_AUTHORITY 표시가 필요하다.

## 사용 방식

1. 원본 자산은 그대로 둔다.
2. 이 workspace 안에 pointer/view/batch를 만든다.
3. 작은 batch 단위로 실제 검증한다.
4. Codex review는 read-only로만 붙인다.
5. 나중에 VectorFL 구조가 성숙하면, 그때 제한된 move/archive manifest를 별도 승인한다.

## 현재 결론

- 지금은 대규모 mv 금지.
- 새 큰틀 폴더를 만들고, 천천히 연결하는 방식이 맞다.
- 실제 이동보다 pointer-first / view-first / batch-first가 안전하다.

<!-- TOP10_MOVE_RISK_PROOF_V0 -->
## TOP10 move-risk proof v0 — 2026-05-25

Status: HOLD / REVIEW_ONLY / NOT_AUTHORITY.

Actual repo search confirmed the first top-10 cleanup blocker batch is not safe for mv/archive:

- HIGH_TRUE_MOVE_BLOCKER: 6
- MEDIUM_CONTROL_SURFACE_UPDATE_RISK: 4
- LOW_SAFE_TO_MOVE: 0

Rules added from the proof:

1. Original paths remain source-of-truth orientation handles.
2. Workspace copy paths must not replace original paths.
3. Pointer/view/control-surface artifacts are not authority registry.
4. HIGH/MEDIUM reference maps are evidence only, not move/archive approval.
5. mv/archive remains HOLD until a future explicit manifest + rollback + post-apply validation approval exists.

Evidence pointers:

- /Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/top10_move_risk_rollup_v0.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/high_risk_6_compact_operator_view_v0.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/medium_4_reference_map_batch01_v0.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/top10_cleanup_blockers_batch01_link_integrity_precheck_v0.json

