# reconstruction_supervisor_fixture_check_scope_note_v1

## purpose

- `scripts/run_reconstruction_supervisor_fixture_check.py`는 reconstruction supervisor builder의 bounded invariant를 확인하는 fixture check다.

## checks

- non-governing guard 유지
- read-only reconstruction 유지
- pointer-backed latest 유지
- receipt / views / sidecar 역할 분리 유지
- selection trace 존재 확인

## non-goals

- semantic quality 평가
- decision correctness 평가
- runtime 본체 연결 검증
