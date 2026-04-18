# controlled validation query contract v1

## 1. purpose

이 문서는 operating UI에서 쓰이는 controlled validation query를
일반 운용 query와 분리해 잠그는 문서다.

핵심 목적:
- `live_mode`, `compare_mode`를 실사용 기능처럼 오해하지 않게 한다
- validation-only override가 baseline semantics를 오염시키지 않게 한다

## 2. allowed validation params

### live_mode

purpose:
- live unavailable path를 controlled하게 재현

allowed values:
- `unavailable`

unknown values:
- ignored
- baseline live path로 내려감

### compare_mode

purpose:
- compare panel state를 controlled하게 재현

allowed values:
- `empty`
- `no_selected`
- `state_unavailable`

unknown values:
- ignored
- baseline compare panel behavior로 내려감

## 3. non-goals

이 query들은 아래를 위한 것이 아니다.

- 일반 사용자 affordance
- persistent preference
- 기능 toggle
- route-driven workflow
- recommendation/search/filter semantics

즉:
- validation query는 기능이 아니라
  **controlled test override**다

## 4. normal operating query boundary

normal operating query:
- `asset_id`
- `sort_by`

validation-only query:
- `live_mode`
- `compare_mode`

원칙:
- normal operating query는 운용 의미를 바꾼다
- validation-only query는 검증용 표면 override만 만든다
- validation-only query가 baseline state semantics를 다시 정의하면 안 된다

## 5. normalization rule

- 허용된 값만 반영
- unknown 값은 무시
- 무시된 경우 baseline live 동작을 유지

즉:
- `live_mode=weird` -> `None`
- `compare_mode=weird` -> `None`

## 6. surface hygiene

- control bar / page / panel은 이 query를 일반 기능처럼 설명하지 않는다
- validation override는 최소 범위에서만 작동한다
- unavailable의 주 설명은 계속 control bar / page fallback이 맡는다
- compare panel override는 compare panel 상태에만 한정된다

## 7. future extension gate

앞으로 validation query를 확장하려면 아래 질문을 먼저 통과해야 한다.

1. 일반 운용 semantics를 오염시키지 않는가
2. validation-only임을 명확히 유지하는가
3. state axis / vocabulary를 흔들지 않는가
4. route/query contract를 기능 affordance처럼 키우지 않는가

이 질문 중 하나라도 애매하면 guarded review가 필요하다.
