# paperclip native product reading v0

## 1. verdict

지금까지의 문제는 Paperclip를 먼저 제품 자체로 읽지 않고, VectorFL 번역을 너무 빨리 시작했다는 데 있었다.  
원본 기준으로 다시 보면 Paperclip는 `그래프형 범용 면`이 아니라, 분명한 page class를 가진 운영 제품이다.

핵심 라인은 이렇다.

- `Issues`가 업무 목록/배정의 중심면이다.
- `IssueDetail`이 업무 수행과 재배정의 중심 상세면이다.
- `IssueProperties`가 우측 assignment/properties inspector다.
- `AgentDetail`이 기관 자체의 instruction/configuration/skills/runs/budget를 수정하는 기관 상세면이다.
- `Inbox`, `Routines`, `Activity`, `Org`, `Company Settings`가 triage, recurring work, audit, hierarchy, company policy를 따로 담당한다.

즉 Paperclip는 먼저 `회사 운영 제품`으로 읽어야 하고, 그 다음에만 어떤 구조를 참조할지 말할 수 있다.

## 2. why this reset

이 재읽기가 필요한 이유는 단순하다.

- Paperclip를 VectorFL의 현재 기관 언어로 먼저 번역하면 원본 제품의 중심 구조를 놓치게 된다.
- 원본 구조를 모르고 shell만 가져오면 결과가 `기존 그래프뷰 변형`처럼 보이게 된다.
- Paperclip를 제대로 참조하려면 먼저 `무슨 페이지가 있고, 어디서 배정하고, 어디서 수정하고, 어디서 audit하고, 어디서 조직을 본다`를 native하게 읽어야 한다.

즉 이번 문서는 VectorFL 적용 문서가 아니라, Paperclip를 Paperclip로 읽은 기준선이다.

## 3. product framing

README 기준 Paperclip의 자기 정의는 분명하다.

- `Open-source orchestration for zero-human companies`
- `If OpenClaw is an employee, Paperclip is the company`
- `Manage business goals, not pull requests`

그리고 문제 설정도 명확하다.

- agent 여러 개를 회사처럼 운영한다
- tasks are ticket-based
- sessions persist across reboots
- governance, budgets, org charts, goal alignment, heartbeats가 같이 묶여 있다

근거:

- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/README.md)

즉 Paperclip의 중심은 보기 좋은 board가 아니라, `회사 운영 control plane`이다.

## 4. route and page taxonomy

`App.tsx` 기준 Paperclip는 page type이 분명하게 나뉜다.

- dashboard
- companies / company settings / export / import
- org
- agents / agent detail
- projects / project detail / project workspace detail
- issues / issue detail
- routines / routine detail
- goals / goal detail
- approvals / approval detail
- costs
- activity
- inbox
- design guide / test labs / instance settings

근거:

- [App.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/App.tsx)

이건 중요하다. Paperclip는 one generic surface가 아니라 `list page / detail page / settings page / audit page / spatial page`가 분리된 제품이다.

## 5. sidebar reading

Sidebar는 제품의 중심 분류를 그대로 보여준다.

- top utility: company switch context, search, new issue
- dashboard, inbox
- work: issues, routines, goals
- projects
- agents
- company: org, skills, costs, activity, settings

근거:

- [Sidebar.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Sidebar.tsx)

즉 native product 기준의 주축은 다음처럼 읽힌다.

- `work allocation`
- `execution ownership`
- `agent management`
- `company governance`

## 6. core assignment line

Paperclip에서 업무 할당 라인의 중심은 `Issues` 계열이다.

### 6-1. issues list is the assignment board

`Issues.tsx`는 업무 목록면이고, 실제 배정/검색/필터/실행 상태를 묶는다.  
`IssuesList.tsx`는 단순 렌더러가 아니라, list/board grouping, filter, assignee 변경, status 변경을 수행하는 operational list다.

특히 `assignIssue(issueId, assigneeAgentId, assigneeUserId)`가 `onUpdateIssue(issueId, { assigneeAgentId, assigneeUserId })`를 호출한다.

근거:

- [Issues.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Issues.tsx)
- [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)

### 6-2. issue detail is the execution page

`IssueDetail.tsx`는 단순 조회면이 아니다.

- comments
- activity
- linked runs
- approvals
- attachments/documents
- live runs
- active run
- child issues
- issue update
- comment + reassign

가 한 페이지에 같이 있다.

특히 `addCommentAndReassign`는 issue update 안에서 comment와 reassignment를 같이 처리한다. 즉 상세면이 실제 운용면이다.

