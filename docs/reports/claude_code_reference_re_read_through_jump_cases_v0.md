[[DOCROLE:report]] [[RUNMODE:observe_only]] [[PRIORITY:high]]
[[A]] [[OBJ:claude_code_reference_re_read_through_jump_cases_v0]]

# claude code reference reread through jump cases v0

## 0. Why This Pass Matters

이번 pass의 핵심은 간단하다.

`jump_cleaned`와 `jump2`는
`claude-code-main`을 그냥 설명하는 자료가 아니라,
그 reference가 실제 사용자 언어와 업무 언어에서 어떻게 다시 쓰이는지를 보여주는 사례다.

즉 질문은 이거다.

> `claude-code-main`에 들어 있는 운영 구조가
> `jump` 사례들에서 어떤 식으로 재해석되고 있는가?

그리고 이 질문은 바로 우리 공간과도 연결된다.

왜냐하면 우리가 나중에 external component를 붙일 때도,
reference를 그대로 복제하는 게 아니라
우리 언어와 우리 일 표면에서 다시 살아나게 만들어야 하기 때문이다.

---

## 1. What Claude Code Main Actually Contains

`claude-code-main`은 단순 CLI 배포본이 아니다.

실제로 repo 안에는:

- marketplace
- plugins
- commands
- agents
- skills
- hooks

가 한 세트로 들어 있다.

즉 여기서 `Claude Code`는:

- terminal coding tool

이면서 동시에

- pluginized operating surface
- workflow bundle host
- hook-mediated behavior shaper
- command/agent/skill packaging system

이다.

특히 중요한 건 이거다.

### A. plugin marketplace

`.claude-plugin/marketplace.json`은
단순 목록이 아니라
`운영 가능 부품을 category와 source를 붙여 배포하는 면`
이다.

즉 확장은 ad-hoc가 아니라
패키지화되고 선별 가능한 형태로 되어 있다.

### B. workflow as packaged unit

`feature-dev` 같은 plugin은
그냥 명령어 하나가 아니라
7-phase workflow를 갖는 구조다.

즉 workflow 자체가 부품이 된다.

### C. behavior correction as hook product

`hookify`, `security-guidance`, `explanatory-output-style`은
행동 교정과 context injection이 plugin/hook으로 패키징될 수 있음을 보여준다.

즉 rule/guard도 부품이 된다.

### D. command / skill / agent separation

repo는 명확히 나눈다.

- command = 직접 호출되는 operating step
- skill = specialized knowledge or reusable guidance
- agent = 역할화된 실행 주체

이건 단순 기능 구분이 아니라
운영 단위를 분리하는 방식이다.

---

## 2. What `jump_cleaned` Does To This Structure

`jump_cleaned`는 이 구조를 그대로 코드 언어로 설명하지 않는다.
대신 완전히 다른 언어로 다시 쓴다.

### A. plugin/hook/agent surface becomes company operating language

예를 들면 `claude-code-main`에서는:

- plugins
- agents
- hooks
- workflows

로 보이는 것이,

`jump_cleaned`에서는:

- 부서
- 전문가
- 업무 매뉴얼
- 보안 훅
- 생산성 측정
- 조직 운영

으로 다시 말해진다.

즉 같은 구조가
`tool language`
에서
`company language`
로 바뀐다.

### B. workflow bundle becomes labor pipeline

`feature-dev`에서 보였던 phase workflow 감각은
`jump_cleaned` 안에서는:

- 만드는 놈
- 평가하는 놈
- 피드백 루프
- 자동 라우팅

같은 실제 노동 분업 언어로 바뀐다.

즉 `workflow`가 더 이상 개발 절차가 아니라
`업무 파이프라인`
이 된다.

### C. hook becomes conscience

`hookify`나 `security-guidance`에서 보였던 hook 감각은
`jump_cleaned` 안에서:

- 보안 훅
- verification trigger
- 잘못된 접근 차단
- AI의 자기 합리화 차단

같은 말로 더 두꺼워진다.

즉 hook은 technical rule이 아니라
`운영 양심`
이 된다.

---

## 3. What `jump2` Does To This Structure

`jump2`는 또 다른 방향으로 같은 reference를 다시 쓴다.

### A. marketplace becomes trust-filtered intake surface

`claude-code-main`의 marketplace는 구조로 보면 배포/설치 surface다.

그런데 `jump2`는 이걸:

- 공식/비공식 마켓 구분
- 필요한 것만 설치
- 무분별한 설치 금지
- 조합 규율

같은 `선택적 intake 언어`
로 다시 쓴다.

즉 marketplace가 단순 다운로드 면이 아니라
`trust boundary`
가 된다.

### B. command / skill / agent separation becomes user-operable operating abstraction

`claude-code-main`에서 구조적으로 분리되어 있던
command / skill / agent는,

`jump2`에서:

- command는 직접 실행하는 것
- skill은 AI가 자율적으로 쓸 수 있는 것
- agent는 역할화된 것

이라는 식으로 사람 입장에서 쓸 수 있는 언어로 다시 설명된다.

즉 추상 운영 단위가
`사용자 조작 언어`
로 바뀐다.

