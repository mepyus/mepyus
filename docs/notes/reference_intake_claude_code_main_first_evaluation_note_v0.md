# reference intake / claude-code-main first evaluation note v0

## 0. verdict

`references/ralph/claude-code-main`은 지금 당장 도입할 운영 본체가 아니다.
하지만 우리 공간을 선명하게 해주는 비교 재료로는 매우 유효하다.

핵심은 Claude Code 전체를 가져오는 것이 아니라,
여기서 보이는 몇 개의 선을
현재 space-first reread 구조와 비교하는 데 쓰는 것이다.

---

## 1. what this reference actually is

이 폴더는 단순 CLI 배포본이 아니다.

이번 first evaluation에서 강하게 보인 것은 아래다.

- pluginized operating surface
- hook-mediated behavior shaping
- specialized agent bundle as workflow unit
- interactive phase-guided feature workflow
- self-referential loop inside session

즉 본체는 “코딩 도구”라기보다,
도구 주위에 `plugin / hook / agent / command`를 붙여
행동과 흐름을 가공하는 표면에 가깝다.

---

## 2. what is useful right now

지금 우리 공간에 유효한 것은 아래다.

- hook을 통해 행동을 미세하게 교정하는 감각
- command / agent / skill을 분리 포장하는 감각
- specialized workflow bundle을 표면 단위로 만들 수 있다는 감각

이건 현재 우리 공간의
`line inspection`, `operating surface`, `later execution harness`
를 더 선명하게 생각하게 해준다.

이번 재독해에서 더 분명해진 것은,
`claude-code-main`의 본체가 단순 코딩 능력이 아니라
`plugin / hook / agent / command`를 전면 surface로 조직하는 방식이라는 점이다.

즉 이 reference는
우리 공간 위에 나중에 어떤 운영 표면을 얹을 수 있을지 보여주는
`surface packaging reference`
로 읽는 것이 맞다.

---

## 3. what should remain in references for now

지금은 `references/`에 두고 보류하는 것이 맞는 것은 아래다.

- plugin-first expansion
- feature-dev seven-phase workflow를 기본 front door로 두는 방식
- in-session self-referential loop를 바로 운영 본체로 삼는 방식

왜냐하면 현재 우리 공간은
surface/tool packaging보다
`construction -> line reading -> meaning reread -> inspection`
루프를 더 두껍게 해야 하는 단계이기 때문이다.

특히 `ralph-wiggum`의 stop hook처럼
세션 종료를 가로막아 같은 prompt를 되먹이는 방식은
지금 우리 공간에 바로 얹기엔 closure/iteration 압력이 너무 강하다.

---

## 4. what this reference reveals about our current space

Claude Code main을 보고 나면
우리 공간의 현재 부족함도 더 잘 보인다.

- 우리는 아직 내부 reread 생활화가 더 중요하다
- plugin surface는 나중에 얹을 층이다
- 지금 plugin을 늘리면 눈이 내부 line이 아니라 표면 도구로 쏠릴 수 있다

즉 이 reference는
“지금 바로 써야 할 것”보다
“나중에 우리 공간이 어느 정도 두꺼워졌을 때 어떤 표면이 생길 수 있는가”
를 미리 비추는 거울에 가깝다.

---

## 5. future reopen condition

아래 조건이 오면 다시 열 가치가 크다.

- line inspection이 충분히 생활화되었을 때
- human-language meaning reread가 안정화되었을 때
- 반복 reread 결과를 명령/훅/에이전트 패키지로 얹을 필요가 생겼을 때

즉 reopen 기준은
Claude Code가 좋아 보이기 때문이 아니라,
우리 공간이 그 표면을 받아도 내부 line ecology를 잃지 않을 만큼 성숙했는가이다.

그때는 `plugin/hook/agent`를 먼저 늘리는 것이 아니라,
이미 두꺼워진 line inspection과 operating surface 위에
선택적으로 얹는 방식이어야 한다.

---

## 6. one-line conclusion

`claude-code-main`은 지금 당장 따라갈 본체가 아니라,
나중에 우리 공간 위에 어떤 plugin/hook/agent 표면을 얹을 수 있을지 미리 보여주는 calibration reference로 유지하는 것이 맞다.
