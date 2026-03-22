# Phase-Compressed Timeline Policy

## Decision

session timeline은 단순 event list 외에 reaction phase로 압축해서 읽을 수 있어야 한다.

## Current rule

- 같은 reaction kind가 연속되면 하나의 phase로 묶는다.
- 각 phase는 `reaction_kind`, `start_at`, `end_at`, `event_count`, `cell_ids`를 가진다.
- 이는 session timeline의 읽기 효율을 높이기 위한 observer 표현이다.

## Why

- 세션의 공간 변화를 event 하나씩 읽으면 흐름 감각이 약하다.
- phase로 압축하면 thickening phase, split phase, relocation phase 같은 국면을 빠르게 볼 수 있다.

## Follow-up risk

- 현재 phase는 contiguous reaction kind만 기준으로 압축한다.
- 다음 단계에서 pressure signature 변화까지 phase 경계에 반영할 수 있다.
