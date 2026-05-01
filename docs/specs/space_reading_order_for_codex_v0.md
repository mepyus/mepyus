# Space Reading Order For Codex v0

## Purpose

Codex CLI가 repo에 처음 진입했을 때 읽을 최소 순서를 고정한다. 이 문서는 기존 문서를 대체하지 않고, 읽기 순서만 제공한다.

## Execution

Default first-read order:

1. `CURRENT.md`
   - 현재 fragment 중심 baseline과 runtime 방향 확인.
2. `vectorfl_status.md`
   - 현재 통합 엔진 포인터, 주요 자산 지도, 현재 priority 확인.
3. `source_assets/baselines/folder_status.md`
   - 상위 baseline 후보 목록 확인.
4. `source_assets/baselines/repo_shared_reality_pack_v1.md`
   - 사용자/어시스턴트/Codex가 같은 repo 현실을 보는 방식 확인.
5. `docs/guides/vectorfl_space_asset_access_map_v0.md`
   - blind search 전에 볼 자산 지도 확인.
6. `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
   - 작업공간 역할층과 폴더 생성/배치 원칙 확인.
7. 현재 질문과 직접 관련된 `docs/specs`, `docs/contracts`, `docs/guides`, `docs/reports`.
8. 필요한 경우에만 repo-wide `rg`.

Read-later groups:

- `runtime/cli_sessions/`: 이력/실행 결과가 많으므로 특정 session이 필요할 때만 읽는다.
- `runtime/views/`: latest surface이므로 source authority로 오해하지 않는다.
- `docs/reports/`: 결과/판독 자산이므로 baseline보다 낮은 권위로 읽는다.
- `references/`: 비교/과거/외부 reference로 읽고 현재 SSOT로 승격하지 않는다.
- UI/surface files: Phase 1에서는 후순위다.

## Interpretation

읽기 순서가 필요한 이유는 Codex가 실제 파일을 볼 수 있어도 그 자체로 권위 질서를 알 수 없기 때문이다. `rg`로 많이 찾는 것은 retrieval을 늘리지만, 어떤 문서를 먼저 믿고 어떤 문서를 보조 근거로 쓸지 정하지 못하면 merge/diff 단계가 흔들린다.

이 순서는 “상위 현재성 -> 공간 지도 -> 역할 원칙 -> 질문별 세부 자산”으로 내려간다. 이는 새 구조가 아니라 기존 구조를 같은 구조로 읽게 만드는 최소 handoff다.

## Validation

- 첫 진입 읽기 시작점은 명확하다.
- runtime latest와 source/baseline을 섞지 않는다.
- 질문 관련 탐색은 asset map을 거친 뒤 확장한다.
- repo-wide search는 보조 수단이다.

## Stage 1 Closeout

- Verdict: `PASS`
- Files created: `docs/specs/space_reading_order_for_codex_v0.md`
- Key decisions: Codex의 기본 읽기는 `CURRENT.md`와 `vectorfl_status.md`에서 시작한다.
- Risks: 긴 `vectorfl_status.md`는 section별 선별 읽기가 필요하다.
- Entry condition for next stage: 읽은 질서를 question packet의 `search_targets`로 연결한다.
