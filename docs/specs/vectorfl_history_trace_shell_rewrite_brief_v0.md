# VectorFL History / Trace Shell Rewrite Brief v0

이 문서는 Paperclip의 activity/history 감각을 참고하되,  
`VectorFL Page`에서 `History / Trace` 면을 어떤 의미로 다시 소유할지 짧게 고정한다.

목적은 append-only 흔적을 `활동 로그`가 아니라  
`trace / residue / reentry` 회고면으로 다시 쓰는 것이다.

## 1. Core Sentence

`History / Trace`는 사건 기록을 시간순으로 나열하는 일반 activity 면이 아니라,  
현재 current-reading과 governance를 다시 읽게 하는 append-only 회고면으로 다시 써야 한다.

## 2. What To Reuse From Paperclip

- time-ordered list composition
- row-based history scan rhythm
- selected detail / side reading 감각
- recent-first activity browsing 방식

즉 가져오는 것은 `history frame rhythm`이지,
issue activity ontology가 아니다.

## 3. What To Rewrite For VectorFL

- activity row -> `trace row`
- generic event log -> `residue / reentry / decision trace`
- actor/action wording -> `reading / caution / carry / unresolved edge`
- completion storytelling -> `append-only preservation`

즉 `무슨 일을 했다`보다
`무엇이 남았고 다시 어디로 읽히는가`가 더 중요하다.

## 4. Core Sections

현재 단계에서 `History / Trace` 면은 아래 section만 우선 가진다.

### 4-1. latest trace list

- 최신 trace / residue / reentry hint를 시간순으로 보여준다

### 4-2. residue emphasis

- closure-ready가 아닌 단서
- unresolved edge
- preserve-first bias
를 숨기지 않는다

### 4-3. decision trace anchors

- governance와 연결되는 decision trace anchor를 붙인다

### 4-4. reentry cues

- 다음 reread 또는 next-hop을 다시 여는 단서를 짧게 보여준다

## 5. What It Must Not Drift Into

- generic audit log
- operator chat transcript
- completed task feed
- success-only timeline

즉 `History / Trace`는 예쁜 activity page가 아니라,
current-reading과 governance를 다시 열어주는 회고면이어야 한다.

## 6. First Rewrite Scope

첫 rewrite에서는 아래까지만 잡는다.

- trace kind
- summary
- residue note
- reentry hint
- created_at
- optional decision trace anchor

아직 잠그지 않는 것:

- deep trace filtering
- replay controls
- diff visualizer
- raw event inspector

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 History / Trace 면은 Paperclip의 activity rhythm만 참고하고, 실제 의미는 append-only trace, residue, reentry, decision anchor를 current-reading과 governance에 다시 접속시키는 회고면으로 다시 소유한다.`