근거:

- [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)

### 6-3. issue properties is the right-side assignment inspector

`IssueProperties.tsx`는 우측 properties inspector다.

- assignee picker
- project picker
- labels picker
- issue metadata row

를 제공하고, `onUpdate`로 assignment와 project, labels를 갱신한다.

근거:

- [IssueProperties.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssueProperties.tsx)
- [PropertiesPanel.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/PropertiesPanel.tsx)

### 6-4. native assignment line summary

Paperclip의 핵심 assignment line은 이렇게 읽힌다.

`Issues list -> IssueDetail -> right-side IssueProperties inspector`

즉 업무는 list에서 선택되고, detail에서 수행되며, properties inspector에서 재배정/속성 수정이 일어난다.

## 7. supporting work surfaces

### 7-1. inbox is work triage, not just notifications

`Inbox.tsx`는 단순 알림면이 아니다.

- mine / recent / unread / all 탭
- work items
- approvals
- failed runs
- alerts
- assignee/workspace/project/status columns

를 묶는 triage surface다.

근거:

- [Inbox.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Inbox.tsx)

즉 Inbox는 “무슨 일을 지금 먼저 봐야 하나”를 고르는 work intake/triage 면이다.

### 7-2. routines is recurring work allocation

`Routines.tsx`는 반복 업무 배정면이다.

- routine list
- assignee grouping
- project grouping
- enable/pause/archive
- run now

가 보이고, `RoutineDetail.tsx` 쪽에서는 assignee, project, variables, schedule을 실제로 수정한다.

근거:

- [Routines.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Routines.tsx)
- [RoutineDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/RoutineDetail.tsx)

즉 routine은 recurring work assignment/productivity surface다.

## 8. agent detail is the operable organ page

이 부분이 중요하다. Paperclip는 기관을 단순히 보여주지 않는다. `AgentDetail`은 실제로 수정 가능한 기관 상세면이다.

`AgentDetail.tsx`에는 다음 탭이 있다.

- dashboard
- instructions
- skills
- configuration
- runs
- budget

그리고 header에서 바로

- assign task
- run heartbeat
- pause/resume
- reset sessions
- terminate

를 할 수 있다.

`instructions`와 `configuration`은 dirty state, save/cancel action bar를 가진 실제 수정면이다.  
또 instructions 쪽에는 bundle/file tree, entry file, virtual file, markdown editing 같은 구조가 있다.

근거:

- [AgentDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/AgentDetail.tsx)
- [AgentConfigForm.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/AgentConfigForm.tsx)

즉 AgentDetail은 단순 observability 페이지가 아니라, `기관 지정 / instruction 수정 / configuration 변경 / skill attachment / budget editing / run inspection`이 가능한 operable organ page다.

이 점을 놓치면 Paperclip를 제대로 참조한 것이 아니다.

## 9. activity, org, settings are separate operational classes

### 9-1. activity is append-only audit page

`Activity.tsx`는 event stream/audit page다.

- filter by entity type
- border + divide list
- activity rows

구조로 되어 있다.

근거:

- [Activity.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Activity.tsx)

즉 activity는 generic log panel이 아니라 회사 단위 append-only audit page다.

### 9-2. org is spatial hierarchy page

`OrgChart.tsx`는 트리 layout, pan/zoom, forest layout, edge collection을 가진 전용 spatial page다.

근거:

- [OrgChart.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/OrgChart.tsx)

즉 관계를 보여줄 때는 generic list/detail이 아니라 spatial page class를 따로 쓴다.

### 9-3. company settings is company policy/config page

`CompanySettings.tsx`는 general/company policy/invite/snippet/logo/board approval 같은 설정면이다.

근거:

- [CompanySettings.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/CompanySettings.tsx)

즉 company-level policy와 bootstrap/invite control도 별도 settings page class로 분리된다.

## 10. structural line extracted from paperclip

Paperclip native reading에서 지금 가장 먼저 뽑아야 하는 structural line은 아래다.

### line A. work allocation line

`Inbox triage -> Issues list -> IssueDetail -> IssueProperties -> runs/comments/approvals/activity`

이 라인은

- 일이 보이는 곳
- 일이 배정되는 곳
- 일이 수행되는 곳
- 일이 조정되는 곳
- 일이 audit/gov/run 흔적을 남기는 곳

을 연결한다.

### line B. operable organ line

`Agents list -> AgentDetail -> instructions/configuration/skills/runs/budget`

