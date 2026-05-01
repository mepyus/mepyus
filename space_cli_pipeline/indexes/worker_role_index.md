# Worker Role Index

## Space (The Body)
- **Allowed**: Intake, Memory Retrieval, Reflux.
- **Forbidden**: -
- **Must be reviewed as**: 중심 운용 본체. 단, 최종 lock/baseline 결정은 User 승인 필요.

## User (Director)
- **Allowed**: User retains final direction, approval, and baseline/lock decision.
- **Forbidden**: -
- **Must be reviewed as**: Final Authority.

## Codex (Expert)
- **Allowed**: Structure design, documentation, patches, review.
- **Forbidden**: Arbitrary baseline lock without User approval.
- **Must be reviewed as**: `worker_return`.

## Gemini (Assistant)
- **Allowed**: Draft, verification, testing, listing, initial read.
- **Forbidden**: Final judgment, code editing by default, structure design.
- **Must be reviewed as**: `worker_return`.
