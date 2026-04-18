# VectorFL Cases Queue Shell Rewrite Brief v0

이 문서는 Paperclip의 `Issues / IssuesList / IssueRow` 계열을  
VectorFL Page의 `Cases / Queue` shell로 다시 쓰기 위한 rewrite brief를 잠근다.  
목적은 list/queue 감각은 참고하되, issue board 의미를 버리고 `current-reading 진입 queue`로 재소유하는 것이다.

## 1. 목적

Current Reading이 중심 console이라면,
Cases / Queue는 그 중심면으로 들어가는 대표 진입면이어야 한다.

따라서 이 문서는 아래를 잠근다.

- 무엇을 list/queue shell 감각으로 가져올 것인가
- 무엇을 issue 의미에서 case 의미로 바꿀 것인가
- queue row가 어떤 snapshot만 보여줘야 하는가

## 2. Source Frame Reading

참조하는 원본은 아래다.

- [Issues.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Issues.tsx)
- [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)
- [IssueRow.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssueRow.tsx)

이 계열에서 참고할 수 있는 것은 아래다.

- list/queue 진입면 구성
- search / filter / group / sort 감각
- row snapshot 구조
- list vs board 전환 가능성

## 3. Do Not Carry Over

아래는 Cases / Queue shell로 그대로 가져오지 않는다.

- issue lifecycle naming
- assignee / participant 중심 의미
- issue identifier 중심성
- inbox/archive action 의미
- project/goal 종속 구조

즉 `Issue`의 세계관은 버리고,
queue/list shell 감각만 가져온다.

## 4. Cases / Queue Target Structure

첫 Cases / Queue shell은 아래 다섯 묶음으로 다시 쓴다.

### 4-1. Search / Filter Header

- 의미:
  - case를 빠르게 좁히는 진입 헤더
  - search / group / sort / filter의 최소 조합

### 4-2. Case Queue List

- 의미:
  - 현재 살아 있는 case들의 진입 목록
  - current-reading으로 들어가기 전의 얕은 snapshot 목록

### 4-3. Case Queue Row

- 의미:
  - case identity
  - current lane snapshot
  - governance snapshot
  - current surface headline preview
  - linked program 존재
  - trace freshness

### 4-4. Optional Grouped Queue

- 의미:
  - lane, governance, 또는 case class 기준으로 grouped reading을 지원할 수 있는 구조
- note:
  - first build에서 꼭 board mode까지 필요하지는 않다

### 4-5. Entry Action

- 의미:
  - case를 열어 Current Reading으로 진입하는 기본 action

## 5. Row Ownership Mapping

### identity

- source of truth:
  - `Case Record`
- shell meaning:
  - case id / kind / status

### lane snapshot

- source of truth:
  - `Lane State Record`
- shell meaning:
  - current lane / lane status / next hop candidate 존재감

### governance snapshot

- source of truth:
  - `Governance Record`
- shell meaning:
  - hold / restriction / release pending badge

### current surface preview

- source of truth:
  - `Surface Packet`
- shell meaning:
  - headline 수준의 current-reading preview

### trace freshness

- source of truth:
  - `Trace / Memory Record` refs
- shell meaning:
  - recent update / trace presence

## 6. Queue Rules

### rule 1. queue is entry, not meaning source

- row는 case 의미를 다 말하려 하지 않는다
- row는 current-reading으로 진입하기 위한 얕은 snapshot만 보여준다

### rule 2. governance stays visible

- hold / restriction / release pending은 queue에서도 가려지면 안 된다

### rule 3. preview stays shallow

- headline preview는 보여주되 current-reading body를 대체하지 않는다

### rule 4. issue worldview removed

- identifier, assignee, inbox/archive action 중심 구조는 Cases / Queue에서 canonical이 아니다

### rule 5. queue may group, but not reinterpret

- lane/governance 기준 group은 가능하나 canonical case state를 다시 해석하지 않는다

## 7. First Rewrite Scope

첫 rewrite에서는 아래만 포함하면 충분하다.

- search / filter header
- case queue list
- case queue row
- current-reading entry action

아래는 뒤로 미룬다.

- board mode
- drag / assignment interaction
- archive / inbox semantics
- multi-case compare
- project/goal cross-links

## 8. First Mock Fit

이 rewrite brief는 아래 문서와 직접 연결된다.

- [vectorfl_cases_queue_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_cases_queue_adapter_contract_v0.md)
- [vectorfl_paper_shell_mapping_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_paper_shell_mapping_v0.md)

즉 first queue shell은 queue item view model을 실제 entry surface로 보이게 하는 단계다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Cases / Queue shell은 Paperclip IssuesList의 list/queue composition을 참고하되, issue lifecycle 의미를 버리고 case identity, lane snapshot, governance snapshot, current surface preview, trace freshness만 보이는 current-reading entry queue로 다시 써야 한다.`
