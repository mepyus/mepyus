# Codex Worklog Policy

## Decision

Codex가 이 저장소에서 수행한 작업은 append-only 로그로 남긴다.

## Why

- Codex의 판단과 구현 흔적도 이후 공간의 material이 될 수 있다.
- 작업 과정이 사라지면 formation path를 다시 읽을 수 없다.
- 결과만 남기면 왜 그런 선택을 했는지 lineage가 끊긴다.

## Log layers

### 1. Human-readable worklog

경로:

- `logs/runlogs/codex_worklog.md`

용도:

- turn 단위 작업 요약
- 판단 근거
- 리스크
- 다음 bounded step

### 2. Structured worklog

경로:

- `logs/audits/codex_worklog.jsonl`

용도:

- 이후 material ingest에 재사용 가능한 구조 로그
- turn, action, affected_paths, contract notes를 기계적으로 읽기 쉽게 보존

## Rules

- append-only로 남긴다.
- 기존 항목을 수정하지 않는다.
- 구현 완료 후 한 번 기록한다.
- 논의만 있었던 턴도 필요하면 남긴다.

## Minimum fields for structured log

- `worklog_id`
- `recorded_at`
- `kind`
- `summary`
- `affected_paths`
- `contract_notes`
- `next_step`
