# operating ui component tree and props spec

## 1. top-level verdict

- 현재 1차 베이스에 필요한 최소 컴포넌트 구조는 아래 8개다.
  - `OperatingBoardPage`
  - `OperatingBoardShell`
  - `DerivedStateStrip`
  - `AssetStateBoard`
  - `AssetStateCard`
  - `SelectedAssetDetailModal`
  - `ActivityPanel`
  - `FeedbackComposer`
  - `OperatingUiPayloadAdapter`

- 이 구조는 **process-console payload를 SSOT로 유지한 채**, donor는 shell/modal/feedback interaction reference로만 쓰는 `hybrid OK` 경로를 전제로 한다.

## 2. component tree

```text
OperatingBoardPage
  -> OperatingUiPayloadAdapter
  -> OperatingBoardShell
     -> DerivedStateStrip
     -> AssetStateBoard
        -> AssetStateCard[]
     -> SelectedAssetDetailModal
        -> ActivityPanel
        -> FeedbackComposer
```

### tree reading

- `OperatingBoardPage`
  - container entry
  - process-console payload 수신
  - adapter 호출

- `OperatingBoardShell`
  - 전체 배치
  - top strip + board area + modal host

- `DerivedStateStrip`
  - selected asset의 `latest / diff / attention / memory` 요약

- `AssetStateBoard`
  - 선택 가능한 카드 리스트/보드

- `AssetStateCard`
  - 개별 asset card

- `SelectedAssetDetailModal`
  - 선택 자산 상세
  - 내부에 `ActivityPanel`, `FeedbackComposer` 포함

## 3. component specs

### `OperatingBoardPage`

- role
  - process-console payload를 읽고 UI render에 필요한 adapted model로 변환하는 최상위 container
  - page-local selection state와 modal open state를 소유

- props
  - `payload: ProcessConsolePayload`
  - `initialAssetId?: string | null`
  - `initialModalOpen?: boolean`
  - `debug?: boolean`

- emits
  - `onAssetSelect?(assetId: string): void`
  - `onModalToggle?(open: boolean): void`
  - `onFeedbackSubmit?(draft: FeedbackDraft): void`

- local state
  - 필요
  - `selectedAssetId`
  - `isDetailModalOpen`
  - `feedbackDraft`

- donor reference
  - none directly
  - current engine container 구조 기준

- build mode
  - fresh build

### `OperatingBoardShell`

- role
  - page-level visual shell
  - toolbar, board area, optional side summary, modal host 배치

- props
  - `title: string`
  - `subtitle?: string | null`
  - `toolbar?: ReactNode`
  - `derivedStrip: ReactNode`
  - `board: ReactNode`
  - `detailModal: ReactNode | null`
  - `emptyState?: ReactNode | null`

- emits
  - none

- local state
  - 불필요

