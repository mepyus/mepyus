# policy executor boundary draft

## 1. current diagnosis
- 현재 엔진의 핵심 실행 파일은 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 이다
- 이 파일은 지금까지는 잘 버텼지만, 다음 phase부터는 `family canonicalization rule` 과 `cross-path approval rule` 이 계속 들어올 가능성이 높다
- 현재 구조는 builder로 분해되어 있어 완전한 스파게티는 아니지만, 다음 단계에서 policy 로직이 계속 들어오면 executor 와 policy 가 강하게 결합될 위험이 크다
- 즉 지금 다음 병목은 viewer 나 translation 확대가 아니라 `policy/evaluator 결합` 이다

## 2. boundary proposal

### executor
- 역할:
  - material 수집
  - local space / pair selection
  - trace lookup
  - basis assembly
  - review payload orchestration
  - runtime persistence
- 현재 코드에서 executor 성격이 강한 지점:
  - `evaluate_mixed_path_pair`
  - `_find_best_cross_path_trace`
  - `_build_possibility_basis`
  - `_build_translation_gap_details`
  - `_build_promotion_blockers`
  - 최종 payload 조립과 반환

### policy
- 역할:
  - 어떤 evidence 를 direct corroboration 으로 볼지
  - translated / derived / direct evidence 를 어디까지 인정할지
  - family별 canonicalization rule
  - threshold / corroboration / approval 조건
  - review candidate / canonical review candidate / canonical readiness 판정
- 현재 코드에서 policy 성격이 강한 지점:
  - `_build_anchor_review`
  - `_build_threshold_review`
  - `_build_cross_path_review`
  - `_build_cross_path_canonicalization_review`
  - `_build_direct_overlap_review`
  - `_build_space_entry_review`
  - `_promotion_readiness_class`
  - `_promotion_decision`

### output / review surface
- 역할:
  - policy 결과를 사람이 읽을 수 있게 설명 필드로 남김
  - blocker, readiness, proposal, state, vector 표현
- 현재 코드에서 output 성격이 강한 지점:
  - `_build_promotion_review`
  - 보고서 문서들

## 3. split recommendation

### phase 1
- 지금은 코드 이동보다 경계선만 잠근다
- executor 는 `data gathering + orchestration`
- policy 는 `evidence interpretation + approval logic`
- output 은 `human-readable explanation`

### phase 2
- 다음 코드화 시 아래처럼 분리하는 것이 적절하다
  - `app/core/runtime/review_executor.py`
  - `app/core/runtime/policies/semantic_canonicalization.py`
  - `app/core/runtime/policies/structural_canonicalization.py`
  - `app/core/runtime/policies/object_canonicalization.py`
  - `app/core/runtime/policies/cross_path_overlap.py`
  - `app/core/runtime/review_surface.py`

## 4. policy candidates
- `evaluate_semantic_canonicalization(...)`
- `evaluate_structural_canonicalization(...)`
- `evaluate_object_canonicalization(...)`
- `evaluate_cross_path_overlap_policy(...)`
- `evaluate_direct_overlap_promotion(...)`
- `evaluate_space_entry_policy(...)`

## 5. minimal interface sketch

```python
def evaluate_structural_canonicalization(
    *,
    live_evidence: dict,
    imported_evidence: dict,
    best_local_ref: str,
    current_overlap: dict,
) -> dict:
    ...
```

```python
def evaluate_cross_path_overlap_policy(
    *,
    anchor_review: dict,
    live_side_review: dict,
    translation_alignment: dict,
) -> dict:
    ...
```

```python
def evaluate_space_entry_policy(
    *,
    gate_vector: dict,
    anchor_review: dict,
    direct_overlap_review: dict,
) -> dict:
    ...
```

## 6. file map from current code

### executor-heavy now
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):108
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):798

### policy-heavy now
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1035
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1075
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1168
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1446
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1551
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1661

## 7. what not changed
- viewer 안 건드림
- canonical 기준 안 건드림
- translation 범위 안 늘림
- processing refinement 재개 안 함
- `live_input_space.py` 전면 분해 안 함

## 8. next recommendation
- 실제 코드화 1순위는 `cross-path overlap / family canonicalization policy` 분리다
- 특히 `structural` family부터 policy 모듈로 분리하는 것이 좋다
- `output surface` 분리는 그 다음에 해도 된다

## 9. final sentence
- 다음 phase에서 가장 위험한 건 규칙이 executor 안으로 계속 누적되는 것이다
- 따라서 지금은 `executor = orchestration`, `policy = approval logic`, `output = readable review surface` 라는 경계선을 먼저 잠가야 한다
