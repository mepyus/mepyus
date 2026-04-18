# vectorfl operable page class reset v0

이 문서는 지금까지의 `그래프뷰 변형` drift를 멈추고,  
Paperclip native page class를 기준으로 `VectorFL 운영화면`을 다시 시작하기 위한 reset 문서다.

목적은 Paperclip를 베끼는 것이 아니라,  
`operable screen grammar`를 가져와 VectorFL의 current-reading / governance / trace / organ 원칙 위에 다시 얹는 것이다.

## 1. reset verdict

지금까지의 문제는 `VectorFL 원칙`이 약해서가 아니라,  
그 원칙을 실제로 운용 가능한 page class로 풀어내지 못했다는 데 있다.

따라서 다음 단계의 기준은 아래처럼 잠근다.

- 기존 `graph-like shell`은 중심 기준으로 쓰지 않는다
- Paperclip native line의 `list / detail / inspector / operable organ page / audit page`를 먼저 기준면으로 삼는다
- 그 위에만 VectorFL core object와 organ 흐름을 다시 얹는다

## 2. what is being reset

리셋 대상은 시각 톤이 아니라 page class다.

즉 아래를 리셋한다.

- `Current Reading`을 generic center panel처럼 읽는 방식
- `Cases / Queue`를 list page가 아니라 카드/preview 모음처럼 읽는 방식
- `Organ Detail`을 단순 drill-in panel처럼 읽는 방식
- `History / Trace`를 generic log strip처럼 읽는 방식

반대로 아래는 유지한다.

- current-reading first
- governance first-class
- trace / memory retention
- ontology non-import rule
- core canonical ownership

## 3. native page classes to inherit from paperclip

Paperclip native reading 기준으로 우선 계승해야 하는 page class는 아래다.

### 3-1. work list page class

native reference:

- `Issues`
- `Inbox`
- `Routines`

구조 핵심:

- 목록면이 중심이다
- row 단위 선택과 상태 읽기가 가능하다
- filter/group/search가 같은 면 안에서 작동한다
- “현재 무엇을 처리해야 하는가”가 먼저 보인다

### 3-2. work detail page class

native reference:

- `IssueDetail`

구조 핵심:

- 하나의 작업 단위가 중심 detail로 열린다
- comments / runs / approvals / activity / documents가 상세면 안에서 만난다
- 실제 수행과 재배정이 detail 안에서 일어난다

### 3-3. right-side inspector class

native reference:

- `IssueProperties`
- `PropertiesPanel`

구조 핵심:

- 우측 inspector는 보조 정보판이 아니라 수정 가능한 control surface다
- assignee, labels, project, metadata 같은 조정이 이 면에서 일어난다

### 3-4. operable organ detail class

native reference:

- `AgentDetail`

구조 핵심:

- 기관은 보이는 대상이 아니라 수정 가능한 대상이다
- instructions / configuration / skills / runs / budget 같은 편집면이 있다
- dirty state와 save/cancel이 분명하다

### 3-5. audit page class

native reference:

- `Activity`

구조 핵심:

- append-only history가 list/divider 기반으로 보인다
- 현재 상태와 연결되지만, 별도 audit page class를 가진다

### 3-6. spatial page class

native reference:

- `OrgChart`

구조 핵심:

- 관계를 보여줄 때만 별도의 공간형 면을 쓴다
- 중심 work/detail 흐름과 섞지 않는다

## 4. vectorfl page classes after reset

VectorFL 쪽은 아래처럼 다시 잡는 것이 맞다.

### 4-1. cases work list page

기존 이름:

- `Cases / Queue`

reset reading:

- 이것은 단순 queue preview가 아니라 `work list page`다
- case row가 중심이다
- current organ, current lane, restriction, next-hop candidate가 row 안에서 읽혀야 한다
- search/filter/group가 이 page의 핵심 기능이어야 한다

즉 Paperclip의 `Issues/Inbox`에 가장 가까운 class로 다시 잡는다.

### 4-2. case work detail page

기존 이름:

- `Current Reading`

reset reading:

- 이것은 center console만이 아니라 `case work detail page`다
- current-reading body가 중심이지만, 그 case의 trace, governance, linked supporting units가 상세면 안에서 묶여야 한다
- “지금 무엇을 읽고 있는가”와 함께 “왜 여기 머무는가 / 다음 어디로 갈 수 있는가”가 같은 page 안에 보여야 한다

즉 Paperclip의 `IssueDetail` class를 참조하되 의미는 current-reading 쪽으로 재소유한다.

### 4-3. case inspector page region

기존 이름:

- `governance side`
- `supporting context side`

