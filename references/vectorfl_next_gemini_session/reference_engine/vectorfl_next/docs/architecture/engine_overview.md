# Engine Overview

`vectorfl_next`는 stage 엔진이 아니라 formation engine이다.
그리고 point-first 엔진이 아니라 `space-first` 엔진이다.

코어 흐름은 아래 순서만 허용한다.

`material -> trace -> point_seed -> space_cell -> local_space -> bridge_trace`

핵심 원칙:

- `material`은 raw payload를 유지하는 불변 입력 단위다.
- `trace`는 확정 edge가 아니라 약한 근거를 담는 기록이다.
- `point_seed`는 최종 point가 아니라 임시 응결핵이다.
- `space_cell`은 point의 약한 버전이 아니라 최소 반응 공간이다.
- `local_space`는 여러 cell의 반복 유지 패턴에서만 형성된다.
- `bridge_trace`는 merge가 아니라 관계 가능성의 흔적이다.

추가 고정 원칙:

- 공간을 먼저 세우고 그 안에서 반응을 본다.
- 점은 코어를 닫는 중심 단위가 아니라 나중에 공간을 관찰하는 보조 수단이다.
- 구현이 애매할 때는 점을 더 만들지 말고 cell과 local space 반응 규칙을 먼저 분명히 한다.
- 입력은 먼저 `material`로 받고, 종류보다 formation role을 늦게 읽는다.

현재 1차 스캐폴드는 알고리즘 완성 대신 아래 경계만 구현한다.

- material ingest
- trace register
- pressure profile creation
- point seed candidate creation
- space cell candidate creation
- local space formation
- bridge trace registration
