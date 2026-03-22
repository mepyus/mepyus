# Reread Layer Audit Policy

terrain reread가 공간 정의를 대신하지 않았는지 주기적으로 감사할 수 있어야 한다.

핵심 원칙:

- reread layer는 descriptive only라는 원칙을 계속 점검한다.
- reread layer 수가 runtime scale보다 먼저 비대해지면 경고한다.
- audit는 코어를 바꾸지 않고 현재 reread posture만 읽는다.

현재 audit가 보는 것:

- 어떤 terrain reread layer가 실제로 활성화되어 있는가
- reread layer 깊이가 현재 cell/local-space scale과 비교해 과한가
- local space visibility 없이 reread만 늘어난 상태는 아닌가

금지 기준:

- audit를 새로운 gate나 build blocker로 쓰지 않는다.
- audit 결과를 core ontology 변경의 자동 트리거로 쓰지 않는다.
