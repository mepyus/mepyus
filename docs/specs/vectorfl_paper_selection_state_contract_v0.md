# VectorFL Paper Selection State Contract v0

## purpose

이 문서는 `VectorFL Paper proper`에서
선택 상태가 어떻게 보이고
어떤 화면들이 그 상태를 같이 공유해야 하는지 잠근다.

## role

선택 상태는 단순 highlight가 아니다.
이것은 현재 loop에서

- 어떤 line을 중심으로 읽고 있는가
- 어떤 bundle이 근거로 묶였는가
- 어떤 compare target을 들고 있는가

를 고정하는 shared operating object다.

## required fields

- selected_case
- selected_line
- selected_bundle
- compare_target
- current_worker_target
- current_return_slot

## propagation rule

이 객체는 최소 아래 면에서 같은 값으로 읽혀야 한다.

- case detail
- inspector
- cell / worker panel
- trace / governance

즉 한 화면의 선택이 다른 화면의 payload basis와 gate reading까지 같이 움직이게 해야 한다.

## one-line lock

선택 상태는 UI 부속물이 아니라
현재 case의 읽기, 실행, 귀속을 묶는 shared operating object다.
