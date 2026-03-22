# Initial Material Seed Policy

첫 입력 묶음은 taxonomy 실험이 아니라 공간 초기 관찰을 위한 최소 seed set으로만 넣는다.

현재 seed set은 아래 세 종류만 허용한다.

- `fresh_material`
- `engine_self_material`
- `observer_material`

세 항목은 모두 먼저 `material`로 ingest한다.

잠금 기준:

- 입력 종류 이름보다 formation role이 앞선다.
- 첫 seed set은 세 종류를 넘기지 않는다.
- `engine_self_material`은 Codex 작업 로그나 runtime 자기기록을 우선 사용한다.
- `observer_material`은 observer 출력 요약을 사용한다.
- `fresh_material`은 공간 의도를 직접 드러내는 짧은 note로 시작한다.

운영 기준:

- seed script는 재실행 가능해야 한다.
- 재실행은 overwrite가 아니라 같은 family의 재유입으로 읽힌다.
- 첫 seed set은 공간을 닫지 않고 관찰 가능성을 여는 데 목적이 있다.

금지 기준:

- 첫 seed set 단계에서 rigid input taxonomy를 도입하지 않는다.
- point, cluster, promotion 언어를 seed helper에 넣지 않는다.
- observer 산출물이 core truth를 대체하게 두지 않는다.
