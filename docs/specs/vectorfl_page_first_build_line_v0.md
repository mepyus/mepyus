# VectorFL Page First Build Line v0

이 문서는 현재까지 잠근 구조를 바탕으로  
VectorFL Page를 실제로 만들 때 따라갈 첫 build line을 짧게 고정한다.  
목적은 구현 순서를 정하는 것이 아니라, 무엇을 중심 축으로 만들고 무엇을 주변에서 붙일지 한 줄의 라인으로 만드는 것이다.

## 1. Core Build Line

첫 build line은 아래처럼 잠근다.

`Current Reading console`
-> `Cases / Queue entry`
-> `Inputs / Intake entry`
-> `History / Trace panel`
-> `Programs / Connections panel`

즉:

- 중심은 `Current Reading`
- 가장 가까운 진입면은 `Cases / Queue`
- 그 다음 전단 확인면은 `Inputs / Intake`
- 이후 회고면과 외부 연결면을 붙인다

## 2. Why This Line

이 순서가 맞는 이유는 아래다.

### 2-1. Current Reading이 core 의미를 가장 직접 드러낸다

- current-reading
- governance
- lane
- trace preview

가 한 자리에서 만난다.

### 2-2. Queue는 중심이 아니라 current-reading 진입면이다

queue만 먼저 만들면 generic board처럼 흐를 수 있다.  
그래서 current-reading를 먼저 만들고, queue는 그 진입면으로 붙여야 한다.

### 2-3. Intake는 전단 확인면으로 붙는 것이 자연스럽다

입력기는 중요하지만, 개인용 VectorFL Page의 중심 console은 아니다.  
먼저 current-reading와 queue를 만들고, intake를 그 앞단 확인면으로 두는 편이 구조가 선명하다.

## 3. First Three Build Units

현재 단계에서 실제로 먼저 구현 대상으로 삼기 좋은 단위는 아래 셋이다.

### unit 1. Current Reading mock shell

- 기준 문서:
  - [vectorfl_current_reading_console_shell_rewrite_brief_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_console_shell_rewrite_brief_v0.md)
  - [vectorfl_current_reading_mock_fixture_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_mock_fixture_contract_v0.md)
  - [vectorfl_current_reading_mock_fixture_set_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_mock_fixture_set_v0.md)

### unit 2. Cases / Queue shell

- 기준 문서:
  - [vectorfl_cases_queue_shell_rewrite_brief_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_cases_queue_shell_rewrite_brief_v0.md)
  - [vectorfl_cases_queue_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_cases_queue_adapter_contract_v0.md)

### unit 3. Inputs / Intake shell

- 기준 문서:
  - [vectorfl_inputs_intake_shell_rewrite_brief_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_inputs_intake_shell_rewrite_brief_v0.md)
  - [vectorfl_inputs_intake_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_inputs_intake_adapter_contract_v0.md)

## 4. What Not To Build First

첫 build line에서는 아래를 먼저 열지 않는다.

- full agent/team shell
- live orchestration shell
- company/workspace ontology
- bidirectional program control
- full history suite
- full connections suite

즉 first line은 `VectorFL 중심 console + 두 개의 entry shell`까지만 잡는다.

## 5. Build Interpretation

이 build line은 기능 나열이 아니라
`VectorFL Page가 어떤 중심축으로 읽혀야 하는가`를 나타낸다.

즉:

- 첫 라인은 current-reading를 중심으로 만든다
- queue와 intake는 그것을 보조하는 입구로 만든다
- history와 program connection은 그 뒤에 붙인다

## 6. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 첫 build line은 Current Reading을 중심 console로 먼저 세우고, Cases / Queue와 Inputs / Intake를 그 주변 entry shell로 붙인 뒤, History / Trace와 Programs / Connections를 후속 panel로 확장하는 순서로 간다.`
