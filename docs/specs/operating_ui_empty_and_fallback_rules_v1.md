# operating ui empty and fallback rules v1

## 1. purpose

- 이 문서는 `OperatingUiPayloadAdapter` 이후 각 UI 컴포넌트가 빈 상태, 약한 상태, 불충분 상태, 비활성 상태를 어떻게 보여야 하는지 고정한다.
- 목적은 “예뻐 보이는 처리”가 아니라, **실패/빈 상태/약한 상태에서도 안 무너지는 UI 규칙**을 먼저 잠그는 것이다.

## 2. component rules

### `DerivedStateStrip`

#### normal state

- 조건
  - `selectedAsset != null`
  - `badgeItems.length > 0`
- 표시
  - latest preview
  - diff summary
  - attention summary
  - memory summary

#### empty state

- 조건
  - `badgeItems.length === 0`
  - `latestPreview == null`
- 표시 문구 가이드
  - `no_canonical_state_yet`

#### fallback state

- `no_previous_state`
  - 표시 문구:
    - `compare to previous unavailable`
  - CTA:
    - diff CTA 비활성

- `no_active_attention`
  - 표시 문구:
    - `no active attention`
  - CTA:
    - attention CTA 숨김 또는 비활성

- `insufficient_attention_history`
  - 표시 문구:
    - `insufficient attention history`
  - CTA:
    - memory CTA 비활성

- `state_unavailable`
  - 표시 문구:
    - `no canonical state yet`
  - CTA:
    - 전부 비활성

#### disabled state

- strip 자체는 disabled보다는 fallback으로 처리

#### null / empty array handling

- `badgeItems = []` 허용
- `attentionSummary = null` 허용
- `memorySummary = null` 대신 summary text normalize 권장

### `AssetStateBoard`

#### normal state

- 조건
  - `items.length > 0`
- 표시
  - grid or board list
  - selected item highlight

#### empty state

- 조건
  - `items.length === 0`
- 표시 문구 가이드
  - `no assets available`

#### fallback state

- `state_unavailable`
  - board 전체 empty state로 동일 처리

#### disabled state

- 별도 disabled 없음
- 빈 보드 상태로 처리

#### CTA 규칙

- card click:
  - `items.length > 0`일 때만 활성

#### null / empty array handling

- `items = []`로 normalize

### `SelectedAssetDetailModal`

#### normal state

- 조건
  - `open = true`
  - `selectedAsset != null`
- 표시
  - canonical rows
  - notes
  - evidence
  - compare reasons
  - blockers
  - activity panel
  - feedback composer

#### empty state

- 조건
  - `selectedAsset = null`
- 표시 문구 가이드
  - modal 자체를 열지 않음

#### fallback state

- `no_selected_asset`
  - modal render 금지

- `state_unavailable`
  - modal render 금지

- `compareCandidates = []`
  - compare section 숨김 가능

- `evidenceRefs = []`
  - evidence section empty helper
  - 표시 문구:
    - `no evidence refs attached`

#### disabled state

- feedback disabled면 modal은 유지
- 내부 `FeedbackComposer`만 disabled

#### CTA 규칙

- close CTA:
  - 항상 활성
- compare CTA:
  - compare candidates 있을 때만 활성
- history CTA:
  - history summary 존재 시 활성

#### null / empty array handling

- `compareCandidates = []`
- `evidenceRefs = []`
- `gateBlockers = []`
- `compareReasons = []`

### `ActivityPanel`

#### normal state

- 조건
  - `items.length > 0`
- 표시
  - recent activity list
  - lineage summary

#### empty state

- 조건
  - `items.length === 0`
- 표시 문구 가이드
  - `no recent activity`

#### fallback state

- `empty_activity`
  - history list는 없고 lineage summary만 있으면 summary만 표시

- `history_unavailable`
  - 표시 문구:
    - `history unavailable`

#### disabled state

- 별도 disabled 없음

#### CTA 규칙

- history item CTA:
  - item 있을 때만 활성
- diff CTA:
  - item이 `compareIndex`를 가질 때만 활성

#### null / empty array handling

- `items = []`
- `latestLineage = null` 허용

### `FeedbackComposer`

#### normal state

- 조건
  - `selectedAsset != null`
  - `disabled = false`

#### empty state

- 조건
  - draft empty
- 표시 문구 가이드
  - placeholder 사용
  - 예: `leave operator feedback`

#### fallback state

- `no_selected_asset`
  - composer 숨김 또는 disabled
  - 권장: disabled card

- `feedback_disabled`
  - 표시 문구:
    - `feedback unavailable in current state`

#### disabled state

- 조건
  - `disabled = true`
- 표시
  - 입력창 disabled
  - submit CTA 비활성

#### CTA 규칙

- submit CTA:
  - `disabled = false` and `selectedAsset != null`일 때만 활성
- cancel CTA:
  - draft non-empty일 때만 활성

#### null / empty array handling

- draft는 항상 controlled object
  - `{ text: '', category: null }`

## 3. display copy guide

- `no_previous_state`
  - `compare to previous unavailable`

- `no_active_attention`
  - `no active attention`

- `insufficient_attention_history`
  - `insufficient attention history`

- `state_unavailable`
  - `no canonical state yet`

- `no_selected_asset`
  - `select an asset to open detail`

- `empty_activity`
  - `no recent activity`

- `feedback_disabled`
  - `feedback unavailable in current state`

## 4. selection default rules

### initial selection

- `initialAssetId`가 있으면 우선 선택
- 없으면 `boardItems[0]` 선택
- `boardItems.length === 0`이면 `selectedAssetId = null`

### modal initial state

- `initialModalOpen` 기본값은 `false`
- `selectedAssetId = null`이면 강제로 `false`

### asset switch policy

- asset 전환 시 `feedbackDraft` reset
- reset 기본값:
  - `{ text: '', category: null }`

### same asset reopen policy

- v1 기본은 retain 안 함
- 동일 asset 재오픈도 reset
- 이유:
  - draft persistence는 아직 범위 밖

## 5. adapter vs component responsibility boundary

### adapter responsibility

- raw payload validation 최소 수준
  - required top-level key 유무 확인
  - missing keys -> safe fallback model

- normalize
  - `null` / `[]` / missing field normalize
  - state code normalize

- regrouping
  - raw payload field를 component-friendly shape로 재배열

- fallback state code 부여
  - `state_unavailable`
  - `no_previous_state`
  - `insufficient_attention_history`
  - `no_active_attention`

### adapter does not own

- 최종 display copy styling
- button placement
- section visibility animation
- feedback draft local UX
- persistence

### component responsibility

- 표시 문구 렌더
- CTA 활성/비활성
- local open/close state
- controlled input UI
- empty/fallback visual treatment

## 6. one-line lock

- v1 UI는 `정상 상태`보다 먼저 `empty / fallback / disabled`를 안정적으로 다루는 규칙 위에서 시작하며, 이 규칙은 adapter가 상태를 정규화하고 component가 표현을 담당하는 방식으로 고정한다.
