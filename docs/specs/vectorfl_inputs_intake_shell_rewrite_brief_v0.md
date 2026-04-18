# VectorFL Inputs Intake Shell Rewrite Brief v0

이 문서는 Paperclip의 list/detail shell 감각을 참고해  
VectorFL Page의 `Inputs / Intake` 면을 다시 쓰기 위한 rewrite brief를 잠근다.  
목적은 입력기 결과를 operator가 읽을 수 있는 전단 shell로 만들되,  
입력기 canonical 의미를 queue나 current-reading 의미와 섞지 않는 것이다.

## 1. 목적

Inputs / Intake shell은 `Current Reading`의 보조면이면서도,
`Cases / Queue`와는 다른 전단 성격을 가져야 한다.

즉 이 문서는 아래를 잠근다.

- 입력 결과를 어떤 shell 감각으로 보여줄 것인가
- source/context/block/status를 어떻게 읽게 할 것인가
- 어떤 의미는 current-reading으로 넘기고, 어떤 의미는 intake에서만 보여줄 것인가

## 2. Source Frame Reading

참조하는 원본 감각은 아래에서 온다.

- [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)
- [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)
- [PropertiesPanel.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/PropertiesPanel.tsx)

참고할 수 있는 것은 아래다.

- searchable list + detail 진입 감각
- center body + side caution/panel 감각
- 상태와 부가 메타를 분리해 보이는 감각

## 3. Do Not Carry Over

아래는 Inputs / Intake shell로 그대로 가져오지 않는다.

- issue title / identifier 중심 구조
- assignee / participant 중심 메타
- comment thread 중심성
- project / goal 종속 의미

즉 intake shell은 issue detail의 변형이 아니라,
source/context/block/status를 읽는 전단 shell이다.

## 4. Inputs / Intake Target Structure

첫 Inputs / Intake shell은 아래 여섯 section으로 다시 쓴다.

### 4-1. Source Header

- 의미:
  - 어떤 source가 들어왔는가
  - source family / subgroup이 무엇인가
  - source locator가 무엇인가

### 4-2. Context Layer Summary

- 의미:
  - 어떤 context가 붙었는가
  - default context와 matched context가 무엇인가
  - classification과 next-lane hint가 무엇인가

### 4-3. Intake Block Body

- 의미:
  - 어떤 block 단위로 입력이 준비되었는가
  - split reason과 protected region이 무엇인가
  - block을 line으로 환원하지 않은 채 관찰 단위로 보여준다

### 4-4. Weakness / Fallback Card

- 의미:
  - weak intake
  - fallback used
  - re-read needed
  - residue-only readiness

### 4-5. Intake Status Strip

- 의미:
  - source registered
  - context attached
  - classification done
  - split generated
  - downstream ready

### 4-6. Linked Case Preview

- 의미:
  - 이미 case와 연결되어 있으면 그 연결만 얕게 보여준다
  - case 의미 자체를 대체하지는 않는다

## 5. Ownership Mapping

### source header

- source of truth:
  - `Source Registry Entry`
- shell meaning:
  - source identity / family / locator snapshot

### context layer summary

- source of truth:
  - `Intake Packet`
- shell meaning:
  - context / classification / next-lane hint summary

### intake block body

- source of truth:
  - `Intake Block`
- shell meaning:
  - structure-aware intake body

### weakness / fallback card

- source of truth:
  - `Intake Packet`
  - `Intake Status Record`
- shell meaning:
  - caution card

### intake status strip

- source of truth:
  - `Intake Status Record`
- shell meaning:
  - readiness / health strip

### linked case preview

- source of truth:
  - linked `Case Record`
- shell meaning:
  - current-reading으로 넘어갈 수 있는 얕은 preview

## 6. Intake Shell Rules

### rule 1. source/context first

- 입력면의 중심은 source와 context다
- case나 lane이 중심이 되면 안 된다

### rule 2. block is not line

- intake block은 line과 동일시하지 않는다
- structure-aware 준비 단위로 보여준다

### rule 3. weakness stays visible

- weak / fallback / re-read needed는 숨기면 안 된다

### rule 4. next-lane hint is not decision

- hint는 보여줄 수 있지만 canonical lane decision처럼 다루면 안 된다

### rule 5. linked case remains preview

- linked case를 보여줄 수는 있지만, current-reading body를 대신하면 안 된다

## 7. First Rewrite Scope

첫 rewrite에서는 아래만 포함하면 충분하다.

- source header
- context layer summary
- intake block body
- weakness / fallback card
- intake status strip
- linked case preview

아래는 뒤로 미룬다.

- full source browser
- multi-source compare
- edit/reclassify controls
- source registry editing
- block-level compare UX

## 8. Relationship To Other Shells

- `Inputs / Intake`는 재료 진입면이다
- `Cases / Queue`는 case 진입면이다
- `Current Reading`은 중심 console이다

즉 intake shell은 current-reading과 queue 사이를 잇는 전단 확인면으로 읽는다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Inputs / Intake shell은 source, context, intake block, weakness, readiness를 중심으로 보여주는 전단 shell로 다시 써야 하며, next-lane hint와 linked case는 보여줄 수 있어도 canonical lane/case 의미를 대신하지 않는다.`
