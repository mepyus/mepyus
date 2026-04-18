# VectorFL Cases Queue Progression Visibility Brief v0

이 문서는 `Cases / Queue` entry surface에서  
case가 단순 목록으로 보이지 않고 진행 구조를 같이 드러내게 하는 기준을 잠근다.

목적은 queue를 generic case list로 두지 않고,
`current-reading entry + progression preview` 면으로 다시 소유하는 것이다.

## 1. Core Sentence

Cases / Queue는 단순 case row 모음이 아니라,  
각 case가 `지금 어느 lane/organ에 있고, 어떤 restriction이 있으며, current-reading으로 들어가면 어떤 진행 구조를 기대할 수 있는지`
를 미리 보여주는 progression entry surface여야 한다.

## 2. Required Row Fields

현재 단계에서 queue row는 아래를 우선 가져야 한다.

- case identity
- lane snapshot
- current organ snapshot
- governance snapshot
- current surface preview
- trace freshness
- linked program preview

## 3. Why Current Organ Snapshot Matters

queue에서 current organ snapshot이 보이지 않으면,
case는 그냥 상태 카드처럼 읽히기 쉽다.

따라서 최소한 아래가 row 또는 expandable preview에 있어야 한다.

- current organ ref
- current lane ref
- short placement reason

## 4. Why Progression Hint Matters

queue에서 progression hint가 없으면,
다음 기관으로의 흐름이 current-reading 안에만 갇힌다.

따라서 최소한 아래 중 일부는 row에 있어야 한다.

- next hop candidate count
- preferred next candidate
- held candidate existence

## 5. What It Must Not Become

- issue kanban clone
- assignee board
- status-only board

즉 queue는 중심면이 아니라 entry surface지만,
그래도 `진행 구조의 예고편`은 가져야 한다.

## 6. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 Cases / Queue는 case/lane/governance/current surface만 보여주는 목록이 아니라, current organ snapshot과 next-hop hint를 포함해 current-reading으로 들어가기 전 진행 구조를 미리 보이게 하는 progression entry surface여야 한다.`
