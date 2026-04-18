# VectorFL Current Reading Console Shell Rewrite Brief v0

이 문서는 Paperclip의 `IssueDetail` frame을  
VectorFL Page의 `Current Reading console`로 다시 쓰기 위한 rewrite brief를 잠근다.  
목적은 frame은 참고하되, 중심 body와 side/strip 의미를 VectorFL 기준으로 완전히 재소유하는 것이다.

## 1. 목적

현재 가장 먼저 필요한 shell 재작성 대상은 `IssueDetail`이 아니라  
`Current Reading console`이다.

따라서 이 문서는 아래를 잠근다.

- 무엇을 frame으로만 가져올 것인가
- 무엇을 완전히 재의미화할 것인가
- 첫 console에서 어떤 section만 유지할 것인가

## 2. Source Frame Reading

참조하는 원본은 아래다.

- [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)
- [PropertiesPanel.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/PropertiesPanel.tsx)
- [PanelContext.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/context/PanelContext.tsx)

현재 이 frame에서 참고할 수 있는 것은 아래다.

- detail 중심 화면 구조
- center content + right panel 감각
- lower/history/comment 계열을 붙일 수 있는 여지
- panel open/close 구조

## 3. Do Not Carry Over

아래는 Current Reading console로 그대로 가져오지 않는다.

- issue title/body/comments ontology
- documents section 의미
- workspace card 의미
- live run widget 의미
- approval section 의미
- comment thread 중심성

즉 IssueDetail의 기존 의미체계는 거의 유지하지 않고,
frame과 panel composition만 참조한다.

## 4. Current Reading Console Target Structure

첫 Current Reading console은 아래 다섯 section으로 다시 쓴다.

### 4-1. Case Header

- 의미:
  - 지금 읽고 있는 case anchor
  - case kind / status
  - linked program 존재 여부
  - last updated

### 4-2. Current Reading Body

- 의미:
  - `Surface Packet` 기반의 중심 reading body
  - 지금 무엇을 먼저 읽어야 하는지
  - supporting unit anchor를 함께 보여주는 핵심 면

### 4-3. Lane Strip

- 의미:
  - 현재 lane
  - lane status
  - next hop candidates
  - 진행/보류의 좁은 strip

### 4-4. Governance Side

- 의미:
  - hold
  - restriction
  - release condition
  - next check trigger
  - weak/fallback / re-read caution

### 4-5. Trace Strip

- 의미:
  - latest trace preview
  - residue note
  - reentry hint
  - decision trace anchor

## 5. Section Ownership Mapping

### center

- source of truth:
  - `Surface Packet`
- shell meaning:
  - current-reading body

### top summary

- source of truth:
  - `Case Record`
- shell meaning:
  - case header

### lane strip

- source of truth:
  - `Lane State Record`
- shell meaning:
  - progression snapshot

### right side / panel

- source of truth:
  - `Governance Record`
  - optional intake caution refs
- shell meaning:
  - governance + caution side

### lower strip / secondary area

- source of truth:
  - `Trace / Memory Record`
- shell meaning:
  - trace/history preview

## 6. Console Rules

### rule 1. current-reading first

- center body는 comment thread가 아니라 current-reading가 차지한다

### rule 2. governance must stay visible

- hold / restriction / release condition은 side에서 계속 보여야 한다

### rule 3. trace is preview, not replacement

- trace strip은 회고 단서를 보여주지만 current-reading body를 대체하지 않는다

### rule 4. shell does not reinterpret

- console은 canonical interpretation을 다시 쓰지 않는다
- 보여주기 좋게 적응만 한다

### rule 5. weakness is not hidden

- fallback, weak intake, re-read needed 같은 caution은 governance side 또는 note 영역에 남긴다

## 7. First Rewrite Scope

첫 rewrite에서는 아래만 포함하면 충분하다.

- `Case Header`
- `Current Reading Body`
- `Lane Strip`
- `Governance Side`
- `Trace Strip`

아래는 뒤로 미룬다.

- edit controls
- action execution buttons
- live program control
- rich comment thread
- document management
- assignment/team UI

## 8. First Mock Fit

이 rewrite brief는 아래 문서와 바로 연결된다.

- [vectorfl_current_reading_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_adapter_contract_v0.md)
- [vectorfl_current_reading_mock_fixture_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_mock_fixture_contract_v0.md)
- [vectorfl_current_reading_mock_fixture_set_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_mock_fixture_set_v0.md)

즉 first mock shell은 이 brief의 section semantics를 실제 fixture에 대입해 보는 단계다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Current Reading console은 Paperclip IssueDetail의 frame과 panel composition만 참고하고, 중심 body는 Surface Packet 기반 current-reading으로, 오른쪽은 Governance/Caution side로, 아래는 Trace preview strip으로 다시 써서 current-reading-first console로 재소유한다.`