- donor reference
  - [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
  - [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)

- build mode
  - hybrid composition

### `DerivedStateStrip`

- role
  - 현재 선택 자산의 derived operating state를 한 줄 또는 얇은 패널로 요약
  - `latest / diff / attention / memory`를 가장 먼저 읽게 하는 상단 요약층

- props
  - `selectedAsset: AdaptedSelectedAsset | null`
  - `latestPreview: AdaptedLatestPreview | null`
  - `diffSummary: AdaptedDiffSummary | null`
  - `attentionSummary: AdaptedAttentionSummary | null`
  - `memorySummary: AdaptedMemorySummary | null`
  - `compareHref?: string | null`

- emits
  - `onOpenDiff?(): void`
  - `onOpenAttention?(): void`
  - `onOpenMemory?(): void`

- local state
  - 불필요

- donor reference
  - layout tone only from [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)

- build mode
  - fresh build

### `AssetStateBoard`

- role
  - 선택 가능한 asset card들을 보드/컬럼/그리드 형태로 배열
  - initial v1에서는 single board grid로 제한

- props
  - `items: AdaptedAssetCardModel[]`
  - `selectedAssetId?: string | null`
  - `emptyLabel?: string`
  - `sortLabel?: string | null`
  - `filterSummary?: string | null`

- emits
  - `onSelectAsset(assetId: string): void`

- local state
  - 불필요

- donor reference
  - [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)

- build mode
  - donor inspired

### `AssetStateCard`

- role
  - 개별 asset의 canonical and derived summary 표시
  - 클릭 시 상세 모달 또는 selection state 열기

- props
  - `item: AdaptedAssetCardModel`
  - `selected?: boolean`
  - `showCompareReason?: boolean`
  - `showAttentionHint?: boolean`

- emits
  - `onClick(assetId: string): void`
  - `onOpenDetail?(assetId: string): void`

- local state
  - 불필요

- donor reference
  - [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)

- build mode
  - donor inspired

### `SelectedAssetDetailModal`

- role
  - 현재 선택 자산의 상세 운용 상태를 modal로 표시
  - created / updated / scope / dependencies / compare / blockers / history summary / activity / feedback shell 포함

- props
  - `open: boolean`
  - `selectedAsset: AdaptedSelectedAsset | null`
  - `activity: AdaptedActivityPanelModel | null`
  - `feedback: AdaptedFeedbackComposerModel | null`
  - `compareCandidates?: AdaptedCompareCandidate[]`
  - `debugExperimentalVisible?: boolean`

- emits
  - `onClose(): void`
  - `onFeedbackChange?(draft: FeedbackDraft): void`
  - `onFeedbackSubmit?(draft: FeedbackDraft): void`
  - `onOpenCompare?(assetId: string): void`
  - `onOpenHistory?(): void`

- local state
  - 없음 권장
  - feedback draft는 상위에서 제어

- donor reference
  - [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)
  - [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx)

- build mode
  - hybrid composition

### `ActivityPanel`

- role
  - recent history / diff summary / attention event / evidence hint를 한 패널에 표시
  - v1에서는 write action 없이 read-first

- props
  - `items: AdaptedActivityItem[]`
  - `historySummary?: AdaptedHistorySummary | null`
  - `latestLineage?: AdaptedLineageSummary | null`
  - `emptyLabel?: string`

- emits
  - `onOpenHistoryItem?(compareIndex: number): void`
  - `onOpenDiff?(compareIndex: number): void`

- local state
  - optional
  - `expandedItemId?: string | null`

- donor reference
  - activity tone from [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
  - list/modality tone from [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)

- build mode
  - hybrid composition

### `FeedbackComposer`

- role
  - operator feedback 입력 shell
  - v1에서는 persistence를 강제하지 않고 UI shell + callback만 제공

- props
  - `draft: FeedbackDraft`
  - `disabled?: boolean`
  - `placeholder?: string`
  - `submitLabel?: string`
  - `scopeLabel?: string | null`

- emits
  - `onChange(draft: FeedbackDraft): void`
  - `onSubmit(draft: FeedbackDraft): void`
  - `onCancel?(): void`

- local state
  - 없음 권장
  - controlled component로 유지

- donor reference
  - [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)

- build mode
  - donor inspired

### `OperatingUiPayloadAdapter`

- role
  - process-console payload를 UI 친화 view model로 변환
  - raw payload null/fallback를 흡수
  - React component는 raw payload shape를 직접 알지 않게 막음

- props
  - 없음
  - pure function or stateless service로 두는 것이 맞다

- emits
  - 없음

- local state
  - 불필요

- donor reference
  - none

- build mode
  - fresh build

## 4. payload adapter spec

### raw source

- SSOT source:
  - [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)

- top-level payload keys:
  - `summary`
  - `header`
  - `asset_rail`
  - `state_panel`
  - `compare_entry`
  - `latest_state_preview`
  - `attention_queue`
  - `history_summary`
  - `history_drilldown`
  - `state_change_diff`
  - `guards`
  - `debug`

### adapted ui shape

```ts
type OperatingUiPageModel = {
  pageTitle: string
  selectedAssetId: string | null
  selectedAsset: AdaptedSelectedAsset | null
  boardItems: AdaptedAssetCardModel[]
  derivedStrip: AdaptedDerivedStripModel | null
  detailModal: AdaptedDetailModalModel | null
  compareCandidates: AdaptedCompareCandidate[]
  guards: AdaptedGuardModel
}
```

### field mapping

#### `AssetStateBoard` item mapping

- raw:
  - `asset_rail[].asset_id`
  - `asset_rail[].asset_name`
  - `asset_rail[].packet_texture_label`
  - `asset_rail[].maturation_state_label`
  - `asset_rail[].traceability_status_label`
  - `asset_rail[].emergence_status_label`
  - `asset_rail[].updated_at`

- adapted:
  - `id`
  - `title`
  - `statusLinePrimary`
  - `statusLineSecondary`
  - `updatedAt`
  - `selected`

#### `DerivedStateStrip` mapping

- raw:
  - `header.badges`
  - `latest_state_preview`
  - `state_panel.diff_summary`
  - `attention_queue.selected_asset_attention`
  - `attention_queue.selected_asset_memory`

- adapted:
  - `badgeItems`
  - `latestSummary`
  - `diffSummary`
  - `attentionSummary`
  - `memorySummary`

#### `SelectedAssetDetailModal` mapping

- raw:
  - `header.asset_name`
  - `header.source_type`
  - `header.updated_at`
  - `state_panel.canonical_fields`
  - `state_panel.state_notes`
  - `state_panel.evidence_refs`
  - `state_panel.compare_reasons`
  - `state_panel.gate_blockers`
  - `compare_entry.related_assets`
  - `history_drilldown.latest_lineage_link`
  - `history_summary`

- adapted:
  - `identity`
  - `canonicalStateRows`
  - `notes`
  - `evidenceRefs`
  - `compareReasonChips`
  - `blockerChips`
  - `scopeLabel`
  - `dependencyList`
  - `createdAt`
  - `updatedAt`

#### `ActivityPanel` mapping

- raw:
  - `history_drilldown.items`
  - `history_drilldown.latest_lineage_link`
  - `history_summary`
  - `state_change_diff`

- adapted:
  - `activityItems`
  - `lineageSummary`
  - `recentUpdateSummary`
  - `diffEntryHint`

#### `FeedbackComposer` mapping

- raw:
  - 없음
  - current payload에 feedback persistence source는 없음

- adapted:
  - `draft`
  - `scopeLabel`
  - `disabled`
  - `submitLabel`

### nullable / optional fields

- `selectedAsset`
  - nullable
  - `state_unavailable`면 `null`

- `detailModal`
  - nullable
  - no selected asset면 닫힘

- `attentionSummary`
  - selected attention 없으면 `null`

- `memorySummary`
  - memory 없음이면 `insufficient_attention_history`

- `compareCandidates`
  - 빈 배열 허용

- `activityItems`
  - empty list 허용

### fallback rendering rules

- `header.state = state_unavailable`
  - board는 유지
  - detail modal은 비활성
  - strip은 neutral fallback badge 표시

- `state_panel.diff_summary.state = no_previous_state`
  - `compare to previous unavailable` 표시
  - diff CTA 비활성

- `attention_queue.selected_asset_attention = null`
  - `no_active_attention` 얇은 표시

- `attention_queue.selected_asset_memory = null`
  - `insufficient_attention_history` 표시

- `evidence_refs = []`
  - evidence section은 empty state로 표시하되 패널은 유지

- `compare_entry.related_assets = []`
  - compare section 숨김 또는 neutral chip

## 5. v1 scope

- board main surface
- selected detail modal
- latest/diff/attention/memory strip
- recent history activity panel
- feedback input shell
- process-console payload adapter
- current viewer route 위에서 동작 가능한 read-first UI

## 6. out of scope

- drag and drop
- multi-board sync
- editing workflow 확장
- realtime mutation
- deep routing
- wash tank service 재사용
- canonical state write
- operator memo persistence
- graph/terrain integration
- experimental namespace 기본 노출

## 7. recommended first implementation slice

- 실제 구현을 시작한다면 가장 먼저 칠 1개는 `OperatingUiPayloadAdapter`다.

### 이유

- 지금 경로의 SSOT는 UI donor가 아니라 process-console payload다.
- adapter가 먼저 잠겨야:
  - UI가 raw payload shape에 직접 결합되지 않고
  - donor reference와 fresh-build 경계가 유지되고
  - 이후 `AssetStateCard`와 `SelectedAssetDetailModal`을 안정적으로 병렬 구현할 수 있다.