이 라인은

- 기관을 고르는 곳
- 기관을 실제로 수정하는 곳
- 기관의 runtime behavior를 조정하는 곳

을 연결한다.

### line C. company control line

`Dashboard / Goals / Costs / Approvals / Activity / Org / Settings`

이 라인은 회사 전체 운영과 감독을 둘러싼 상위 control line이다.

## 11. what this means for later VectorFL attachment

이번 문서의 목적은 아직 VectorFL 설계가 아니다.  
다만 native reading 기준으로 한 가지는 이미 분명하다.

VectorFL을 붙이려면 먼저 Paperclip에서 다음 두 class를 제대로 다뤄야 한다.

- `work pages`
  - issue list
  - issue detail
  - issue properties
- `organ pages`
  - agent detail
  - instruction/config/skills/runs/budget

즉 VectorFL이 나중에 붙더라도 먼저 참조해야 할 것은

- 업무 배정면
- 업무 상세면
- 우측 속성면
- 기관 수정면

이지, generic graph-like reading surface가 아니다.

## 12. final judgment

Paperclip를 native하게 다시 읽은 결과, 지금까지의 drift는 분명하다.

- 나는 Paperclip의 shell rhythm만 가져오고, 정작 native product class는 놓쳤다.
- 특히 `기관을 수정하고 배정하는 operable page`를 충분히 반영하지 못했다.
- 따라서 지금까지 만든 VectorFL Page는 Paperclip 참조가 얕았고, 사용자가 느낀 `그래프뷰 변형` 인상이 맞다.

다음 단계는 이 native line을 기준으로 다시 시작해야 한다.

- `Issues list / IssueDetail / IssueProperties`
- `AgentDetail with instructions/configuration`

를 먼저 기준면으로 붙들고, 그 뒤에만 VectorFL을 어디에 어떻게 얹을지 판단해야 한다.

## 13. deeper ui/src rereading: why the page structure exists

2026-04-11 재확인 기준으로, Paperclip `ui/src`의 핵심은 `탭으로 많은 정보를 나열하는 것`이 아니다. 구조의 중심은 다음 네 가지다.

- `App.tsx`는 회사/보드 루트 아래에 inbox, issues, issue detail, agents, agent detail, approvals, activity, settings를 분리한다. 이건 view mode 분리가 아니라 운영 리소스 분리다.
- `Layout.tsx`는 `CompanyRail`, `Sidebar`, `BreadcrumbBar`, `PropertiesPanel`, `CommandPalette`, 생성 다이얼로그, toast, mobile nav를 한 프레임으로 묶는다. 즉 각 페이지는 독립 카드가 아니라 회사 운영 프레임 안에서 움직인다.
- `Sidebar.tsx`는 Dashboard/Inbox, Work(Issues/Routines/Goals), Projects, Agents, Company(Org/Skills/Costs/Activity/Settings)로 나뉜다. 이것은 시각 메뉴가 아니라 work allocation, organ management, company governance를 분리하는 제품 판단이다.
- `queryKeys.ts`와 `api/*`는 issues, agents, heartbeats, approvals, activity, budgets, companies를 별도 리소스로 유지한다. 페이지는 이 리소스들을 임의로 합친 dashboard가 아니라, 각 리소스의 운용 책임을 맡는다.

따라서 Paperclip의 페이지 구성 이유는 다음처럼 읽어야 한다.

- `Inbox`는 알림함이 아니라 work/approval/failed-run/join-request triage queue다.
- `Issues`는 단순 목록이 아니라 검색, 필터, list/board, assignee/status update가 가능한 work allocation board다.
- `IssueDetail`은 상세 조회가 아니라 description, documents, attachments, workspace, comments, live run, linked approvals, subissues, activity가 연결되는 execution surface다.
- `IssueProperties`와 `PropertiesPanel`은 상세면 옆에 남는 assignment/gate inspector다. 상태, priority, labels, assignee, project를 본문 흐름과 분리하지 않고 동시에 조정한다.
- `AgentDetail`은 worker 이름을 보여주는 페이지가 아니라 assign task, run heartbeat, pause/resume, reset sessions, terminate를 가진 organ operation page다.
- `AgentDetail`의 dashboard/instructions/configuration/skills/runs/budget 탭은 정보 나열 탭이 아니라 한 기관의 행동 조건, 실행 기록, 비용 한계를 다루는 하위 운용 슬롯이다.
- `Approvals`와 `ApprovalDetail`은 read-only 보고서가 아니라 approve/reject/request revision/resubmit/comment로 hold/continue 판단을 실제 액션으로 귀속시키는 governance surface다.
- `Activity`는 보조 로그가 아니라 회사 단위 append-only audit surface다.

