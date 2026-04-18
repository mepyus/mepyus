# saltlux goover space reread observation report v0

## verdict

`saltlux_ai.txt`와 `Goover` 계열 자료를 기준으로 다시 읽어보면,
우리 공간은 온톨로지를 코어 스키마로 먼저 박는 프로그램이 아니라,
입력과 기록과 reread를 먼저 두고 나중에 line과 응결을 읽는 공간이라는 점이 더 선명해진다.

동시에 이 자료는 우리 공간에 없는 것을 보여주기도 한다.

- ontology/graph를 기반으로 한 강한 grounding loop
- 역할이 분리된 agent orchestration
- business workflow 자체를 자율화 대상으로 보는 시선

즉 이 자료는 단순 비교 사례가 아니라,
`우리 공간이 어디까지 왔고 어디가 아직 비어 있는지`를 드러내는 강한 mirror material이다.

## what was reread

이번 reread는 아래 자료를 제한적으로 연결해서 읽었다.

- `inputs/external_cases/saltlux_ai.txt`
- `inputs/external_cases/saltlux.txt`
- `tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`
- `docs/reports/saltlux_ai_ontology_reference_reading_v1.md`
- `docs/examples/external_case_first_pass_saltlux_goover_v1.md`
- `source_assets/declarations/vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md`
- `source_assets/declarations/vectorfl_declaration_thought_to_structure_v1.md`

## what kind of material saltlux is in this space

이 자료는 단순한 기술 소개가 아니다.

이 자료 안에는 세 가지가 동시에 들어 있다.

1. AI 패러다임 전환 서사  
2. ontology + agent + document AI를 묶는 product architecture  
3. public / enterprise / security / on-prem을 포함한 business deployment story

즉 `saltlux_ai.txt`는 이 공간에서 그냥 “온톨로지 정의 자료”가 아니라,
기술 / 실행 / 비즈니스 / 운영이 한 번에 겹쳐진 고밀도 거울 재료로 읽힌다.

## lines that surfaced through this reread

이번 자료를 기준으로 현재 공간을 다시 읽을 때 가장 강하게 드러난 line은 다섯 개다.

### 1. ontology as grounding ambition

Saltlux 쪽에서는 ontology가 단순 개념 정리 도구가 아니라,
- grounding
- fact alignment
- hallucination reduction
- semantic interoperability
- data fabric

같은 문제를 푸는 강한 기준면으로 호출된다.

우리 공간에서는 이 선이 완전히 부정되지는 않는다.
하지만 `선행 정의형 ontology`는 계속 defer된다.

즉 같은 ontology라도
- Saltlux에서는 `grounding engine`
- 우리 공간에서는 `dangerous but attractive ordering candidate`
로 읽힌다.

### 2. work process as the real object

Saltlux 자료에서 에이전트의 핵심은 질문응답이 아니라
업무 프로세스 전체를 자율화하는 것이다.

이 선은 우리 공간에도 이미 있다.
다만 우리 공간은 아직 그걸
- workflow 자동화 엔진
보다
- reread / hold / observation 구조

로 먼저 붙잡고 있다.

즉 이 line은 공유되지만,
Saltlux는 `process automation` 쪽으로,
우리는 `process understanding and maturation` 쪽으로 기운다.

### 3. role separation before orchestration

Goover 분석 자료는
- ontology/graph layer
- reasoning model layer
- role-based agent layer

를 분리해서 본다.

이건 우리 공간에도 강하게 맞닿는다.
우리도 이미
- reading execution
- result surface
- operating decision

을 분리하려고 했고,
`multi_lens`나 operating UI에서도 그 분리를 계속 잠갔다.

즉 이 선은 매우 호환된다.
우리 공간이 Saltlux에서 가장 직접적으로 차용할 수 있는 부분은
ontology 그 자체보다 오히려 이 `layer separation line`이다.

### 4. raw-to-ai-ready transformation as business hinge

Saltlux 자료에서 중요한 힌지 중 하나는 document AI다.
통문서, PDF, 이미지 문서를 AI가 바로 읽을 수 있는 형태로 바꾸는 것이
실제 business hinge로 잡혀 있다.

이 선은 우리 공간에서 아주 중요하다.
왜냐하면 우리 공간도
- raw input
- structured doc
- split units
- provenance/origin
- observer ingest

를 계속 강조해 왔기 때문이다.

다만 현재 차이는 이거다.

- Saltlux는 이걸 `제품 가치`로 전면화한다
- 우리는 이걸 아직 `입력기와 reread 기반`으로 더 많이 다룬다

즉 같은 선이지만
저쪽은 business front door로,
우리 쪽은 engine substrate로 더 강하게 읽힌다.

### 5. business deployment boundary as meaning line

