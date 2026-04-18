# operating ui payload adapter spec v1

## 1. builder payload source reading

- SSOT payload source는 [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py) 다.
- adapter는 Python builder가 주는 payload를 **UI-specific view model**로 바꾸는 얇은 read model 계층이다.
- 이 adapter는 service layer replacement가 아니라, `Container / View / Styles / Service` 분리 원칙에서 **View adapter** 역할만 맡는다.

## 2. UI adapter target shape

```ts
type OperatingUiPageModel = {
  pageTitle: string
  selectedAssetId: string | null
  boardItems: AdaptedAssetCardModel[]
  selectedAsset: AdaptedSelectedAsset | null
  derivedStrip: AdaptedDerivedStripModel | null
  detailModal: AdaptedDetailModalModel | null
  compareCandidates: AdaptedCompareCandidate[]
  guards: AdaptedGuardModel
}
```

### adapted sub-models

```ts
type AdaptedAssetCardModel = {
  id: string
  title: string
  sourceType?: string | null
  packetTextureLabel: string
  maturationLabel: string
  traceabilityLabel: string
  emergenceLabel: string
  updatedAt?: string | null
}

type AdaptedDerivedStripModel = {
  badgeItems: Array<{ key: string; label: string }>
  latestPreview: { packetTexture: string; maturation: string; traceability: string; updatedAt?: string | null } | null
  diffSummary: { state: string; diffClass?: string | null; changedFieldCount?: number; provenanceOnly?: boolean } | null
  attentionSummary: { state: string; priority?: string | null; reason?: string | null; queueStatus?: string | null } | null
  memorySummary: { summary: string; totalEvents?: number; provenanceDensity?: number | null; dominantShiftTypes?: string[] } | null
}

type AdaptedDetailModalModel = {
  title: string
  subtitle?: string | null
  createdAt?: string | null
  updatedAt?: string | null
  canonicalStateRows: Array<{ key: string; label: string }>
  stateNotes?: string | null
  scopeLabel?: string | null
  dependencyList: string[]
  evidenceRefs: Array<{ kind?: string | null; id?: string | null; label: string }>
  compareReasons: string[]
  gateBlockers: string[]
  historySummary?: { latestTrigger?: string | null; latestReason?: string | null; recentUpdateCount?: number | null } | null
}

type AdaptedActivityPanelModel = {
  items: AdaptedActivityItem[]
  latestLineageSummary?: string | null
  latestTrigger?: string | null
  latestReason?: string | null
  latestUpdatedAt?: string | null
}

type AdaptedFeedbackComposerModel = {
  draft: { text: string; category?: string | null }
  disabled: boolean
  submitLabel: string
  scopeLabel?: string | null
}
```

## 3. field mapping table

| raw source | adapted target | note |
| --- | --- | --- |
| `summary.selected_asset_id` | `selectedAssetId` | nullable |
| `header.asset_name` | `pageTitle` and `detailModal.title` | `state_unavailable`면 fallback |
| `asset_rail[]` | `boardItems[]` | board main cards |
| `header.badges[]` | `derivedStrip.badgeItems[]` | top-level state strip |
| `latest_state_preview` | `derivedStrip.latestPreview` | nullable |
| `state_panel.diff_summary` | `derivedStrip.diffSummary` | no previous state 포함 |
| `attention_queue.selected_asset_attention` | `derivedStrip.attentionSummary` | selected asset only |
| `attention_queue.selected_asset_memory` | `derivedStrip.memorySummary` | `insufficient_attention_history` fallback |
| `state_panel.canonical_fields[]` | `detailModal.canonicalStateRows[]` | modal core rows |
| `state_panel.state_notes` | `detailModal.stateNotes` | nullable |
| `state_panel.evidence_refs[]` | `detailModal.evidenceRefs[]` | label formatting 필요 |
| `state_panel.compare_reasons[]` | `detailModal.compareReasons[]` | chip list |
| `state_panel.gate_blockers[]` | `detailModal.gateBlockers[]` | chip list |
| `history_drilldown.items[]` | `activityPanel.items[]` | recent history feed |
| `history_drilldown.latest_lineage_link` | `activityPanel.latestLineageSummary*` | latest lineage summary |
| `history_summary` | `detailModal.historySummary` | latest trigger/reason count |
| `compare_entry.related_assets[]` | `compareCandidates[]` | optional side/inline compare |

## 4. fallback / null handling

### global fallback

- `summary.state_unavailable = true`
  - `selectedAsset = null`
  - `detailModal = null`
  - `derivedStrip`는 neutral state로 렌더

### derived strip fallback

- `header.badges = []`
  - `badgeItems = []`
  - strip은 `no_canonical_state_yet`만 표시

- `latest_state_preview.state = state_unavailable`
  - `latestPreview = null`

- `state_panel.diff_summary.state = no_previous_state`
  - `diffSummary.state = no_previous_state`
  - changed count는 0
  - CTA 비활성

- `attention_queue.selected_asset_attention = null`
  - `attentionSummary = null`
  - 표시 텍스트는 `no_active_attention`

- `attention_queue.selected_asset_memory = null`
  - `memorySummary.summary = insufficient_attention_history`

### detail modal fallback

- `state_panel.state = state_unavailable`
  - modal 열지 않음

- `state_panel.evidence_refs = []`
  - `evidenceRefs = []`
  - evidence section은 empty helper text 유지

- `compare_entry.related_assets = []`
  - compare section 숨김 가능

### activity fallback

- `history_drilldown.items = []`
  - activity panel은 `no_recent_activity`

- `history_drilldown.state = history_unavailable`
  - panel 유지, neutral empty state 표시

## 5. derived strip에 필요한 최소 필드

- `header.badges`
- `latest_state_preview.packet_texture_label`
- `latest_state_preview.maturation_state_label`
- `latest_state_preview.traceability_status_label`
- `state_panel.diff_summary.state`
- `state_panel.diff_summary.diff_class`
- `state_panel.diff_summary.changed_field_count`
- `state_panel.diff_summary.provenance_only`
- `attention_queue.selected_asset_attention`
- `attention_queue.selected_asset_memory`

## 6. modal/detail에 필요한 최소 필드

- `header.asset_name`
- `header.source_type`
- `header.updated_at`
- `state_panel.canonical_fields`
- `state_panel.state_notes`
- `state_panel.evidence_refs`
- `state_panel.compare_reasons`
- `state_panel.gate_blockers`
- `history_summary.latest_update_trigger_type`
- `history_summary.latest_update_reason`
- `history_summary.recent_update_count`
- `compare_entry.related_assets`

## 7. activity/feedback에 필요한 최소 필드

### activity

- `history_drilldown.items`
- `history_drilldown.latest_lineage_link`
- `state_change_diff.state`
- `state_change_diff.diff_class`

### feedback

- 현재 payload에서 직접 source 없음
- adapter는 local draft model만 제공
- persistence source는 v1 범위 밖

## 8. adapter guard rules

- raw payload shape를 React component가 직접 참조하지 않게 한다.
- `experimental_namespace`는 adapted model에 기본 포함하지 않는다.
- nullable field는 UI model에서 explicit null로 유지한다.
- array field는 빈 배열로 normalize한다.
- timestamp는 formatting보다 전달을 우선하고, 표시 형식은 view layer에 맡긴다.

## 9. one-line lock

- `OperatingUiPayloadAdapter`는 process-console payload를 UI 친화 shape로 바꾸는 **단 하나의 read adapter**이며, donor UI나 raw runtime payload가 직접 결합되는 것을 막는 1차 경계다.
