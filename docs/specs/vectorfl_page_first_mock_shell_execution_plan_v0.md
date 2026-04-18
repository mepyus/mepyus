# VectorFL Page First Mock Shell Execution Plan v0

이 문서는 현재까지 잠근 구조와 rewrite brief를 기준으로  
`VectorFL Page` 첫 mock shell을 어떤 순서로 만들지 실행 단계만 짧게 고정한다.  
목적은 full 구현 전에 첫 mock을 작게, current-reading 중심으로 여는 것이다.

## 1. Goal

첫 mock shell의 목표는 아래다.

- Paperclip frame 감각을 참고하되 VectorFL semantics로 다시 읽힌다
- `Current Reading`이 중심 console로 보인다
- `Cases / Queue`와 `Inputs / Intake`는 entry shell로 붙는다
- governance / weakness / trace가 숨겨지지 않는다

즉 첫 mock은 `VectorFL다운 current-reading shell capability` 확인용이다.

## 2. Build Order

### step 1. Current Reading fixture 준비

- 기준 문서:
  - [vectorfl_current_reading_mock_fixture_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_mock_fixture_contract_v0.md)
  - [vectorfl_current_reading_mock_fixture_set_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_mock_fixture_set_v0.md)
- 산출물:
  - mock JSON fixture set 1개

### step 2. Current Reading console shell mock

- 기준 문서:
  - [vectorfl_current_reading_console_shell_rewrite_brief_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_console_shell_rewrite_brief_v0.md)
  - [vectorfl_current_reading_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_adapter_contract_v0.md)
- 확인할 것:
  - case header
  - current reading body
  - lane strip
  - governance side
  - trace strip
  - optional caution note

### step 3. Cases / Queue entry shell

- 기준 문서:
  - [vectorfl_cases_queue_shell_rewrite_brief_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_cases_queue_shell_rewrite_brief_v0.md)
  - [vectorfl_cases_queue_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_cases_queue_adapter_contract_v0.md)
- 확인할 것:
  - current-reading 진입용 row snapshot만 보이는지
  - queue가 해석면을 대체하지 않는지

### step 4. Inputs / Intake entry shell

- 기준 문서:
  - [vectorfl_inputs_intake_shell_rewrite_brief_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_inputs_intake_shell_rewrite_brief_v0.md)
  - [vectorfl_inputs_intake_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_inputs_intake_adapter_contract_v0.md)
- 확인할 것:
  - source/context/block/weakness/readiness가 살아 있는지
  - next-lane hint가 canonical decision처럼 보이지 않는지

## 3. Scope Guard

첫 mock shell에서는 아래를 하지 않는다.

- live integration
- bidirectional program action
- agent/team UI
- company/issue ontology 도입
- full history suite
- full programs/connections suite

즉 first mock은 `current-reading-first shell`까지만 연다.

## 4. Success Criteria

아래가 보이면 first mock은 성공으로 본다.

- current-reading body가 중심으로 보임
- governance가 side에서 숨겨지지 않음
- trace/residue/reentry가 preview로 보임
- queue row가 얕은 snapshot으로 current-reading 진입을 돕음
- intake가 source/context/block/weakness 중심으로 읽힘
- 전체 shell이 issue board가 아니라 VectorFL Page처럼 읽힘

## 5. Immediate Inputs

현재 바로 사용할 수 있는 입력은 아래다.

- [vectorfl_current_reading_mock_fixture_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_current_reading_mock_fixture_v0.json)
- 이 fixture는 first mock의 기준 case로 사용한다

## 6. Final Plan Sentence

현재 기준의 first mock shell execution plan은 다음 문장으로 잠근다.

`먼저 Current Reading fixture와 console shell을 만들고, 그 다음 Cases / Queue와 Inputs / Intake를 entry shell로 붙여, current-reading-first VectorFL Page가 issue board가 아니라는 점을 먼저 증명한다.`
