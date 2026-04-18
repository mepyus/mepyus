# space wide line ecology observation report v0

## verdict

현재 공간은 `line을 만들고 표면화하는 능력`보다 `line이 전체 공간을 어떻게 순환하며 두꺼워지는지 보는 능력`이 약하다.

지금 가장 두껍게 커진 hub는 `multi_lens + operating surface + active/parked` 축이다.
반대로 `ontology`, `harness`, `human-language chronicle` 축은 살아 있지만, 아직 전체 공간을 다시 움직이는 reusable operator hub로는 충분히 자라지 못했다.

즉 현재 공간은
- local observation과 operating composition은 강하고
- whole-space ecology observation과 reusable line reuse는 약하다.

## what was actually inspected

이번 관찰은 새 spec 잠금이 아니라 아래 실제 재료를 다시 읽는 방식으로 진행했다.

- `docs/specs`
- `docs/notes`
- `docs/reports`
- `source_assets`
- `runtime/manifests/line_registry.json`
- `runtime/views/multi_lens_document_reading/*supervisor_surface*.json`
- `docs/reports/today_handoff_index_v1.md`
- `docs/reports/vectorfl_replica_repo_wide_structure_and_trace_survey_v1.md`
- `docs/reports/vectorfl_new_feature_starting_points_v1.md`
- `app/runtime/operating_ui_phase1.py`
- `app/core/runtime/multi_lens_runtime_flow.py`

## cluster concentration

관찰 시점의 대략적 file concentration은 아래처럼 보였다.

- `operating_multi_lens` 관련 문서: `157`
- `ontology` 관련 문서: `43`
- `harness` 관련 문서: `24`
- `chronicle_translation` 관련 문서: `15`

이 분포는 지금 공간이 무엇을 가장 많이 반복하고 있는지 보여준다.

현재 가장 큰 문서 밀도는
- `multi_lens`
- `operating surface`
- `active`
- `parked`

같은 운영 표면 축에 몰려 있다.

반면
- `ontology`
- `harness`
- `human language`
- `chronicle`

축은 살아 있지만, 아직 운영 표면 축만큼 두껍게 확장되지는 않았다.

## dominant hub

현재 공간의 실제 dominant hub는 `multi_lens / operating-ui / active-parked semantics`다.

근거:
- `operating-ui-phase1`에 observation panel chain이 실제로 들어가 있음
- `multi_lens_runtime_flow.py`에서 segmentation 이후 multi-lens observation이 실제 runtime flow에 연결돼 있음
- supervisor surface artifact에서 아래가 반복적으로 고정됨
  - `line_input_to_reading_organ = active`
  - `line_transition_over_surface = parked`
  - `decision_logic_in_runtime = false`

즉 이 축은
- 문서로 많이 잠겼고
- code call site가 있고
- surfaced artifact가 있고
- UI panel에도 올라가 있다.

이건 단순 선언이 아니라 실제 space materialization이 일어난 hub다.

## weaker but living hubs

`ontology`와 `harness`는 죽은 축이 아니다.
둘 다 내부 corpus reread와 human-language chronicle로 이미 여러 번 다시 읽혔다.

하지만 현재 상태를 보면 이 축들은
- 강한 operating panel
- runtime call site
- reusable operator

로 내려온 hub라기보다,
아직은 `의미가 반복적으로 호출되는 concept hub`에 더 가깝다.

### ontology

`ontology`는 현재 공간에서
- 반복적으로 호출되고
- 위험과 매혹이 함께 붙고
- 구조/검증/grounding 욕망을 드러내는 tension hub

로는 분명히 살아 있다.

하지만 아직은
- 다른 과업으로 직접 옮겨 쓰는 operator
- 구현 규칙으로 바로 내려가는 line

보다 `philosophical-operational tension hub` 성격이 더 강하다.

### harness

`harness`는 `ontology`보다 더 강하게 공간 안에 살아 있다.
특히
- control plane
- alignment-before-autonomy
- work absorption

축과의 연결은 이미 여러 문서에서 반복된다.

하지만 이것도 아직은
- 여러 과업으로 portable하게 재사용되는 operator

보다
- 운영 형식을 설명하는 thick concept hub

성격이 더 강하다.

## key mismatch

현재 가장 중요한 mismatch는 이거다.

### 1. docs are thick, runtime line memory is thin

문서 밀도는 높다.
하지만 `runtime/manifests/line_registry.json`을 보면 현재 네 line 모두 아래처럼 매우 얇다.

