# Bootstrap Scope

## Goal

초기 부트스트랩 단계의 목표는 완성 엔진이 아니라 contract-safe scaffold를 세우는 것이다.

## Included now

- Python project skeleton
- immutable core models
- state enums
- append-only event schema
- file-backed runtime storage
- minimal formation service boundary
- contract alignment tests

## Excluded now

- semantic ranking
- point promotion
- cluster synthesis
- automatic merge
- reader vocabulary integration
- control-plane orchestration

## Reason

`vectorfl`에서 반복된 실수는 중간 형성 단계를 충분히 보존하지 않은 채 너무 빨리 판정 구조로 이동하는 것이었다.
이번 부트스트랩은 그 반대 방향을 강제한다.
