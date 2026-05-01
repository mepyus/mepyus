# Run Record: Run 032

## 0. Meta
- run_id: 032
- title: Tool Affordance / Caller Shift Lens v0 Creation
- timestamp: 2026-04-29
- actor: Gemini (Agent)
- packet_ref: Minimal Brief for Run 032
- status: COMPLETED

## 1. Intent
'Operating Order Principles v0'의 핵심 원칙인 Affordance, Program as Material, Plan before Execution을 실제 샌드박스 작업에서 사용할 수 있는 분석 렌즈(`tool_affordance_caller_shift_lens_v0.md`)로 구체화함.

## 2. Actions Performed
- [x] 핵심 참조 문서 7개 surgical read (principles, source_map, pipeline, role_map, handoff, provenance, output_contract)
- [x] 'Principles v0' 내 #2, #10, #11 원칙 분석 및 렌즈 항목 도출
- [x] `app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md` 작성
- [x] 샌드박스 표준 출력 계약(Standard Output Contract v0) 준수 확인

## 3. Findings & Decisions
- **Caller Shift Risk**: 호출자가 인간에서 LLM으로 바뀔 때 '상식적 제동'이 사라지는 것을 핵심 위험으로 정의하고, 이를 보완하기 위한 명시적 경로 제약과 Preflight 중단점을 렌즈에 포함함.
- **Affordance as Handle**: 도구의 기능 설명보다 "언제 쓰지 말아야 하는지"와 "누가 써야 하는지"를 정의하는 것이 운영 질서 유지에 더 중요하다고 판단함.
- **Program as Material**: 기존 프로그램을 단순 기능(Function)으로 보지 않고, 상태 변이 위험과 세션 역할 적합성을 따지는 '재료'로 정의함.

## 4. Boundary Check
- source_space_modified: false
- baseline_created: false
- relay_v1_declared: false
- worker_guide_modified: false
- automation_created: false
- agent_implementation_created: false
- tool_installed: false

## 5. Missing Reference Note
- `principles_v0.md`에서 missing으로 표시되었던 `sandbox_promotion_pipeline_v0.md`와 `session_role_map_v0.md`가 실제로는 `outputs` 폴더에 존재함을 확인하고 참조에 포함함.

## 6. Closeout
Run 032의 목적에 따라 최소한의 가이드라인 하에 도구(Gemini)의 판단을 담은 렌즈 초안 작성을 완료함. 이 결과물은 사용자 리뷰를 거쳐 사후 분석 및 운영 질서 보강의 재료로 사용됨.
