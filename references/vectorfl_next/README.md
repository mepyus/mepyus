# vectorfl_next

`vectorfl_next`는 기존 `vectorfl`를 수정하거나 복제하는 프로젝트가 아니다.

이 저장소의 목적은 아래 코어 순서를 따르는 formation-first engine을 새로 세우는 것이다.

`material -> trace -> point_seed -> space_cell -> local_space -> bridge_trace`

핵심 원칙:

- 입력을 빨리 point나 cluster로 닫지 않는다.
- `space_cell`을 최소 공간 단위로 취급한다.
- `local_space`는 여러 cell의 반복 유지 패턴에서만 형성한다.
- `bridge_trace`는 merge가 아니라 관계 가능성의 흔적이다.
- reader vocabulary는 core schema에 넣지 않는다.

작업 방식:

- `../vectorfl`는 frozen reference로만 읽는다.
- 현재 저장소에서는 새 코어와 runtime만 만든다.
- 애매한 판단은 즉흥 구현으로 덮지 않고 체크리스트와 decision 문서로 남긴다.
