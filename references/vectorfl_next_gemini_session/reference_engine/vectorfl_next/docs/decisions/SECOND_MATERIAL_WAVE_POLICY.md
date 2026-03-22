# Second Material Wave Policy

초기 한 개 cell terrain만으로는 multi-local space가 실제로 자라는지 충분히 보기 어렵다.

두 번째 material wave의 역할:

- 기존 first cell을 덮어쓰지 않는다.
- 같은 family reentry를 이용하되 pressure variation을 통해 neighboring cell을 연다.
- 그 결과 local space가 둘 이상 생기도록 유도한다.
- bridge는 merge가 아니라 adjacent trace로만 남긴다.

핵심 원칙:

- second wave는 overwrite가 아니라 terrain expansion이어야 한다.
- 같은 family라도 shifted pressure는 새로운 neighboring cell로 읽을 수 있어야 한다.
- local space는 둘 다 독립성을 유지한다.
- bridge는 adjacency를 남기되 collapse를 일으키지 않는다.

금지 기준:

- second wave를 first cell thickening으로만 회수하지 않는다.
- second wave를 point-first shortcut으로 쓰지 않는다.
- bridge를 multi-local terrain collapse trigger로 쓰지 않는다.
