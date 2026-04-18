# paperclip native page taxonomy and operable flow v0

## 1. verdict

Paperclip를 원본 제품으로 다시 읽으면, 이것은 단순한 multi-agent dashboard가 아니다.
핵심은 `company-first control plane` 위에 놓인 `operable page taxonomy`다.

즉 사용자는 단순히 상태를 보지 않는다.
다음 page class를 오가며 실제로 회사를 운영한다.

- work list
- work detail
- right-side properties inspector
- agent operable detail
- triage inbox
- audit/activity
- org/spatial view
- company/settings/config

이 구조를 먼저 Paperclip의 native line으로 이해해야 한다.

## 2. product-native reading

`README.md`와 `doc/PRODUCT.md` 기준으로 Paperclip의 본체는:

- autonomous AI companies를 위한 control plane
- company를 first-order object로 둠
- agents/employees, org structure, goals, issues/comments, heartbeats, budgets, approvals, board governance를 운영함

중요한 건 Paperclip가 스스로를 이렇게 규정한다는 점이다.

- not a chatbot
- not an agent framework
- not a workflow builder
- not a prompt manager

즉 Paperclip는 “대화”보다 “운영”을 중심으로 설계된 앱이다.

## 3. route and shell reading

`ui/src/App.tsx` 기준으로 Paperclip의 board routes는 분명한 page taxonomy를 가진다.

주요 축:

- dashboard
- companies / company settings / import / export / skills
- org
- agents / agent detail
- projects / project detail / workspaces
- issues / issue detail
- routines / routine detail
- goals / goal detail
- approvals / approval detail
- costs
- activity
- inbox
- instance settings / plugin / adapter / tests

즉 route 수준에서 이미 list/detail/settings/audit/org/config가 분리되어 있다.

`ui/src/components/Layout.tsx`와 `ui/src/components/Sidebar.tsx` 기준으로 shell도 분명하다.

- left sidebar navigation
- breadcrumb bar
- main content
- optional right properties panel

이 구조는 “graph center + floating panels”가 아니라
`앱형 운용면`이다.

## 4. native page taxonomy

### 4-1. work list page

대표:

- `ui/src/pages/Issues.tsx`
- `ui/src/components/IssuesList.tsx`

역할:

- issues를 목록으로 운영
- search / filter / sort / group / board-list toggle
- assignee / status / priority / project 기준 조작

핵심:

- row-level assignment와 state change가 가능
- list page가 단순 entry가 아니라 실제 운영면

### 4-2. work detail page

대표:

- `ui/src/pages/IssueDetail.tsx`

역할:

- issue 하나를 중심으로 현재 work object를 깊게 다룸

포함 surface:

- comment thread
- documents
- workspace
- live run widget
- timeline/event reading
- inline editing

핵심:

- detail page는 passive viewer가 아니다
- 실제 작업, 대화, 문서, run 상태가 한곳에서 합쳐진다

### 4-3. right-side properties inspector

대표:

- `ui/src/components/IssueProperties.tsx`
- `ui/src/components/PropertiesPanel.tsx`

역할:

- assignee 변경
- project 변경
- labels 변경
- priority / status 읽기
- linked workspace 맥락 읽기

핵심:

- inspector는 장식 side note가 아니다
- 실제 reassignment / retagging / project rebinding이 일어나는 조작면

### 4-4. triage / inbox page

대표:

- `ui/src/pages/Inbox.tsx`

역할:

- 내가 만져야 하는 work만 모아서 triage
- approvals / failed runs / alerts / touched issues / join requests를 inbox model로 묶음

핵심:

- inbox는 secondary convenience가 아니라 board operator의 1차 triage 면

### 4-5. agent operable detail page

대표:

- `ui/src/pages/AgentDetail.tsx`

핵심 탭:

- dashboard
- instructions
- configuration
- skills
- runs
- budget

역할:

- agent 하나를 실제로 운용/수정
- adapter config 수정
- instruction 수정
- skills 적용
- run transcript/usage 확인
- budget policy 관리
- action buttons로 run/pause/reset/terminate

핵심:

- 이 페이지가 Paperclip의 가장 중요한 `operable organ page`다
- 단순 agent label viewer가 아니다

### 4-6. audit page

대표:

- `ui/src/pages/Activity.tsx`

역할:

