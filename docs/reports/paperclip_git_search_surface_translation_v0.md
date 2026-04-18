# Paperclip Git Search Surface Translation v0

## 목적

이 문서는 `references/git_search/paperclip-master`를 다시 읽고,
`VectorFL Paper`가 왜 단순 결과 뷰어를 넘어 실제 운영면으로 바뀌어야 하는지,
그리고 어떤 page grammar를 차용해야 하는지 기록하기 위한 문서다.

핵심 판단:

`Paperclip`의 힘은 검은 테마가 아니라,
`목록 -> 상세 -> 설정 -> 승인 -> 활동 -> 회신`
으로 이어지는 실제 운용 흐름에 있다.

따라서 `VectorFL Paper`도
`읽기 결과 표시`만이 아니라
`선택 / 설정 / 배정 / 승인 / 회신 / 재개방`
을 할 수 있는 구조로 올라가야 한다.

## 직접 다시 본 주요 파일

- `ui/src/pages/Dashboard.tsx`
- `ui/src/pages/Issues.tsx`
- `ui/src/pages/IssueDetail.tsx`
- `ui/src/pages/Approvals.tsx`
- `ui/src/pages/Inbox.tsx`
- `ui/src/pages/NewAgent.tsx`
- `ui/src/components/OnboardingWizard.tsx`
- `ui/src/components/AgentConfigForm.tsx`
- `ui/src/components/ApprovalCard.tsx`
- `ui/src/pages/AdapterManager.tsx`

## 다시 확인된 핵심 문법

### 1. Dashboard는 overview가 아니라 board operator 면이다

`Dashboard.tsx`는 metric card, active agents, recent activity, recent issues를 한데 모아
지금 어디에 개입해야 하는지를 먼저 보여준다.

VectorFL 번역:

- `운영 보드`는 단순 case list가 아니라
  `decision queue`, `active teams / cli`, `latest updates`가 먼저 보여야 한다.

### 2. Issues는 work unit 목록이다

`Issues.tsx`는 목록을 필터링하고,
live issue 상태를 반영하며,
상세로 자연스럽게 넘어가게 만든다.

VectorFL 번역:

- `case list`는 읽은 결과 나열이 아니라
  지금 감독해야 하는 `current case / work packet` 목록이어야 한다.

### 3. IssueDetail은 한 work unit의 중심 workspace다

`IssueDetail.tsx`는
comment thread,
properties,
documents,
workspace,
live run,
activity
를 한 unit 안에 모은다.

VectorFL 번역:

- `현재 케이스`는 source/line/bundle만이 아니라
  `next action`, `worker request`, `governance`, `return path`까지 묶는 중심면이어야 한다.

### 4. Approvals는 로그가 아니라 decision gate다

`Approvals.tsx`는 pending/all을 나누고,
approve/reject action을 바로 수행하게 한다.

VectorFL 번역:

- `이슈 / 감사`는 append-only trace만 보여주면 안 되고,
  `approve / hold / reopen` 판단면을 함께 가져야 한다.

### 5. Inbox는 회신과 재개방의 작업면이다

`Inbox.tsx`는
issue,
approval,
failed run,
alert를 한데 모으고,
archive/reopen/selection 같은 후속 행위를 엮는다.

VectorFL 번역:

- `결과 회신`은 결과 보관함이 아니라
  `comment / reopen / redirect / approve`를 다시 거는 귀속면이어야 한다.

### 6. Onboarding / NewAgent는 단계형 진입면이다

`OnboardingWizard.tsx`는

- company
- agent
- task
- launch

를 단계적으로 밟게 한다.

`NewAgent.tsx`는

- role
- reports to
- adapter type
- adapter config
- runtime heartbeat

를 실제로 고르게 한다.

VectorFL 번역:

- `입력 / 외부 비교`는 단순 search planning이 아니라
  `scenario -> material bundle review -> team -> cli -> task -> launch`
  흐름으로 자라야 한다.
- launch 전에는 반드시
  `source confirmation`, `env check`, `hold / preview / launch`
  같은 판단 블록이 따로 보여야 한다.

### 7. AgentConfigForm은 실제 운용 설정면이다

`AgentConfigForm.tsx`는

- adapter type
- provider / model
- environment
- role / runtime
- instructions file
- dirty tracking
- approvals / sandbox / runtime section

을 함께 다룬다.

VectorFL 번역:

- `CLI / 어댑터`는 단순 lane 비교면이 아니라
  `provider`, `model`, `owning cli`, `payload policy`, `return route`, `contract`
  를 같이 다루는 설정면이어야 한다.
- 거기에 더해
  `adapter type`, `command`, `args`, `working directory`, `env status`,
  `approvals policy`, `sandbox policy`, `search policy`
  를 form처럼 읽을 수 있어야 한다.

### 8. AdapterManager는 adapter registry 면이다

`AdapterManager.tsx`는

- adapter 설치
- external / built-in 구분
- enable/disable
- reload
- reinstall

같은 실제 관리 행위를 제공한다.

VectorFL 번역:

- `팀 계약 / 설정`과 `CLI / 어댑터`는
  단순 설명 페이지가 아니라
  `등록 / 연결 / 숨김 / 확장 / 교체`
  가 가능한 registry seam으로 가야 한다.

### 9. ApprovalCard는 decision gate의 최소 단위다

`ApprovalCard.tsx`는

- 요청 label
- requester
- status
- payload summary
- decision note
- approve / reject
- detail 보기

를 카드 하나에 넣는다.

VectorFL 번역:

- `이슈 / 감사`는 trace 아래에 승인 텍스트를 붙이는 방식으로는 부족하다.
- 최소한
  `무슨 요청인가`, `누가 요청했는가`, `왜 멈췄는가`, `지금 승인 / 보류 / 재개방 중 무엇을 해야 하는가`
  를 카드 단위로 보여줘야 한다.

## VectorFL에 바로 옮겨야 하는 구조적 결론

### A. 보여주기보다 행동을 먼저 둔다

각 핵심 페이지는 최소 아래 행동 중 일부를 가져야 한다.

- assign
- hold
- launch
- export
- approve
- reject
- reopen
- redirect

### B. 팀과 CLI는 별도 라벨이 아니라 연결 구조다

한 팀을 표시할 때 최소 아래가 함께 보여야 한다.

- lens
- managing cli
- handoff target
- paired external team
- human report format

한 CLI lane을 표시할 때 최소 아래가 함께 보여야 한다.

- provider
- model
- owning cli
- managed teams
- payload policy
- return route

### C. 이슈 loop가 중심이다

`운영 보드 -> 현재 케이스 -> 업무 배정 -> 이슈 / 감사 -> 결과 회신`
는 하나의 루프로 읽혀야 한다.

## 이번 반영 기준

이 재독해를 바탕으로 `VectorFL Paper` 기존 surface에 다음을 더 강하게 반영한다.

- `decision queue`
- `active teams / cli`
- `latest updates`
- `staged intake setup`
- `scenario entry`
- `material bundle review`
- `team assignment candidates`
- `cli assignment candidates`
- `adapter manager`
- `runtime policy form`
- `approval gate`
- `approval cards`
- `comment / reopen / redirect / approve loop`
- `setup flow` for teams and cli adapters

## 최종 문장

`Paperclip`에서 적극적으로 가져와야 하는 것은
UI 외형이 아니라,
사용자가 실제로 설정하고, 배정하고, 승인하고, 회신을 처리할 수 있게 만드는
운용 흐름과 page grammar다.
