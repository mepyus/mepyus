# Integrated Engine Koreanization Loop Round 1 Closeout Note v0

## Verdict

PASS_WITH_NOTE

## Goal

Reset the internal language loop so it collects data for Koreanizing integrated-engine spatial/internal language, then run the loop through the integrated engine path instead of running it as a direct terminal-only script.

## What Changed

- The loop prompt now asks for Koreanization data, not only line / connection / axis cleanup.
- The loop is assigned to `user_surface`, matching the User surface internal team / language 담당 role.
- The User surface panel now reads `Internal Team / Koreanization Data Loop`.
- The API state now records the loop position as `user_surface_internal_team_language_owner`.
- The harvest script now extracts:
  - Koreanization candidates
  - Korean preservation requirements
  - risky Korean flattening to avoid
  - why the expression helps user operation

## What Ran

### Main 10-loop

- route: integrated-engine action endpoint
- loop id: `language_loop_20260416T114515Z`
- status: `completed`
- completed: `10 / 10`
- harvest path: `runtime/language_loops/language_loop_20260416T114515Z/harvest.md`
- extracted rows: `14`

This was started through the integrated-engine action path, not by directly invoking the loop script as the user-facing operation.

### Background smoke check

- route: integrated-engine action endpoint with `background: true`
- loop id: `language_loop_20260416T115540Z`
- status: `completed`
- completed: `1 / 1`

This verifies that future User surface loop runs can be started and then tracked by refresh instead of blocking the whole operating flow until completion.

## First Koreanization Harvest Findings

The strongest candidates from the 10-loop were:

- `상태 -> 3면별 읽기 -> 열린/닫힌 route -> 마찰 -> 다음 작은 실행`
- `보류 / 관찰 유지 / 이어 가져감 / 충돌로 거절`
- `최신 반환 / 최근 반환 / 최근 판단 보조 기록`
- `각 면의 정체성은 계속 보여야 함`
- `화면 번역 전 보고 문법 / UI copy 전 운영 보고 문법`
- `평탄화 전 연결 / 단순화 전 브리지`

These are not final UI phrases. They are Koreanization data candidates.

## Risky Flattening Already Found

- `대기`, `유지`, `거절`만으로 줄이면 hold / watch keep / carry-forward / reject-conflict 차이가 사라진다.
- `전체 기록`, `메모리`, `완전한 히스토리`로 줄이면 latest/recent return의 제한된 역할이 사라진다.
- `통합 화면`, `하나의 작업판`으로 줄이면 3면 역할 분리가 흐려진다.
- `한국어로 바꾸기`, `번역 작업`, `UI 문구 작성`으로 줄이면 Koreanization loop가 final UI copy 작업처럼 오해된다.
- `쉽게 바꾸기`, `사용자 친화 표현`으로 줄이면 bridge-before-flatten 원칙이 사라진다.

## Why This Is Still Not UI Copy

This round collected Koreanization evidence. It did not choose final labels, patch visible copy, or create a glossary.

The next layer should use these candidates to help the user read operational meaning, but only after preserving route / authority / state / boundary.

## Remaining Watchpoints

1. Some candidates still mix English terms like `route`, `UI copy`, and `surface`; this may be correct for now, but needs later validation.
2. `reflux`, `anchor drift`, `support reread recovery`, and `workspace ownership` still need stronger Koreanization evidence.
3. Background loop start is now available, but the UI still needs user refresh to track progress.

## Next Smallest Step

Use the harvested Koreanization data to make the User surface language 담당 output easier to read, without turning it into final UI copy or replacing internal terms globally.