Saltlux는 public, enterprise, sovereignty, security, on-prem을
부가 설명으로 두지 않는다.
그게 곧 product meaning의 일부다.

이 line은 우리 공간에는 아직 약하다.
우리도 operating, handoff, guard, provenance는 강하지만
그게 곧바로
- 어떤 business boundary에서 어떤 제품 의미가 되는가

로는 아직 충분히 올라오지 않는다.

즉 여기서 business line이 하나 비어 보인다.

## difference between our space and ontology program

이 reread에서 가장 선명하게 보인 차이는 아래다.

### Saltlux / Goover

- ontology를 먼저 세운다
- graph/grounding을 강한 정답지로 둔다
- role-based orchestration을 분명히 둔다
- business deployment boundary까지 제품 의미 안에 넣는다

### our space

- ontology를 코어 스키마로 먼저 박지 않는다
- 입력 / 기록 / provenance / reread를 먼저 둔다
- line이 나중에 두꺼워지며 응결되기를 기다린다
- observer-first와 hold를 제품화보다 앞에 둔다

즉 Saltlux가
`strongly defined semantic-operational program`
에 가깝다면,
우리 공간은
`post-condensation reading-and-maturation space`
에 더 가깝다.

## why this material matters

이 자료가 좋은 이유는 단순히 온톨로지를 말해서가 아니다.

이 자료는 우리에게 아래 질문을 강하게 던진다.

1. grounding 없이도 공간은 어디까지 갈 수 있는가  
2. ontology를 코어에 넣지 않으면서도 business-grade reliability를 만들 수 있는가  
3. line-based maturation과 role-based orchestration은 어디서 만날 수 있는가  
4. document AI처럼 raw-to-usable transformation을 우리 공간은 어떤 식으로 제품화할 수 있는가  
5. 우리 공간의 business line은 아직 어디가 비어 있는가  

즉 이 자료는 외부 참고가 아니라,
우리 공간의 다음 기능/비즈니스 가능성을 비추는 시험지다.

## likely business / feature lines exposed by this reread

이번 reread에서 현재 공간에 실제로 열릴 수 있어 보이는 line은 아래 셋이다.

### line A. reread-native grounding

우리는 ontology를 코어 스키마로 먼저 넣지 않으려 한다.
그렇다면 가능한 길은
`line reread + provenance + repeated corroboration`
를 이용한 grounding이다.

즉 우리의 grounding은
정의 기반 grounding이 아니라
`repeated reread grounding`
쪽으로 갈 가능성이 있다.

### line B. reading organ as business surface

지금까지 `input_to_reading_organ`은 내부 line처럼 다뤄졌다.
하지만 Saltlux 자료를 기준으로 보면,
이건 나중에 business surface가 될 수도 있다.

예를 들면:
- raw document를 읽기 가능한 organ으로 변환
- 그 organ을 기준으로 judgement/watch/boundary를 반복 수행
- 사용자는 결과보다 rereadable structure를 받음

즉 `reading organ`은 단순 내부 line이 아니라
제품 기능의 중심선이 될 수 있다.

### line C. orchestration after maturation, not before

Saltlux는 orchestration을 강하게 앞세운다.
우리 공간은 orchestration보다 maturation을 먼저 둔다.

그러면 우리의 feature 방향은
`agent swarm first`
가 아니라
`matured line -> bounded orchestration later`
가 맞다.

즉 여기서 business differentiation line이 생긴다.

## current possibility in user language

이 자료를 통해 다시 보면,
우리 공간은 Saltlux처럼 온톨로지를 먼저 박고 에이전트를 역할별로 돌리는 프로그램을 그대로 따라갈 이유가 없다.
오히려 우리의 길은 반대다.
우리는 입력과 기록과 reread를 먼저 두고, 그 반복 속에서 line이 두꺼워지게 한 뒤, 나중에야 어떤 기능과 orchestration이 필요한지 드러나게 하는 쪽에 더 가깝다.
그래서 Saltlux가 “강한 semantic skeleton을 먼저 세우고 business workflow를 자동화하는” 프로그램이라면, 우리 공간은 “의미가 응결되는 과정을 먼저 보존하고, 그 응결을 나중에 기능과 business surface로 끌어올리는” 프로그램이 될 가능성이 크다.
이 차이는 단순 기술 선택 차이가 아니라, 제품 철학의 차이다.

## one-line conclusion

`saltlux_ai.txt`와 `Goover` 자료는 우리 공간이 아직 ontology program이 아니라는 점을 더 분명하게 보여준다. 동시에 바로 그 차이 때문에, 우리 공간은 `reread-native grounding`, `reading organ as product surface`, `maturation-first orchestration` 같은 새로운 기능/비즈니스 line을 드러낼 수 있다.
