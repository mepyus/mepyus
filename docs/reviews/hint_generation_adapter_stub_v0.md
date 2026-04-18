# Hint Generation Adapter Stub v0

## 목적

이 문서는
[auto_hint_generation_rules_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/auto_hint_generation_rules_v0.json)
을 실제로 읽어
artifact에서 hint candidate를 뽑는 최소 실행 stub를 고정한다.

실행 스크립트:

- [run_auto_hint_generation_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_auto_hint_generation_stub.py)

핵심 로직:

- [auto_hint_generation.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/auto_hint_generation.py)

## stub 범위

이 stub는 아래까지만 한다.

- JSON artifact 하나를 읽는다
- rules registry를 읽는다
- `match_all` bundle을 검사한다
- matching rule마다 hint candidate를 만든다
- 결과를 JSON으로 출력한다

추가로 `--save` 를 쓰면
[source_to_family_hints_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_to_family_hints_v0.json)
형식 manifest에 첫 hint candidate를 append/update 한다.

즉 아직 classifier나 prebias를 직접 실행하지는 않지만,
hint 저장까지는 연결할 수 있다.

## 현재 지원 pattern

- `field.path=value`
- `field.path exists`
- `items[].field exists`

즉 v0는
현재 만든 세 family 대표 bundle을 돌리기에 충분한 최소 matcher다.

## expected use

예:

```bash
python3 scripts/run_auto_hint_generation_stub.py app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json
python3 scripts/run_auto_hint_generation_stub.py runtime/preflight_last_decision.json
python3 scripts/run_auto_hint_generation_stub.py runtime/views/engine_state_latest/index.json
python3 scripts/run_auto_hint_generation_stub.py runtime/current_phase.json --first-only --save
```

## 현재 의미

이 stub가 생기면서
auto hint generation은 더 이상 문서만이 아니라
실제로 artifact에 대해 first hint candidate를 뽑아볼 수 있는 단계가 된다.

## 한 줄 요약

hint generation adapter stub v0는
JSON artifact와 bundle rules를 받아
first family/projection/route hint candidate를 출력하고 필요하면 hint manifest에 저장하는 최소 실행 도구다.
