# operating ui validation override isolation v1

## 1. verdict

완료.

이번 작업은 새 기능 추가가 아니라,
`live_mode`, `compare_mode` 같은 validation-only override를
`operating_ui_live`의 main assembly 흐름에서 분리해
코드 구조상으로도
**normal operating path**와
**validation-only path**의 경계를 더 분명하게 만든 작업이다.

## 2. modified files

- [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

## 3. separation summary

### before

main assembly 안에 아래가 직접 섞여 있었다.
- validation query normalization
- controlled unavailable path 분기
- compare panel controlled override resolution

### after

분리된 helper:
- ` _resolve_validation_overrides(...)`
- `_build_compare_panel_with_validation(...)`
- `_resolve_compare_panel_validation(...)`

구조 읽기:
1. validation query normalize
2. controlled unavailable path 조기 분기
3. normal live payload build
4. normal shell assembly
5. compare panel에만 validation override 후단 적용

즉 validation-only logic은 이제
main live composition의 본체가 아니라
**제한된 보정층**처럼 읽힌다.

## 4. behavior unchanged check

검증 케이스:
- default live
- valid asset
- invalid asset
- `live_mode=unavailable`
- `compare_mode=empty`
- `compare_mode=no_selected`
- `compare_mode=state_unavailable`
- unknown `live_mode`
- unknown `compare_mode`

결과:

| case | result |
| --- | --- |
| default | unchanged |
| valid asset | unchanged |
| invalid asset | unchanged |
| `live_mode=unavailable` | unchanged |
| `compare_mode=empty` | unchanged |
| `compare_mode=no_selected` | unchanged |
| `compare_mode=state_unavailable` | unchanged |
| unknown `live_mode` | normalized to baseline live path |
| unknown `compare_mode` | normalized to baseline compare panel path |

## 5. why this helps

- baseline live path가 먼저 읽힌다
- validation-only override가 기능처럼 보이지 않는다
- compare panel controlled override가 right-column panel에만 국한된다는 점이 코드 구조에서도 드러난다
- 이후 validation query를 더 붙일 때도 어디에 놓여야 하는지 기준이 선다

## 6. remaining limitations

- validation override는 여전히 같은 파일 안에 있다
- 별도 helper module로 완전 분리하지는 않았다

하지만 현재 단계에서는:
- semantics unchanged
- minimal file touch
- readability improvement
이 우선이라 이 정도 분리까지만 하는 것이 적절하다
