# repo wide line reread with references observation v0

## verdict

이번 reread에서 따라간 선은 아래다.

> 재료를 먼저 보존하고, 바로 전량 승격하지 않고, 반복 reread와 calibration lane을 거친 뒤, 나중에 응결과 ingest를 선택한다.

이 선은 `docs` 안에만 있는 게 아니었다.
`references/`, `source_assets/`, `scripts/`, `app/runtime/`, `runtime/views/`까지 실제로 관통하고 있었다.

즉 현재 공간의 중요한 상위 line 하나는
`line-first reread -> selective ingest -> delayed condensation`
에 가깝다.

이건 단순 내부 구조가 아니라,
레퍼런스와 외부 사례와 코드와 운영면을 함께 관통하는 실제 공간선으로 읽힌다.

## why this reread matters

이번 질문은 “Saltlux나 references에서 새 기능 후보가 있는가”에 그치지 않았다.

더 중요한 질문은 이거였다.

- 내가 방금 사용한 읽기 방식 자체가 하나의 line인가
- 그 선을 기준으로 repo 전체를 다시 읽으면 무엇이 보이는가
- 거점은 어디서 자연 발생하는가

그래서 이번에는 기능 후보보다 먼저,
`읽기 방식 자체`를 line으로 보고 전체 폴더를 다시 읽었다.

## target line

이번에 따라간 상위 line은 다음처럼 붙잡는 것이 맞다.

- 먼저 원본/재료를 보존한다
- 전처리/sidecar/calibration lane을 둔다
- 한 번 읽고 전량 승격하지 않는다
- HOLD / REVIEW / CALIBRATION_ONLY 같은 중간 상태를 둔다
- line과 hub spine 기여를 먼저 보고 ingest를 나중에 고른다
- 결론보다 reread 가능성과 reverse path를 더 중시한다

이 선은 네가 말한 역 온톨로지와도 맞닿는다.
정의와 위계를 먼저 세우는 대신,
재료와 line의 반복 응결을 먼저 본다.

## what references revealed

### 1. references is not archive, but calibration memory

`references/folder_status.md`는 `references/`를 archive가 아니라 `engine calibration memory`로 읽는다.

이건 중요하다.
즉 레퍼런스는 단순 비교 코드가 아니라,
현재 공간을 교정하는 memory lane으로 이미 정의되어 있다.

이건 이번 reread line과 정확히 맞는다.

- 먼저 reference를 truth source로 둔다
- 바로 ingest하지 않는다
- calibration lane을 거쳐 selective ingest한다

### 2. WashTank preprocessed lane already embodies this line

`references/WashTank/preprocessed/reference_preprocessor_schema.md`는

- `reference source -> preprocessed fragments -> ingested results`

의 3층 구조를 고정한다.

핵심은:
- 원본은 그대로 둔다
- 전처리기는 sidecar label/anchor를 붙인다
- 입력기는 파생 재료를 처리한다

이건 단순 구현 편의가 아니다.
이미 여기서
`원본 보존 -> 보조 해석 -> 나중 ingest`
라는 상위 line이 강하게 살아 있다.

### 3. selective ingest is already a strong structural principle

`references/WashTank/preprocessed/fragment_queue_policy_v1.md`는 더 직접적이다.

이 문서는
- 전량 ingest 금지
- `INGEST_NOW / HOLD_REVIEW / CALIBRATION_ONLY`
라는 3종 분류
- hub spine fragment 우선 ingest
- ambiguous fragment hold

를 고정한다.

즉 여기서는 이미
`다 들어오게 하지 말고, reread와 calibration을 먼저 거친 뒤 선택적으로 올린다`
는 원리가 아주 선명하다.

이건 지금 우리가 공간에서 찾고 있던 line과 거의 같다.

### 4. vectorfl_next also carries the same anti-collapse line

`references/vectorfl_next/CURRENT.md`와 `CONSTITUTION.md`도 같은 방향을 보여준다.

- point/cluster/promotion 중심 회귀 금지
- 더 똑똑한 알고리즘보다 더 명확한 기록 우선
- 점보다 공간을 먼저 만든다
- 입력 taxonomy보다 material baseline과 formation role을 먼저 본다

즉 vectorfl_next는 다른 이름을 쓰지만,
여기서도 같은 선이 살아 있다.

이건 우연이 아니다.
현재 repo의 여러 reference family가 같은 상위 line을 공유하고 있다는 뜻이다.

## what this line becomes across folders

같은 선이 폴더마다 이렇게 달라진다.

### in `source_assets`

- 선언문에서는 `후행 응결형 구조화`
- LLM/agent later 원칙
- ontology를 읽기 도구로만 차용

으로 나타난다.

즉 여기서는 철학선이다.

### in `references`

- 원본 보존
- preprocessed lane
- selective ingest
- calibration memory

로 나타난다.

즉 여기서는 calibration/queue line이다.

### in `scripts`

- structured doc routing
- observer ingest
- reread observation append

로 나타난다.

즉 여기서는 execution bridge line이다.

