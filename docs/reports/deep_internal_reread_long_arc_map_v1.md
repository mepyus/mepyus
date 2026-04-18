# deep internal reread long arc map v1

## 1. 이 문서의 목적

이 문서는 최근 장치들만 다시 요약하는 문서가 아니다.

목적은 이 공간이 왜 처음부터 필요했는지부터 시작해서,
과거의 레퍼런스, 입력, 기록, 구조 작업이 어떻게 지금의 제어면과 관찰 기관들로 응축되었는지를 다시 읽게 하는 장기 형성사 지도다.

`process_reread_map_v1`가 최근 형성된 장치들의 발생 경로를 보여주는 지도라면,
이 문서는 그보다 더 길게,
그 장치들이 왜 그 시점에 생겨날 수밖에 없었는지까지 돌아가는 장기 발생사 지도다.

## 2. 시작점: 처음의 질문

처음의 질문은 단순 기능 개선이 아니었다.

핵심은 다음과 같았다.

- 왜 단순 앱, 단순 요약기, 단순 RAG로는 부족한가
- 왜 기억을 더 먹이면 해결될 것 같지 않은가
- 왜 필요한 것은 답변기가 아니라 이해가 자라는 공간인가

이 질문이 결국 `내 공간 위에서 추론`이라는 질문으로 이동했다.

즉 시작점은 기능이 아니라, **내 생각이 올라설 바닥 자체가 필요한가**라는 질문이었다.

## 3. 장기 형성 단계

### 3.1 1기: 공간 자체를 붙들던 시기

무엇을 하던 시기였는가:
- 공간을 만들고 싶다는 감각이 먼저 있었다.
- 자료를 저장하고 보여주는 것보다, 무언가가 자라날 공간 자체를 상상했다.

무엇이 부족했는가:
- 읽기 전에 방향을 정하는 눈이 없었다.
- 무엇을 먼저 읽고 무엇을 드리프트로 볼지 정리되지 않았다.

무엇이 씨앗이 되었는가:
- 공간은 단순 저장소가 아니라는 감각
- 이해가 쌓여야 한다는 감각

### 3.2 2기: 입력/기록/구조를 만들던 시기

무엇을 하던 시기였는가:
- `fragment`, `anchor`, `provenance`, `measurement`, `observer`, `report` 같은 입력/기록/구조 층을 세우려 했다.
- `CURRENT.md`, `vectorfl_status.md`, `vectorfl_philosophical_interpretation_v1.md`, `codex_content_pack.md`, `codex_processor_standard.md` 같은 상위 기준이 이때부터 중요해졌다.

무엇이 부족했는가:
- 구조는 있었지만 그 구조를 어떤 기준으로 읽어야 하는지 더 상위의 제어면이 부족했다.
- 기록은 많아질 수 있지만, 판단 이동 경로를 남기는 방식이 아직 얇았다.

무엇이 씨앗이 되었는가:
- source -> fragment -> anchor + processing values -> measurement -> observer -> projection
- 입력기/앵커기/라벨기/비교 기준선이라는 감각

### 3.3 3기: 페이지/운용/읽기 문제를 겪던 시기

무엇을 하던 시기였는가:
- WashTank, officeout, page composition, operating surface 같은 레퍼런스를 읽으며
  "페이지"와 "운용"과 "읽기"가 어떻게 다르게 살아야 하는지 보려 했다.
- 화면이 단순 UI가 아니라 transition hub, process hub, operator surface로 읽힐 수 있다는 점이 중요해졌다.

무엇이 부족했는가:
- 페이지를 읽는 기준이 아직 공간 전체를 안내하지 못했다.
- 구조보다 표면이 먼저 보이는 문제가 있었다.

무엇이 씨앗이 되었는가:
- 화면이 아니라 전이 허브를 본다는 관점
- `officeout.jsx`를 terminal operations hub로 읽는 시도
- WashTank를 공정/역할/부지/전이의 분화된 운영 프로그램으로 읽는 시도

### 3.4 4기: 눈이 없다는 자각

무엇을 하던 시기였는가:
- 공간은 있었지만 읽기 전에 모드/국면/드리프트를 선행 제어하는 눈이 없었다.
- 단순 결과를 보는 것이 아니라, 읽기 시작 전에 무엇을 읽을지 정하는 제어면이 필요하다는 자각이 생겼다.

무엇이 부족했는가:
- 관찰 이전의 분기
- 읽기 순서를 먼저 고정하는 장치

무엇이 씨앗이 되었는가:
- control plane 필요성
- `space_kernel`, `turn_router`, `drift_guard`, `current_phase`

### 3.5 5기: 감독 렌즈 형성

무엇을 하던 시기였는가:
- active asset 판정과 saved_connection reread를 평가하기 위해 감독 렌즈가 잠겼다.
- `binding closed -> semantic fidelity -> output-worthiness -> meaning-context sufficiency -> detector -> widening trigger` 순서가 고정되었다.

무엇이 부족했는가:
- 닫힘과 의미 충실도를 분리해서 읽는 규칙이 없으면, 닫혔다는 사실만으로 성공으로 오해하기 쉬웠다.

무엇이 씨앗이 되었는가:
- closure와 fidelity의 분리
- output-worthiness와 meaning-context sufficiency의 분리
- narrow mechanism closure detector

### 3.6 6기: control plane / breadcrumbs / candidate / boundary / watch rule 형성

