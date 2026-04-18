# VectorFL Programs / Connections Shell Rewrite Brief v0

이 문서는 Paperclip의 연결/부가 panel 감각을 참고하되,  
`VectorFL Page`에서 `Programs / Connections` 면을 어떤 의미로 다시 소유할지 짧게 고정한다.

목적은 외부 프로그램을 작업 ontology로 끌어들이는 것이 아니라,  
`VectorFL core와 외부 프로그램 사이의 접속 상태와 제한 조건`을 읽는 면으로 두는 것이다.

## 1. Core Sentence

`Programs / Connections`는 외부 프로그램을 지배하는 control console이 아니라,  
현재 case와 lane이 어떤 프로그램 표면과 연결되어 있고 어디까지 읽기/요청만 가능한지를 보여주는 접속면이다.

## 2. What To Reuse From Paperclip

- side panel composition
- linked object summary 감각
- compact status card rhythm
- detail page 주변부에 붙는 secondary panel 구조

즉 가져오는 것은 `connection panel composition`이지,
program/company/workspace ontology가 아니다.

## 3. What To Rewrite For VectorFL

- linked issue/project -> `linked program refs`
- workspace/status card -> `connection state / request boundary`
- operator action affordance -> `request preview / restriction note`
- system ownership wording -> `program remains SSOT`

즉 이 면의 핵심은
`무엇을 바꿀 수 있는가`보다
`무엇이 연결돼 있고 어디까지 읽기/요청만 가능한가`다.

## 4. Core Sections

현재 단계에서 `Programs / Connections` 면은 아래 section만 우선 가진다.

### 4-1. linked program list

- 현재 case와 연결된 프로그램 ref 목록

### 4-2. connection status

- 연결 상태
- 최근 읽은 surface 또는 input/output ref

### 4-3. action request preview

- 실제 실행이 아니라 request 또는 next request 초안 수준만 보여준다

### 4-4. governance restriction note

- observer-only
- promotion forbidden
- direct action hold
같은 제한을 연결면에서도 숨기지 않는다

## 5. What It Must Not Drift Into

- program control dashboard
- live orchestrator
- bidirectional execution console
- external SSOT replacement

즉 `Programs / Connections`는 외부 프로그램을 대신 운용하는 곳이 아니라,
`읽기 / 요청 / 제한 경계`를 보이게 하는 면이다.

## 6. First Rewrite Scope

첫 rewrite에서는 아래까지만 잡는다.

- linked program ref
- connection state
- current linked surface
- request preview text
- governance restriction summary

아직 잠그지 않는 것:

- live write-back
- transactional action queue
- bidirectional sync controls
- external program deep inspector

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 Programs / Connections 면은 Paperclip의 secondary panel 감각만 참고하고, 실제 의미는 linked program, current connection state, request preview, governance restriction을 보여주는 접속 경계면으로 다시 소유한다.`