- `line_pre_read_eye`: `candidate`, support `0`
- `line_raw_return_preservation`: `candidate`, support `0`
- `line_input_to_reading_organ`: `stable`, support `0`
- `line_transition_over_surface`: `stable`, support `0`

즉 지금 공간은 문서/노트/리포트 차원에서는 line을 반복해서 말하고 있지만,
그 line의 supporting material, weakness pattern, caution pattern이 runtime memory에서 실제로 축적되는 구조는 아직 매우 약하다.

이건 중요한 신호다.

현재 line은
- 말해지고
- 설명되고
- 표면화되지만

아직 충분히 `material-backed growing line memory`로 자라지 못했다.

### 2. surfaced semantics are stable, but still local

supervisor surface artifact를 보면 active/parked semantics는 안정적이다.

- `line_input_to_reading_organ = active`
- `line_transition_over_surface = parked`
- `runtime_stops_after = surfaced_readout`

하지만 이 안정성은 아직 `local observational stability`에 가깝다.

즉 지금 space는
- 이 line을 어떻게 읽는지는 보여주지만
- 이 line이 다른 자료, 다른 과업, 다른 폴더를 어떻게 다시 읽는지

까지는 충분히 보여주지 못한다.

### 3. line is still closer to annotation than reusable operator

현재 line은
- reread
- observation
- chronicle

에는 쓰인다.

하지만 아직은
- 글쓰기
- 논문
- 발표
- 새로운 기능
- 내부 구조
- 스크립트

처럼 목적어가 바뀌어도 같은 structural demand를 재적용하는 operator로는 충분히 자라지 못했다.

그래서 지금의 line은 아직
`look here`
에 더 가깝고,
`use me like this in the next context`
까지는 못 간다.

## philosophy fit

이 mismatch가 곧바로 실패를 뜻하는 건 아니다.

오히려 현재 공간은 철학적으로는 꽤 일관되다.

맞는 부분:
- premature promotion을 막는다
- parked discipline이 있다
- runtime과 decision을 분리한다
- observation을 maturity로 과장하지 않는다

하지만 철학과 실제 성장의 간격도 보인다.

철학은 이미
- line emergence
- thickening
- reuse
- merge
- hub growth

를 상정한다.

그런데 실제 공간은 아직
- emergence 기록
- observation 표면
- close-out discipline

쪽이 더 강하고,
- reuse
- merge
- hub-to-hub transfer
- philosophy-fit reinspection

은 약하다.

즉 철학은 순환 생태를 가리키는데,
현재 materialization은 아직 observational-operating layer에 더 많이 머물러 있다.

## current reading

현재 공간을 한 문장으로 다시 읽으면 이렇다.

이 공간은 line을 만들어 문서와 runtime과 UI에까지 올릴 수 있는 observation engine으로는 분명히 자랐지만, 그 line이 다른 재료를 재독해하고 다시 재사용되며 hub를 키우는 전체 생태 시야는 아직 약해서, space-wide operator ecology보다는 well-structured observation ecology에 더 가깝다.

## why this matters

이 상태에서는 두 가지 위험이 생긴다.

### risk 1. lock-heavy growth

관찰보다 잠금이 더 빨리 늘어난다.
그러면 space는 안정적이지만 점점 문서화된 operating grammar에 머무를 수 있다.

### risk 2. user dependence remains

`ontology`, `harness` 같은 concept hub는 인간 언어 chronicle로는 다시 풀 수 있지만,
그 chronicle이 아직 line reuse operator로 내려오지 않기 때문에,
사용자는 계속 해석자 역할을 많이 맡아야 한다.

## next observation question

지금 필요한 다음 질문은 새 spec을 더 잠그는 것이 아니라 아래에 가깝다.

- 어떤 line이 실제로 다른 task family로 재적용되었는가
- 어떤 hub가 다른 hub를 읽는 데 재사용되었는가
- reusable operator로 자랄 line 후보는 무엇인가
- line registry runtime memory를 실제 재료 기반으로 두껍게 만들 수 있는가
- user language itself를 line source로 읽기 시작하면 어떤 hub가 새로 보이는가

## one-line conclusion

현재 공간은 이미 `line을 만들고 표면화하는 공간`으로는 많이 자랐지만, 아직 `그 line들이 전체 공간을 순환하며 다른 재료를 다시 읽고 reusable operator로 자라는 공간`으로는 충분히 가지 못했다. 지금 가장 두꺼운 것은 operating observation hub이고, 아직 가장 부족한 것은 whole-space line ecology vision이다.
