# CONTEXT_BUNDLE_TEMPLATE_V0

## 1. Fields
- `bundle_id`: 식별자
- `user_purpose`: 현재 목표
- `activation_trigger`: 트리거 종류
- `related_line`/`related_axis`/`camera`/`lens`: 분석 틀
- `standing_context`: 모드 및 경계
- `activated_materials`: 활성화된 기록군
- `evidence_pointers`: 근거 인덱스
- `worker_role`: 도구의 역할
- `closed_boundaries`: 절대 금지 항목
- `return_format`: 결과 반환 형식
- `stop_conditions`: 즉시 중단 사유
- `recovery_route`: 결과 회수 경로

---

# CONTEXT_BUNDLE_TYPES_V0

1. **Intake**: 외부 자료 입력용.
2. **Codex Review**: 코드/구조 분석용.
3. **Gemini Analysis**: 비교 및 확장 분석용.
4. **Boundary Risk**: 위반 감시 및 교정용.
5. **Surface Revision**: 표면 문서 정제용.
6. **Issue Review**: 사후 이슈 정리용.

---

# CONTEXT_BUNDLE_ASSEMBLY_FLOW_V0

1. **User Purpose** -> 2. **Trigger** -> 3. **Line/Axis** -> 4. **Activation** -> 5. **Evidence Packaging** -> 6. **Boundary Check** -> 7. **Handoff** -> 8. **Recovery**

---

# CONTEXT_BUNDLE_EXAMPLES_V0

### 1. External Intake
- `bundle_id`: EX-INTAKE-001
- `task_request`: "이 외부 문서를 우리 구조에 적합한지 분석해"

### 2. Codex Review
- `bundle_id`: CODEX-REV-001
- `task_request`: "이 파일 구조를 우리 파이프라인에서 읽을 수 있는지 평가해"

### 3. Boundary Review
- `bundle_id`: BOUND-REV-001
- `task_request`: "이 자동화 제안이 우리의 Boundary를 침범하는지 진단해"
