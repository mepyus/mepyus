# FIRST_FULL_PASS_PLAN_V0

- **pass_id**: PASS-V0-001
- **pass_goal**: 7개 세션 산출물을 연결한 워크플로우 후보 검증
- **pass_scope**: 프로그램 수준 파이프라인 전 구간
- **session_sequence**: Session 0 ~ Session 7의 핵심 루프 순서
- **completion_criteria**: 각 단계별 산출물이 생성되고 이슈가 기록되었는가?

---

# FIRST_PASS_FLOW_V0

1. **User Purpose** -> 2. **Activation** (Space Map) -> 3. **Packaging** (Bundle) -> 4. **Handoff** (Role) -> 5. **Work** (Tool) -> 6. **Recovery** (Gate)

---

# FIRST_PASS_TEST_CASES_V0

1. **External Intake**: 외부 문서의 파이프라인 적합성 분석.
2. **Codex Review**: 구조적 읽기 가능성 평가.
3. **Gemini Analysis**: 외부 참조 자료와 현재 구조 비교.
4. **Boundary Risk**: 자동화 제안 시 차단 로직 테스트.
5. **Session Continuity**: 1회차 세션 종료 후 다음 세션 Handoff 정보 확인.

---

# FIRST_PASS_STOP_AND_CONTINUE_RULES_V0

- **STOP**: 구현 제안, 자동화 시도, 경계 침범, 사용자 강제 투입.
- **CONTINUE**: 단순 문구 오류, 중복 구조, 비차단 드리프트(기록 후 통과).

---

# POST_PASS_REVIEW_INPUT_V0

- **Summary**: 1회 관통 성공/실패 여부.
- **Gaps**: 구조적 누락, 템플릿 오류, 도구 실수 패턴.
- **Second Pass Candidates**: 2회차에 다듬을 구조적 개선점.