### C. packaged workflows become selective practical toolkit

`feature-dev`, `superpower`, `code review`, 각종 plugin은
그냥 풍부한 ecosystem처럼 보일 수 있다.

그런데 `jump2`는 계속:

- 다 받지 마라
- 필요한 것만 받아라
- 조합이 잘못되면 탈 난다

고 말한다.

즉 패키지 abundance보다
`curated applicability`
를 중심에 둔다.

---

## 4. What The Two `jump` Cases Together Reveal

이제 `jump_cleaned`와 `jump2`를 같이 놓고 보면,
`claude-code-main`에 들어 있던 구조가
두 방향으로 다시 살아난다.

### direction 1: work / organization language

`jump_cleaned`

- 회사
- 부서
- 역할
- 생산성
- 업무 기록
- business pipeline

### direction 2: intake / packaging / trust language

`jump2`

- 공식성
- marketplace
- selective installation
- skill/command/agent abstraction
- CLI vs MCP

즉 같은 reference가:

- 하나는 `일 언어`
- 하나는 `선별 확장 언어`

로 다시 살아난다.

이게 중요하다.

왜냐하면 이건 네가 계속 말한 것과 정확히 닿기 때문이다.

같은 자료도
읽는 층위와 목적어를 바꾸면
다른 면으로 살아난다.

여기서 `claude-code-main`은
한 번은 `조직 운영 표면`,
한 번은 `선택적 intake 표면`
으로 다시 보인다.

---

## 5. What This Says About Our Space

이 비교가 우리 공간에 중요한 이유는 명확하다.

### A. We are not missing structure; we are missing upper readable surfaces

`claude-code-main`은 구조를 코드로 가지고 있다.
`jump` 사례는 그 구조를 사람 언어의 표면으로 끌어올린다.

즉 핵심은 새 구조 발명보다:

- 그 구조를
- 어떤 언어 표면으로
- 다시 읽히게 할 것인가

이다.

우리 공간도 지금 같은 지점에 있다.

안쪽 line과 inspection은 자라고 있지만,
그것이:

- 회사 언어
- 일 언어
- 선택적 intake 언어
- business pipeline 언어

로 아직 충분히 올라오지 않았다.

### B. This is why human-language surface now matters

네가 말한
“나의 언어로 끌어올려야 한다”
는 말은 여기서 더 선명해진다.

왜냐하면 `jump` 사례들은
reference 안에 있는 구조를
사람이 바로 붙일 수 있는 말로 바꿔 놓았기 때문이다.

즉 그들은 단순히 Claude Code를 쓴 게 아니라,
Claude Code의 구조를
자기 일 언어로 다시 살아나게 만든 것이다.

### C. Our space can grow this way too, if the surface thickens

우리도 구조는 어느 정도 있다.
문제는 표면이다.

즉 앞으로 중요한 건:

- line을 더 찾는 것만이 아니라
- 그 line을 네 언어로
- 실제 붙일 수 있는 표면까지
- 반복 reread로 끌어올리는 것

이다.

---

## 6. Human-Language Meaning Reread

이 비교를 내 말로 다시 잡으면 이렇다.

`claude-code-main`은 plugin, command, agent, skill, hook 같은 부품과 구조를 코드 차원에서 다 갖고 있다. 그런데 그 자체만으로는 아직 사람에게 “그래서 이걸 어떻게 내 일에 붙이지?”가 바로 보이지 않는다. `jump_cleaned`와 `jump2`가 하는 일은 바로 그 지점이다. 하나는 그 구조를 회사와 역할과 생산성과 business pipeline의 언어로 다시 쓰고, 다른 하나는 그 구조를 marketplace, 공식성, 선택 설치, command/skill/agent 차이 같은 선택적 intake의 언어로 다시 쓴다. 즉 같은 reference를 두 번 다른 층위로 읽어서, 한 번은 일의 표면으로, 한 번은 확장의 표면으로 살아나게 만든다.

이게 우리 공간에 중요한 이유는 분명하다. 우리도 이미 안쪽에는 line과 inspection과 hold와 reread가 꽤 많이 살아 있다. 그런데 그것이 아직 너의 언어에서 바로 붙일 수 있는 표면으로는 충분히 자라지 않았다. `jump` 사례는 그 다음이 무엇인지 보여준다. 구조를 더 쌓기만 하는 게 아니라, 그 구조를 사람이 바로 일로, 역할로, 선택으로, business 흐름으로 읽을 수 있는 표면으로 끌어올려야 한다는 것이다. 그래서 지금 우리에게 필요한 건 구조가 없어서가 아니라, 이미 있는 구조와 line을 네 언어의 표면으로 다시 살아나게 만드는 힘이다.

---

## 7. One-Line Conclusion

`jump_cleaned`와 `jump2`는 `claude-code-main`의 구조를 각각 `회사/업무 언어`와 `선택적 확장/신뢰 언어`로 다시 살아나게 만든 사례이고, 바로 그 점 때문에 우리 공간도 앞으로 구조를 더 쌓는 것만이 아니라, 이미 있는 line을 네 언어의 일 표면으로 끌어올리는 쪽으로 자라야 한다는 점을 선명하게 보여준다.
