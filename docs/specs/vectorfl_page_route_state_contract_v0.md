# VectorFL Page Route State Contract v0

이 문서는 `VectorFL Page` mock이  
여러 분리된 화면 파일이 아니라
`current-reading first` route state로 읽히게 만드는 최소 계약을 잠근다.

목적은 primary surface와 contextual drill-in panel의 관계를 분명히 해서,
organ detail이 primary nav로 drift하지 않게 하는 것이다.

## 1. Core Sentence

VectorFL Page의 route state는  
`Current Reading`을 active primary surface로 두고,
`Cases / Queue`, `Inputs / Intake`, `History / Trace`, `Programs / Connections`는 support surface로,
`Organ Detail`은 active contextual panel로 읽는 구조가 맞다.

## 2. Minimum Route State Fields

- `active_primary_surface`
- `active_case_ref`
- `active_contextual_panel`
- `contextual_entry_targets`
- `route_note`

## 3. Meaning Rule

- primary surface는 case 중심 읽기를 유지한다
- contextual panel은 현재 책임 기관 또는 next candidate 기관을 더 깊게 읽게 한다
- contextual panel이 active여도 semantic center는 여전히 current-reading에 남는다

## 4. What Must Not Happen

- organ detail이 top-level primary route처럼 drift하는 것
- queue가 semantic center처럼 보이는 것
- history/trace가 generic activity feed route가 되는 것

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 route state는 Current Reading을 중심 primary surface로 유지하고, Organ Detail은 current responsibility 또는 progression candidate에서 열리는 contextual panel state로만 다루는 것이 맞다.`
