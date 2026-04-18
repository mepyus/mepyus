# exploration_observation_layer_v1

## purpose
탐색 결과를 읽었음 수준으로 흘려보내지 않고,
session / run 기준으로 얇게 반복 기록할 수 있는
runtime observer sidecar 층을 고정한다.

## location
- `runtime/observer/exploration/`
- `runtime/observer/exploration/json/`
- `runtime/observer/exploration/md/`

## principles
- 코어 본체 변경보다 observer sidecar 를 우선한다.
- append-only 감각을 유지한다.
- session_id / run_id / source_ref 연결 가능해야 한다.
- heavy DB / complex pipeline 없이 json / md sidecar 로 충분하다.
- refinement pass 에서 다시 읽을 수 있어야 한다.

## minimum fields
- `exploration_id`
- `session_id`
- `run_id`
- `observed_at`
- `source_ref`
- `source_type`
- `observation_type`
- `candidate_slots`
- `kept_as_core_candidate`
- `kept_as_outer_candidate`
- `deferred_items`
- `deferred_reason`
- `future_use_hint`
- `next_action_hint`
- `notes`

## optional fields
- `related_run_ids`
- `related_session_ids`
- `evidence_refs`
- `translation_candidate_notes`
- `user_facing_phrase_candidates`

## observation type set
- `pattern_seen`
- `relation_repeat`
- `reusable_translation`
- `defer_needed`
- `refinement_candidate`
- `outer_only_reading`

## file role split

### json sidecar
- 기계 판독용 최소 구조
- refinement 후보 판독과 누적 관찰에 사용

### md sidecar
- 사람이 읽는 해석 메모
- user language readout 과 notes 를 담는 보조 읽기면

## boundaries
- 정식 translation layer 를 지금 만들지 않는다.
- core semantics 를 직접 수정하지 않는다.
- relation_kind 최종 잠금 장치로 오해하지 않는다.

## reading
- exploration observation 은 “결론 확정”이 아니라 “현재 판독과 보류 이유”를 남기는 층이다.
