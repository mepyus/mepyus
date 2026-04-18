# Paperclip Frame Component Extraction Reading v0

이 문서는 `git_search/paperclip`의 실제 UI/frame/component를 읽고,  
VectorFL Page로 포크할 때 어떤 것은 shell-only로 가져올 수 있고 어떤 것은 강하게 재의미화해야 하는지 정리한 문서다.  
목적은 구현 전에 `포크 가능한 껍데기 단위`를 더 선명하게 고정하는 것이다.

## 1. Verdict

Paperclip에서 가장 유용한 것은 `앱 프레임`, `queue/list 감각`, `detail console frame`, `activity/history list`, `optional side panel`이다.  
반대로 `issue/company/agent` 중심 의미체계는 거의 전부 VectorFL 쪽으로 다시 써야 한다.

즉 지금 기준에서 포크하기 좋은 것은 `frame composition`이고,  
포크 후 반드시 재소유해야 하는 것은 `navigation semantics`, `panel meaning`, `row meaning`, `detail body meaning`이다.

## 2. Key Files Read

- [App.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/App.tsx)
- [Layout.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Layout.tsx)
- [Sidebar.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Sidebar.tsx)
- [CompanyRail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/CompanyRail.tsx)
- [BreadcrumbBar.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/BreadcrumbBar.tsx)
- [Issues.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Issues.tsx)
- [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)
- [IssueRow.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssueRow.tsx)
- [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)
- [Activity.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Activity.tsx)
- [ActivityRow.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/ActivityRow.tsx)
- [PanelContext.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/context/PanelContext.tsx)

## 3. What Reads As Reusable Shell

### 3-1. Global App Frame

- evidence:
  - [Layout.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Layout.tsx)
  - [App.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/App.tsx)
- reusable shell value:
  - left rail + sidebar + breadcrumb bar + center content + optional right panel 구조
  - mobile/open-close behavior
  - board-wide frame composition
- note:
  - frame 자체는 재사용 가치가 높다
  - route semantics는 VectorFL 기준으로 다시 써야 한다

### 3-2. Queue/List Entry Surface

- evidence:
  - [Issues.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Issues.tsx)
  - [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)
  - [IssueRow.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssueRow.tsx)
- reusable shell value:
  - search/filter/group/view-mode를 가진 진입면 구조
  - row/card 기반 queue entry 감각
  - list vs board 전환 감각
- note:
  - `Issue` 의미는 버리고 `Case / Queue` entry surface 감각만 가져오는 것이 맞다

### 3-3. Detail Console Frame

- evidence:
  - [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)
  - [PropertiesPanel.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/PropertiesPanel.tsx)
  - [PanelContext.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/context/PanelContext.tsx)
- reusable shell value:
  - center detail body + side properties panel 구조
  - panel visibility 토글
  - supporting section을 오른쪽 패널로 빼는 감각
- note:
  - detail page의 내용 ontology는 대부분 VectorFL로 다시 써야 한다
  - 하지만 `current-reading console` frame으로는 매우 유효하다

### 3-4. History / Activity Surface

- evidence:
  - [Activity.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Activity.tsx)
  - [ActivityRow.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/ActivityRow.tsx)
- reusable shell value:
  - append-only activity list 감각
  - event row + relative time + entity link 구조
  - 별도 history page로 분리하는 감각
- note:
  - VectorFL의 `Trace / History` 면으로 포크하기 좋다

### 3-5. Breadcrumb / Top Bar

- evidence:
  - [BreadcrumbBar.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/BreadcrumbBar.tsx)
- reusable shell value:
  - page title / breadcrumb / global toolbar slot 구조
- note:
  - top bar는 재사용 가치가 높다
  - breadcrumb label 체계는 VectorFL navigation semantics로 다시 정의해야 한다

## 4. What Must Be Re-Semanticized

### 4-1. Sidebar Meaning

- evidence:
  - [Sidebar.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Sidebar.tsx)
- why:
  - 현재 sidebar는 Dashboard / Inbox / Issues / Goals / Org / Skills / Costs / Activity 등 issue-company worldview를 강하게 가진다
- VectorFL action:
  - frame은 참고
  - nav item semantics는 `Current Reading / Inputs / Cases / History / Programs`로 다시 재정의

### 4-2. Company Rail Meaning

- evidence:
  - [CompanyRail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/CompanyRail.tsx)
- why:
  - 현재는 company workspace selector다
- VectorFL action:
  - rail 자체는 쓸 수 있어도, 그대로 company selector로 두면 안 된다
  - 개인용 VectorFL Page에서는 instance/program/workspace 전환 또는 완전 제거 대상일 수 있다

### 4-3. Issue Detail Content

- evidence:
  - [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)
- why:
  - comments, documents, workspaces, approvals, live runs 등 Paperclip ontology가 detail body에 너무 깊게 들어가 있다
- VectorFL action:
  - detail frame은 참고
  - 중심 body는 `Current Reading`
  - side panel은 `Governance / Supporting Context`
  - lower strip은 `Trace / History Preview`
  로 다시 써야 한다

## 5. Reuse Strength By Component

### high reuse as shell

- `Layout`
- `PropertiesPanel`
- `PanelContext`
- `IssuesList`의 entry/list structure
- `Activity` / `ActivityRow`
- `BreadcrumbBar`

### medium reuse with strong renaming

- `Sidebar`
- `IssueRow`
- `IssueDetail` frame

### low reuse without heavy rewrite

- company/issue specific route tree
- issue/company/agent/project naming 체계
- issue lifecycle interactions

## 6. Practical Fork Guidance

현재 기준의 포크 순서는 아래처럼 읽는다.

1. `Layout`과 right panel 구조를 shell frame으로 가져온다
2. `BreadcrumbBar`를 top bar base로 가져온다
3. `IssuesList` 감각으로 `Cases / Queue`와 `Inputs / Intake` entry surface를 다시 만든다
4. `IssueDetail` frame을 `Current Reading` console로 다시 쓴다
5. `Activity`를 `History / Trace` 면으로 다시 쓴다
6. `Sidebar`는 마지막에 VectorFL navigation semantics로 완전 재작성한다

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Paperclip에서 VectorFL Page로 포크하기 가장 좋은 것은 Layout, list/queue structure, detail console frame, activity/history list, panel toggle 구조이고, Sidebar 의미체계와 Issue/Company ontology는 거의 전부 VectorFL navigation과 current-reading semantics로 다시 재의미화해야 한다.`
