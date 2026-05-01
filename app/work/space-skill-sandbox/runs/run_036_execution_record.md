# Run Record: Run 036

## 0. Meta
- run_id: 036
- title: Tool Affordance Lens v0.1 Evidence-based Risk Naming Patch
- timestamp: 2026-04-29
- actor: Gemini (Agent)
- packet_ref: Minimal Brief for Run 036
- status: COMPLETED

## 1. Intent
Run 034/035에서 드러난 '보안 용어 오용 및 위험 오판' 사례를 바탕으로 Tool Affordance Lens를 v0.1로 업데이트하여 판단의 기술적 정밀도를 높이고 운영 질서를 보강함.

## 2. Actions Performed
- [x] `outputs/tool_affordance_caller_shift_lens_v0.md` 읽기
- [x] 'Evidence-based Risk Naming' 원칙 및 위험 분류 체계(Risk Classification) 설계
- [x] Run 034 사례를 Case Study로 포함한 `v0.1` 문서 작성
- [x] 샌드박스 표준 출력 계약 준수 및 경계 확인

## 3. Findings & Decisions
- **정밀도 강화**: "그럴듯한 용어" 대신 "코드 기반 증거"를 요구하도록 렌즈를 패치함.
- **학습 보존**: Run 034의 오판을 지우지 않고 렌즈 내의 공식 사례로 기록하여 반복되는 실수를 방지함.
- **분류 체계 도입**: `Risk Candidate`에서 `Confirmed Risk`로 가는 명시적 단계를 정의함.

## 4. Boundary Check
- source_space_modified: false
- baseline_created: false
- tool_installed: false
- automation_created: false
- existing_program_modified: false

## 5. Closeout
Tool Affordance Lens v0.1 패치를 완료함. 이제 에이전트는 더 신중하고 근거 중심적인 위험 분석을 수행해야 함.
