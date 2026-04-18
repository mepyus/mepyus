# processor_compare root retention note v1

## 판단

`app/work/processor_compare` 는 support cluster이지만 현재는 root `app/work` 에 남긴다.

## 이유

- `app/core/runtime/live_input.py` 가 anchor pipeline을 직접 사용한다.
- `app/core/runtime/runtime_observer_baseline.py` 가 observer engine을 직접 사용한다.
- `scripts/ingest_fragments.py`, `scripts/apply_internal_observer.py`, `scripts/apply_anchor_engine_to_processor_docs.py` 같은 실행 경로가 직접 물고 있다.
- 즉 이 폴더는 단순 과거 실험 보관소가 아니라, 여전히 현재 runtime sidecar의 실행 기반이다.

## 정리 규칙

- reports/standards 가 많아도 지금은 archive belt로 내리지 않는다.
- 대신 root 잔류 이유를 문서로 잠그고, 나중에 import 경계가 풀릴 때만 재검토한다.
- 재검토 조건은 `app.core.runtime.*` 와 scripts 의 직접 import 제거다.
