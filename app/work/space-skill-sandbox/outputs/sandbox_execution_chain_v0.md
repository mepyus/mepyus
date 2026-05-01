# Sandbox Execution Chain v0

## 0. Status
- status: sandbox candidate
- automation: false
- relay_v1: false
- source_space_rule: false
- baseline: false

## 1. Purpose
이 문서는 Codex와 Gemini의 직렬 분업 구조를 sandbox 안에서 운영하기 위한 실행 체인 후보 문서다.

핵심 원칙:

Codex는 repo 상태, 파일 구조, run 기록, validation, next packet 생성을 담당한다.
Gemini는 Codex가 만든 task packet을 바탕으로 무거운 분석/작성 작업을 수행한다.
사용자는 두 도구 사이의 최종 판단자이자 전달자다.

## 2. Role Split

### Codex Role
- repo 상태 확인
- 생성 파일 확인
- 누락 파일 확인
- 다음 run 번호 결정
- next Gemini task packet 작성
- validation record 작성
- closeout 보고

Codex must not:
- source-space promotion
- baseline creation
- Relay v1.0 declaration
- worker guide modification
- automation
- MCP / hook / watch mode
- agent implementation
- production workflow
- existing program merge

### Gemini Role
- task packet 기반 분석/작성
- sandbox output 문서 작성
- run record 작성
- validation record 작성
- closeout 보고

Gemini must not:
- source-space 수정
- baseline 선언
- Relay v1.0 선언
- worker guide 수정
- 자동화 구현
- repo 구조 임의 변경

### User Role
- Codex가 만든 packet을 Gemini에게 전달
- Gemini 결과를 Codex 또는 reviewer에게 전달
- 최종 판단

## 3. Execution Queue
1. Run 032 - Tool Affordance / Caller Shift Lens v0 - Gemini
2. Run 033 - Run 032 Validation + Next Packet - Codex
3. Run 034 - Existing Program Integration Lens v0 - Gemini
4. Run 035 - Run 034 Validation + Next Packet - Codex
5. Run 036 - Intent-Level Route Map v0 - Gemini
6. Run 037 - Run 036 Validation + Next Packet - Codex
7. Run 038 - Skill Metadata Discipline Lens v0 - Gemini
8. Run 039 - Cross-review of Run 031~038 - Codex

## 4. Handoff Rule
Codex는 각 검증 run 이후 다음 Gemini task packet을 생성한다.

파일명 규칙:

```text
next_gemini_task_packet_run_XXX_short_name_v0.md
```

각 packet에는 다음을 포함한다.

- mode
- purpose
- input references
- created files
- forbidden actions
- required sections
- validation checks
- closeout statement
- final report format

## 5. Non-Automation Note
이 문서는 자동화가 아니다.
이 문서는 Relay v1.0이 아니다.
이 문서는 agent implementation이 아니다.
이 문서는 source-space rule이 아니다.
이 문서는 Codex/Gemini 사이의 수동 직렬 실행 체인 후보일 뿐이다.

## 6. Closeout Note
This document is a sandbox execution chain candidate only.
No automation was created.
No Relay v1.0 was declared.
No source-space promotion was performed.
No baseline was created.
No worker_guide_v0_4 was created.

## 7. 4-line Footer
status: 완료
summary: sandbox_execution_chain_v0는 Codex를 구조/검증/next packet 담당, Gemini를 무거운 분석/작성 담당으로 나누는 수동 직렬 실행 체인 후보를 기록함
risk: 이 문서를 자동화, Relay v1.0, agent implementation, source-space rule, baseline으로 오해하면 안 됨
next: next_gemini_task_packet_run_032_tool_affordance_v0.md를 사용자 판단에 따라 Gemini에게 전달
