# vectorfl lane registry and editor surface lock v0

## 1. purpose

`Lane Runs`만으로는 충분하지 않다.

VectorFL Paper는
- top fixed
- middle pluggable
- bottom fixed

모델을 표면에서도 읽을 수 있어야 한다.

그러므로 `lane comparison page`와 별도로
- lane registry page
- lane detail page
- lane editor page

가 필요하다.

## 2. fixed boundary

lane surface에서 바꿀 수 있는 것:
- lane name
- provider/model
- role md
- task md
- caution md
- output schema
- timeout
- budget
- enabled flag
- notes

lane surface에서 바꾸면 안 되는 것:
- top final judgment ownership
- current-reading authority
- governance final authority
- bottom fixed pipeline order

## 3. required page classes

### lanes
- middle-layer registry page
- lane list
- enabled/disabled
- provider/model
- status
- detail link
- edit link

### lane detail
- one lane as operable execution object
- role/task/caution summary
- timeout/budget/schema
- notes

### lane editor
- editable configuration shell
- role/task/caution blocks
- clone/disable/remove affordance
- boundary rule note

## 4. relation to lane runs

`Lane Runs`는
같은 case에 대해 lane 결과를 비교하는 page다.

`Lanes`는
lane 자체를 등록/수정/관리하는 page다.

둘은 섞이면 안 된다.

## 5. visible language

주 표면은 product-readable language를 사용한다.

- Lanes
- Lane Detail
- Lane Editor
- Provider / Model
- Enabled
- Budget
- Output Schema

내부 semantics인 `top fixed / middle pluggable / bottom fixed`는
보조 note나 explainer에서만 드러낸다.

## 6. why this matters

이 page class가 없으면
middle lane은 말로만 pluggable이고,
실제로는 수정 불가능한 고정 panel처럼 보이게 된다.

VectorFL Paper는
기관뿐 아니라 lane도 operable surface로 가져야 한다.