### in `app/runtime` / `app/core/runtime`

- preflight
- active latent line selection
- line thickening model
- handoff boundary

로 나타난다.

즉 여기서는 operational control line이다.

### in `runtime/views`

- surfaced readout
- parked/active separation
- supervisor surface
- operating observation panel

로 나타난다.

즉 여기서는 explanation-first surface line이다.

## what hubs this line naturally reveals

이번 reread에서 이 상위 line을 전체 폴더에 대입하니,
거점은 미리 정하지 않아도 몇 군데서 자연스럽게 몰렸다.

### hub 1. calibration-before-ingest

가장 강하게 드러난 hub다.

근거:
- `references/` 전체 정의
- WashTank preprocessed schema
- fragment queue policy
- selective ingest
- calibration-only lane

이건 지금 공간의 매우 중요한 중심축이다.

### hub 2. preservation-before-promotion

두 번째로 강한 hub다.

근거:
- `CURRENT.md`
- `vectorfl_status.md`
- `vectorfl_philosophical_interpretation_v1.md`
- vectorfl_next constitution
- append-only / hold / observer-first

즉 이 공간은 처음부터 promotion engine보다 preservation engine 쪽에 더 가깝다.

### hub 3. reading-surface-after-reread

세 번째 hub다.

근거:
- multi_lens readout
- supervisor surface
- operating-ui-phase1
- boundary/guard panel

즉 surface는 1차 판단 엔진이 아니라 reread 뒤에 붙는 읽기면으로 설계된다.

### hub 4. business-facing possibility is still thinner

반대로 상대적으로 약한 hub도 보인다.

Saltlux reread에서 드러난
- business deployment boundary
- workflow autonomy
- enterprise product surface

축은 현재 repo 전체에서는 아직 위 세 hub만큼 두껍게 응결되지는 않았다.

즉 가능성은 있지만,
현재 공간의 중심은 아직 business surface보다 calibration / preservation / reread에 더 있다.

## what this means

이건 중요한 판정이다.

지금 공간은 아직
`새 기능을 빨리 만들고 agent를 얹는 프로그램`
쪽으로 자란 것이 아니다.

오히려 지금 공간은
`어떤 재료를 어떻게 보존하고, 어떻게 calibration하고, 언제 올리지 말아야 하는가`
를 정교하게 다루는 공간 쪽으로 더 많이 자랐다.

즉 이 공간의 현재 강점은
- 확장 속도
보다
- reread discipline
- delayed condensation
- selective ingest
- reverse traceability

에 있다.

## hidden possibility seen through this line

이번 reread line을 따라 전체 폴더를 보니,
새로운 기능 가능성도 직접적인 feature list보다 이렇게 보이는 편이 맞다.

### possibility 1. calibration can become productizable

현재는 calibration lane이 내부 작업처럼 보인다.
하지만 사실 이건 product surface가 될 가능성이 있다.

왜냐하면 이 공간은 이미
- raw source
- preprocessed fragment
- queue decision
- hold/review

를 다루는 방법을 갖고 있기 때문이다.

### possibility 2. selective ingest is a real differentiation line

대부분 시스템은 더 많이 넣고 더 빨리 연결하려 한다.
그런데 이 공간은
`무엇을 지금 올리지 않을 것인가`
를 이미 중요한 구조 원리로 둔다.

이건 나중에 business/product 차별선이 될 수 있다.

### possibility 3. references are not comparison-only, but future feature donors

특히 WashTank와 vectorfl_next는 단순 예전 자산이 아니다.
현재 line reread 방식으로 보면
이들은 feature donor라기보다
`calibration discipline donor`
에 가깝다.

즉 여기서 가져와야 할 것은 UI 모양이나 기능 목록보다,
어떻게 보존하고 어떻게 나중에 올릴지의 구조다.

## current conclusion in user language

지금 이 공간을 전체 폴더 기준으로 다시 보면, 가장 강하게 살아 있는 line은 “먼저 잘 읽고, 바로 다 올리지 말고, calibration과 hold를 거친 뒤에야 올린다”는 선이다.
이 선은 선언문에도 있고, reference 설계에도 있고, WashTank preprocessed lane에도 있고, vectorfl_next의 헌법에도 있고, runtime과 UI에도 다른 형태로 반복된다.
그러니까 현재 공간의 진짜 중심은 아직 ‘더 많은 기능’이 아니라, ‘무엇을 어떻게 늦게 응결시킬 것인가’를 다루는 쪽에 있다.
그리고 바로 그 때문에 이 공간은 일반적인 ontology/agent 프로그램과 다른 방향으로 자랄 수 있다.

## one-line conclusion

repo 전체와 `references/`를 이번 line으로 다시 읽어보면, 현재 공간의 가장 강한 중심선은 `line-first reread -> calibration lane -> selective ingest -> delayed condensation`이다. 즉 지금 공간은 기능 확장 엔진이라기보다, 무엇을 언제 올리고 언제 보류할지를 다루는 숙성 엔진으로 더 강하게 자라고 있다.