무엇을 하던 시기였는가:
- preflight gate가 읽기 전에 mode와 drift를 먼저 정하도록 만들었다.
- breadcrumbs가 판단 이동을 남기기 시작했다.
- `raw_to_first_pass_to_report` 같은 경로를 observation candidate로만 다루고, boundary note와 watch rule로 경계를 확인했다.

무엇이 부족했는가:
- candidate를 억지로 만들지 않고, 언제까지를 같은 경로로 봐야 하는지 경계가 더 필요했다.
- second seed는 아직 없었다.

무엇이 씨앗이 되었는가:
- runtime preflight gate
- pipeline observation registry
- candidate scope summary
- second candidate watch rule
- watch rule auto connection

## 4. 장기 재료가 현재 장치로 응축된 경로

### 4.1 탱크 프로그램 / WashTank 레퍼런스

탱크 프로그램을 읽은 핵심은 화면이 아니라 전이였다.

WashTank와 officeout를 읽으면서 다음이 보였다.

- 공정은 단계별 전이로 읽어야 한다
- 화면은 콘솔/허브/전이면이어야 한다
- 역할과 부지 차이가 화면 구조를 만든다

이 흐름이 나중에 운영 surface, transition hub, compaction of surfaces에 대한 감각으로 응축되었다.

### 4.2 선언문 / 기준문 / 지시서

이것들은 단순 텍스트가 아니라, 공간이 어떻게 읽혀야 하는지를 잠그는 상위 자료였다.

이 문서들은 다음을 만들었다.

- 공간은 저장소가 아니라 이해 기반 추론 공간이라는 관점
- 결과보다 과정과 경로를 읽는 태도
- raw / first-pass / report / trace를 분리하는 감각

### 4.3 입력기 / 기록 / provenance / folder_status

입력과 기록을 다루는 방식은 memory layer separation map, existing_assets_to_memory_layers_map 같은 문서에서 더 선명해졌다.

여기서 중요한 것은:

- raw를 raw로 보존해야 한다
- interpretation은 raw를 대체하지 않는다
- observation은 raw와 interpretation을 정답처럼 덮지 않는다
- provenance는 다시 돌아가기 위한 손잡이다

이 감각이 현재의 `breadcrumbs`, `observation registry`, `candidate summary`로 이어졌다.

### 4.4 페이지 / 운용 / 읽기 시도

페이지는 단순 UI가 아니라 운용 표면으로 읽혔다.

하지만 페이지만 강조하면 바닥이 약했다.
그래서 page composition보다 먼저 control plane과 reading layers가 필요해졌다.

### 4.5 recent runtime 장치

최근 장치는 갑자기 생긴 것이 아니라,
위의 재료들이 다음처럼 응축되며 생겼다.

- control plane -> 읽기 전에 mode와 drift를 정함
- breadcrumbs -> 판단 이동을 기록함
- observation registry -> 반복되는 경로 후보를 남김
- candidate summary -> 후보를 한 장으로 읽게 함
- watch rule -> 두 번째 후보 발생 시점만 얇게 감시함

## 5. 현재 살아 있는 최소 기관

지금 실제로 살아 있다고 볼 수 있는 것은 다음이다.

- preflight가 읽기 전에 모드를 먼저 정한다
- breadcrumb가 판단 이동을 남긴다
- `raw_to_first_pass_to_report`가 mode-scoped observation candidate로 관찰된다
- watch rule이 append 시점에 collapse / boundary / seed 여부를 얇게 평가한다
- candidate summary가 registry를 한 장으로 읽게 한다

이들은 모두 완성형은 아니지만 실제로 작동한다.

## 6. 아직 잠복 상태인 것

아직 아닌 것도 분명하다.

- weak pipeline 아님
- locked pipeline 아님
- second seed 없음
- interpretation packets는 아직 바닥 수준
- decision lineage는 아직 얇은 초기층
- multi-lens는 본격 확장 전

즉 장기 형성사 안에서 씨앗은 이미 보이지만, 아직 기관으로 충분히 자란 것은 아니다.

## 7. 이번 재독해로 새롭게 보인 것

이번 재독해에서 더 선명해진 점은 다음이다.

1. 현재 장치들은 최근 공사 구간에서 갑자기 생긴 것이 아니다.
2. 탱크 프로그램, 페이지 운용, 입력/기록/provenance 작업, 문서 헌법이 장기간 응축되며 현재 장치로 내려왔다.
3. `space -> trace -> boundary -> watch` 구조는 최근 발명이라기보다 오래된 형성사가 압축된 결과다.
4. 앞으로 내부를 다시 읽을 때는 최근 장치만 보지 말고, 탱크/입력/기록/운용/기준문 층을 함께 봐야 한다.

즉 지금 공간은 최근 공사 구간이 아니라,
장기 발생사가 계속 응축되어 현재 기관으로 보이기 시작한 공간이다.

## 8. 이 자료가 필요한 이유

이 문서는 나중에 내부를 다시 볼 때 다음을 가능하게 한다.

- 왜 이런 공간을 원했는지부터 다시 읽기
- 탱크 / WashTank / md_maker / 입력기 / 기록기 / 제어면이 어떻게 한 흐름인지 보기
- 최근의 preflight, breadcrumbs, watch rule이 어디서 왔는지 보기
- 현재 살아 있는 최소 기관과 아직 잠복 상태인 선을 구분하기

즉 이 문서는 결과 요약이 아니라, 내부 형성사를 다시 따라 읽기 위한 지도다.

