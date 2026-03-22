# Session-Scoped Observer Policy

## Decision

reactive observer는 session 단위로도 잘라 읽을 수 있어야 한다.

## Current rule

- `session_id`를 주면 해당 session material을 포함한 cell만 관찰 대상으로 삼는다.
- family scope와 마찬가지로 코어 객체를 바꾸지 않고 읽기만 한다.

## Why

- 같은 세션 안에서 공간이 어떻게 두꺼워지거나 갈라졌는지 읽는 것은 중요하다.
- session scope는 작업 흐름 단위 관찰에 가깝다.

## Follow-up risk

- 아직 duration-based recent window와 함께 조합한 시계열 분석은 거칠다.
