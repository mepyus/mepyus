# VectorFL Page App Shell Runtime Brief v0

이 문서는 현재까지 만든 `Unified Shell`과 `Route-Aware Surface Set`을  
실제 `VectorFL Page shell`처럼 읽히는 정적 runtime shell 세트로 내릴 때의 기준을 잠근다.

목적은 demo 산출물을 넘어서,
로컬에서 직접 열어보며 navigation, breadcrumb, primary surface, contextual panel의 관계를
한 프로그램 흐름처럼 검토할 수 있게 만드는 것이다.

## 1. Core Sentence

VectorFL Page app shell은  
각 primary surface state를 개별 shell page로 갖되,
공통 sidebar/topbar/breadcrumb rhythm과
동일한 contextual organ detail panel 구조를 유지하는 runtime shell 세트여야 한다.

## 2. Required Runtime Traits

- `current-reading first` primary navigation
- shared topbar / breadcrumb rhythm
- stable contextual panel zone
- local cross-links between primary surfaces
- no Paperclip ontology wording import

## 3. What This Shell Is

- local runtime inspection shell
- VectorFL Paper prototype carrier
- surface/state validation shell

## 4. What This Shell Is Not

- full live integration
- canonical backend runtime
- orchestration engine

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page app shell은 route-aware primary surfaces를 공통 frame 안에서 로컬 inspection 가능하게 보여주는 정적 runtime shell 세트로 두고, Current Reading 중심성과 contextual organ detail 구조를 전 페이지에서 일관되게 유지해야 한다.`
