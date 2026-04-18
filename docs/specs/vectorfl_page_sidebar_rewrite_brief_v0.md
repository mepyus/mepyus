# VectorFL Page Sidebar Rewrite Brief v0

이 문서는 Paperclip의 `Sidebar`를 참고하되,
`VectorFL Page`에서 left navigation을 어떤 의미로 다시 소유할지 짧게 잠근다.

목적은 Paperclip의 issue/company/workspace worldview를 버리고,
`current-reading first` 기준의 개인용 VectorFL navigation을 실제 sidebar semantics로 내리는 것이다.

## 1. Core Sentence

VectorFL Page의 sidebar는
`무엇을 관리하는가`를 나열하는 메뉴가 아니라,
`지금 무엇을 읽고 어디로 drill-in 할 수 있는가`
를 current-reading 중심으로 정리하는 navigation이어야 한다.

## 2. Primary Nav Group

현재 단계에서 1차 nav는 아래 묶음으로 읽는 것이 맞다.

- `Current Reading`
- `Cases / Queue`
- `Inputs / Intake`
- `History / Trace`
- `Programs / Connections`

즉 Paperclip의

- Dashboard
- Inbox
- Issues
- Goals
- Org
- Skills
- Costs
- Activity

를 그대로 옮기지 않는다.

## 3. Sidebar Meaning Rule

각 nav item은 `관리 대상`보다 `읽기 목적`을 나타내야 한다.

예:

- `Current Reading`
  - 지금 가장 먼저 읽어야 할 중심면
- `Cases / Queue`
  - current-reading으로 들어가기 전 case progression entry
- `Inputs / Intake`
  - 재료 품질과 weak/fallback를 보는 전단면
- `History / Trace`
  - residue/reentry를 회고하는 면
- `Programs / Connections`
  - 외부 프로그램과의 경계면

## 4. What Stays From Paperclip

- sectioned vertical nav rhythm
- top identity slot
- active item emphasis
- lightweight badge/chip affordance
- optional lower plugin/panel slot 감각

즉 frame rhythm은 유지할 수 있다.

## 5. What Must Be Rewritten

- nav labels
- icon meaning
- grouping logic
- company/org wording
- work/goals/issues wording

즉 sidebar는 거의 전면 재작성 대상이다.

## 6. Relation To Organ Detail

현재 단계에서 `Organ Detail`은 primary nav로 두지 않는다.

이유:

- organ detail은 중심면이 아니라 drill-in 보조면이다
- current-reading에서 진입하는 것이 더 자연스럽다

즉 organ detail은 sidebar top-level보다
contextual entry가 맞다.

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 sidebar는 Paperclip의 세로 nav rhythm은 참고하되, 실제 의미는 Current Reading, Cases/Queue, Inputs/Intake, History/Trace, Programs/Connections를 current-reading-first 읽기 목적 기준으로 다시 그룹화한 전면 재작성 navigation이어야 한다.`