- append-only activity stream
- issue/agent/project/goal 등 entity type별 audit reading

핵심:

- activity는 아래 strip이 아니라 별도 page class

### 4-7. org / spatial page

대표:

- `ui/src/pages/OrgChart.tsx`

역할:

- org tree를 canvas-like 표면에 배치
- hierarchy / reporting line을 spatially 읽게 함

핵심:

- spatial page는 모든 것을 canvas로 만들지 않는다
- hierarchy라는 특정 문제에만 spatial class를 사용

### 4-8. company / policy / settings page

대표:

- `ui/src/pages/CompanySettings.tsx`

역할:

- company metadata
- invite/onboarding snippet
- approval policy
- feedback/data sharing
- import/export / logo / branding

핵심:

- settings는 단순 환경설정이 아니라 운영 정책 surface

## 5. operable flow reading

Paperclip의 실제 native 운용 흐름은 대체로 이 line으로 읽힌다.

1. sidebar/inbox/issues에서 work object를 찾음
2. list page에서 filter/search/grouping 하며 현재 work를 triage
3. issue detail로 들어가 현재 work를 중심으로 run/comment/doc/workspace를 봄
4. right-side inspector에서 assignee/project/labels를 수정
5. 필요하면 agent detail로 이동해 instructions/config/budget/runs를 수정
6. activity와 org, settings는 보조가 아니라 각각 audit / hierarchy / policy page class로 따로 존재

즉 Paperclip의 핵심은 “그래프를 보는 것”이 아니라
`list -> detail -> inspector -> operable agent/config -> audit/policy`
연쇄다.

## 6. strengths of paperclip as native product

- operable page taxonomy가 분명하다
- list/detail/inspector가 실제로 수정 가능한 면이다
- agent detail이 진짜 runtime node control page로 존재한다
- triage(inbox)와 audit(activity)가 독립 page class로 강하다
- shell이 앱형으로 안정적이다

## 7. limits of paperclip for vectorfl adoption

- ontology가 company/agent/issue/goal/approval 중심이다
- assignment-first이며 current-reading-first가 아니다
- governance는 board/company governance이지 reading-protection governance가 아니다
- issue/task model이 canonical이고 line/family/residue/current-reading이 아니다

즉 그대로 들이면 VectorFL core를 덮는다.

## 8. comparison cue for next step

이 native reading이 시사하는 건 단순하다.

VectorFL는 Paperclip에서 다음을 참조해야 한다.

- work list page
- work detail page
- right-side inspector
- operable organ detail/editor
- triage page
- audit page
- org/spatial page
- policy/settings page

반대로 들이면 안 되는 건:

- company / issue / goal / approval ontology
- assignment-first worldview
- board/company governance semantics

## 9. final judgment

Paperclip를 제대로 다시 읽으면,
우리가 차용해야 하는 건 스타일이 아니라 `operable screen grammar`다.

그리고 그 grammar의 중심은:

- list page
- detail page
- inspector
- operable node detail
- triage
- audit

이다.

즉 다음 VectorFL 비교와 재구성은 이제부터
“이 page class를 우리 core semantics 위에 어떻게 얹을 것인가”
로 가야 한다.

## appendix. evidence files

- `references/git_search/paperclip-master/README.md`
- `references/git_search/paperclip-master/doc/PRODUCT.md`
- `references/git_search/paperclip-master/doc/spec/ui.md`
- `references/git_search/paperclip-master/ui/src/App.tsx`
- `references/git_search/paperclip-master/ui/src/components/Layout.tsx`
- `references/git_search/paperclip-master/ui/src/components/Sidebar.tsx`
- `references/git_search/paperclip-master/ui/src/pages/Issues.tsx`
- `references/git_search/paperclip-master/ui/src/components/IssuesList.tsx`
- `references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx`
- `references/git_search/paperclip-master/ui/src/components/IssueProperties.tsx`
- `references/git_search/paperclip-master/ui/src/pages/Inbox.tsx`
- `references/git_search/paperclip-master/ui/src/pages/Activity.tsx`
- `references/git_search/paperclip-master/ui/src/pages/OrgChart.tsx`
- `references/git_search/paperclip-master/ui/src/pages/CompanySettings.tsx`
- `references/git_search/paperclip-master/ui/src/pages/AgentDetail.tsx`
