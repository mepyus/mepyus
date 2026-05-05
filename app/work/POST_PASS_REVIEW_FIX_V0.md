# POST_PASS_REVIEW_FIX_V0

## 1. Review Summary
- 1회 관통 성공: 전 구간 연결성 확인.
- 주요 드리프트: 일부 도구의 '구현' 및 '확정 언어' 사용.
- 구조적 결함: Review Gate의 판단 세분화 필요.

---

# ISSUE_CLASSIFICATION_TABLE_V0

| issue_id | issue_type | severity | classification | fix_timing | recommendation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ISS-01 | wording | post_session | Watch | post_session | Gemini 언어 수정 지침 강화 |
| ISS-02 | tool_drift | immediate | Needs Codex | immediate | Codex 패치 계획 강제 차단 |

---

# IMMEDIATE_FIX_PLAN_V0

1. **Drift 방지 강화**: Codex 프로필에 '구현 제안 시 즉시 경고' 조항 추가.
2. **Review Gate 정교화**: Needs User와 Needs Codex 분류 기준 업데이트.

---

# SECOND_PASS_FIX_BACKLOG_V0

- **Tool-Readable Surface**: 검색 인덱스 구조 최적화.
- **CLI Session Protocol**: Issue Log 처리 루틴 구체화.

---

# RECOVERED_WORKING_PATTERNS_V0

1. **검색 우선(Search-First) 루틴**: 모든 세션에서 기록 먼저 찾는 패턴.
2. **Context Bundle**: 불필요한 전체 공간 덤프 방지 패턴.
3. **분리된 이슈 로그**: 즉시 중단해야 할 것과 보정해야 할 것을 분리하는 관행.

---

# SESSION_10_HANDOFF
- **Goal**: 최종 보정 및 2회차 재구성(Second Pass).
- **Focus**: Immediate Fix 반영 및 Backlog를 반영한 시스템 정렬.
