# PROGRAM_FRAME_V0

## 1. 목적 (Goal)
- 샌드박스 단위의 파편적 실험을 종료하고, VectorFL 공간을 외부 도구(Codex, OmX, Hermes, Gemini 등)가 **직접 검색하고 활용할 수 있는 구조적 어댑터**로 전환함.
- 외부 도구가 작업을 수행하기 전, VectorFL의 기존 기록(SSOT)을 먼저 검색하여 세션을 셋업하도록 강제함.

## 2. 작업 철학 (Philosophy)
- **Tool-Readable Space**: VectorFL의 모든 공간 기록은 외부 도구가 읽을 수 있는 인터페이스(README, Index, Boundary 등)로 정렬됨.
- **Search-First Pipeline**: 도구는 새로운 상상을 구현하기 전에, 해당 목적과 관련된 과거 기록을 검색하여 맥락을 확보해야 함.
- **No Implementation/Automation**: 도구의 역할은 "검색-이해-제안"까지임. 실제 구현이나 배포는 사용자/CLI의 승인 하에 원자적으로 이루어짐.

## 3. 운영 방식 (Operating Method)
- **1회 관통(First Pass)**: 프로그램 전반의 구조를 한 번에 연결하여 전체 흐름을 확인.
- **문제 기록(Issue Log)**: 즉시 해결 불가능한 파편적 문제는 세션 중단 없이 기록 후 사후 점검.
- **재구성(Second Pass)**: 1회차 경험을 바탕으로 실제 사용 가능한 최적 구조로 구조 재편.

## 4. 경계 (Hard Boundaries)
- 무단 실행(Runner, Router, Controller) 금지.
- 무단 구조 변경(DB, Schema, Registry) 금지.
- 최종/준비됨/검증됨 등의 단정적 언어 사용 금지.
- 사용자의 판단권을 최우선으로 보존.

## 5. 역할 분담 (Role Split)
- **User**: 의사결정권자, 승인자.
- **Codex/CLI**: 공간 검색, 인터페이스 셋업, 실행 어댑터.
- **Gemini**: 메타 분석, 비교, 구조 확장 지원.
- **VectorFL Space**: 모든 작업의 근간이 되는 단일 진실 공급원(SSOT).
