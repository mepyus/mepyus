# VectorFL Page Route Wiring Contract v0

이 문서는 `VectorFL Page` route-aware shell에서  
primary surface state, nav active state, breadcrumb, contextual panel entry가
어떻게 함께 맞물리는지 잠근다.

목적은 페이지 전환이 semantic drift 없이 보이게 하고,
`current-reading first` 기준이 route wiring에서도 유지되게 하는 것이다.

## 1. Core Sentence

VectorFL Page의 route wiring은
`active_primary_surface`가 어떤 면인지 분명히 보여주고,
그에 맞는 nav active item과 breadcrumb를 맞춘 다음,
필요하면 contextual panel entry를 같은 route state 안에 덧붙이는 구조여야 한다.

## 2. Required Wiring Pieces

- `active_primary_surface`
- `active_nav_key`
- `breadcrumb_chain`
- `contextual_panel_entry`
- `carried_refs`

## 3. Wiring Meaning Rule

- nav는 현재 어떤 primary surface를 보고 있는지 보여준다
- breadcrumb는 현재 page state와 case context를 압축해서 보여준다
- contextual panel은 current-reading 또는 candidate drill-in을 열되, primary surface를 대체하지 않는다

## 4. What Must Stay True

- `Current Reading`은 canonical center다
- 다른 primary surface가 active여도 current-reading 의미축은 남는다
- contextual panel은 항상 부가 drill-in이다

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 route wiring은 active primary surface, active nav key, breadcrumb, contextual panel entry를 함께 보여주되, contextual panel이 primary route를 대체하지 않도록 하고 current-reading-first 의미축을 계속 유지해야 한다.`
