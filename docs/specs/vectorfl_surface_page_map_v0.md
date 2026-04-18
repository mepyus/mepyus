# vectorfl surface page map v0

이 문서는 `surface-only paperclip adoption` 기준 위에서  
VectorFL canonical object와 surface page class를 어떻게 매핑할지 짧게 고정한다.

목적은 Paperclip ontology를 들이지 않고도,  
어떤 canonical object가 어떤 운영화면 class에서 다뤄져야 하는지 분명히 하는 것이다.

## 1. core sentence

VectorFL surface는 `canonical object -> page class -> operator action` 순서로 읽어야 한다.

즉:

- 먼저 core object가 있다
- 그 object는 알맞은 page class에 올라간다
- 그 page에서만 operator action이 허용된다

## 2. page map

### 2-1. cases page

- page class:
  - `work list page`
- native paperclip reference:
  - `Issues`
  - `Inbox`
- primary canonical objects:
  - `Case Record`
  - `Lane State Record`
  - `Governance Record`
  - `Surface Packet` preview
- operator can do:
  - case 선택
  - current organ/lane 확인
  - restriction 상태 확인
  - next-hop candidate 확인
  - case detail로 진입

### 2-2. case detail page

- page class:
  - `work detail page`
- native paperclip reference:
  - `IssueDetail`
- primary canonical objects:
  - `Surface Packet`
  - `Lane State Record`
  - `Governance Record`
  - `Trace / Memory Record` preview
  - linked intake refs
- operator can do:
  - current-reading 읽기
  - current responsibility 확인
  - progression 확인
  - trace-coupled explanation 확인
  - case inspector 열기

### 2-3. case inspector

- page class:
  - `right-side inspector`
- native paperclip reference:
  - `IssueProperties`
  - `PropertiesPanel`
- primary canonical objects:
  - `Governance Record`
  - `Lane State Record`
  - linked source/context refs
  - selected intake packet refs
- operator can do:
  - restriction 확인
  - release condition 확인
  - next-hop candidate 확인
  - selected anchor/context 확인
  - case-level control adjustment entry

### 2-4. inputs intake page

- page class:
  - `intake work page`
- native paperclip reference:
  - `Inbox` 일부
  - work intake list grammar
- primary canonical objects:
  - `Source Registry Entry`
  - `Intake Block`
  - `Intake Packet`
  - `Intake Status Record`
- operator can do:
  - source/context 확인
  - block/split 확인
  - weakness/fallback 확인
  - linked case 확인
  - organ handoff readiness 확인

### 2-5. organs page

- page class:
  - `organ management list page`
- native paperclip reference:
  - `Agents`
- primary canonical objects:
  - organ registry or organ refs
  - current responsibility summary
  - caution summary
  - recent return summary
- operator can do:
  - 기관 선택
  - 활성/비활성 확인
  - 역할 범위 확인
  - 기관 상세 진입
  - 신규 기관 추가 entry

### 2-6. organ detail page

- page class:
  - `operable organ detail page`
- native paperclip reference:
  - `AgentDetail`
- primary canonical objects:
  - organ instruction bundle refs
  - recent handoff packet examples
  - caution profile
  - recent returns
  - organ continuity refs
- operator can do:
  - ROLE/HANDOFF/CAUTION/RETURN 보기
  - md 수정
  - save/cancel
  - 기관별 recent run/return 확인
  - 연결된 외부 팀/프로그램 설정 entry

### 2-7. trace audit page

- page class:
  - `audit page`
- native paperclip reference:
  - `Activity`
- primary canonical objects:
  - `Trace / Memory Record`
  - governance decision trace refs
  - residue / reentry refs
- operator can do:
  - trace row 목록 보기
  - trace detail drill-in
  - origin / supporting refs 확인

### 2-8. spatial flow page

- page class:
  - `spatial relation page`
- native paperclip reference:
  - `OrgChart`
- primary canonical objects:
  - organ relation refs
  - case-to-organ relation refs
  - flow candidate relation refs
- operator can do:
  - 관계 읽기
  - topology 확인
  - 중심 work/detail page로 되돌아가기

## 3. action boundary rule

각 page class는 보여주기만 하는 면이 아니라, 허용된 operator action 범위를 가진다.

하지만 아래는 그대로 유지한다.

- canonical interpretation decision은 core 소유
- governance final decision은 core 소유
- shell/page는 조정 entry와 표시를 제공하지만 canonical source of truth는 아니다

즉 page가 operable하더라도 ownership rule은 깨지지 않는다.

## 4. minimum first set

현재 가장 먼저 다시 세워야 할 surface set은 아래다.

1. `Cases`
2. `Case Detail`
3. `Case Inspector`
4. `Organs`
5. `Organ Detail`
6. `Trace Audit`

즉 이 여섯 page class가 먼저 operable해져야 한다.

## 5. final map sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL surface는 Cases를 work list page로, Case Detail을 current-reading 중심의 work detail page로, Case Inspector를 governance/source control inspector로, Organs와 Organ Detail을 기관 운용면으로, Trace Audit을 append-only audit page로, Spatial Flow를 관계 page로 두고, 각 page는 VectorFL canonical object를 적응시켜 operator action을 제공하되 canonical ownership은 core에 남긴다.`
