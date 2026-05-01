# Space Asset Map v0

## Purpose

Codex CLI가 Phase 1 질문 처리에 필요한 자산군을 빠르게 찾도록 하는 최소 지도다. 전체 inventory가 아니며 기존 `vectorfl_space_asset_access_map_v0.md`를 대체하지 않는다.

## Execution

## Authority And Baseline

- `CURRENT.md`: 현재 fragment/runtime baseline.
- `vectorfl_status.md`: 현재 repo-scale 상태 포인터.
- `source_assets/baselines/`: baseline, lock, 운영 철학.
- `docs/policies/`: 정책과 작업공간 운영 기준.
- `docs/baselines/`: docs 내부 baseline 계열.

## Contracts And Specs

- `docs/specs/`: working spec, process contract, schema explanation.
- `docs/contracts/`: 명시 계약과 field-level contract.
- `runtime/contracts/`: JSON skeleton, template, concrete contract instance.

## Guides And Indexes

- `docs/guides/`: 사용법, access map, 탐색 경로.
- `docs/indexes/`: Phase 1처럼 asset grouping이 필요한 얇은 색인.
- `docs/notes/`: 판독 메모, 구조 읽기, 구현 노트.

## Runtime Artifacts

- `runtime/query_packets/`: question interpretation packet instances.
- `runtime/exploration_results/`: evidence bundle/result instances.
- `runtime/merge_diff_reports/`: merge/diff/hold report instances.
- `runtime/reingress_records/`: final return/reingress traces.
- `runtime/views/`: latest/read surface. 원장 아님.
- `runtime/events/`, `runtime/receipts/`, `runtime/manifests/`: 실행/기록/registry 계열.

## Inputs And Source Assets

- `inputs/`: raw input and external cases.
- `source_assets/`: declaration, baseline, directive, handoff, session note source assets.
- root markdown assets: legacy canonical root assets일 수 있으므로 임의 이동 금지.

## Scripts

- `scripts/`: 기존 실행/검증/관측 스크립트.
- `scripts/cli/`: Phase 1 CLI translation/handoff skeleton.

## Lower Priority For This Phase

- UI surface implementation files.
- large historical `runtime/cli_sessions/` unless a specific session is referenced.
- reference repos unless comparison is requested.
- generated html/view artifacts unless user asks about display output.

## Interpretation

질문 유형별 탐색 경로가 필요한 이유는 같은 repo 안에서도 질문이 요구하는 근거층이 다르기 때문이다. 정책 질문은 baseline/policy에서 시작해야 하고, 실행 흔적 질문은 runtime/event/receipt에서 시작해야 하며, 현재 작업공간 방향 질문은 `vectorfl_status.md`와 current working docs를 우선해야 한다.

## Validation

- SSOT/baseline, working spec, runtime artifact, generated view를 분리했다.
- 새 자산군은 기존 역할층 위에 얇게 추가했다.
- 이동/삭제 없이 지도만 추가했다.

## Stage 1 Closeout

- Verdict: `PASS`
- Files created: `docs/indexes/space_asset_map_v0.md`
- Key decisions: Phase 1 runtime packet 계열은 `runtime/*`에 별도 보관한다.
- Risks: existing map과 중복될 수 있으나 이 문서는 Phase 1 질문 루프 전용 shortcut이다.
- Entry condition for next stage: packet의 `search_targets`가 이 지도 항목을 참조할 수 있다.
