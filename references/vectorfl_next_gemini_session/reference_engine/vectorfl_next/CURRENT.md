# Current Status

## Current diagnosis

- 1차 formation core scaffold가 들어가 있다.
- 불변 모델, 상태 enum, append-only event schema, 파일 기반 저장소, 최소 formation service가 있다.
- 아직 형성 알고리즘은 거의 비어 있다.

## What is intentionally missing

- point ranking
- cluster formation
- promotion logic
- reader physics
- scoring optimization
- visualization

## Current risks

- pressure 변화가 실제 경로를 어떻게 바꾸는지 아직 구현되지 않았다.
- reentry가 구조적으로만 열려 있고 formation rule로 연결되지 않았다.
- 기존 `runtime/` 디렉터리 이름 일부는 새 계약 언어와 완전히 맞지 않는다.

## Active discipline

- 구현 전에 계약 위반 위험을 먼저 점검한다.
- 애매하면 checklist 또는 decision 문서를 먼저 만든다.
- `vectorfl`의 stage 언어를 새 코어 언어로 들여오지 않는다.
- Codex 작업은 `logs/runlogs/codex_worklog.md`와 `logs/audits/codex_worklog.jsonl`에 append-only로 남긴다.
- 점보다 공간을 먼저 만든다.
- 입력 taxonomy보다 material baseline과 formation role을 먼저 본다.
