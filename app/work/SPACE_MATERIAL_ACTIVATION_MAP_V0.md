# SPACE_MATERIAL_ACTIVATION_MAP_V0

| activation_id | trigger | related_line | related_axis | camera | lens | material_family | recovery_route |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | External Material Intake | Pipeline | Intake | Intake | Transparency | Pipeline Harness | Review Gate |
| 2 | Codex/OmX Review | Workflow | Attachment | Product | Usability | Hermes/OmX | Recovery Gate |
| 3 | Gemini Output | Analysis | Comparison | Meta | Expansion | Gemini Drift | Issue Log |
| 4 | Boundary Risk | Safety | Constraint | Boundary | Preservation | Boundary Risk | Boundary Check |
| 5 | Tool Surface | Interface | Readability | Surface | Clarity | Tool Surface | Surface Review |
| 6 | Bundle Creation | Pipeline | Package | Packaging | Minimization | Material Index | Review Gate |
| 7 | Review & Recovery | Management | Judgment | Supervisory | Discipline | Recovery | Issue Log |
| 8 | Post-Session Issue | Management | Refinement | Meta | Audit | Issue Log | Second Pass |

---

# MATERIAL_FAMILY_INDEX_V0

1. **Pipeline Harness Records**: [ID: MF01] 작업 흐름을 고정하는 핵심 재료군.
2. **Tool-Readable Surface Records**: [ID: MF02] 외부 도구와의 경계 표면.
3. **Boundary Risk Records**: [ID: MF03] 드리프트 및 실패 사례.
4. **Gemini Drift Records**: [ID: MF04] LLM 특유의 언어적 드리프트 분석.
5. **Codex/OmX Workflow Records**: [ID: MF05] 도구별 작업 흐름 패턴.
6. **Hermes Interface Records**: [ID: MF06] 메시지/미션 인터페이스 정의.
7. **OpenClaw Gateway Watch Records**: [ID: MF07] 미래 확장성 참조군.
8. **Digest / Recovery Records**: [ID: MF08] 회수 데이터 및 히스토리.
9. **User Operating Principles**: [ID: MF09] 최상위 원칙.
10. **Program-Level Setup Records**: [ID: MF10] 현재 세션 프레임워크.

---

# CONTEXT_BUNDLE_REQUIREMENTS_V0

### bundle_id: 컨텍스트 패킷 식별자
### user_purpose: 현재 세션의 목표
### standing_context: 현재 모드, 권한, 경계 규칙
### activated_materials: Activation Map에서 활성화된 해당 재료군
### evidence_pointers: 근거 자료 인덱스
### line_axis_camera_lens: 현재 분석/작업의 틀
### worker_role: 해당 도구의 역할 및 제약 사항
### allowed_autonomy: 도구의 허용된 작업 범위 (Search/Critique/Plan)
### closed_boundaries: 절대 실행 불가 항목
### return_format: 예상 출력 결과 형식
### stop_conditions: 세션 즉시 종료 사유
### recovery_route: 결과물을 어떻게 VectorFL로 재반입할지 정의