핵심 오해는 `탭이 많다`가 아니다. Paperclip에서 탭은 최상위 제품 구조가 아니라 detail page 안의 하위 운용 분기다. 최상위 구조는 `inbox -> work board -> work detail + right inspector -> organ detail -> approval/audit/settings`다.

## 14. VectorFL translation lock from this rereading

VectorFL 통합 운용 페이지는 지금 만든 `paper_proper`나 `operable_surface`와 같은 층위로 커지면 안 된다. 그 둘은 내부 상태/검증/bridge substrate다.

Paperclip식으로 번역하면 VectorFL의 상위 페이지 클래스는 이렇게 잡아야 한다.

- `VectorFL operating workspace`: Paperclip의 company/board boundary에 해당한다.
- `Work triage`: Paperclip Inbox에 해당한다. Codex/Gemini return, hold item, failed validation, actual candidate arrival을 우선순위 큐로 본다.
- `Work packet board`: Paperclip Issues에 해당한다. scenario-bearing packet, validation packet, export candidate packet, merge packet을 배치한다.
- `Work packet detail`: Paperclip IssueDetail에 해당한다. 선택된 packet의 goal, context, evidence, returns, live run, trace를 본다.
- `Right assignment/gate inspector`: Paperclip IssueProperties/PropertiesPanel에 해당한다. current organ/lane, target worker, forbidden scope, gate posture, continue/hold/reopen condition을 항상 옆에 둔다.
- `Organ runtime detail`: Paperclip AgentDetail에 해당한다. Codex/Gemini/미래 기관을 단순 텍스트가 아니라 instructions/configuration/skills/runs/budget 또는 VectorFL식 동등 슬롯으로 다룬다.
- `Approval/gate surface`: Paperclip Approvals에 해당한다. hold/continue/reopen/cross-check를 실제 supervisor decision action으로 귀속시킨다.
- `Trace/audit surface`: Paperclip Activity에 해당한다. manifest 변경, worker run, validation result, decision을 append-only reading lane으로 본다.

따라서 다음 구현에서 금지할 것은 분명하다.

- `operable_surface` 안에 탭만 더 늘려 통합 운용 페이지라고 부르지 말 것.
- Codex/Gemini를 이름만 표시하고 입력/선택/지정/확인/감독 장치 없이 worker로 부르지 말 것.
- `paper_proper`의 bridge state를 그대로 상단 카드로 옮기는 수준에서 멈추지 말 것.
- 기존 그래프뷰 shell을 조금 고쳐 control plane이라고 부르지 말 것.

다음 구현 기준은 이 문장이다.

`VectorFL integrated operating page = work packet control plane + organ runtime control plane + supervisor gate/audit plane`

이 기준으로만 `paper_proper`의 목적성, `operable_surface`의 본문 상태, actual Codex/Gemini bridge 결과를 상위 제품 페이지에 재배치해야 한다.

## appendix. evidence files

- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/README.md)
- [App.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/App.tsx)
- [Layout.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Layout.tsx)
- [Sidebar.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/Sidebar.tsx)
- [Issues.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Issues.tsx)
- [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)
- [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)
- [IssueProperties.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssueProperties.tsx)
- [PropertiesPanel.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/PropertiesPanel.tsx)
- [CommentThread.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/CommentThread.tsx)
- [LiveRunWidget.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/LiveRunWidget.tsx)
- [Inbox.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Inbox.tsx)
- [Routines.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Routines.tsx)
- [RoutineDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/RoutineDetail.tsx)
- [Agents.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Agents.tsx)
- [AgentDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/AgentDetail.tsx)
- [AgentActionButtons.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/AgentActionButtons.tsx)
- [AgentConfigForm.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/AgentConfigForm.tsx)
- [Approvals.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Approvals.tsx)
- [ApprovalDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/ApprovalDetail.tsx)
- [ApprovalCard.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/ApprovalCard.tsx)
- [Activity.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Activity.tsx)
- [ActivityRow.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/ActivityRow.tsx)
- [OrgChart.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/OrgChart.tsx)
- [CompanySettings.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/CompanySettings.tsx)
- [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/api/issues.ts)
- [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/api/agents.ts)
- [queryKeys.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/lib/queryKeys.ts)