reset reading:

- 이것은 단순 side note가 아니라 `right-side inspector`다
- governance restriction
- linked source/context
- next-hop candidate
- release condition
- selected packet/anchor

같은 조정 정보가 이 면에 들어와야 한다

즉 Paperclip의 `IssueProperties` class를 참조하되, 내용은 VectorFL governance/context로 바꾼다.

### 4-4. organ management list page

새로 필요한 page class:

- `Organs`

reset reading:

- 기관 목록은 별도 page가 필요하다
- 현재 활성 기관, 기관 종류, 현재 책임 수, caution 상태가 row로 보여야 한다
- 새 기관 추가나 비활성/활성 같은 관리 entry가 여기 있어야 한다

이건 지금까지 가장 부족했던 class다.

### 4-5. operable organ detail page

새로 필요한 page class:

- `Organ Detail`

reset reading:

- 기관 상세는 단순 status drill-in이 아니다
- ROLE / HANDOFF / CAUTION / RETURN md를 보고 수정하는 면이어야 한다
- 기관별 instruction bundle, accepted handoff shape, recent returns, caution profile을 함께 다뤄야 한다
- save/cancel/dirty state가 있어야 한다

즉 Paperclip `AgentDetail`에 가장 가까운 class를 VectorFL 뜻으로 다시 만드는 것이다.

### 4-6. trace audit page

기존 이름:

- `History / Trace`

reset reading:

- 이것은 단순 preview strip이 아니라 별도 `audit page`다
- trace row를 따라 들어가고, residue/reentry/decision anchor를 회고적으로 볼 수 있어야 한다

### 4-7. inputs intake page

기존 이름:

- `Inputs / Intake`

reset reading:

- 이것은 전단 확인면이다
- 다만 generic source preview가 아니라, 어떤 source가 어떤 case와 연결되고 어떤 next lane hint를 내는지까지 보이는 operable intake page여야 한다

## 5. page priority after reset

리셋 이후 우선순위는 아래처럼 잡는다.

1. `Cases` as work list page
2. `Case Detail` as current-reading work detail page
3. `Case Inspector` as right-side inspector
4. `Organ Detail` as operable organ page
5. `Trace Audit`
6. `Inputs Intake`
7. `Spatial Flow` later

즉 예전처럼 `Current Reading` 단독 중심에서 출발하지 않고,  
`work list -> work detail -> inspector -> operable organ detail` 구조를 먼저 세운다.

## 6. what this changes in our previous locks

### 6-1. what stays valid

- `current-reading first`는 여전히 valid하다
- 하지만 그것은 `work detail page의 중심 내용`으로 읽혀야지, 전체 제품 구조를 혼자 대체하면 안 된다

### 6-2. what needs reinterpretation

- `Cases / Queue`는 `entry shell`보다 `work list page`로 재해석해야 한다
- `Organ Detail`은 `contextual drill-in`보다 `operable organ page`로 승격해서 봐야 한다
- `History / Trace`는 preview strip보다 `audit class`로 더 강하게 분리해야 한다

### 6-3. what was missing

아래 class는 거의 비어 있었다.

- 기관 목록/관리 page
- 기관 수정 page
- case inspector as editable control surface

## 7. minimal surface obligations

리셋 이후 각 page class는 최소 아래를 가져야 한다.

### cases work list

- row selection
- current organ visibility
- restriction badge
- next-hop hint
- linked detail entry

### case work detail

- current-reading body
- progression + responsibility
- trace-coupled explanation
- linked runs/returns/history

### right-side inspector

- governance restriction
- release condition
- linked source/context
- next-hop candidate
- editable or selectable control anchors

### organ detail

- role md
- handoff md
- caution md
- return md
- save/cancel/dirty state

### trace audit

- append-only rows
- detail drill-in
- origin/supporting refs

## 8. what must not happen again

다시 아래로 돌아가면 안 된다.

- graph-like center panel을 제품 구조처럼 착각하는 것
- operable page class 없이 current-reading만 크게 키우는 것
- organ을 “보여주기만 하는 대상”으로 두는 것
- inspector를 단순 설명 panel로 두는 것
- list/detail/audit/config class를 섞어버리는 것

## 9. final reset sentence

다음 단계의 기준은 아래 문장으로 잠근다.

`VectorFL 운영화면은 더 이상 graph-like shell을 다듬는 방향으로 가지 않고, Paperclip native line에서 확인된 work list, work detail, right-side inspector, operable organ detail, audit page class를 먼저 기준면으로 삼은 뒤 그 위에 current-reading/governance/trace/organ 원칙을 다시 얹는 방향으로 재시작한다.`
