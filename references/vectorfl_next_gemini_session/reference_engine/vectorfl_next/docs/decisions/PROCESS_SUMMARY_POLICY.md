# Process Summary Policy

process summary는 runtime을 단일 정답으로 환원하지 않고, 현재 어떤 과정 국면이 공존하는지 짧게 읽기 위한 observer 요약층이다.

현재 summary는 아래 모드를 사용한다.

- `sparse_process`
- `continuity_process`
- `branching_process`
- `reactive_process`
- `mixed_process`

잠금 기준:

- `thickening`이 있으면 continuity를 읽는다.
- `pressure_signature_mismatch_or_absent` branch가 있으면 mismatch branching을 읽는다.
- continuity와 mismatch branching이 함께 있으면 `mixed_process`로 읽는다.
- summary는 observer 표현이며 core ontology를 늘리지 않는다.

의도:

- runtime이 두꺼워지는 흐름과 갈라지는 흐름을 동시에 갖고 있어도 둘 중 하나로 지워지지 않게 한다.
- 긴 event 목록 위에 빠른 판정보다 공존하는 과정 국면을 보여준다.

금지 기준:

- process summary를 canonical diagnosis처럼 쓰지 않는다.
- summary가 event history나 branch history를 대체하게 두지 않는다.
