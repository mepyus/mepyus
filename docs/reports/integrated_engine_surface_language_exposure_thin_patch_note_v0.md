# Integrated Engine Surface Language Exposure Thin Patch Note v0

## 1. Verdict

PASS_WITH_NOTE.

This was a thin surface-language exposure patch, not a translation finalization pass. The goal was to reduce front-facing internal-label density so the screen starts with human-readable operating meaning while preserving internal labels as badges/support.

## 2. Why This Patch Followed Support-Layer Pruning

After moving excess panels into support layers, the remaining front shell still exposed too many internal labels as primary reading:

- shared operating spine
- active turn
- authority state
- surface role / next
- assignment / decision candidate
- request / validation / deposit material

Those terms are useful internally, but they should not all be the first thing a user must decode. The body/camera/lens model requires the surface to show what the current object means in that surface before showing internal labels.

## 3. What Changed

### Shell / Navigation

- Main title changed from `Integrated Engine` to `통합엔진`.
- Surface navigation now shows Korean-facing labels first:
  - `사용자면`
  - `VectorFL면`
  - `엔진면`
- The internal `User / VectorFL / Engine surface` labels remain as small secondary badges.

### Orientation Band

The orientation path now uses Korean-readable front labels:

- 사용자 목적
- VectorFL 패킷
- CLI / 엔진 반환
- VectorFL 재독해
- 결정 / 퇴적 후보

The internal route structure is preserved, but the first-pass reading is less like an internal architecture diagram.

### Shared Operating Spine

The spine now starts with Korean-facing labels:

- 공통 작업 방향층
- 현재 turn
- 현재 목적
- 상태 / route
- 권위 상태
- 근거 준비
- 면의 역할 / 다음 후보

The internal route terms are still present where they carry structural meaning, but they no longer dominate every label.

### Surface Current Object Focus

Surface focus now foregrounds:

- 사용자면 현재 읽기
- VectorFL면 현재 읽기
- 엔진면 현재 읽기

The prior English internal focus labels remain as small badges:

- `user local focus`
- `vectorfl local focus`
- `engine local focus`

The main role phrases now read:

- 배정 / 결정 후보
- 재독해 / 중재 재료
- 요청 / 검증 / 퇴적 재료

## 4. What Was Not Changed

- No final Korean glossary was created.
- No UI copy was locked as final.
- No wording patch gate was reopened.
- No scaffold/read-map/backend changes.
- No new panels.
- No new route or authority state.

## 5. Why This Is Safe

This patch changes display wording and exposure order only. It does not change the underlying CLI host state, surface split, marks, routes, packet draft, handoff queues, or engine flow.

It follows the current rule:

- human-readable operating meaning first
- internal label as badge/support
- do not flatten route / authority / state / boundary

## 6. Verification

Passed:

- `npm run build` in `app/ui/integrated_engine`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Watchpoints

1. Do not mistake this for final translation or Koreanization completion.
2. Some internal terms such as `route`, `turn`, `CLI`, and `VectorFL` remain because they still carry structural meaning.
3. If the screen still feels like internal-space language first, the next step should be another exposure-language pass based on actual browser reading, not a broad glossary rewrite.

## 8. Next Smallest Step

Browser-read the shell and first focus layer only:

- Can the user identify which surface they are in without decoding English architecture labels?
- Can the user understand whether the current object is a candidate, return, hold, or decision material?
- Are internal labels present but visually subordinate?

If yes, continue use validation. If no, perform another thin exposure pass, not a new feature pass.
