# build_reconstruction_supervisor_surface_scope_note_v1

## in scope

- `scripts/build_reconstruction_supervisor_surface.py` 초안 구현
- `runtime/observer/exploration`, `runtime/receipts`, `runtime/views`를 read-only로 재구성
- `runtime/views/reconstruction_supervisor/` 아래 `json + md`와 `latest pointer` 생성

## out of scope

- runtime 본체 연결
- decision logic 추가
- governing behavior 추가
- state mutation
- receipt, view, sidecar contract 변경

## lock

- 이 builder는 surfaced-first / pointer-backed reconstruction only를 수행한다.
