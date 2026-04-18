# executable capability registry note v0

## Purpose

실행 스크립트가 늘어날수록 폴더 분류만으로는 충분하지 않다.

같은 기능이:

- 입력기
- 라벨기
- 앵커기
- 내부 루프
- validation chain
- sandbox probe

처럼 서로 다른 표면에 흩어질 수 있기 때문이다.

그래서 이 문서는 `무슨 파일이 있나`보다
`무슨 capability가 있고, 어떤 entrypoint가 그 capability를 호출하나`를 먼저 읽게 하기 위한 잠금이다.

## Core rule

- primary unit is `capability`
- script path is only one access surface
- later reference / reuse should start from intent alias, not exact filename

## Stored surfaces

- machine-readable registry:
  - [executable_capability_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/executable_capability_registry_v0.json)
- human-readable quick index:
  - [executable_runner_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/notes/executable_runner_index_v0.md)

## Why both are needed

- runner index is fast for humans
- capability registry is better for later lookup, grouping, and reference-style reuse

The runner index says:
- what to run

The capability registry says:
- what kind of thing this is
- what it touches
- how safe it is
- what user intent aliases should resolve to it

## Current capability classes

- `inputter`
- `inputter_probe`
- `inputter_component`
- `labeler`
- `anchorizer`
- `loop`
- `loop_probe`
- `grounded_feed`
- `summary_sink`
- `validation_chain`
- `sandbox_probe`

## Reading rule

When new script bundles appear later:

1. do not only place them in folders
2. record them as a capability
3. assign:
   - capability class
   - intent aliases
   - entrypoint refs
   - output surfaces
   - safety mode

That is what will make later reference-style reuse possible even when the exact command is not remembered.
