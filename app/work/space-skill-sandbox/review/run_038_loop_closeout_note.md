# Affordance Lens Learning Loop Closeout Note

## 1. Loop Overview
Run 032부터 Run 037까지 진행된 'Tool Affordance / Caller Shift Lens' 실험 루프를 마감한다. 이 루프는 운영 질서 원칙 #2, #10, #11을 실제 분석 도구로 구체화하고, 도구(Gemini)의 판단 오류를 통해 운영 하네스(Harness)를 보강하는 과정이었다.

## 2. Learning History

### v0 렌즈의 성과 (Run 032)
- **잘한 것**: 호출자가 인간에서 LLM으로 바뀔 때의 '상식 상실' 위험을 포착하고, 기능을 넘어선 '운영 손잡이(Affordance)' 개념을 도입함.

### 오판과 교정 (Run 034, Run 035)
- **오판 (Run 034)**: `scripts/sandbox/run_gemini_packet.sh` 분석 중 'Shell Injection'이라는 강력한 보안 용어를 오용함.
- **교정 (Run 035)**: 기술적 전수 조사를 통해 모든 변수가 인용 부호(Quoting)로 보호됨을 확인하고, 위험을 `Filename Pollution`으로 재분류함. "보안 용어 남용(Risk Naming Hallucination)" 시그널을 식별함.

### v0.1 보강 및 검증 (Run 036, Run 037)
- **보강 (Run 036)**: "Risk Naming Requires Evidence" 원칙과 위험 분류 체계(Confirmed/Candidate/Refuted)를 도입함.
- **검증 (Run 037)**: `app/generate_folder_status.py` 분석 시, 쉘 주입 주장을 스스로 **REFUTED** 처리하고 실제 위험인 **File Overwrite**를 **CONFIRMED**로 정확히 짚어냄. 판단의 노이즈가 획기적으로 감소함.

## 3. Current Status & Precautions
- **Current Status**: Lens v0.1은 샌드박스 내 기존 프로그램 분석을 위한 '안전한 필터'로 작동 가능함.
- **Precautions**: 에이전트는 여전히 "위험해 보이는 현상"을 "치명적 보안 사고"로 연결하려는 경향이 있으므로, `Refuted Claim` 섹션을 적극적으로 활용해야 함.

## 4. Next Step Requirements
더 복잡한 기존 프로그램(DB, Network 포함)으로 확장하기 위한 최소 조건:
1. **Evidence Source Mapping**: 코드 라인 번호뿐만 아니라, 실제 데이터 흐름(Data Flow)을 추적할 수 있는 툴(grep 등)의 병행 사용.
2. **Session Role Isolation**: 분석된 도구가 영향을 미칠 수 있는 세션 역할의 쓰기 권한이 엄격히 격리된 상태여야 함.
3. **Preflight First**: 모든 분석 결과는 해당 도구의 `--preflight` 또는 `--dry-run` 핸들 설계로 연결되어야 함.

## 5. Non-Promotion Note
이 결산은 학습 기록일 뿐이다.
Lens v0.1은 여전히 샌드박스 후보 상태이며, 어떠한 소스 공간 수정이나 자동화 승인을 포함하지 않는다.

---
**4-line Footer**
status: 완료
summary: Run 032~037 루프를 통해 Tool Affordance Lens v0.1을 정교화하고, 근거 기반 위험 분석의 운영적 유효성을 확인함
risk: 에이전트의 판단 결과가 '근거(Evidence)' 없이 명사화될 때 발생하는 노이즈를 상시 경계해야 함
next: 사용자 승인 후 다음 단계인 'Complex Existing Program Analysis' 또는 'Route Map v0' 작성으로 진행
