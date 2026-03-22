# Third Material Wave Policy

두 번째 wave가 observer-facing neighboring terrain을 열었다면, 세 번째 wave는 다른 pressure axis를 가진 제3 terrain을 열어야 한다.

세 번째 material wave의 역할:

- 기존 observer-facing adjacency를 반복 두껍게 만들지 않는다.
- temporal/project pressure가 강한 다른 terrain을 연다.
- third terrain은 기존 multi-local terrain과 weak reference만 가지며 독립성을 유지한다.

핵심 원칙:

- third wave는 scale expansion이어야 한다.
- pressure axis가 달라지면 새로운 terrain으로 읽는다.
- third terrain은 bridge 없이도 local space로 설 수 있어야 한다.
- observer reference가 있어도 observer-facing terrain으로 다시 회수되지 않는다.

금지 기준:

- third wave를 second wave의 변주로만 만들지 않는다.
- third wave를 existing bridge 강화 장치로 축소하지 않는다.
- new terrain을 old terrain의 부속 terrain처럼 모델링하지 않는다.
